from collections import OrderedDict
import os
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

class Element(Node):
    def __init__(self, kind, attrs):
        self.kind = kind
        self.attrs = attrs
        self.children = []

    def __repr__(self):
        return 'Element(%r, %r)' % (self.kind, self.attrs, )

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

'''
class RstDocument(RstNode):
    def __init__(self, name):
        RstNode.__init__(self)
        self.name = name

    def __repr__(self):
        return 'RstDocument(%r)' % self.name

class RstInclude(RstNode):
    def __init__(self, doc):
        RstNode.__init__(self)
        self.doc = doc

    def __repr__(self):
        return 'RstInclude(%r)' % self.doc.name

    def write(self, w, depth=0):
        w.write ('.. include:: %s\n\n' % self.doc.name)

class RstInlineMarkup(RstNode):
    def __init__(self, prefix, suffix):
        RstNode.__init__(self)
        self.prefix = prefix
        self.suffix = suffix

    def pre_write(self, w, depth=0):
        w.write(self.prefix)

    def post_write(self, w, depth=0):
        w.write(self.suffix)

class RstLiteralBlock(RstNode):
    def pre_write(self, w, depth=0):
        w.write('\n.. code-block:: c++\n') # FIXME: language
        w.indent += 1

    def post_write(self, w, depth=0):
        w.indent -= 1

class RstBlock(RstNode):
    def __init__(self, name, args):
        RstNode.__init__(self)
        self.name = name
        self.args = args

    def pre_write(self, w, depth=0):
        w.write('\n.. %s:: %s' % (self.name, self.args))
        w.indent += 1
        w.write('\n')

    def post_write(self, w, depth=0):
        w.indent -= 1

class RstText(RstNode):
    def __init__(self, data):
        RstNode.__init__(self)
        self.data = data

    def __repr__(self):
        return 'RstText(%r)' % self.data

    def write(self, w, depth=0):
        w.write(self.data)

class Texi2Rst(NoopVisitor):
    def __init__(self, uninclusions):
        self.uninclusions = uninclusions
        self.documents = []
        self.stack = []
        self.root = RstDocument('gcc.rst') # FIXME
        self.documents.append(self.root)
        self.stack.append(self.root)

    def visit_element(self, node):
        #sys.stdout.write('\n\n')
        if node.tagName == 'node':
            node_name = node.getAttributeNode('name').value
            if node_name in self.uninclusions.dict:
                print('splitting for node_name: %r' % node_name)
                texi_name = self.uninclusions.dict[node_name]
                new_doc = RstDocument(texi_name.replace('.texi', '.rst'))
                self.documents.append(new_doc)
                child = RstInclude(new_doc)
                self.stack[-1].children.append(child)
                self.stack.append(new_doc)

        elif node.tagName == 'indexterm':
            # Assume this the definition of an option, for now.
            # Though we really want to put the subsequent text inside this node
            child = RstBlock('option', 'FIXME')
        else:
            child = RstNode()
        self.stack[-1].children.append(child)
        self.stack.append(child)

    def postvisit_element(self, node):
        self.stack.pop()
'''

class Uninclusions:
    """
    "makeinfo --xml" processes @include directives.
    We want to undo this, and restore the original file structure
    """
    def __init__(self, dict_):
        self.dict = dict_

