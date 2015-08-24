import os
import sys
import xml.dom.minidom

"""
gcc.xml created from a gcc build/gcc tree using:

makeinfo --xml -I ABSPATH_OF_SRC/gcc/doc/ -I ABSPATH_OF_SRC/gcc/doc/include ABSPATH_OF_SRC/gcc/doc/gcc.texi 

TODO:
  map back to the include structure of the underlying .texi files
"""

#tree = ET.parse('gcc.xml')
# can't handle 
# I get:
# xml.etree.ElementTree.ParseError: undefined entity &copyright;: line 97, column 16
#print(tree)

class Visitor:
    def visit(self, node, depth=0):
        #print('%s%s' %  (' ' * depth, node))
        if node.nodeType == node.ELEMENT_NODE:
            self.visit_element(node)
        elif node.nodeType == node.ATTRIBUTE_NODE:
            self.visit_attribute(node)
        elif node.nodeType == node.TEXT_NODE:
            self.visit_text(node)
        elif node.nodeType == node.CDATA_SECTION_NODE:
            self.visit_cdata_section(node)
        elif node.nodeType == node.ENTITY_NODE:
            self.visit_entity(node)
        elif node.nodeType == node.PROCESSING_INSTRUCTION_NODE:
            self.visit_pi(node)
        elif node.nodeType == node.COMMENT_NODE:
            self.visit_comment(node)
        elif node.nodeType == node.DOCUMENT_NODE:
            self.visit_document(node)
        elif node.nodeType == node.DOCUMENT_TYPE_NODE:
            self.visit_document_type(node)
        elif node.nodeType == node.NOTATION_NODE:
            self.visit_notation(node)
        if node.hasChildNodes():
            for child in node.childNodes:
                self.visit(child, depth + 1)

        if node.nodeType == node.ELEMENT_NODE:
            self.postvisit_element(node)

    def visit_element(self, node):
        raise NotImplementedError

    def postvisit_element(self, node):
        raise NotImplementedError

    def visit_attribute(self, node):
        raise NotImplementedError

    def visit_text(self, node):
        raise NotImplementedError

    def visit_cdata_section(self, node):
        raise NotImplementedError

    def visit_entity(self, node):
        raise NotImplementedError

    def visit_pi(self, node):
        raise NotImplementedError

    def visit_comment(self, node):
        raise NotImplementedError

    def visit_document(self, node):
        raise NotImplementedError

    def visit_document_type(self, node):
        raise NotImplementedError

    def visit_notation(self, node):
        raise NotImplementedError

class NoopVisitor(Visitor):
    def visit_element(self, node):
        pass

    def postvisit_element(self, node):
        pass

    def visit_attribute(self, node):
        pass

    def visit_text(self, node):
        pass

    def visit_cdata_section(self, node):
        pass

    def visit_entity(self, node):
        pass

    def visit_pi(self, node):
        pass

    def visit_comment(self, node):
        pass

    def visit_document(self, node):
        pass

    def visit_document_type(self, node):
        pass

    def visit_notation(self, node):
        pass

class RstNode:
    def __init__(self):
        self.children = []

    def write(self, f_out, depth=0):
        #f_out.write('%s%r\n' %  (' ' * depth, self))
        self.pre_write(f_out, depth)
        for child in self.children:
            child.write(f_out, depth + 1)
        self.post_write(f_out, depth)

    def pre_write(self, f_out, depth=0):
        pass

    def post_write(self, f_out, depth=0):
        pass

    def __repr__(self):
        return 'RstNode()'

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

    def write(self, f_out, depth=0):
        f_out.write ('.. include:: %s\n\n' % self.doc.name)

class RstComment(RstNode):
    def __init__(self, data):
        RstNode.__init__(self)
        self.data = data

    def __repr__(self):
        return 'RstComment(%r)' % self.data

    def write(self, f_out, depth=0):
        lines = self.data.splitlines()
        f_out.write('\n.. %s\n' % lines[0])
        for line in lines[1:]:
            f_out.write('   %s\n' % line)
        f_out.write('\n')

class RstTitle(RstNode):
    def __init__(self, underline):
        RstNode.__init__(self)
        self.underline = underline

    def pre_write(self, f_out, depth=0):
        f_out.write('\n\n')

    def post_write(self, f_out, depth=0):
        if len(self.children) == 1:
            if isinstance(self.children[0], RstText):
                len_ = len(self.children[0].data)
                f_out.write('\n%s\n' % (self.underline * len_))

class RstInlineMarkup(RstNode):
    def __init__(self, prefix, suffix):
        RstNode.__init__(self)
        self.prefix = prefix
        self.suffix = suffix

    def pre_write(self, f_out, depth=0):
        f_out.write(self.prefix)

    def post_write(self, f_out, depth=0):
        f_out.write(self.suffix)

class RstText(RstNode):
    def __init__(self, data):
        RstNode.__init__(self)
        self.data = data

    def __repr__(self):
        return 'RstText(%r)' % self.data

    def write(self, f_out, depth=0):
        f_out.write(self.data)

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

        if node.tagName == 'sectiontitle':
            child = RstTitle('=')
        elif node.tagName == 'command':
            child = RstInlineMarkup(':command:`', '`')
        else:
            child = RstNode()
        self.stack[-1].children.append(child)
        self.stack.append(child)

    def postvisit_element(self, node):
        self.stack.pop()

    def visit_comment(self, node):
        data = node.data
        print(repr(data))
        if data.startswith(' c '):
            data = data[3:]
        # Attempt to merge
        #   COMMENT(x) WHITESPACE(y) COMMENT(z)
        # into
        #   COMMENT(x + y + z)
        if len(self.stack[-1].children) >= 2:
            last = self.stack[-1].children[-1]
            penult = self.stack[-1].children[-2]
            print(penult)
            print(last)
            if isinstance(penult, RstComment):
                if isinstance(last, RstText):
                    if last.data.isspace():
                        self.stack[-1].children.pop()
                        penult.data = penult.data + last.data + data
                        return
        child = RstComment(data)
        self.stack[-1].children.append(child)

    def visit_text(self, node):
        child = RstText(node.data)
        self.stack[-1].children.append(child)

    def write_output(self, output_dir):
        for doc in self.documents:
            path = os.path.join(output_dir, doc.name)
            with open(path, 'w') as f_out:
                doc.write(f_out)

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

dom = xml.dom.minidom.parse(inputfile)
v = Texi2Rst(GccUninclusions())
v.visit(dom)
v.write_output(output_dir = 'output')
