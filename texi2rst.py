from collections import OrderedDict
import os
import re
import StringIO
import sys
import unittest
import xml.dom.minidom

"""
gcc.xml created from a gcc build/gcc tree using:

makeinfo --xml -I ABSPATH_OF_SRC/gcc/doc/ -I ABSPATH_OF_SRC/gcc/doc/include ABSPATH_OF_SRC/gcc/doc/gcc.texi 

TODO:
  map back to the include structure of the underlying .texi files
"""

# A minimal IR for transforming texinfo XML into rst

class Node:
    def __repr__(self):
        return 'Node()'

    def dump(self, f_out, depth=0):
        f_out.write('%s%r\n' %  (' ' * depth, self))

    def is_element(self, kind):
        if isinstance(self, Element):
            if self.kind == kind:
                return True

class Element(Node):
    def __init__(self, kind, attrs):
        self.kind = kind
        self.attrs = attrs
        self.children = []
        self.rst_kind = None

    def __repr__(self):
        return 'Element(%r, %r, %r)' % (self.kind, self.attrs, self.rst_kind)

    def dump(self, f_out, depth=0):
        f_out.write('%s%r\n' %  (' ' * depth, self))
        for child in self.children:
            child.dump(f_out, depth + 1)

    def first_element_named(self, name):
        for child in self.children:
            if isinstance(child, Element):
                if child.kind == name:
                    return child

    def get_sole_text(self):
        if len(self.children) == 1:
            child = self.children[0]
            if isinstance(child, Text):
                return child

    def get_first_text(self):
        for child in self.children:
            if isinstance(child, Text):
                return child

    def get_all_text(self):
        result = ''
        for child in self.children:
            if isinstance(child, Text):
                result += child.data
            elif isinstance(child, Element):
                result += child.get_all_text()
        return result

    def delete_children_named(self, name):
        new_children = []
        for child in self.children:
            if child.is_element(name):
                continue
            new_children.append(child)
        self.children = new_children

class Comment(Node):
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return 'Comment(%r)' % self.data

class Text(Node):
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return 'Text(%r)' % self.data


# Convert from XML nodes to our easier-to-work-with data structure

def convert_attrs_from_xml(namednodemap):
    result = OrderedDict()
    if namednodemap:
        for i in range(namednodemap.length):
            attr = namednodemap.item(i)
            result[attr.name] = attr.value
    return result

def convert_from_xml(xmlnode):
    kind = xmlnode.nodeType
    if kind == xmlnode.ELEMENT_NODE:
        new_node = Element(xmlnode.tagName,
                           convert_attrs_from_xml(xmlnode.attributes))
    elif kind == xmlnode.ATTRIBUTE_NODE:
        pass
    elif kind == xmlnode.TEXT_NODE:
        new_node = Text(xmlnode.data)
    elif kind == xmlnode.CDATA_SECTION_NODE:
        return None
    elif kind == xmlnode.ENTITY_NODE:
        # FIXME: xml.dom.minidom appears to be discarding entities,
        # which is a problem since the texinfo xml contains numerous
        # &lbrace; and &brace; in code examples
        raise ValueError()
    elif kind == xmlnode.PROCESSING_INSTRUCTION_NODE:
        raise ValueError()
    elif kind == xmlnode.COMMENT_NODE:
        new_node = Comment(xmlnode.data)
    elif kind == xmlnode.DOCUMENT_NODE:
        new_node = Element('document',
                           convert_attrs_from_xml(xmlnode.attributes))
    elif kind == xmlnode.DOCUMENT_TYPE_NODE:
        return None
    elif kind == xmlnode.NOTATION_NODE:
        raise ValueError()

    if xmlnode.hasChildNodes():
        for child_xmlnode in xmlnode.childNodes:
            child = convert_from_xml(child_xmlnode)
            if child:
                new_node.children.append(child)
    return new_node

def from_xml_string(xml_src):
    # Hack: not sure how to correctly handle entities using
    # xml.dom.minidom (if it is indeed possible), so do a textual
    # substitution first:
    xml_src = xml_src.replace('&lbrace;', '{')
    xml_src = xml_src.replace('&rbrace;', '}')
    xml_src = xml_src.replace('&bullet;', '*')
    xml_src = xml_src.replace('&dots;', '...')
    xml_src = xml_src.replace('&eosperiod;', '.')
    xml_src = xml_src.replace('&textndash;', '-')
    dom = xml.dom.minidom.parseString(xml_src)
    tree = convert_from_xml(dom)
    return tree

# Visitor base class

class Visitor:
    def visit(self, node):
        if isinstance(node, Element):
            self.previsit_element(node)
            for child in node.children:
                self.visit(child)
            self.postvisit_element(node)
        elif isinstance(node, Comment):
            self.visit_comment(node)
        elif  isinstance(node, Text):
            self.visit_text(node)
        else:
            raise ValueError('unknown node: %r' % (node, ))

    def previsit_element(self, element):
        raise NotImplementedError

    def postvisit_element(self, element):
        raise NotImplementedError

    def visit_comment(self, comment):
        raise NotImplementedError

    def visit_text(self, text):
        raise NotImplementedError

class NoopVisitor(Visitor):
    def previsit_element(self, element):
        pass

    def postvisit_element(self, element):
        pass

    def visit_comment(self, comment):
        pass

    def visit_text(self, text):
        pass

def for_each_node_below(node):
    if isinstance(node, Element):
        for child in node.children:
            yield child
            for node in for_each_node_below(child):
                yield node

def fixup_whitespace(tree):
    class WhitespaceFixer(NoopVisitor):
        """
        Strip redundant Text nodes
        """
        def previsit_element(self, element):
            if element.kind in ('pre', 'para'):
                return

            new_children = []
            for child in element.children:
                if isinstance(child, Text):
                    if child.data.isspace():
                        continue
                new_children.append(child)
            element.children = new_children

    v = WhitespaceFixer()
    v.visit(tree)
    return tree

# Conversion pipeline

def convert_comments(tree):
    class CommentConverter(NoopVisitor):
        def visit_comment(self, comment):
            if comment.data.startswith(' c '):
                comment.data = comment.data[3:]
    CommentConverter().visit(tree)
    return tree

def combine_commments(tree):
    class CommentCombiner(NoopVisitor):
        def previsit_element(self, element):
            # Attempt to merge
            #   COMMENT(x) WHITESPACE(y) COMMENT(z)
            # into
            #   COMMENT(x + y + z)
            new_children = []
            for child in element.children:
                if isinstance(child, Comment):
                    if len(new_children) >= 2:
                        last = new_children[-1]
                        penult = new_children[-2]
                        if isinstance(penult, Comment):
                            if isinstance(last, Text):
                                if last.data.isspace():
                                    element.children.pop()
                                    penult.data = penult.data + last.data + child.data
                                    continue
                new_children.append(child)
            element.children = new_children

    v = CommentCombiner()
    v.visit(tree)
    return tree

