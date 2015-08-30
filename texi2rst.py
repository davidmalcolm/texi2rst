from collections import OrderedDict
import os
import re
import StringIO
import sys
import unittest
import xml.dom.minidom

from node import Node, Element, Comment, Text

"""
gcc.xml created from a gcc build/gcc tree using:

makeinfo --xml -I ABSPATH_OF_SRC/gcc/doc/ -I ABSPATH_OF_SRC/gcc/doc/include ABSPATH_OF_SRC/gcc/doc/gcc.texi 

TODO:
  map back to the include structure of the underlying .texi files
"""

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
    # FIXME: use correct unicode chars for the results
    xml_src = xml_src.replace('&arobase;', "@")
    xml_src = xml_src.replace('&bullet;', '*')
    xml_src = xml_src.replace('&copyright;', "(C)")
    xml_src = xml_src.replace('&dots;', '...')
    xml_src = xml_src.replace('&eosperiod;', '.')
    xml_src = xml_src.replace('&equiv;', '==')
    xml_src = xml_src.replace('&lbrace;', '{')
    xml_src = xml_src.replace('&linebreak;', "\n")
    xml_src = xml_src.replace('&rbrace;', '}')
    xml_src = xml_src.replace('&slashbreak;', "/")
    xml_src = xml_src.replace('&minus;', '-')
    xml_src = xml_src.replace('&nbsp;', ' ')
    xml_src = xml_src.replace('&noeos;', '')
    xml_src = xml_src.replace('&tex;', 'Tex')
    xml_src = xml_src.replace('&textmdash;', '-')
    xml_src = xml_src.replace('&textndash;', '-')
    xml_src = xml_src.replace('&textldquo;', "'")
    xml_src = xml_src.replace('&textrdquo;', "'")
    xml_src = xml_src.replace('&textlsquo;', "'")
    xml_src = xml_src.replace('&textrsquo;', "'")

    # Complain about any entities still present
    for m in re.finditer('(&[a-z]+;)', xml_src):
        BUILTIN_XML_ENTITIES = ('&quot;', '&amp;', '&apos;', '&lt;', '&gt;')
        if m.group(1) not in BUILTIN_XML_ENTITIES:
            raise ValueError('Unhandled entity: %r' % m.group(1))

    dom = xml.dom.minidom.parseString(xml_src)
    tree = convert_from_xml(dom)
    tree = fixup_whitespace(tree)
    return tree

# Visitor base class

class Visitor:
    def visit(self, node):
        if isinstance(node, Element):
            early_exit = self.previsit_element(node)
            if early_exit:
                return
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
            if element.kind == 'pre':
                return

            if element.kind == 'para':
                # Strip trailing whitespace within <para>
                text = element.get_sole_text()
                if text:
                    text.data = text.data.rstrip()
                return

            # Within other kinds of element, fully strip
            # pure-whitespace text nodes.
            new_children = []
            for child in element.children:
                if isinstance(child, Text):
                    if child.data.isspace():
                        continue
                new_children.append(child)
            element.children = new_children

        def visit_comment(self, comment):
            comment.data = comment.data.rstrip()

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
            #   COMMENT(x) COMMENT(y)
            # into
            #   COMMENT(x + '\n' + y)
            new_children = []
            for child in element.children:
                if isinstance(child, Comment):
                    if len(new_children) >= 1:
                        last = new_children[-1]
                        if isinstance(last, Comment):
                            last.data = last.data + '\n' + child.data
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
    data = data.replace('\n', '-')
    data = data.replace('/', '-')
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

    class ToctreeAdder(NoopVisitor):
        """
        Add toctree directives referencing the split content
        """
        def previsit_element(self, element):
            new_children = []
            toctree = None
            for child in element.children:
                if isinstance(child, Element):
                    if child.kind == 'toctree':
                        toctree = child
                    if isinstance(child.rst_kind, OutputFile):
                        toctree_element = Element('toctree-element', {})
                        toctree_element.rst_kind = ToctreeEntry()
                        toctree_element.children = [Text(child.rst_kind.name)]
                        # Try to consolidate all toctree entries into one
                        # toctree:
                        if toctree:
                            toctree.children.append(toctree_element)
                        else:
                            toctree = Element('toctree', {})
                            toctree.rst_kind = Directive('toctree', None)
                            toctree.children = [toctree_element]
                            new_children.append(toctree)

                new_children.append(child)
            element.children = new_children

    v = Splitter()
    v.visit(tree)

    v = ToctreeAdder()
    v.visit(tree)
    return tree