class GccUninclusions(Uninclusions):
    def __init__(self):
        # Assume a node with the given key (with some leading comments)
        dict_ = {'G++ and GCC' : 'frontends.texi',
                 # ends with text starting "Historically, compilers for many languages"

                 'Standards' : 'standards.texi',
                 'Invoking-GCC' : 'invoke.texi',
                 'C-Implementation' : 'implement-c.texi',
                 'C_002b_002b-Implementation' : 'implement-cxx.texi'}
        """
cppinternals.texi:5:@include gcc-common.texi
cpp.texi:9:@include gcc-common.texi
cpp.texi:4484:@include cppopts.texi
                 '<!-- c Options affecting the preprocessor -->
cpp.texi:4502:@include cppenv.texi
        @c Environment variables affecting the preprocessor
cpp.texi:4506:@include fdl.texi
extend.texi:8024:@include md.texi
gccint.texi:11:@include gcc-common.texi
gccint.texi:139:@include contribute.texi
gccint.texi:140:@include portability.texi
gccint.texi:141:@include interface.texi
gccint.texi:142:@include libgcc.texi
gccint.texi:143:@include languages.texi
gccint.texi:144:@include sourcebuild.texi
gccint.texi:145:@include options.texi
gccint.texi:146:@include passes.texi
gccint.texi:147:@include generic.texi
gccint.texi:148:@include gimple.texi
gccint.texi:149:@include tree-ssa.texi
gccint.texi:150:@include rtl.texi
gccint.texi:151:@include cfg.texi
gccint.texi:152:@include loop.texi
gccint.texi:153:@include md.texi
gccint.texi:154:@include tm.texi
gccint.texi:155:@include hostconfig.texi
gccint.texi:156:@include fragments.texi
gccint.texi:157:@include collect2.texi
gccint.texi:158:@include headerdirs.texi
gccint.texi:159:@include gty.texi
gccint.texi:160:@include plugins.texi
gccint.texi:161:@include lto.texi
gccint.texi:162:@include match-and-simplify.texi
gccint.texi:164:@include funding.texi
gccint.texi:165:@include gnu.texi
gccint.texi:166:@include gpl_v3.texi
gccint.texi:172:@include fdl.texi
gccint.texi:174:@include contrib.texi
gcc.texi:25:@include gcc-common.texi
gcc.texi:160:@include frontends.texi
gcc.texi:161:@include standards.texi
gcc.texi:164:@include implement-cxx.texi
gcc.texi:165:@include extend.texi
gcc.texi:166:@include objc.texi
gcc.texi:167:@include compat.texi
gcc.texi:168:@include gcov.texi
gcc.texi:169:@include gcov-tool.texi
gcc.texi:170:@include trouble.texi
gcc.texi:171:@include bugreport.texi
gcc.texi:172:@include service.texi
gcc.texi:173:@include contribute.texi
gcc.texi:175:@include funding.texi
gcc.texi:176:@include gnu.texi
gcc.texi:177:@include gpl_v3.texi
gcc.texi:183:@include fdl.texi
gcc.texi:185:@include contrib.texi
grep: include: Is a directory
install.texi:10:@include gcc-common.texi
install.texi:4958:@include install-old.texi
install.texi:4970:@include fdl.texi
invoke.texi:7:@include gcc-vers.texi
invoke.texi:1584:@include @value{srcdir}/../libiberty/at-file.texi
invoke.texi:11095:@include cppopts.texi
invoke.texi:13590:@include avr-mmcu.texi
invoke.texi:24297:@include cppenv.texi
passes.texi:988:@include optinfo.texi
sourcebuild.texi:19:@include configterms.texi
sourcebuild.texi:274:@include configfiles.texi
sourcebuild.texi:284:@include makefile.texi
        """
        Uninclusions.__init__(self, dict_)

inputfile = 'gcc.xml'
output_dir = 'output'

#dom = xml.dom.minidom.parse(inputfile)

#tree = convert_from_xml(dom)
#tree.dump(sys.stdout)

#tree = texi2rst(tree)

#v = Texi2Rst(GccUninclusions())
#v.visit(dom)
#v.write_output(output_dir = 'output')

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
                              'paragraphindent'):
                return True
            else:
                return False

    v = Pruner()
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

def fixup_option_descriptions(tree):
    """
    Options come in the form:

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
    """
    class OptionDescFixer(NoopVisitor):
        def previsit_element(self, element):
            if element.kind == 'tableentry':
                tableterm = element.first_element_named('tableterm')
                tableitem = element.first_element_named('tableitem')
                if tableterm and tableitem:
                    item = tableterm.first_element_named('item')
                    if item:
                        itemformat = item.first_element_named('itemformat')
                        if itemformat:
                            text = itemformat.get_sole_text()
                            if text:
                                self.convert_to_directive(element,
                                                          tableitem,
                                                          text.data)

        def convert_to_directive(self, tableentry, tableitem, itemformat_text):
            # Start with a dummy value for "args":
            tableentry.rst_kind = Directive('option', None)

            options = [itemformat_text]

            # Strip away tableterm, adding content to
            # the directive, and gathering options:
            new_children = []
            for child in tableitem.children:
                if isinstance(child, Element):
                    if child.kind == 'indexcommand':
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

            # Update the directive args to include all the options found:
            tableentry.rst_kind.args = ', '.join(options)

            tableentry.children = new_children

    v = OptionDescFixer()
    v.visit(tree)
    return tree

def fixup_examples(tree):
    class ExampleFixer(NoopVisitor):
        def previsit_element(self, element):
            if element.kind in ('example', 'smallexample'):
                pre = element.first_element_named('pre')
                if pre:
                    text = pre.get_sole_text()
                    if text:
                        lang = self.guess_language(text.data)
                        element.rst_kind = Directive('code-block', lang)

        def guess_language(self, data):
            if 'DO ' in data:
                return 'fortran'
            if data.startswith('gcc '):
                return 'bash'
            return 'c++'

    v = ExampleFixer()
    v.visit(tree)
    return tree

def fixup_titles(tree):
    class TitleFixer(NoopVisitor):
        def previsit_element(self, element):
            if element.kind == 'sectiontitle':
                element.rst_kind = Title(element, '=')
            elif element.kind == 'subsubheading':
                element.rst_kind = Title(element, '^')

    v = TitleFixer()
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

# Top-level conversion routine

def convert_to_rst(tree):
    tree = fixup_comments(tree)
    tree = prune(tree)
    tree = fixup_option_refs(tree)
    tree = fixup_option_descriptions(tree)
    tree = fixup_examples(tree)
    tree = fixup_titles(tree)
    tree = fixup_lists(tree)
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

    def before(self, w):
        w.write(':%s:`' % self.name)

    def after(self, w):
        w.write('`')