def fixup_comments(tree):
    tree = convert_comments(tree)
    tree = combine_commments(tree)
    return tree

def prune(tree):
    class Pruner(NoopVisitor):
        def previsit_element(self, element):
            new_children = []
            for child in element.children:
                if self.should_strip(child):
                    continue
                new_children.append(child)
            element.children = new_children

        def should_strip(self, child):
            if not isinstance(child, Element):
                return False
            if child.kind in ('filename', 'preamble', 'setfilename', 'clear',
                              'set', 'macro', 'settitle',
                              'defcodeindex', 'syncodeindex',
                              'paragraphindent',
                              'nodenext', 'nodeprev', 'nodeup'):
                return True
            else:
                return False

    v = Pruner()
    v.visit(tree)
    return tree

def convert_text_to_label(data):
    data = data.replace(' ', '-')
    data = data.lower()
    return data

def fixup_menus(tree):
    """
    Given:
      <menu endspaces=" ">
         <menuentry leadingtext="* ">
            <menunode separator="::     ">TEXT</menunode>
            <menudescription><pre xml:space="preserve">TEXT</pre></menudescription>
         </menuentry>
         [... more menuentry ...]
      </menu>
    convert as follows:
      * the <menu> becomes a "toctree" .rst directive
        (http://sphinx-doc.org/markup/toctree.html#directive-toctree)
      * the <menuentry> elements are pruned and tagged with ToctreeEntry, to
        be rendered using the given descriptions.
    """
    class MenuFixer(NoopVisitor):
        def previsit_element(self, element):
            if element.kind == 'menu':
                element.rst_kind = Directive('toctree', None)

            if element.kind == 'menuentry':
                menunode = element.first_element_named('menunode')
                menudescription = element.first_element_named('menudescription')
                if menunode and menudescription:
                    # Prune the menuentry, giving it an explicit title.
                    element.rst_kind = ToctreeEntry()
                    element.children = menudescription.children
                    for node in for_each_node_below(element):
                        if isinstance(node, Text):
                            if node.data.endswith('\n'):
                                node.data = node.data[:-1]
                    # FIXME: express this cross-reference at the Node level:
                    data = menunode.get_first_text().data
                    label = convert_text_to_label(data)
                    element.children += [Text(' <%s>' % label)]

    v = MenuFixer()
    v.visit(tree)
    return tree

def split(tree):
    class Splitter(NoopVisitor):
        def __init__(self):
            self.split_kinds = ('chapter', 'section', )

        def previsit_element(self, element):
            if element.kind in self.split_kinds:
                sectiontitle = element.first_element_named('sectiontitle')
                if sectiontitle:
                    text = sectiontitle.get_all_text()
                    text = text.lower()
                    text = text.replace(' ', '-')
                    text = text.replace('/', '-')
                    element.rst_kind = OutputFile(text)

    v = Splitter()
    v.visit(tree)
    return tree

def fixup_nodes(tree):
    """
    Given:
      <node name="C-Implementation" spaces=" ">
         <nodename>C Implementation</nodename>
         <nodenext automatic="on">C++ Implementation</nodenext>
         <nodeprev automatic="on">Invoking GCC</nodeprev>
         <nodeup automatic="on">Top</nodeup>
      </node>'''
    convert the <node> into a label for use by a ref:

       :: _c-implementation

    (see http://sphinx-doc.org/markup/inline.html#role-ref)
    """
    class MenuFixer(NoopVisitor):
        def previsit_element(self, element):
            if element.kind == 'node':
                nodename = element.first_element_named('nodename')
                text = nodename.get_sole_text()
                if nodename and text:
                    element.children = []
                    label = convert_text_to_label(text.data)
                    element.rst_kind = Label(label)

    v = MenuFixer()
    v.visit(tree)
    return tree

def fixup_option_refs(tree):
    class OptionRefFixer(NoopVisitor):
        # We'd like to handle texinfo "<option>" using sphinx's
        # inline ":option:" markup but Sphinx requires that the option
        # have a leading dash.
        # Conditionally retain options (or else they will be
        # stripped at output)
        def previsit_element(self, element):
            if element.kind == 'option':
                firstchild = element.children[0]
                if isinstance(firstchild, Text):
                    if firstchild.data.startswith('-'):
                        element.rst_kind = InlineMarkup('option')

    v = OptionRefFixer()
    v.visit(tree)
    return tree