def fixup_nodes(tree, ctxt):
    """
    Given:
      <node name="C-Implementation" spaces=" ">
         <nodename>C Implementation</nodename>
         <nodenext automatic="on">C++ Implementation</nodenext>
         <nodeprev automatic="on">Invoking GCC</nodeprev>
         <nodeup automatic="on">Top</nodeup>
      </node>'''
    convert the <node> into a label for use by a ref:

       :: _c-implementation:

    (see http://sphinx-doc.org/markup/inline.html#role-ref)

    We also need to handle <anchor> in a similar way, so that:
      <anchor name="GotoLabels">GotoLabels</anchor>
    becomes:
       :: _gotolabels:

    Also, we are given a structure like this:
      Element(PARENT)
        <node/> for chapter 1
        <chapter/>
          ...content of chapter 1...
        <node/> for chapter 2
          ...content of chapter 1...
        <chapter/>
    whereas we want the nodes/anchors inside the things they describe,
    so that the label will work.  Move them, to be the first child,
    like this:
      Element(PARENT)
        <chapter/>
          <node/> for chapter 1
          ...content of chapter 1...
        <chapter)
          <node/> for chapter 2
          ...content of chapter 1...

    But we could have:
      Element(ANCESTOR)
        Element
          Element
            Element
              <anchor>
      Element
        ...content...
    where we want to put the <anchor> after the next Element in depth-first
    order:
      Element(ANCESTOR)
        Element
          Element
            Element
      Element
        <anchor>
        ...content...
    """
    class NodeFixer(NoopVisitor):
        def previsit_element(self, element):
            if element.kind == 'node':
                nodename = element.first_element_named('nodename')
                text = nodename.get_sole_text()
                if nodename and text:
                    element.children = []
                    label = convert_text_to_label(text.data)
                    element.rst_kind = Label(label)

            if element.kind == 'anchor':
                text = element.get_sole_text()
                if text:
                    element.children = []
                    label = convert_text_to_label(text.data)
                    element.rst_kind = Label(label)

    def move_nodes(tree):
        # Gather a list of (parent, child) pairs
        if ctxt.debug:
            for node in tree.iter_depth_first():
                print(node)

        edges = list(tree.iter_depth_first_edges())
        for i, (parent, child) in enumerate(edges):
                if ctxt.debug:
                    print i, parent, child
                if child.is_element('node') or child.is_element('anchor'):

                    def get_next_child_element():
                        for cand_parent, cand_child in edges[i + 1:]:
                            if isinstance(cand_child, Element):
                                return cand_child

                    next_parent = get_next_child_element()
                    if next_parent:
                        if ctxt.debug:
                            print('\nMOVING %r from %r to %r\n'
                                  % (child, parent, next_parent))
                        parent.children.remove(child)
                        next_parent.children.insert(0, child)

    v = NodeFixer()
    v.visit(tree)

    if ctxt.debug:
        print
        tree.dump(sys.stdout)
        print
    move_nodes(tree)
    if ctxt.debug:
        print
        tree.dump(sys.stdout)
        print

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
                                self.convert_to_definition_list(tableterm,
                                                                tableitem)

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

        def convert_to_definition_list(self, tableterm, tableitem):
            tableterm.rst_kind = DefinitionListHeader()
            tableitem.rst_kind = DefinitionListBody()

            # Add whitespace before <itemx> items
            new_children = []
            for child in tableterm.children:
                if child.is_element('itemx'):
                    new_children.append(Text(' '))
                new_children.append(child)
            tableterm.children = new_children

    v = TableEntryFixer()
    v.visit(tree)
    return tree