class Title(RstKind):
    def __init__(self, element, underline):
        self.element = element
        self.underline = underline

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

    def before(self, w):
        w.write('\n.. %s:: %s\n\n' % (self.name, self.args))
        w.indent += 1

    def after(self, w):
        w.indent -= 1

class ListItem(RstKind):
    def __init__(self, bullet):
        self.bullet = bullet

    def before(self, w):
        w.write('%s ' % (self.bullet, ))
        w.indent += 1

    def after(self, w):
        w.indent -= 1

# Output of a converted tree to .rst file

class RstWriter(Visitor):
    def __init__(self, f_out):
        self.f_out = f_out
        self.indent = 0

    def write(self, text):
        text = text.replace('\n',
                            '\n%s' % ('  ' * self.indent))
        self.f_out.write(text)

    def previsit_element(self, element):
        if hasattr(element, 'rst_kind'):
            element.rst_kind.before(self)
        elif element.kind == 'document':
            pass
        elif element.kind == 'texinfo':
            pass
        elif element.kind == 'command':
            self.write(':command:`')
        elif element.kind == 'var':
            self.write('``')
        elif element.kind == 'code':
            self.write('``')
        else:
            pass
            #raise ValueError('unhandled element: %r' % (element, ))

    def postvisit_element(self, element):
        if hasattr(element, 'rst_kind'):
            element.rst_kind.after(self)
        if element.kind == 'command':
            self.write('`')
        elif element.kind == 'var':
            self.write('``')
        elif element.kind == 'code':
            self.write('``')

    def visit_comment(self, comment):
        lines = comment.data.splitlines()
        self.write('\n.. %s\n' % lines[0])
        for line in lines[1:]:
            self.write('   %s\n' % line)
        self.write('\n')

    def visit_text(self, text):
        self.write(text.data)

# Unit tests

class Texi2RstTests(unittest.TestCase):
    def make_rst_string(self, doc):
        w = RstWriter(StringIO.StringIO())
        w.visit(doc)
        return w.f_out.getvalue()

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
        self.assertEqual(u'\n\n.. First line \n   Second line \n\n\n', out)

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

class InlineMarkupTests(Texi2RstTests):
    def test_command(self):
        xml_src = '<texinfo>Before <command>gcc</command> after</texinfo>'
        doc = from_xml_string(xml_src)
        out = self.make_rst_string(doc)
        self.assertEqual(u'Before :command:`gcc` after', out)

    def test_var(self):
        xml_src = '<texinfo>Before <var>gcc</var> after</texinfo>'
        doc = from_xml_string(xml_src)
        out = self.make_rst_string(doc)
        self.assertEqual(u'Before ``gcc`` after', out)

    def test_code(self):
        xml_src = '<texinfo>Before <code>gcc</code> after</texinfo>'
        doc = from_xml_string(xml_src)
        out = self.make_rst_string(doc)
        self.assertEqual(u'Before ``gcc`` after', out)

class TitleTests(Texi2RstTests):
    def test_section_title(self):
        xml_src = ('<texinfo><sectiontitle>A section title</sectiontitle>'
                   + '<para>some text</para></texinfo>')
        doc = from_xml_string(xml_src)
        doc = fixup_titles(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'\nA section title\n===============\n\nsome text',
                         out)

    def test_subsubheading(self):
        xml_src = ('<texinfo><subsubheading>A sub-sub-heading</subsubheading>'
                   + '<para>some text</para></texinfo>')
        doc = from_xml_string(xml_src)
        doc = fixup_titles(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'\nA sub-sub-heading\n^^^^^^^^^^^^^^^^^\n\nsome text',
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
        doc = fixup_option_descriptions(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(
            u'''

.. option:: -Wunused-label, -Wno-unused-label


  
  Warn whenever a label is declared but not used.
  This warning is enabled by -Wall.
  
  To suppress this warning use the ``unused`` attribute.
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
            (u'''
.. code-block:: fortran


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
            (u'''
.. code-block:: bash


  gcc -c -Q -O3 --help=optimizers > /tmp/O3-opts
  gcc -c -Q -O2 --help=optimizers > /tmp/O2-opts
  diff /tmp/O2-opts /tmp/O3-opts | grep enabled
  '''),
            out)

class ListTests(Texi2RstTests):
    def test_bulleted(self):
        xml_src = ("""
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
""")
        doc = from_xml_string(xml_src)
        doc = fixup_lists(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(
            (u'''
* Empty.  Empty attributes are ignored.
  
* An attribute name
  (which may be an identifier such as ``unused``, or a reserved
  word such as ``const``).
  
  
* An attribute name followed by a parenthesized list of
  parameters for the attribute.
  These parameters take one of the following forms:
  
  
'''),
            out)




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
                w = RstWriter(f_out)
                w.visit(tree)
        else:
            w = RstWriter(sys.stdout)
            w.visit(tree)