def fixup_table_entry(tree):
    """
    Fixup <tableentry> elements.

    They can be used for descriptions of options, in this form:

       <tableentry>
         <tableterm>
           <item>
             <itemformat command="code">NAME OF OPTION</itemformat>
           </item>
         </tableterm>
         <tableitem>
           <indexcommand command="opindex" index="op" spaces=" ">
             <indexterm index="op" number="260" incode="1">NAME OF OPTION WITHOUT DASH</indexterm>
           </indexcommand>
           (...and more <indexcommand> for variant versions of the option...)
           <para>...</para><para>...</para>
         </tableitem>
       </tableentry>

    Transform this so that we can emit it as a .rst "option" directive.
    (see http://sphinx-doc.org/domains.html#directive-option)

    Alternatively, it can be a .rst "envvar" directive
    (see http://sphinx-doc.org/domains.html#directive-envvar)

    Alternatively, <tableentry> can be used to make lists of items, e.g.:

    <table commandarg="code" spaces=" " endspaces=" ">
      <tableentry>
        <tableterm>
          <item spaces=" ">
            <itemformat command="code"><var>file</var>.c</itemformat>
          </item>
        </tableterm>
        <tableitem>
          <para>C source code that must be preprocessed.</para>
        </tableitem>
      </tableentry>
      ... more <tableentry> elements ...
    </table>

    Transform this to a definition list.
    """
    class TableEntryFixer(NoopVisitor):
        def previsit_element(self, element):
            if element.kind == 'tableentry':
                tableterm = element.first_element_named('tableterm')
                tableitem = element.first_element_named('tableitem')
                if tableterm and tableitem:
                    item = tableterm.first_element_named('item')
                    if item:
                        itemformat = item.first_element_named('itemformat')
                        if itemformat:
                            # Detect:
                            #   <itemformat>
                            #     TEXT
                            #     <r>TEXT</r>
                            #   </itemformat>
                            # and move the <r>TEXT</r> to be a ".. note::"
                            # within the <tableitem>
                            if len(itemformat.children) == 2:
                                if itemformat.children[1].is_element('r'):
                                    r = itemformat.children[1]
                                    itemformat.children = \
                                        itemformat.children[:-1]
                                    note = Element('note', {})
                                    note.rst_kind = Directive('note', None)
                                    note.children = [r]

                                    tableitem.children = \
                                        [note] + tableitem.children

                            if self.convert_to_option(element, tableitem,
                                                      itemformat):
                                return
                            else:
                                tableterm.rst_kind = DefinitionListHeader()
                                tableitem.rst_kind = DefinitionListBody()
                                tableterm = fixup_whitespace(tableterm)

        def convert_to_option(self, tableentry, tableitem,
                              itemformat):
            text = itemformat.get_all_text()
            if text:
                options = [text]
            else:
                options = []

            # This might be a description of an option.
            # Scan below <tableitem> looking for <indexcommand>,
            # gathering options, and preparing a list of children
            # with the <indexcommand> instances purged.
            new_children = []
            found_indexcommand = False
            for child in tableitem.children:
                if isinstance(child, Element):
                    if child.kind == 'indexcommand':
                        found_indexcommand = True
                        indexterm = child.first_element_named('indexterm')
                        if indexterm:
                            text = indexterm.get_sole_text()
                            if text:
                                option = text.data
                                if not option.startswith('-'):
                                    option = '-' + option
                                if option not in options:
                                    options.append(option)
                                # Drop this <indexcommand>
                                continue
                new_children.append(child)

            # If the initial option (from "text") is of the form
            # "-option=value", then don't add all the extra options
            # from the <indexcommand>.
            if len(options) > 1:
                if '=' in options[0]:
                    options = [options[0]]

            if found_indexcommand:
                # Then it is a description of an option, mark it as such,
                # using all the option names found, and purge the
                # <indexcommand> instances:
                tableentry.rst_kind = Directive('option',
                                                ', '.join(options))
                tableentry.children = new_children
                return True

            # Otherwise, if it's all uppercase/underscores, make it
            # an "envvar" directive.
            if text and len(text) > 3 and re.match('^[A-Z][_A-Z]+$', text):
                tableentry.rst_kind = Directive('envvar', text)
                tableentry.children = new_children
                # The "envvar" directive will add it to the index; strip
                # any <findex> element below <tableitem>.
                tableentry.delete_children_named('findex')
                return True

    v = TableEntryFixer()
    v.visit(tree)
    return tree

def fixup_examples(tree):
    """
    Handle:
      <example>
        <pre>
          CODE EXAMPLE
        </pre>
      </example>
    and:
      <smallexample>
        <pre>
          CODE EXAMPLE
        </pre>
      </smallexample>

    Also, there could be a <group> wrapping the <pre>.

    We special-case where <smallexample> has been used to
    list a set of options (e.g. to describe "-O2").
    """
    class ExampleFixer(NoopVisitor):
        def previsit_element(self, element):
            if element.kind in ('example', 'smallexample'):
                example = element
                # There could be a "group" holding the "pre"
                group = element.first_element_named('group')
                if group:
                    element = group
                pre = element.first_element_named('pre')
                if pre:
                    text = pre.get_first_text()
                    if text:
                        if text.data.startswith('-'):
                            self.handle_option_listing(element, pre)
                            return
                        lang = self.guess_language(text.data)
                        example.rst_kind = Directive('code-block', lang)

        def guess_language(self, data):
            if 'DO ' in data:
                return 'fortran'
            if data.startswith('gcc ') or data.startswith('% gcc '):
                return 'bash'
            if data.startswith('--'):
                return 'bash'
            return 'c++'

        def handle_option_listing(self, element, pre):
            class OptionWrappingVisitor(NoopVisitor):
                def postvisit_element(self, element):
                    new_children = []
                    for child in element.children:
                        if isinstance(child, Text):
                            new_children += self.split_text(child)
                        else:
                            new_children.append(child)
                    element.children = new_children
                def split_text(self, text):
                    result = []
                    last_idx = 0
                    for m in re.finditer('(-\S+)', text.data):
                        if m.start(1) > 0:
                            result.append(Text(text.data[last_idx:m.start(1)]))
                        option = Element('option', {})
                        option.rst_kind = InlineMarkup('option')
                        option.children = [Text(m.group(1))]
                        last_idx = m.end(1)
                        result.append(option)
                    # Any trailing content?
                    if last_idx or not result:
                        result.append(Text(text.data[last_idx:]))
                    return result
            OptionWrappingVisitor().visit(pre)

    v = ExampleFixer()
    v.visit(tree)
    return tree

def fixup_titles(tree):
    class TitleFixer(NoopVisitor):
        def __init__(self):
            self.cur_section_level = None
            self.section_kinds = {
                'top'           : '=',
                'chapter'       : '-',
                'section'       : '*',
                'subsection'    : '^',
                'subsubsection' : '~',
                'unnumbered'    : '=',
                'unnumberedsec' : '='}

        def previsit_element(self, element):
            if element.kind in self.section_kinds:
                self.cur_section_level = element.kind

            if element.kind == 'sectiontitle':
                if self.cur_section_level:
                    underline = self.section_kinds[self.cur_section_level]
                else:
                    underline = '='
                element.rst_kind = Title(element, underline)

            elif element.kind == 'subsubheading':
                element.rst_kind = Title(element, '^')

    v = TitleFixer()
    v.visit(tree)
    return tree

def fixup_index(tree):
    class IndexFixer(NoopVisitor):
        """
        Look for <cindex><indexterm>TEXT</indexterm></cindex>
        """
        def previsit_element(self, element):
            if isinstance(element, Element):
                if element.kind == 'indexterm':
                    text = element.get_sole_text()
                    if text:
                        element.rst_kind = Directive('index', text.data)
                        element.children = []
    v = IndexFixer()
    v.visit(tree)
    return tree

def fixup_lists(tree):
    class ListFixer(NoopVisitor):
        """
        Convert:
          <listitem>
             <prepend>&bullet;</prepend>
             ...ELEMENTS...
          </listitem>
        to:
          <listitem rst_kind=ListItem(BULLET)>
             ...ELEMENTS...
          </listitem>
        """
        def previsit_element(self, element):
            if element.kind == 'listitem':
                new_children = []
                element.rst_kind = ListItem('*')
                skip_ws = True
                for child in element.children:
                    if isinstance(child, Element):
                        if child.kind == 'prepend':
                            continue
                    if isinstance(child, Text):
                        if child.data.isspace():
                            if skip_ws:
                                continue
                    skip_ws = False
                    new_children.append(child)
                element.children = new_children

    v = ListFixer()
    v.visit(tree)
    return tree