def fixup_multitables(tree, ctxt):
    """
    Given:
          <multitable spaces=" " endspaces=" ">
            <columnprototypes>
              <columnprototype bracketed="on">Modifier</columnprototype>
              <columnprototype bracketed="on">Print the opcode suffix for the size of th</columnprototype>
              <columnprototype bracketed="on">Operand</columnprototype>
              <columnprototype bracketed="on">masm=att</columnprototype>
              <columnprototype bracketed="on">masm=intel</columnprototype>
            </columnprototypes>
            <thead>
              <row>
                <entry command="headitem" spaces=" ">
                  <para>Modifier </para>
                </entry>
                <entry command="tab" spaces=" ">
                  <para>Description </para>
                </entry>
                <entry command="tab" spaces=" ">
                  <para>Operand </para>
                </entry>
                <entry command="tab" spaces=" ">
                  <para>
                    <option>masm=att</option>
                  </para>
                </entry>
                <entry command="tab" spaces=" ">
                  <para>
                    <option>masm=intel</option>
                  </para>
                </entry>
              </row>
            </thead>
            <tbody>
              <row>
                <entry command="item" spaces=" ">
                  <para>
                    <code>z</code>
                  </para>
                </entry>
                <entry command="tab" spaces=" ">
                  <para>Print the opcode suffix for the size of the current integer operand (one of <code>b</code>/<code>w</code>/<code>l</code>/<code>q</code>).
</para>
                </entry>
                <entry command="tab" spaces=" ">
                  <para>
                    <code>%z0</code>
                  </para>
                </entry>
                <entry command="tab" spaces=" ">
                  <para>
                    <code>l</code>
                  </para>
                </entry>
                <entry command="tab"> </entry>
              </row>
              <row/>
              ...etc...
            </tbody>
          </multitable>
    convert to a .rst table
    """
    class MultitableFixer(NoopVisitor):
        def previsit_element(self, element):
            if element.kind == 'multitable':
                element.rst_kind = Table(element, ctxt)
            element.delete_children_named('columnprototypes')

        def postvisit_element(self, element):
            if ctxt.debug:
                if element.kind == 'multitable':
                    element.dump(sys.stdout)

    v = MultitableFixer()
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
        def __init__(self):
            self.default_lang_stack = ['c++']

        def previsit_element(self, element):
            if hasattr(element, 'default_language'):
                self.default_lang_stack.append(element.default_language)

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

        def postvisit_element(self, element):
            if hasattr(element, 'default_language'):
                self.default_lang_stack.pop()

        def guess_language(self, data):
            if 'DO ' in data:
                return 'fortran'
            if data.startswith('gcc ') or data.startswith('% gcc '):
                return 'bash'
            if data.startswith('--'):
                return 'bash'
            return self.default_lang_stack[-1]

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
                    text = element.get_all_text()
                    if text:
                        element.rst_kind = Directive('index', text)
                        element.children = []
    v = IndexFixer()
    v.visit(tree)
    return tree

def fixup_xrefs(tree):
    class XRefFixer(NoopVisitor):
        """
        Given:
          <xref label="C-Dialect-Options">
            <xrefnodename>C Dialect Options</xrefnodename>
            <xrefprinteddesc>Options Controlling C Dialect</xrefprinteddesc>
          </xref>
        generate:
          Element("xref")
            Text("See ")
            Element(Ref(REF_DESC, REF_NAME))
        giving this .rst text:
          See :ref:`REF_DESC <REF_NAME>`
        (see http://sphinx-doc.org/markup/inline.html#role-ref)
        Note that the XML already contains a trailing period.
        """
        def previsit_element(self, element):
            if element.kind in ('xref', 'pxref'):
                xrefnodename = element.first_element_named('xrefnodename')
                xrefprinteddesc = element.first_element_named('xrefprinteddesc')
                ref_desc = self.get_desc(element)
                ref_name = convert_text_to_label(xrefnodename.get_sole_text().data)
                ref = Element('ref', {})
                ref.rst_kind = Ref(ref_desc, ref_name)
                if element.kind == 'xref':
                    text = 'See '
                else:
                    assert element.kind == 'pxref'
                    text = 'see '
                element.children = [Text(text), ref]

        def get_desc(self, element):
            xrefprinteddesc = element.first_element_named('xrefprinteddesc')
            if not xrefprinteddesc:
                return None
            desc = xrefprinteddesc.get_sole_text()
            if not desc:
                return None
            return desc.data

    v = XRefFixer()
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
        <emph>TEXT</emph>          *TEXT*
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
            elif element.kind == 'emph':
                element.rst_kind = MatchedInlineMarkup('*')

    v = InlineMarkupFixer()
    v.visit(tree)
    return tree

# Top-level conversion routine

def convert_to_rst(tree, ctxt):
    tree = ctxt.preprocess(tree)
    tree = fixup_comments(tree)
    tree = prune(tree)
    tree = fixup_nodes(tree, ctxt)
    tree = fixup_menus(tree)
    tree = split(tree)
    tree = fixup_option_refs(tree)
    tree = fixup_table_entry(tree)
    tree = fixup_multitables(tree, ctxt)
    tree = fixup_examples(tree)
    tree = fixup_titles(tree)
    tree = fixup_index(tree)
    tree = fixup_xrefs(tree)
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

class Ref(RstKind):
    def __init__(self, desc, name):
        self.desc = desc
        self.name = name

    def __repr__(self):
        return 'Ref(%r, %r)' % (self.desc, self.name)

    def before(self, w):
        if self.desc:
            w.write(':ref:`%s <%s>`' % (self.desc, self.name))
        else:
            w.write(':ref:`%s`' % self.name)

    def after(self, w):
        pass

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
        w.write('\n\n')

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
        w.write('\n\n')

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
        w.write('.. _%s:\n' % (self.title, ))

class OutputFile(RstKind):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'OutputFile(%r)' % self.name

    def before(self, w):
        w.push_output_file(self)

    def after(self, w):
        w.pop_output_file(self)