def fixup_inline_markup(tree):
    class InlineMarkupFixer(NoopVisitor):
        """
        Inline markup conversions:
        =========================  ==================
        XML INPUT                  .rst OUTPUT
        =========================  ==================
        <command>TEXT</command>    :command:`TEXT`
        <var>TEXT</var>            ``TEXT``
        <code>TEXT</code>          ``TEXT``
        <dfn>TEXT</dfn>            :dfn:`TEXT`
        <env>TEXT</env>            :envvar:`TEXT`
        =========================  ==================
        """
        def previsit_element(self, element):
            if element.kind == 'command':
                element.rst_kind = InlineMarkup('command')
            elif element.kind == 'var':
                element.rst_kind = MatchedInlineMarkup('``')
            elif element.kind == 'code':
                element.rst_kind = MatchedInlineMarkup('``')
            elif element.kind == 'dfn':
                element.rst_kind = InlineMarkup('dfn')
            elif element.kind == 'env':
                element.rst_kind = InlineMarkup('envvar')

    v = InlineMarkupFixer()
    v.visit(tree)
    return tree

# Top-level conversion routine

def convert_to_rst(tree):
    tree = fixup_comments(tree)
    tree = prune(tree)
    tree = fixup_menus(tree)
    tree = split(tree)
    tree = fixup_nodes(tree)
    tree = fixup_option_refs(tree)
    tree = fixup_table_entry(tree)
    tree = fixup_examples(tree)
    tree = fixup_titles(tree)
    tree = fixup_index(tree)
    tree = fixup_lists(tree)
    tree = fixup_inline_markup(tree)
    return tree

# Policies for converting elements to rst (element.rst_kind):

class RstKind:
    def before(self, w):
        pass

    def after(self, w):
        pass

class InlineMarkup(RstKind):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'InlineMarkup(%r)' % self.name

    def before(self, w):
        w.write(':%s:`' % self.name)

    def after(self, w):
        w.write('`')

class MatchedInlineMarkup(RstKind):
    """
    For handling '*foo*', '**foo**' and '``foo``'.
    """
    def __init__(self, tag):
        self.tag = tag

    def __repr__(self):
        return 'MatchedInlineMarkup(%r)' % self.tag

    def before(self, w):
        w.write(self.tag)

    def after(self, w):
        w.write(self.tag)

class Title(RstKind):
    def __init__(self, element, underline):
        self.element = element
        self.underline = underline

    def __repr__(self):
        return 'Title(element, %r)' % (self.underline, )

    def before(self, w):
        w.write('\n')

    def after(self, w):
        if len(self.element.children) == 1:
            if isinstance(self.element.children[0], Text):
                len_ = len(self.element.children[0].data)
                w.write('\n%s\n\n' % (self.underline * len_))

class Directive(RstKind):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __repr__(self):
        return 'Directive(%r, %r)' % (self.name, self.args)

    def before(self, w):
        w.write('\n.. %s::' % (self.name, ))
        if self.args:
            w.write(' %s' % (self.args, ))
        w.indent += 1
        w.write('\n\n')

    def after(self, w):
        w.indent -= 1

class ListItem(RstKind):
    def __init__(self, bullet):
        self.bullet = bullet

    def __repr__(self):
        return 'ListItem(%r)' % self.bullet

    def before(self, w):
        w.write('%s ' % (self.bullet, ))
        w.indent += 1

    def after(self, w):
        w.indent -= 1

class DefinitionListHeader(RstKind):
    """
    http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#definition-lists
    """
    def __repr__(self):
        return 'DefinitionListHeader()'

    def before(self, w):
        w.write('\n')

    def after(self, w):
        pass

class DefinitionListBody(RstKind):
    """
    http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#definition-lists
    """
    def __repr__(self):
        return 'DefinitionListBody()'

    def before(self, w):
        w.indent += 1
        w.write('\n')

    def after(self, w):
        w.indent -= 1

class ToctreeEntry(RstKind):
    def __init__(self):
        pass

    def after(self, w):
        w.write('\n')

class Label(RstKind):
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return 'Label(%r)' % self.title

    def before(self, w):
        w.write(':: _%s:\n' % (self.title, ))

class OutputFile(RstKind):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'OutputFile(%r)' % self.name

    def before(self, w):
        w.push_output_file(self)

    def after(self, w):
        w.pop_output_file(self)

# Output of a converted tree to .rst file

class RstWriter(Visitor):
    def __init__(self, f_out, opener=None):
        self.f_out = f_out
        self.indent = 0
        self.curline = ''
        self.had_nonempty_line = False
        self.opener = opener
        if self.f_out is None:
            self.f_out = self.opener.open(None)
        self.output_file_stack = [self.f_out]

    def finish(self):
        self._flush_line()

    def write(self, text):
        text = text.replace('\n',
                            '\n%s' % ('  ' * self.indent))
        for ch in text:
            if ch == '\n':
                nonempty_line = self._flush_line()
                # Avoid repeated blank lines:
                if nonempty_line or self.had_nonempty_line:
                    self.f_out.write('\n')
                self.had_nonempty_line = nonempty_line
            else:
                self.curline += ch

    def _flush_line(self):
        # Don't print lines containing purely whitespace
        # (just print their newlines)
        if not self.curline:
            return False

        if self.curline.isspace():
            self.curline = ''
            return False

        self.f_out.write(self.curline)
        self.curline = ''
        return True

    def previsit_element(self, element):
        if element.rst_kind:
            element.rst_kind.before(self)
        else:
            if 0:
                print('unhandled element: %r' % (element, ))

    def postvisit_element(self, element):
        if element.rst_kind:
            element.rst_kind.after(self)

    def visit_comment(self, comment):
        lines = comment.data.splitlines()
        self.write('\n.. %s\n' % lines[0])
        for line in lines[1:]:
            self.write('   %s\n' % line)
        self.write('\n')

    def visit_text(self, text):
        self.write(text.data)

    def push_output_file(self, output_file):
        self.f_out = self.opener.open(output_file)
        self.output_file_stack.append(self.f_out)

    def pop_output_file(self, output_file):
        self.opener.close(self.f_out)
        self.output_file_stack.pop()
        self.f_out = self.output_file_stack[-1]

class RstOpener:
    """
    Policy for how RstWriter should handle OutputFile instances
    """
    def open(self, output_file):
        raise NotImplementedError
    def close(self, f_out):
        raise NotImplementedError

# Unit tests

class Texi2RstTests(unittest.TestCase):
    def make_rst_string(self, doc):
        w = RstWriter(StringIO.StringIO())
        w.visit(doc)
        w.finish()
        return w.f_out.getvalue()

    def make_rst_strings(self, doc):
        class StringOpener(RstOpener):
            def __init__(self):
                self.dict_ = OrderedDict()
            def open(self, output_file):
                f_out = StringIO.StringIO()
                self.dict_[output_file] = f_out
                return f_out
            def close(self, f_out):
                pass # don't close; we need to call getvalue on it

        opener = StringOpener()
        w = RstWriter(None, opener)
        w.visit(doc)
        w.finish()
        result = OrderedDict()
        for k in opener.dict_:
            if k:
                name = k.name
            else:
                name = 'gcc' # FIXME
            result[name] = opener.dict_[k].getvalue()
        return result

class CommentTests(Texi2RstTests):
    xml_src = (
'''<texinfo>
<!-- c First line -->
<!-- c Second line -->
</texinfo>''')

    def test_parsing(self):
        doc = from_xml_string(self.xml_src)
        self.assertIsInstance(doc, Element)
        self.assertEqual(len(doc.children), 1)
        texinfo = doc.children[0]
        self.assertIsInstance(texinfo, Element)
        self.assertEqual(texinfo.kind, 'texinfo')
        self.assertEqual(len(texinfo.children), 5)
        self.assertIsInstance(texinfo.children[0], Text)
        self.assertEqual(texinfo.children[0].data, u'\n')
        self.assertIsInstance(texinfo.children[1], Comment)
        self.assertEqual(texinfo.children[1].data, u' c First line ')
        self.assertIsInstance(texinfo.children[2], Text)
        self.assertIsInstance(texinfo.children[3], Comment)
        self.assertIsInstance(texinfo.children[4], Text)

    def test_comment_converter(self):
        doc = from_xml_string(self.xml_src)
        doc = convert_comments(doc)
        texinfo = doc.children[0]
        self.assertEqual(len(texinfo.children), 5)
        self.assertEqual(texinfo.children[1].data, u'First line ')

    def test_comment_combining(self):
        doc = from_xml_string(self.xml_src)
        doc = fixup_comments(doc)
        texinfo = doc.children[0]
        self.assertEqual(len(texinfo.children), 3)
        self.assertIsInstance(texinfo.children[0], Text)
        self.assertIsInstance(texinfo.children[1], Comment)
        self.assertEqual(texinfo.children[1].data, u'First line \nSecond line ')
        self.assertIsInstance(texinfo.children[2], Text)

    def test_rst_output(self):
        doc = from_xml_string(self.xml_src)
        doc = fixup_comments(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'.. First line \n   Second line \n\n', out)

class PruningTests(Texi2RstTests):
    def test_command(self):
        xml_src = '<texinfo><filename/></texinfo>'
        doc = from_xml_string(xml_src)
        texinfo = doc.children[0]
        self.assertEqual(len(texinfo.children), 1)
        doc = prune(doc)
        self.assertEqual(len(texinfo.children), 0)
        out = self.make_rst_string(doc)
        self.assertEqual(u'', out)

class MenuTests(Texi2RstTests):
    def test_menu(self):
        xml_src = u'''
<menu endspaces=" ">
<menuentry leadingtext="* "><menunode separator="::     ">G++ and GCC</menunode><menudescription><pre xml:space="preserve">You can compile C or C++ programs.
</pre></menudescription></menuentry><menuentry leadingtext="* "><menunode separator="::       ">Standards</menunode><menudescription><pre xml:space="preserve">Language standards supported by GCC.
</pre></menudescription></menuentry><menuentry leadingtext="* "><menunode separator="::    ">Invoking GCC</menunode><menudescription><pre xml:space="preserve">Command options supported by <samp>gcc</samp>.
</pre></menudescription></menuentry><menuentry leadingtext="* "><menunode separator=":: ">C Implementation</menunode><menudescription><pre xml:space="preserve">How GCC implements the ISO C specification.
</pre></menudescription></menuentry><menuentry leadingtext="* "><menunode separator=":: ">C++ Implementation</menunode><menudescription><pre xml:space="preserve">How GCC implements the ISO C++ specification.
</pre></menudescription></menuentry><menuentry leadingtext="* "><menunode separator="::    ">C Extensions</menunode><menudescription><pre xml:space="preserve">GNU extensions to the C language family.
</pre></menudescription></menuentry><menuentry leadingtext="* "><menunode separator="::  ">C++ Extensions</menunode><menudescription><pre xml:space="preserve">GNU extensions to the C++ language.
</pre></menudescription></menuentry></menu>
        '''
        doc = from_xml_string(xml_src)
        doc = fixup_menus(doc)
        out = self.make_rst_string(doc)
        self.maxDiff = 2000
        self.assertEqual(u'''.. toctree::

  You can compile C or C++ programs. <g++-and-gcc>
  Language standards supported by GCC. <standards>
  Command options supported by gcc. <invoking-gcc>
  How GCC implements the ISO C specification. <c-implementation>
  How GCC implements the ISO C++ specification. <c++-implementation>
  GNU extensions to the C language family. <c-extensions>
  GNU extensions to the C++ language. <c++-extensions>
''',
                         out)

    def test_nodename(self):
        xml_src = u'''<node name="C-Implementation" spaces=" "><nodename>C Implementation</nodename><nodenext automatic="on">C++ Implementation</nodenext><nodeprev automatic="on">Invoking GCC</nodeprev><nodeup automatic="on">Top</nodeup></node>'''
        doc = from_xml_string(xml_src)
        doc = fixup_nodes(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u':: _c-implementation:\n',
                         out)

class InlineMarkupTests(Texi2RstTests):
    def test_command(self):
        xml_src = '<texinfo>Before <command>gcc</command> after</texinfo>'
        doc = from_xml_string(xml_src)
        doc = fixup_inline_markup(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'Before :command:`gcc` after', out)

    def test_var(self):
        xml_src = '<texinfo>Before <var>gcc</var> after</texinfo>'
        doc = from_xml_string(xml_src)
        doc = fixup_inline_markup(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'Before ``gcc`` after', out)

    def test_code(self):
        xml_src = '<texinfo>Before <code>gcc</code> after</texinfo>'
        doc = from_xml_string(xml_src)
        doc = fixup_inline_markup(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'Before ``gcc`` after', out)

    def test_dfn(self):
        xml_src = (u'<para>An <dfn>attribute specifier list</dfn> is...</para>')
        doc = from_xml_string(xml_src)
        doc = fixup_inline_markup(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'An :dfn:`attribute specifier list` is...', out)

    def test_env(self):
        xml_src = u'<para>The default <env>GCC_COLORS</env> is...</para>'
        doc = from_xml_string(xml_src)
        doc = fixup_inline_markup(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'The default :envvar:`GCC_COLORS` is...', out)