class TableLayout:
    def __init__(self, table_element, debug):
        if debug:
            table_element.dump(sys.stdout)
        self.components = []
        for child in table_element.children:
            if child.is_element('thead') or child.is_element('tbody'):
                self.components.append(child)
        if debug:
            print('self.components: %r' % (self.components, ))

        self.needs_grid_table = False

        for comp in self.components:
            comp.rows = []
            for child in comp.children:
                if child.is_element('row'):
                    comp.rows.append(child)
            if debug:
                print('comp.rows: %r' % (comp.rows, ))

            for row in comp.rows:
                row.entries = []
                for child in row.children:
                    if child.is_element('entry'):
                        row.entries.append(child)
                    if self._entry_needs_grid_table(child):
                        self.needs_grid_table = True
                if debug:
                    print('row.entries: %r' % (row.entries, ))

        # If we just have a body, turn the first row into a header:
        if len(self.components) == 1:
            thead = Element('thead', {})
            first_row = self.components[0].rows[0]
            thead.rows = [first_row]
            self.components[0].rows = self.components[0].rows[1:]
            self.components.insert(0, thead)

        self.num_columns = len(self.components[0].rows[0].entries)
        if debug:
            print('self.num_columns: %r' % self.num_columns)
        for comp in self.components:
            comp.columns = []
            for idx in range(self.num_columns):
                column = []
                for row in comp.rows:
                    column.append(row.entries[idx])
                if debug:
                    print('column: %r' % (column, ))
                comp.columns.append(column)
            if debug:
                print('comp.columns: %r' % (comp.columns, ))

        # Requisition:
        self.width_needed_for_x = {}
        for x in range(self.num_columns):
            for comp in self.components:
                for y, entry in enumerate(comp.columns[x]):
                    w, h = self._get_requisition(entry)
                    if w > self.width_needed_for_x.get(x, 0):
                        self.width_needed_for_x[x] = w

        for comp in self.components:
            comp.height_needed_for_y = {}
            for x in range(self.num_columns):
                for y, entry in enumerate(comp.columns[x]):
                    w, h = self._get_requisition(entry)
                    if h > comp.height_needed_for_y.get(y, 0):
                        comp.height_needed_for_y[y] = h

    def _entry_needs_grid_table(self, entry):
        for desc in entry.iter_depth_first():
            if isinstance(desc, Element):
                if isinstance(desc.rst_kind, Directive):
                    return True
        return False

    def _get_requisition(self, entry):
        text = self._render_entry(entry)
        if text:
            lines = text.splitlines()
            w = max([len(line) for line in lines])
            h = len(lines)
            return w, h
        else:
            return 0, 0

    def _render_entry(self, entry):
        # Nested writer
        w = RstWriter(StringIO.StringIO())
        w.visit(entry)
        w.finish()
        result = w.f_out.getvalue()
        result = result.rstrip()
        if 0:
            print('%r from %r' % (result, entry))
        return result

    def render(self, w):
        if self.needs_grid_table:
            self.render_grid_table(w)
        else:
            self.render_simple_table(w)

    def render_grid_table(self, w):
        self.draw_grid_table_border(w, '-')
        for comp_idx, comp in enumerate(self.components):
            for y, row in enumerate(comp.rows):
                # Cope with newlines in "text":
                lines_at_x = {}
                for x, entry in enumerate(row.entries):
                    lines_at_x[x] = (
                        self._render_entry(entry).splitlines())

                for line_idx in range(comp.height_needed_for_y[y]):
                    w.write('|')
                    for x, entry in enumerate(row.entries):
                        lines = lines_at_x[x]
                        if line_idx < len(lines):
                            text = lines[line_idx]
                        else:
                            text = ''
                        w.write(text)
                        w.write(' ' *
                                (self.width_needed_for_x[x] - len(text)))
                        w.write('|')
                    w.write('\n')
                if comp_idx == 0:
                    self.draw_grid_table_border(w, '=')
                else:
                    self.draw_grid_table_border(w, '-')

    def draw_grid_table_border(self, w, sep):
        w.write('+')
        for x in range(self.num_columns):
            w.write(sep * self.width_needed_for_x[x])
            w.write('+')
        w.write('\n')

    def render_simple_table(self, w):
        self.draw_simple_table_border(w)
        for comp in self.components:
            for y, row in enumerate(comp.rows):
                # Cope with newlines in "text":
                lines_at_x = {}
                for x, entry in enumerate(row.entries):
                    lines_at_x[x] = self._render_entry(entry).splitlines()

                for line_idx in range(comp.height_needed_for_y[y]):
                    # Determine within this line which is the final
                    # non-empty entry, to avoid surplus whitespace
                    # to the right of it.
                    final_x_with_text = 0
                    for x, entry in enumerate(row.entries):
                        if line_idx < len(lines_at_x[x]):
                            if lines_at_x[x][line_idx]:
                                final_x_with_text = x

                    for x, entry in enumerate(row.entries):
                        if x and x <= final_x_with_text:
                            w.write('  ')
                        lines = lines_at_x[x]
                        if line_idx < len(lines):
                            text = lines[line_idx]
                        else:
                            text = ''
                        w.write(text)
                        if x < final_x_with_text:
                            w.write(' ' *
                                    (self.width_needed_for_x[x] - len(text)))
                    w.write('\n')
            self.draw_simple_table_border(w)

    def draw_simple_table_border(self, w):
        for x in range(self.num_columns):
            if x:
                w.write('  ')
            w.write('=' * self.width_needed_for_x[x])
        w.write('\n')

class Table(RstKind):
    def __init__(self, element, ctxt):
        self.element = element
        self.ctxt = ctxt

    def before(self, w):
        table_layout = TableLayout(self.element, self.ctxt.debug)
        table_layout.render(w)

        # Don't traverse children; we've already rendered them
        return True

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
            return element.rst_kind.before(self)
        else:
            if 0:
                print('unhandled element: %r' % (element, ))

    def postvisit_element(self, element):
        if element.rst_kind:
            element.rst_kind.after(self)
        if element.kind == 'para':
            self.write('\n\n')

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

class Context:
    def __init__(self):
        self.debug = False

    def preprocess(self, tree):
        return tree

# Unit tests

class Texi2RstTests(unittest.TestCase):
    def setUp(self):
        self.ctxt = Context()

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
        self.assertEqual(len(texinfo.children), 2)
        self.assertIsInstance(texinfo.children[0], Comment)
        self.assertEqual(texinfo.children[0].data, u' c First line')
        self.assertIsInstance(texinfo.children[1], Comment)
        self.assertEqual(texinfo.children[1].data, u' c Second line')

    def test_comment_converter(self):
        doc = from_xml_string(self.xml_src)
        doc = convert_comments(doc)
        texinfo = doc.children[0]
        self.assertEqual(len(texinfo.children), 2)
        self.assertEqual(texinfo.children[0].data, u'First line')

    def test_comment_combining(self):
        doc = from_xml_string(self.xml_src)
        doc = fixup_comments(doc)
        texinfo = doc.children[0]
        self.assertEqual(len(texinfo.children), 1)
        self.assertIsInstance(texinfo.children[0], Comment)
        self.assertEqual(texinfo.children[0].data, u'First line\nSecond line')

    def test_rst_output(self):
        doc = from_xml_string(self.xml_src)
        doc = fixup_comments(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'.. First line\n   Second line\n\n', out)

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
        doc = fixup_nodes(doc, self.ctxt)
        out = self.make_rst_string(doc)
        self.assertEqual(u'.. _c-implementation:\n',
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
        self.assertEqual(u'An :dfn:`attribute specifier list` is...\n\n', out)

    def test_env(self):
        xml_src = u'<para>The default <env>GCC_COLORS</env> is...</para>'
        doc = from_xml_string(xml_src)
        doc = fixup_inline_markup(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'The default :envvar:`GCC_COLORS` is...\n\n', out)

class TitleTests(Texi2RstTests):
    def test_section_title(self):
        xml_src = ('<texinfo><sectiontitle>A section title</sectiontitle>'
                   + '<para>some text</para></texinfo>')
        doc = from_xml_string(xml_src)
        doc = fixup_titles(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'A section title\n===============\n\nsome text\n\n',
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
        self.assertEqual(u'A sub-sub-heading\n^^^^^^^^^^^^^^^^^\n\nsome text\n\n',
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

  DESCRIPTION WOULD GO HERE

''',
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

    def test_itemx(self):
        xml_src = u'''<texinfo>
<tableentry><tableterm><item spaces=" "><itemformat command="samp">c90</itemformat></item>
<itemx spaces=" "><itemformat command="samp">c89</itemformat></itemx>
<itemx spaces=" "><itemformat command="samp">iso9899:1990</itemformat></itemx>
</tableterm><tableitem><para>Support all ISO C90 programs (certain GNU extensions that conflict
with ISO C90 are disabled). Same as <option>-ansi</option> for C code.
</para>
</tableitem></tableentry></texinfo>'''
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual(u'''c90 c89 iso9899:1990
  Support all ISO C90 programs (certain GNU extensions that conflict
  with ISO C90 are disabled). Same as :option:`-ansi` for C code.

''', out)

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
            (u'''* Outer list's first item.

* A nested list

  * Nested list's first item.

  * Nested list's second item.

* Outer list's 3rd item.

'''),
            out)

    def test_issue_3(self):
        xml_src = (u'''<texinfo><para>There is no formal written standard for Objective-C or Objective-C++&eosperiod;
The authoritative manual on traditional Objective-C (1.0) is
&textldquo;Object-Oriented Programming and the Objective-C Language&textrdquo;,
available at a number of web sites:
</para><itemize commandarg="bullet" endspaces=" ">
<listitem><prepend>&bullet;</prepend>
<para><uref><urefurl>http://www.gnustep.org/&slashbreak;resources/&slashbreak;documentation/&slashbreak;ObjectivCBook.pdf</urefurl></uref>
is the original NeXTstep document;
</para></listitem><listitem><prepend>&bullet;</prepend>
<para><uref><urefurl>http://objc.toodarkpark.net</urefurl></uref>
is the same document in another format;
</para></listitem><listitem><prepend>&bullet;</prepend>
<para><uref><urefurl>http://developer.apple.com/&slashbreak;mac/&slashbreak;library/&slashbreak;documentation/&slashbreak;Cocoa/&slashbreak;Conceptual/&slashbreak;ObjectiveC/</urefurl></uref>
has an updated version but make sure you search for &textldquo;Object Oriented Programming and the Objective-C Programming Language 1.0&textrdquo;,
not documentation on the newer &textldquo;Objective-C 2.0&textrdquo; language
</para></listitem></itemize></texinfo>''')
        doc = from_xml_string(xml_src)
        doc = fixup_lists(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(
            (u'''There is no formal written standard for Objective-C or Objective-C++.
The authoritative manual on traditional Objective-C (1.0) is
'Object-Oriented Programming and the Objective-C Language',
available at a number of web sites:

* http://www.gnustep.org//resources//documentation//ObjectivCBook.pdf
  is the original NeXTstep document;

* http://objc.toodarkpark.net
  is the same document in another format;

* http://developer.apple.com//mac//library//documentation//Cocoa//Conceptual//ObjectiveC/
  has an updated version but make sure you search for 'Object Oriented Programming and the Objective-C Programming Language 1.0',
  not documentation on the newer 'Objective-C 2.0' language

'''), out)

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

class XRefTests(Texi2RstTests):
    def test_xref(self):
        xml_src = ('''<para>Some text.
<xref label="C-Dialect-Options"><xrefnodename>C Dialect Options</xrefnodename><xrefprinteddesc>Options Controlling C Dialect</xrefprinteddesc></xref>.
</para>''')
        doc = from_xml_string(xml_src)
        doc = fixup_xrefs(doc)
        out = self.make_rst_string(doc)
        self.maxDiff = 2000
        self.assertEqual(
            (u'''Some text.
See :ref:`Options Controlling C Dialect <c-dialect-options>`.

'''),
        out)

    def test_xref_with_infoname(self):
        xml_src = ('''<para>Some text.
<xref label="C_002b_002b-Dialect-Options"><xrefnodename>C++
Dialect Options</xrefnodename><xrefinfoname>Options Controlling C++ Dialect</xrefinfoname></xref>.</para>''')
        doc = from_xml_string(xml_src)
        doc = fixup_xrefs(doc)
        out = self.make_rst_string(doc)
        self.maxDiff = 2000
        self.assertEqual(
            (u'''Some text.
See :ref:`c++-dialect-options`.

'''),
        out)


class IntegrationTests(Texi2RstTests):
    def test_empty(self):
        xml_src = '''<texinfo/>'''
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual(u'', out)

    def test_anchor(self):
        xml_src = u'''<texinfo>
<subsubsection>
  <subsubheading spaces=" ">Qualifiers</subsubheading>
  <para>Some text about qualifiers.  <xref label="GotoLabels"><xrefnodename>GotoLabels</xrefnodename></xref>.</para>
  <anchor name="GotoLabels">GotoLabels</anchor>
</subsubsection>
<subsubsection spaces=" ">
  <sectiontitle>Goto Labels</sectiontitle>
  <cindex index="cp" spaces=" ">
    <indexterm index="cp" number="789"><code>asm</code> goto labels</indexterm>
  </cindex>
  <para>Some text about goto labels.</para>
</subsubsection>
</texinfo>
'''
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual(u'''Qualifiers
^^^^^^^^^^

Some text about qualifiers.  See :ref:`gotolabels`.

.. _gotolabels:

Goto Labels
~~~~~~~~~~~

.. index:: asm goto labels

Some text about goto labels.

''', out)

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
        tree = convert_to_rst(tree, self.ctxt)
        dict_ = self.make_rst_strings(tree)
        self.assertEqual(
            (u'Top-level title\n' +
             u'===============\n' +
             u'\n' +
             u'Top-level text.' +
             u'''

.. toctree::

  chapter-1-title
  chapter-2-title

'''),
            dict_[u'gcc'])
        self.assertEqual(
            (u'Chapter 1 title\n---------------\n\n' +
             u'Chapter 1 text.' +
             u'''

.. toctree::

  chapter-1-section-1-title
  chapter-1-section-2-title

'''),
            dict_[u'chapter-1-title'])
        self.assertEqual(
            (u'Chapter 2 Section 2 title\n*************************\n\n' +
             'Chapter 2 Section 2 text.\n\n'),
            dict_[u'chapter-2-section-2-title'])

        if 0:
            for k in dict_:
                print(repr(k))
                print(repr(dict_[k]))
                print(dict_[k])

    def test_nodes_placed_before_section_titles(self):
        # Make sure that nodes get placed with their sections, with links
        # appearing before section titles
        xml_src = u'''
<texinfo>
  <para>Top level para.  <xref><xrefnodename>Standards</xrefnodename></xref> and <xref><xrefnodename>Function Attributes</xrefnodename></xref>.
  </para>
  <node name="Standards" spaces=" "><nodename>Standards</nodename><nodenext automatic="on">Invoking GCC</nodenext><nodeprev automatic="on">G++ and GCC</nodeprev><nodeup automatic="on">Top</nodeup></node>
  <chapter spaces=" ">
    <sectiontitle>Language Standards Supported by GCC</sectiontitle>
    <para>First para of standards</para>
  </chapter>
  <node name="Function-Attributes" spaces=" "><nodename>Function Attributes</nodename><nodenext automatic="on">Variable Attributes</nodenext><nodeprev automatic="on">Mixed Declarations</nodeprev><nodeup automatic="on">C Extensions</nodeup></node>
  <!-- some comment -->
  <chapter spaces=" ">
    <sectiontitle>Declaring Attributes of Functions</sectiontitle>
    <para>First para of attributes</para>
  </chapter>
</texinfo>
'''
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_strings(tree)
        dict_ = self.make_rst_strings(tree)
        self.assertEqual(
            u'''Top level para.  See :ref:`standards` and See :ref:`function-attributes`.

.. toctree::

  language-standards-supported-by-gcc
  declaring-attributes-of-functions

..  some comment

''',
            dict_['gcc'])
        self.assertEqual(
            dict_['language-standards-supported-by-gcc'],
            u'''.. _standards:

Language Standards Supported by GCC
-----------------------------------

First para of standards

''')
        self.assertEqual(
            dict_['declaring-attributes-of-functions'],
            u'''.. _function-attributes:

Declaring Attributes of Functions
---------------------------------

First para of attributes

''')

class TestIter(Texi2RstTests):
    def test_traversal(self):
        xml_src = u'''<A>
   <B-1>
      <C-1/>
      <C-2/>
   </B-1>
   <B-2>
      <C-3/>
      <C-4/>
   </B-2>
</A>'''
        tree = from_xml_string(xml_src)
        dfs = list(tree.iter_depth_first())
        self.assertEqual(len(dfs), 8)
        self.assert_(dfs[0].is_element('document'))
        self.assert_(dfs[1].is_element('A'))
        self.assert_(dfs[2].is_element('B-1'))
        self.assert_(dfs[3].is_element('C-1'))
        self.assert_(dfs[4].is_element('C-2'))
        self.assert_(dfs[5].is_element('B-2'))
        self.assert_(dfs[6].is_element('C-3'))
        self.assert_(dfs[7].is_element('C-4'))

        dfs_edges = list(tree.iter_depth_first_edges())
        self.assertEqual(len(dfs_edges), 7)
        self.assert_edge_from(dfs_edges[0], 'document', 'A')
        self.assert_edge_from(dfs_edges[1], 'A', 'B-1')
        self.assert_edge_from(dfs_edges[2], 'B-1', 'C-1')
        self.assert_edge_from(dfs_edges[3], 'B-1', 'C-2')
        self.assert_edge_from(dfs_edges[4], 'A', 'B-2')
        self.assert_edge_from(dfs_edges[5], 'B-2', 'C-3')
        self.assert_edge_from(dfs_edges[6], 'B-2', 'C-4')

    def assert_is_element(self, node, element_name):
        if not isinstance(node, Element):
            raise ValueError('%r is not an element' % node)
        if node.kind != element_name:
            raise ValueError('%r is not of kind %r' % (node, element_name))

    def assert_edge_from(self, edge, src_element_name, dst_element_name):
        self.assert_is_element(edge[0], src_element_name)
        self.assert_is_element(edge[1], dst_element_name)

class TableTests(Texi2RstTests):
    def test_multitable(self):
        xml_src = u'''<multitable spaces=" " endspaces=" "><columnprototypes><columnprototype bracketed="on">Operand</columnprototype> <columnprototype bracketed="on">masm=att</columnprototype> <columnprototype bracketed="on">OFFSET FLAT:.L2</columnprototype></columnprototypes>
<thead><row><entry command="headitem" spaces=" "><para>Operand </para></entry><entry command="tab" spaces=" "><para>masm=att </para></entry><entry command="tab" spaces=" "><para>masm=intel
</para></entry></row></thead><tbody><row><entry command="item" spaces=" "><para><code>%0</code>
</para></entry><entry command="tab" spaces=" "><para><code>%eax</code>
</para></entry><entry command="tab" spaces=" "><para><code>eax</code>
</para></entry></row><row><entry command="item" spaces=" "><para><code>%1</code>
</para></entry><entry command="tab" spaces=" "><para><code>$2</code>
</para></entry><entry command="tab" spaces=" "><para><code>2</code>
</para></entry></row><row><entry command="item" spaces=" "><para><code>%2</code>
</para></entry><entry command="tab" spaces=" "><para><code>$.L2</code>
</para></entry><entry command="tab" spaces=" "><para><code>OFFSET FLAT:.L2</code>
</para></entry></row></tbody></multitable>'''
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual(
            u'''=======  ========  ===================
Operand  masm=att  masm=intel
=======  ========  ===================
``%0``   ``%eax``  ``eax``
``%1``   ``$2``    ``2``
``%2``   ``$.L2``  ``OFFSET FLAT:.L2``
=======  ========  ===================
''',
            out)

    def test_multitable_without_header(self):
        xml_src = u'''<multitable spaces=" " endspaces=" ">
        <columnfractions line=" .25 .75">
          <columnfraction value=".25"/>
          <columnfraction value=".75"/>
        </columnfractions>
        <tbody>
          <row>
            <entry command="item" spaces=" ">
              <para>Objective-C type
</para>
            </entry>
            <entry command="tab" spaces=" ">
              <para>Compiler encoding
</para>
            </entry>
          </row>
          <row>
            <entry command="item">
              <smallexample endspaces=" ">
                <pre xml:space="preserve">int a[10];
</pre>
              </smallexample>
            </entry>
            <entry command="tab" spaces=" ">
              <para>
                <code>[10i]</code>
              </para>
            </entry>
          </row>
          <row>
            <entry command="item">
              <smallexample endspaces=" ">
                <pre xml:space="preserve">struct &lbrace;
  int i;
  float f[3];
  int a:3;
  int b:2;
  char c;
&rbrace;
</pre>
              </smallexample>
            </entry>
            <entry command="tab" spaces=" ">
              <para>
                <code>&lbrace;?=i[3f]b128i3b131i2c&rbrace;</code>
              </para>
            </entry>
          </row>
          <row>
            <entry command="item">
              <smallexample endspaces=" ">
                <pre xml:space="preserve">int a __attribute__ ((vector_size (16)));
</pre>
              </smallexample>
            </entry>
            <entry command="tab" spaces=" ">
              <para><code>![16,16i]</code> (alignment would depend on the machine)
</para>
            </entry>
          </row>
        </tbody>
      </multitable>'''

        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual(
            u'''+-------------------------------------------+-----------------------------------------------------+
|Objective-C type                           |Compiler encoding                                    |
+===========================================+=====================================================+
|.. code-block:: c++                        |                ``[10i]``                            |
|                                           |                                                     |
|  int a[10];                               |                                                     |
+-------------------------------------------+-----------------------------------------------------+
|.. code-block:: c++                        |                ``{?=i[3f]b128i3b131i2c}``           |
|                                           |                                                     |
|  struct {                                 |                                                     |
|    int i;                                 |                                                     |
|    float f[3];                            |                                                     |
|    int a:3;                               |                                                     |
|    int b:2;                               |                                                     |
|    char c;                                |                                                     |
|  }                                        |                                                     |
+-------------------------------------------+-----------------------------------------------------+
|.. code-block:: c++                        |``![16,16i]`` (alignment would depend on the machine)|
|                                           |                                                     |
|  int a __attribute__ ((vector_size (16)));|                                                     |
+-------------------------------------------+-----------------------------------------------------+
''',
            out)



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

#

class GccContext(Context):
    def preprocess(self, tree):
        class GccVisitor(NoopVisitor):
            def previsit_element(self, element):
                if element.kind == 'chapter':
                    for child in element.children:
                        if child.is_element('sectiontitle'):
                            text = child.get_sole_text()
                            if text:
                                if text.data == 'GNU Objective-C Features':
                                    element.default_language = 'objective-c'

        v = GccVisitor()
        v.visit(tree)
        return tree

# Entrypoint

if __name__ == '__main__':
    if len(sys.argv) < 2:
        unittest.main()
    else:
        with open(sys.argv[1]) as f_in:
            xml_src = f_in.read()
            tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, GccContext())
        if 1:
            with open('output/gcc.rst', 'w') as f_out:
                w = RstWriter(f_out, FileOpener('output'))
                w.visit(tree)
        else:
            w = RstWriter(sys.stdout)
            w.visit(tree)