class TitleTests(Texi2RstTests):
    def test_section_title(self):
        xml_src = ('<texinfo><sectiontitle>A section title</sectiontitle>'
                   + '<para>some text</para></texinfo>')
        doc = from_xml_string(xml_src)
        doc = fixup_titles(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'A section title\n===============\n\nsome text',
                         out)

    def test_nested_section_titles(self):
        xml_src = (u'''<texinfo>
<top><sectiontitle>A top-level title</sectiontitle>
<para>some top text</para></top>
<chapter><sectiontitle>A chapter title</sectiontitle>
<para>some chapter text</para></chapter>
</texinfo>''')
        doc = from_xml_string(xml_src)
        doc = fixup_titles(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'''A top-level title
=================

some top text

A chapter title
---------------

some chapter text
''',
                         out)

    def test_subsubheading(self):
        xml_src = ('<texinfo><subsubheading>A sub-sub-heading</subsubheading>'
                   + '<para>some text</para></texinfo>')
        doc = from_xml_string(xml_src)
        doc = fixup_titles(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'A sub-sub-heading\n^^^^^^^^^^^^^^^^^\n\nsome text',
                         out)

class OptionTests(Texi2RstTests):
    def test_valid_option_ref(self):
        xml_src = ('<texinfo><option>--some-opt</option></texinfo>')
        doc = from_xml_string(xml_src)
        doc = fixup_option_refs(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u':option:`--some-opt`', out)

    def test_invalid_option_ref(self):
        xml_src = ('<texinfo><option>some-opt</option></texinfo>')
        doc = from_xml_string(xml_src)
        doc = fixup_option_refs(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'some-opt', out)

    def test_option_description(self):
        xml_src = ('''<texinfo>
<tableentry><tableterm><item spaces=" "><itemformat command="code">-Wunused-label</itemformat></item>
</tableterm><tableitem><indexcommand command="opindex" index="op" spaces=" "><indexterm index="op" number="260" incode="1">Wunused-label</indexterm></indexcommand>
<indexcommand command="opindex" index="op" spaces=" "><indexterm index="op" number="261" incode="1">Wno-unused-label</indexterm></indexcommand>
<para>Warn whenever a label is declared but not used.
This warning is enabled by <option>-Wall</option>.
</para>
<para>To suppress this warning use the <code>unused</code> attribute.</para>
</tableitem></tableentry></texinfo>''')
        doc = from_xml_string(xml_src)
        doc = fixup_table_entry(doc)
        doc = fixup_inline_markup(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(
            u'''.. option:: -Wunused-label, -Wno-unused-label

  Warn whenever a label is declared but not used.
  This warning is enabled by -Wall.

  To suppress this warning use the ``unused`` attribute.
''',
            out)

    def test_option_description_with_r(self):
        xml_src = ('''<texinfo>
<tableentry><tableterm><item spaces=" "><itemformat command="code">-Wstrict-prototypes <r>(C and Objective-C only)</r></itemformat></item>
</tableterm><tableitem><indexcommand command="opindex" index="op" spaces=" "><indexterm index="op" number="417" incode="1">Wstrict-prototypes</indexterm></indexcommand>
<indexcommand command="opindex" index="op" spaces=" "><indexterm index="op" number="418" incode="1">Wno-strict-prototypes</indexterm></indexcommand>
<para>Warn if a function is declared or defined without specifying the
argument types.  (An old-style function definition is permitted without
a warning if preceded by a declaration that specifies the argument
types.)
</para>
</tableitem></tableentry></texinfo>''')
        doc = from_xml_string(xml_src)
        doc = fixup_table_entry(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(
            u'''.. option:: -Wstrict-prototypes , -Wstrict-prototypes, -Wno-strict-prototypes

  .. note::

    (C and Objective-C only)

  Warn if a function is declared or defined without specifying the
  argument types.  (An old-style function definition is permitted without
  a warning if preceded by a declaration that specifies the argument
  types.)

''',
            out)

    def test_option_with_var(self):
        # Ensure that the <var> within <iterformat> doesn't confuse the option-finder
        xml_src = (u'<tableentry><tableterm><item spaces=" ">'
                   + u'<itemformat command="code">-fabi-version=<var>n</var></itemformat></item>'
                   + u'</tableterm><tableitem><indexcommand command="opindex" index="op" spaces=" "><indexterm index="op" number="52" incode="1">fabi-version</indexterm></indexcommand>'
                   + u'<para>DESCRIPTION WOULD GO HERE</para></tableitem></tableentry>')
        doc = from_xml_string(xml_src)
        doc = fixup_table_entry(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(
            u'''.. option:: -fabi-version=n

  DESCRIPTION WOULD GO HERE''',
            out)

    def test_option_listing(self):
        xml_src = ('''<texinfo>
<para><option>-Wall</option> turns on the following warning flags:
</para>
<smallexample endspaces=" ">
<pre xml:space="preserve">-Waddress   
-Warray-bounds=1 <r>(only with</r> <option>-O2</option><r>)</r>  
-Wc++11-compat  -Wc++14-compat
-Wchar-subscripts  
-Wenum-compare <r>(in C/ObjC; this is on by default in C++)</r> 
-Wimplicit-int <r>(C and Objective-C only)</r> 
-Wimplicit-function-declaration <r>(C and Objective-C only)</r> 
-Wcomment  
-Wformat   
-Wmain <r>(only for C/ObjC and unless</r> <option>-ffreestanding</option><r>)</r>  
-Wmaybe-uninitialized 
-Wmissing-braces <r>(only for C/ObjC)</r> 
-Wnonnull  
-Wopenmp-simd 
-Wparentheses  
-Wpointer-sign  
-Wreorder   
-Wreturn-type  
-Wsequence-point  
-Wsign-compare <r>(only in C++)</r>  
-Wstrict-aliasing  
-Wstrict-overflow=1  
-Wswitch  
-Wtrigraphs  
-Wuninitialized  
-Wunknown-pragmas  
-Wunused-function  
-Wunused-label     
-Wunused-value     
-Wunused-variable  
-Wvolatile-register-var 

</pre></smallexample></texinfo>''')
        doc = from_xml_string(xml_src)
        doc = fixup_examples(doc)
        out = self.make_rst_string(doc)
        self.maxDiff = 5000
        self.assertEqual(
            u'''-Wall turns on the following warning flags:

:option:`-Waddress`   
:option:`-Warray-bounds=1` (only with :option:`-O2`)  
:option:`-Wc++11-compat`  :option:`-Wc++14-compat`
:option:`-Wchar-subscripts`  
:option:`-Wenum-compare` (in C/ObjC; this is on by default in C++) 
:option:`-Wimplicit-int` (C and Objective:option:`-C` only) 
:option:`-Wimplicit-function-declaration` (C and Objective:option:`-C` only) 
:option:`-Wcomment`  
:option:`-Wformat`   
:option:`-Wmain` (only for C/ObjC and unless :option:`-ffreestanding`)  
:option:`-Wmaybe-uninitialized` 
:option:`-Wmissing-braces` (only for C/ObjC) 
:option:`-Wnonnull`  
:option:`-Wopenmp-simd` 
:option:`-Wparentheses`  
:option:`-Wpointer-sign`  
:option:`-Wreorder`   
:option:`-Wreturn-type`  
:option:`-Wsequence-point`  
:option:`-Wsign-compare` (only in C++)  
:option:`-Wstrict-aliasing`  
:option:`-Wstrict-overflow=1`  
:option:`-Wswitch`  
:option:`-Wtrigraphs`  
:option:`-Wuninitialized`  
:option:`-Wunknown-pragmas`  
:option:`-Wunused-function`  
:option:`-Wunused-label`     
:option:`-Wunused-value`     
:option:`-Wunused-variable`  
:option:`-Wvolatile-register-var` 

''',
            out)

class TableEntryTests(Texi2RstTests):
    def test_generating_definition_list(self):
        xml_src = u'''
<table commandarg="code" spaces=" " endspaces=" ">
<tableentry><tableterm><item spaces=" "><itemformat command="code"><var>file</var>.c</itemformat></item>
</tableterm><tableitem><para>C source code that must be preprocessed.
</para>
</tableitem></tableentry><tableentry><tableterm><item spaces=" "><itemformat command="code"><var>file</var>.i</itemformat></item>
</tableterm><tableitem><para>C source code that should not be preprocessed.
</para>
</tableitem></tableentry><tableentry><tableterm><item spaces=" "><itemformat command="code"><var>file</var>.ii</itemformat></item>
</tableterm><tableitem><para>C++ source code that should not be preprocessed.
</para>
</tableitem></tableentry>
</table>
'''
        doc = from_xml_string(xml_src)
        doc = fixup_table_entry(doc)
        doc = fixup_inline_markup(doc)
        out = self.make_rst_string(doc)
        self.maxDiff = 3000
        self.assertEqual(
            u'''``file``.c
  C source code that must be preprocessed.

``file``.i
  C source code that should not be preprocessed.

``file``.ii
  C++ source code that should not be preprocessed.

''',
            out)

    def test_generating_envvar_directive(self):
        xml_src = u'''<tableentry><tableterm><item spaces=" "><itemformat command="env">TMPDIR</itemformat></item>
</tableterm><tableitem><findex index="fn" spaces=" "><indexterm index="fn" number="8" mergedindex="cp">TMPDIR</indexterm></findex>
<para>If <env>TMPDIR</env> is set, it specifies the directory to use for temporary
files.  GCC uses temporary files to hold the output of one stage of
compilation which is to be used as input to the next stage: for example,
the output of the preprocessor, which is the input to the compiler
proper.
</para>
</tableitem></tableentry>'''
        doc = from_xml_string(xml_src)
        doc = fixup_table_entry(doc)
        doc = fixup_inline_markup(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'''.. envvar:: TMPDIR

  If :envvar:`TMPDIR` is set, it specifies the directory to use for temporary
  files.  GCC uses temporary files to hold the output of one stage of
  compilation which is to be used as input to the next stage: for example,
  the output of the preprocessor, which is the input to the compiler
  proper.

''',
                         out)

class CodeFragmentTests(Texi2RstTests):
    def test_smallexample_option(self):
        xml_src = ('''
<texinfo>An example:
<smallexample endspaces=" ">
<pre xml:space="preserve">static int
test (int i)
&lbrace;
  return i * i;
&rbrace;
</pre></smallexample></texinfo>''')
        doc = from_xml_string(xml_src)
        doc = fixup_examples(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(
            (u'''An example:

.. code-block:: c++

  static int
  test (int i)
  {
    return i * i;
  }
'''),
            out)

    def test_fortran(self):
        xml_src = ('''
<smallexample endspaces=" ">
<pre xml:space="preserve">DO J = 1, M
  DO I = 1, N
    A(J, I) = A(J, I) * C
  ENDDO
ENDDO
</pre></smallexample>''')
        doc = from_xml_string(xml_src)
        doc = fixup_examples(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(
            (u'''.. code-block:: fortran

  DO J = 1, M
    DO I = 1, N
      A(J, I) = A(J, I) * C
    ENDDO
  ENDDO
'''),
            out)

    def test_shell(self):
        xml_src = ('''<smallexample endspaces=" ">
<pre xml:space="preserve">gcc -c -Q -O3 --help=optimizers &gt; /tmp/O3-opts
gcc -c -Q -O2 --help=optimizers &gt; /tmp/O2-opts
diff /tmp/O2-opts /tmp/O3-opts | grep enabled
</pre></smallexample>''')
        doc = from_xml_string(xml_src)
        doc = fixup_examples(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(
            (u'''.. code-block:: bash

  gcc -c -Q -O3 --help=optimizers > /tmp/O3-opts
  gcc -c -Q -O2 --help=optimizers > /tmp/O2-opts
  diff /tmp/O2-opts /tmp/O3-opts | grep enabled
'''),
            out)

    def test_group_and_ellipsis(self):
        # Example of a <group> wrapping the <pre>, with "&dots;"
        # entity and embedded markup.
        xml_src = ('''<smallexample endspaces=" ">
<group endspaces=" ">
<pre xml:space="preserve">bar (int *array, int offset, int size)
&lbrace;
  __label__ failure;
  int access (int *array, int index)
    &lbrace;
      if (index &gt; size)
        goto failure;
      return array[index + offset];
    &rbrace;
  int i;
  /* <r>&dots;</r> */
  for (i = 0; i &lt; size; i++)
    /* <r>&dots;</r> */ access (array, i) /* <r>&dots;</r> */
  /* <r>&dots;</r> */
  return 0;

 /* <r>Control comes here from <code>access</code>
    if it detects an error.</r>  */
 failure:
  return -1;
&rbrace;
</pre></group>
</smallexample>''')
        doc = from_xml_string(xml_src)
        doc = fixup_examples(doc)
        doc = fixup_inline_markup(doc)
        out = self.make_rst_string(doc)
        self.maxDiff = 2000
        self.assertEqual(u'''.. code-block:: c++

  bar (int *array, int offset, int size)
  {
    __label__ failure;
    int access (int *array, int index)
      {
        if (index > size)
          goto failure;
        return array[index + offset];
      }
    int i;
    /* ... */
    for (i = 0; i < size; i++)
      /* ... */ access (array, i) /* ... */
    /* ... */
    return 0;

   /* Control comes here from ``access``
      if it detects an error.  */
   failure:
    return -1;
  }

''',
                         out)


class ListTests(Texi2RstTests):
    def test_bulleted(self):
        xml_src = ('''
<itemize commandarg="bullet" spaces=" " endspaces=" "><itemprepend><formattingcommand command="bullet"/></itemprepend>
<listitem><prepend>&bullet;</prepend>
<para>Empty.  Empty attributes are ignored.</para>
</listitem>
<listitem><prepend>&bullet;</prepend>
<para>An attribute name
(which may be an identifier such as <code>unused</code>, or a reserved
word such as <code>const</code>).
</para>
</listitem>
<listitem><prepend>&bullet;</prepend>
<para>An attribute name followed by a parenthesized list of
parameters for the attribute.
These parameters take one of the following forms:
</para>
</listitem>
</itemize>
''')
        doc = from_xml_string(xml_src)
        doc = fixup_lists(doc)
        doc = fixup_inline_markup(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(
            (u'''* Empty.  Empty attributes are ignored.

* An attribute name
  (which may be an identifier such as ``unused``, or a reserved
  word such as ``const``).

* An attribute name followed by a parenthesized list of
  parameters for the attribute.
  These parameters take one of the following forms:

'''),
            out)

    def test_nested(self):
        xml_src = ('''
<itemize commandarg="bullet" spaces=" " endspaces=" ">
  <itemprepend><formattingcommand command="bullet"/></itemprepend>
  <listitem><prepend>&bullet;</prepend>
    <para>Outer list's first item.</para>
  </listitem>
  <listitem><prepend>&bullet;</prepend>
    <para>A nested list</para>
    <itemize commandarg="bullet" spaces=" " endspaces=" ">
      <itemprepend><formattingcommand command="bullet"/></itemprepend>
      <listitem><prepend>&bullet;</prepend>
        <para>Nested list's first item.</para>
      </listitem>
      <listitem><prepend>&bullet;</prepend>
        <para>Nested list's second item.</para>
      </listitem>
    </itemize>
  </listitem>
  <listitem><prepend>&bullet;</prepend>
    <para>Outer list's 3rd item.</para>
  </listitem>
</itemize>
''')
        doc = from_xml_string(xml_src)
        doc = fixup_lists(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(
            (u'''  * Outer list's first item.

  * A nested list

        * Nested list's first item.

        * Nested list's second item.

  * Outer list's 3rd item.

'''),
            out)


class IndexTests(Texi2RstTests):
    def test_cindex(self):
        xml_src = ('''<node>
<sectiontitle>GCC Command Options</sectiontitle>
<cindex index="cp" spaces=" "><indexterm index="cp" number="61">GCC command options</indexterm></cindex>
<cindex index="cp" spaces=" "><indexterm index="cp" number="62">command options</indexterm></cindex>
<cindex index="cp" spaces=" "><indexterm index="cp" number="63">options, GCC command</indexterm></cindex>
<para>Some text about GCC command options.</para>
<cindex index="cp" spaces=" "><indexterm index="cp" number="64">C compilation options</indexterm></cindex>
<para>Some text about C compilation options.</para>
<cindex index="cp" spaces=" "><indexterm index="cp" number="66">grouping options</indexterm></cindex>
<cindex index="cp" spaces=" "><indexterm index="cp" number="67">options, grouping</indexterm></cindex>
<para>Some text about grouping options.
</para>
</node>''')
        doc = from_xml_string(xml_src)
        doc = fixup_titles(doc)
        doc = fixup_index(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(
            (u'''GCC Command Options
===================

.. index:: GCC command options

.. index:: command options

.. index:: options, GCC command

Some text about GCC command options.

.. index:: C compilation options

Some text about C compilation options.

.. index:: grouping options

.. index:: options, grouping

Some text about grouping options.

'''),
        out)

class IntegrationTests(Texi2RstTests):
    def test_empty(self):
        xml_src = '''<texinfo/>'''
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree)
        out = self.make_rst_string(tree)
        self.assertEqual(u'', out)

    def test_splitting(self):
        xml_src = u'''<texinfo>
<top>
   <sectiontitle>Top-level title</sectiontitle>
   <para>Top-level text.</para>
</top>
<chapter>
  <sectiontitle>Chapter 1 title</sectiontitle>
  <para>Chapter 1 text.</para>
  <section spaces=" ">
     <sectiontitle>Chapter 1 Section 1 title</sectiontitle>
     <para>Chapter 1 Section 1 text.</para>
  </section>
  <section spaces=" ">
     <sectiontitle>Chapter 1 Section 2 title</sectiontitle>
     <para>Chapter 1 Section 2 text.</para>
  </section>
</chapter>
<chapter>
  <sectiontitle>Chapter 2 title</sectiontitle>
  <para>Chapter 2 text.</para>
  <section spaces=" ">
     <sectiontitle>Chapter 2 Section 1 title</sectiontitle>
     <para>Chapter 2 Section 1 text.</para>
  </section>
  <section spaces=" ">
     <sectiontitle>Chapter 2 Section 2 title</sectiontitle>
     <para>Chapter 2 Section 2 text.</para>
  </section>
</chapter>
</texinfo>
'''
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree)
        dict_ = self.make_rst_strings(tree)
        self.assertEqual(
            dict_[u'gcc'],
            (u'Top-level title\n' +
             u'===============\n' +
             u'\n' +
             u'   Top-level text.\n\n')) # FIXME < this indentation is wrong
        self.assertEqual(
            dict_[u'chapter-1-title'],
            (u'Chapter 1 title\n---------------\n\n' +
             u'  Chapter 1 text.\n\n\n')) # FIXME < this indentation is wrong
        self.assertEqual(
            dict_[u'chapter-2-section-2-title'],
            (u'Chapter 2 Section 2 title\n*************************\n\n' +
             '     Chapter 2 Section 2 text.\n'))
        # FIXME and the above indentation is also wrong

        if 0:
            for k in dict_:
                print(repr(k))
                print(repr(dict_[k]))
                print(dict_[k])

#

class FileOpener(RstOpener):
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def open(self, output_file):
        path = os.path.join(self.output_dir, '%s.rst' % output_file.name)
        print('opening: %s' % path)
        f_out = open(path, 'w')
        return f_out

    def close(self, f_out):
        print('closing')
        f_out.close()

# Entrypoint

if __name__ == '__main__':
    if len(sys.argv) < 2:
        unittest.main()
    else:
        with open(sys.argv[1]) as f_in:
            xml_src = f_in.read()
            tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree)
        if 1:
            with open('output/gcc.rst', 'w') as f_out:
                w = RstWriter(f_out, FileOpener('output'))
                w.visit(tree)
        else:
            w = RstWriter(sys.stdout)
            w.visit(tree)
