#!/usr/bin/env python3

import argparse
import io
import os
import re
import sys
import xml.dom.minidom
from collections import OrderedDict

from node import Comment, Element, NoopVisitor, Text, Visitor

"""
gcc.xml created from a gcc build/gcc tree using:

makeinfo --xml -I ABSPATH_OF_SRC/gcc/doc/ -I ABSPATH_OF_SRC/gcc/doc/include ABSPATH_OF_SRC/gcc/doc/gcc.texi

TODO:
  map back to the include structure of the underlying .texi files
"""

args = None
detected_option_directives = {}


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
    xml_src = xml_src.replace('&arobase;', '@')
    xml_src = xml_src.replace('&bullet;', '*')
    xml_src = xml_src.replace('&copyright;', '(C)')
    xml_src = xml_src.replace('&dots;', '...')
    xml_src = xml_src.replace('&enddots;', '…')
    xml_src = xml_src.replace('&eosperiod;', '.')
    xml_src = xml_src.replace('&comma;', ',')
    xml_src = xml_src.replace('&equiv;', '==')
    xml_src = xml_src.replace('&lbrace;', '{')
    xml_src = xml_src.replace('&linebreak;', '\n')
    xml_src = xml_src.replace('&rbrace;', '}')
    xml_src = xml_src.replace('&slashbreak;', '')
    xml_src = xml_src.replace('&minus;', '-')
    xml_src = xml_src.replace('&nbsp;', ' |nbsp| ')
    xml_src = xml_src.replace('&noeos;', '')
    xml_src = xml_src.replace('&tex;', 'Tex')
    xml_src = xml_src.replace('&textmdash;', '---')
    xml_src = xml_src.replace('&textndash;', '--')
    xml_src = xml_src.replace('&textldquo;', "'")
    xml_src = xml_src.replace('&textrdquo;', "'")
    xml_src = xml_src.replace('&textlsquo;', "'")
    xml_src = xml_src.replace('&textrsquo;', "'")
    xml_src = xml_src.replace('&eosquest;', '?')
    xml_src = xml_src.replace('&expansion;', '→')
    xml_src = xml_src.replace('&result;', '⇒')
    xml_src = xml_src.replace('&errorglyph;', 'error')
    xml_src = xml_src.replace('\\u2018', '‘')
    xml_src = xml_src.replace('\\u2019', '’')

    # It is used in manual pages
    xml_src = xml_src.replace('@dots{}', '...')

    # Complain about any entities still present
    for m in re.finditer('(&[a-z]+;)', xml_src):
        BUILTIN_XML_ENTITIES = ('&quot;', '&amp;', '&apos;', '&lt;', '&gt;')
        if m.group(1) not in BUILTIN_XML_ENTITIES:
            raise ValueError('Unhandled entity: %r' % m.group(1))

    dom = xml.dom.minidom.parseString(xml_src)
    tree = convert_from_xml(dom)
    tree = fixup_whitespace(tree)
    return tree


def fixup_whitespace(tree):
    class WhitespaceFixer(NoopVisitor):
        """
        Strip redundant Text nodes
        """
        def previsit_element(self, element, parents):
            if element.kind in ('pre', 'definitionterm'):
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

    WhitespaceFixer().visit(tree)
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
        def ignore_comment(self, line):
            if (line.startswith('Copyright ') or line.startswith('This is part')
                    or line.startswith('For copying conditions')):
                return True
            return False

        def previsit_element(self, element, parents):
            # Attempt to merge
            #   COMMENT(x) COMMENT(y)
            # into
            #   COMMENT(x + '\n' + y)
            new_children = []
            for child in element.children:
                if isinstance(child, Comment):
                    if 'hook-start' in child.data or 'hook-end' in child.data:
                        return
                    text = child.data
                    if self.ignore_comment(text):
                        continue
                    if text.lstrip().startswith('comment') or text.startswith('man '):
                        continue
                    if len(new_children) >= 1:
                        last = new_children[-1]
                        if isinstance(last, Comment):
                            last.data = last.data + '\n' + text
                            continue
                new_children.append(child)
            element.children = new_children

    CommentCombiner().visit(tree)
    return tree


def fixup_comments(tree):
    tree = convert_comments(tree)
    tree = combine_commments(tree)
    return tree


def prune(tree):
    class Pruner(NoopVisitor):
        def previsit_element(self, element, parents):
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
                              'dircategory', 'direntry', 'vskip',
                              'titlepage',
                              'set', 'macro', 'settitle',
                              'defcodeindex', 'syncodeindex',
                              'paragraphindent',
                              'nodenext', 'nodeprev', 'nodeup'):
                return True
            else:
                return False

    Pruner().visit(tree)
    return tree


def convert_text_to_label(data):
    data = data.replace(' ', '-')
    data = data.replace('\n', '-')
    data = data.replace('/', '-')
    data = data.replace('#', '')
    data = data.lstrip('_')
    data = data.lower()
    return data


def is_directive(element, name):
    return isinstance(element.rst_kind, Directive) and element.rst_kind.name == name


def is_movable_index(element):
    return (element.kind in ('cindex', 'findex', 'vindex', 'kindex', 'indexcommand')
            and len(element.children) == 1 and is_directive(element.children[0], 'index'))


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
        def previsit_element(self, element, parents):
            if element.kind == 'menu':
                element.rst_kind = Directive('toctree')

            if element.kind == 'menuentry':
                menunode = element.first_element_named('menunode')
                menudescription = element.first_element_named('menudescription')
                if menunode and menudescription:
                    # Prune the menuentry, giving it an explicit title.
                    element.rst_kind = ToctreeEntry()
                    element.children = menudescription.children
                    # FIXME: express this cross-reference at the Node level:
                    data = menunode.get_all_text()
                    label = convert_text_to_label(data)
                    element.children = [Text(label)]

    MenuFixer().visit(tree)
    return tree


def split(tree):
    class Splitter(NoopVisitor):
        MAPPING = {
                'target-description-macros-and-functions': 'target-macros',
                'built-in-functions-specific-to-particular-target-machines': 'target-builtins',
                'runtime-influencing-runtime-behavior-with-environment-variables': 'runtime'
        }

        def __init__(self):
            self.split_kinds = ('chapter', 'section', )

        @classmethod
        def _prune_filename(cls, text):
            if '--' in text:
                text = text.split('--')[0]
            text = text.lower()
            for c in ' /':
                text = text.replace(c, '-')
            for c in "()?',.:_":
                text = text.replace(c, '')
            text = text.strip('+').strip('-')
            text = text.replace('[no-changes]-', '')
            text = text.replace('[new]-', '')
            text = text.replace('#', '')
            text = re.sub(r'-+', '-', text)

            if text in cls.MAPPING:
                return cls.MAPPING[text]

            return text

        def should_split(self, element, text, parent_text):
            if element.kind in self.split_kinds:
                return True
            # split '$target Option' subsections
            elif (args and 'gcc.xml' in args.xml_file and element.kind == 'subsection'
                    and (text.endswith('Options')
                         or text.endswith('Function Attributes')
                         or text == 'Options for System V'
                         or parent_text == 'Built-in Functions Specific to Particular Target Machines')):
                return True
            elif (args and 'gccint.xml' in args.xml_file and element.kind == 'subsection'
                    and parent_text in ('The gcc Subdirectory', 'Directives used within DejaGnu tests',
                                        'Tuple specific accessors', 'Defining the Output Assembler Language',
                                        'Stack Layout and Calling Conventions')):
                return True
            elif text == 'Contributors to GCC':
                return True
            elif (args and 'gm2.xml' in args.xml_file and element.kind == 'subsection'):
                return True
            else:
                return False

        def previsit_element(self, element, parents):
            sectiontitle = element.first_element_named('sectiontitle')
            text = sectiontitle.get_all_text() if sectiontitle else None
            psectiontitle = parents[-1].first_element_named('sectiontitle') if parents else None
            parent_text = psectiontitle.get_all_text() if psectiontitle else None
            if self.should_split(element, text, parent_text):
                if text:
                    element.rst_kind = OutputFile(self._prune_filename(text))

    class ToctreeAdder(NoopVisitor):
        """
        Add toctree directives referencing the split content
        """
        def previsit_element(self, element, parents):
            new_children = []
            toctree = None
            for child in element.children:
                if isinstance(child, Element):
                    if is_directive(child, 'toctree'):
                        toctree = child
                    if isinstance(child.rst_kind, OutputFile):
                        toctree_element = Element('toctree-element', {})
                        toctree_element.rst_kind = ToctreeEntry()
                        toctree_element.children = [Text(child.rst_kind.name)]
                        # Try to consolidate all toctree entries into one
                        # toctree:
                        if toctree:
                            if not self.contains_toc_element(toctree, toctree_element.get_all_text()):
                                toctree.children.append(toctree_element)
                        else:
                            toctree = Element('toctree', {})
                            toctree.rst_kind = Directive('toctree')
                            toctree.children = [toctree_element]
                            new_children.append(toctree)

                new_children.append(child)
            element.children = new_children

        @staticmethod
        def contains_toc_element(toctree, refname):
            for child in toctree.children:
                if child.get_all_text() == refname:
                    return True
            return False

    Splitter().visit(tree)
    ToctreeAdder().visit(tree)
    return tree


def fixup_merge_toctree(tree):
    class MergeToctreeFixer(NoopVisitor):
        def __init__(self):
            self.seen_toctree_entries = set()

        def previsit_element(self, element, parents):
            if isinstance(element.rst_kind, ToctreeEntry):
                name = element.get_all_text()
                if name in self.seen_toctree_entries:
                    parents[-1].children.remove(element)
                else:
                    self.seen_toctree_entries.add(name)

    class MergeTreeRootFixer(NoopVisitor):
        def previsit_element(self, element, parents):
            if is_directive(element, 'toctree'):
                if not element.children:
                    parents[-1].children.remove(element)

    class ToctreeFolderVisitor(NoopVisitor):
        def __init__(self):
            self.output_file = None
            self.mapping = {}

        def previsit_element(self, element, parents):
            if isinstance(element.rst_kind, OutputFile):
                self.output_file = element.rst_kind.name
            elif isinstance(element.rst_kind, ToctreeEntry):
                name = element.get_all_text()
                self.mapping.setdefault(self.output_file, []).append(name)

    class ToctreeFolderCreator(NoopVisitor):
        def __init__(self, mapping):
            self.mapping = mapping

        @classmethod
        def _get_components(cls, parents):
            return [o.rst_kind.name for o in parents if isinstance(o.rst_kind, OutputFile) and o.rst_kind.folder]

        def previsit_element(self, element, parents):
            if isinstance(element.rst_kind, OutputFile):
                name = element.rst_kind.name
                if name in self.mapping and len(self.mapping[name]) >= 5:
                    element.rst_kind.folder = True
                element.rst_kind.path_components = self._get_components(parents)
            elif isinstance(element.rst_kind, ToctreeEntry):
                for parent in reversed(parents):
                    if isinstance(parent.rst_kind, OutputFile):
                        if parent.rst_kind.folder:
                            text = element.get_first_text()
                            text.data = parent.rst_kind.name + '/' + text.data
                        break

    MergeToctreeFixer().visit(tree)
    MergeTreeRootFixer().visit(tree)

    foldercreator = ToctreeFolderVisitor()
    foldercreator.visit(tree)
    ToctreeFolderCreator(foldercreator.mapping).visit(tree)
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
        def previsit_element(self, element, parents):
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
                print(i, parent, child)
            if child.is_element('node') or child.is_element('anchor'):

                def get_next_child_element():
                    for _, cand_child in edges[i + 1:]:  # noqa: B023
                        if isinstance(cand_child, Element):
                            return cand_child

                next_parent = get_next_child_element()
                if next_parent:
                    if ctxt.debug:
                        print('\nMOVING %r from %r to %r\n'
                              % (child, parent, next_parent))
                    parent.children.remove(child)
                    next_parent.children.insert(0, child)

    NodeFixer().visit(tree)

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
        def previsit_element(self, element, parents):
            if element.kind == 'option':
                firstchild = element.children[0]
                if isinstance(firstchild, Text):
                    if firstchild.data.startswith('-'):
                        element.rst_kind = InlineMarkup('option')

    OptionRefFixer().visit(tree)
    return tree


def fixup_empty_texts(tree):
    class EmptyTextFixer(NoopVisitor):
        # Remove all empty Text elements.
        def previsit_element(self, element, parents):
            element.children = [c for c in element.children if not isinstance(c, Text) or c.data]

    EmptyTextFixer().visit(tree)
    return tree


def fixup_ignored_strings(tree):
    class IgnoredTextFixer(NoopVisitor):
        IGNORED = ('Keyword Index', 'Concept Index', 'Index of Directives', 'Library Index')

        def __init__(self):
            self.first_section_seen = False

        def previsit_element(self, element, parents):
            # Remove all <itemprepend>&bullet;</itemprepend>
            if (element.kind == 'itemprepend'
                    or (element.kind == 'sectiontitle' and element.get_all_text() in self.IGNORED)):
                parents[-1].children.remove(element)
            elif element.kind == 'sectiontitle':
                self.first_section_seen = True

            if not self.first_section_seen and element.kind == 'para' and args:
                parents[-1].children.remove(element)

    IgnoredTextFixer().visit(tree)
    return tree


def fixup_vars_in_samps(tree):
    class VarsInSampsFixer(NoopVisitor):
        def previsit_element(self, element, parents):
            if element.kind in ('samp', 'file'):
                for i, child in enumerate(element.children):
                    if isinstance(child, Element) and child.kind == 'var':
                        element.children[i] = Text(child.get_all_text())

    VarsInSampsFixer().visit(tree)
    return tree


def fixup_element_spacing(tree):
    class ElementSpacingFixer(NoopVisitor):
        ALLOWED_CHARS_AFTER = (' ', '\n', '.', ',', ')')
        ALLOWED_CHARS_BEFORE = (' ', '\n', '(')

        @staticmethod
        def element_needs_space_p(element):
            return element.is_element('r') or (isinstance(element, Element) and element.kind == 'code')

        # Wrap option and var elements with a space character
        def postvisit_element(self, element, parents):
            if element.kind in ('option', 'var', 'code'):
                parent = parents[-1]
                i = parent.children.index(element)
                if i + 1 < len(parent.children):
                    rsibling = parent.children[i + 1]
                    if isinstance(rsibling, Text):
                        if not rsibling.data[0] in self.ALLOWED_CHARS_AFTER:
                            rsibling.data = ' ' + rsibling.data
                    elif self.element_needs_space_p(rsibling):
                        parent.children.insert(i + 1, Text(' '))
                if i > 0:
                    lsibling = parent.children[i - 1]
                    if isinstance(lsibling, Text):
                        if not lsibling.data[-1] in self.ALLOWED_CHARS_BEFORE:
                            lsibling.data += ' '
                    elif self.element_needs_space_p(lsibling):
                        parent.children.insert(i - 1, Text(' '))

    ElementSpacingFixer().visit(tree)
    return tree


def fixup_machine_dependant_options(tree):
    class MachineDependantOptionFixer(NoopVisitor):
        def __init__(self):
            self.parent_seen = False

        def previsit_element(self, element, parents):
            if isinstance(element.rst_kind, OutputFile):
                if (isinstance(parents[-1].rst_kind, OutputFile)
                        and parents[-1].rst_kind.name == 'machine-dependent-options'):
                    # Skip anchor and maybe index elements
                    start = 1
                    while start < len(element.children) and is_movable_index(element.children[start]):
                        start += 1
                    name = element.children[start].get_all_text()
                    name = name.replace(' Options', '').replace('Options for ', '')

                    program = Element('program', {})
                    program.rst_kind = Directive('program', name)
                    element.children.insert(0, program)

        def postvisit_element(self, element, parents):
            # add newline before all Machine-Dependent Options subsections
            text = element.get_all_text()
            if element.kind == 'emph' and text.endswith('Options'):
                parent = parents[-1]
                if text == 'Machine-Dependent Options':
                    self.parent_seen = True
                elif self.parent_seen:
                    parent.children.insert(parent.children.index(element) - 2, Text('\n'))

    MachineDependantOptionFixer().visit(tree)
    return tree


def fixup_params(tree):
    class ParamFixer(NoopVisitor):
        def __init__(self):
            self.in_param_option = False

        def previsit_element(self, element, parents):
            if (element.kind == 'option' and is_directive(element, 'option')):
                if '--param' in element.rst_kind.args:
                    self.in_param_option = True
                else:
                    self.in_param_option = False
            elif self.in_param_option and element.kind == 'code' and parents[-1].kind == 'item':
                element.rst_kind = Directive('gcc-param', element.get_all_text())
                element.children = []

    ParamFixer().visit(tree)
    return tree


def fixup_text_variables(tree):
    class TextVariableFixer(NoopVisitor):
        REPLACEMENTS = (('$$VERSION_PACKAGE$$', '|package_version|'),
                        ('$$version-GCC$$', '|gcc_version|',),
                        ('$$BUGURL$$', '|bugurl|'))

        def previsit_element(self, element, parents):
            for child in element.children:
                if isinstance(child, Text):
                    for k, v in self.REPLACEMENTS:
                        child.data = child.data.replace(k, v)

    TextVariableFixer().visit(tree)
    return tree


def fixup_fortran_functions(tree):
    class FortranFunctionFixer(NoopVisitor):
        def _convert_section(self, element, parents):
            NEEDLES = ('Function ABI Documentation', 'Intrinsic Procedures', 'Non-Fortran Main Program')
            if parents:
                sectiontitle = parents[-1].first_element_named('sectiontitle')
                if (sectiontitle
                        and sectiontitle.get_all_text() in NEEDLES
                        and element.kind in ('section', 'subsection')):
                    return True
            return False

        def previsit_element(self, element, parents):
            if self._convert_section(element, parents):
                stitle = element.first_element_named('sectiontitle').get_all_text()
                if '---' in stitle:
                    tableentry = element.first_element_named('table')
                    function = stitle.split('---')[0].strip()
                    tableentry.rst_kind = Directive('function', function)
                    newchildren = []
                    newchildren2 = []
                    fname_fixed = False
                    for table in tableentry.children:
                        assert table.kind == 'tableentry'
                        if is_directive(table, 'envvar'):
                            table.rst_kind = Directive('note')
                            newchildren2.append(table)
                            continue
                        tterm = table.first_element_named('tableterm')
                        titem = table.first_element_named('tableitem')
                        if not tterm:
                            newchildren2.append(table)
                            continue
                        termname = tterm.get_all_text().strip('{}:')
                        if termname == 'Description':
                            para = titem.first_element_named('para')
                            newchildren.append(para)
                            code = para.first_element_named('code')
                            if code:
                                code = code.get_all_text()
                                if code.startswith(function):
                                    tableentry.rst_kind.args = code
                                    fname_fixed = True
                        elif termname == 'Return value':
                            ret = Element('param')
                            ret.rst_kind = FnDirective('return')
                            ret.children = [titem.first_element_named('para')]
                            newchildren.append(ret)
                        elif termname == 'Arguments':
                            body = titem.get_all_elements('tbody')
                            if body:
                                body = body[0]
                                for row in body.children:
                                    if len(row.children) != 2:
                                        continue
                                    name = row.children[0].get_all_text().strip('{} ')
                                    value = row.children[1].first_element_named('para')
                                    param = Element('param')
                                    param.rst_kind = FnDirective(f'param {name}')
                                    param.children = [value]
                                    newchildren.append(param)
                            else:
                                newchildren2.append(table)
                        elif termname == 'Syntax':
                            if stitle.startswith('_gfortran_'):
                                tableentry.rst_kind.args = titem.get_all_text().replace('\n', ' ')
                            else:
                                last = titem.get_all_text().strip().splitlines()[-1]
                                # Handle things like: RESULT = MINLOC(ARRAY [, MASK], [,KIND] [,BACK])
                                if not fname_fixed:
                                    last = last.replace('CALL ', '')
                                    if '=' in last:
                                        last = last.split('=')[-1].strip()
                                    last = last.replace('[', '').replace(']', '')
                                    tableentry.rst_kind.args = last
                                    fname_fixed = True
                                code = Element('syntax')
                                code.rst_kind = Directive('code-block', 'fortran')
                                code.children = [Text(titem.get_all_text())]
                                block = Element('block')
                                block.rst_kind = DefinitionListBody()
                                block.children = [code]
                                tterm.children.append(block)
                                newchildren2.append(tterm)
                        else:
                            newchildren2.append(table)

                    tableentry.children = newchildren + newchildren2

    class OpenMPFixer(NoopVisitor):
        def previsit_element(self, element, parents):
            if parents:
                sectiontitle = parents[-1].first_element_named('sectiontitle')
                if (sectiontitle and sectiontitle.get_all_text() == 'OpenMP Modules OMP_LIB and OMP_LIB_KINDS'):
                    if element.kind == 'table':
                        text = '\n'.join(x.get_all_text() for x in element.get_all_elements('asis'))
                        code_block = Element('cb')
                        code_block.rst_kind = Directive('code-block')
                        code_block.children = [Text(text)]
                        element.children = [code_block]

    FortranFunctionFixer().visit(tree)
    OpenMPFixer().visit(tree)
    return tree


def fixup_libquadmath(tree):
    class LibQuadMathFixer(NoopVisitor):
        def previsit_element(self, element, parents):
            NEEDLES = ('Typedef and constants', 'Math Library Routines')
            if parents:
                sectiontitle = parents[-1].first_element_named('sectiontitle')
                if sectiontitle and sectiontitle.get_all_text() in NEEDLES:
                    if element.kind == 'table':
                        for item in element.get_all_elements('item'):
                            parts = item.get_all_text().split(':')
                            assert len(parts) == 2
                            samp = Element('samp')
                            samp.rst_kind = InlineMarkup('samp')
                            samp.children = [Text(parts[0])]
                            item.children = [Text('* '), samp, Text(f': {parts[1]}\n')]

    LibQuadMathFixer().visit(tree)
    return tree


def fixup_merge_functions(tree):
    class MergeFunctionFixer(NoopVisitor):
        def previsit_element(self, element, parents):
            if is_directive(element, 'function') and not element.children:
                children = parents[-1].children
                i = children.index(element)
                if i + 1 < len(children):
                    sibling = children[i + 1]
                    if is_directive(sibling, 'function'):
                        spaces = len(sibling.rst_kind.name) + 6
                        sibling.rst_kind.args = element.rst_kind.args + f'\n{" " * spaces}' + sibling.rst_kind.args
                        element.rst_kind = None

    MergeFunctionFixer().visit(tree)
    return tree


def fixup_option_listing(tree):
    class OptionListingFixer(NoopVisitor):
        def __init__(self):
            self.seen = False

        def previsit_element(self, element, parents):
            if element.kind == 'tableitem' and 'AArch64 Options' in element.get_all_text() and not self.seen:
                self.seen = True
                target = None
                for child in list(element.children):
                    if child.kind == 'para':
                        target = child.get_all_text().strip()
                        target = target.replace(' Options', '').replace('Options for ', '')
                        i = element.children.index(child)
                        program = Element('program')
                        program.rst_kind = Directive('program', target)
                        element.children.insert(i + 1, program)

                program = Element('program')
                program.rst_kind = Directive('program', 'None')
                element.children.append(program)

    OptionListingFixer().visit(tree)
    return tree


def fixup_licenses(tree):
    class LicenseFixer(NoopVisitor):
        def previsit_element(self, element, parents):
            # skip ignores with License description
            if element.kind == 'ignore':
                text = element.get_all_text()
                if ('@settitle GNU Free Documentation License' in text
                        or '@settitle GNU General Public License' in text):
                    element.children = []
            elif element.kind == 'unnumbered':
                sectiontitle = element.first_element_named('sectiontitle')
                if sectiontitle:
                    section = sectiontitle.get_all_text()
                    if (section == 'GNU Free Documentation License'
                            or section == 'GNU General Public License'
                            or section == 'Funding Free Software'):
                        element.children = []

            # Rename license files
            elif isinstance(element.rst_kind, ToctreeEntry):
                name = element.get_all_text()
                if name == 'copying':
                    element.children = [Text('general-public-license-3')]

    LicenseFixer().visit(tree)
    return tree


def fixup_quoting(tree):
    class QuoteFixer(NoopVisitor):
        def previsit_element(self, element, parents):
            for child in element.children:
                if isinstance(child, Text):
                    if isinstance(element.rst_kind, Title) or not element.rst_kind:
                        child.data = child.data.replace('*', '\\*')
                    elif isinstance(element.rst_kind, InlineMarkup):
                        child.data = child.data.replace('\\', '\\\\')

    QuoteFixer().visit(tree)
    return tree


def fixup_wrapped_options(tree):
    class WrapperOptionFixer(NoopVisitor):
        # Move out all inner elements in option nodes as siblings:
        # <option>-foo=<var>n</var></option>.
        def postvisit_element(self, element, parents):
            if isinstance(element.rst_kind, InlineMarkup) and element.kind == 'option':
                element.children = [Text(element.get_all_text())]

    WrapperOptionFixer().visit(tree)
    return tree


def fixup_inline_option(tree):
    class InlineOptionFixer(NoopVisitor):
        def postvisit_element(self, element, parents):
            if element.kind == 'option':
                parent = parents[-1]
                i = parent.children.index(element)
                if i == len(parent.children) - 1:
                    return
                sib = parent.children[i + 1]
                if not isinstance(sib, Text) and isinstance(sib.rst_kind, InlineMarkup):
                    text = sib.get_all_text()
                    # TODO: a bit hack
                    if text[0] == '{' and text[-1] == '}':
                        text = text[1:-1]
                    element.children += [Text(text)]
                    parent.children.remove(sib)

    InlineOptionFixer().visit(tree)
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
        def previsit_element(self, element, parents):
            # Convert:
            #   <itemformat command="COMMAND">TEXT</itemformat>
            # into:
            #   <COMMAND>TEXT</command>
            # which will typically be later converted to an
            # appropriate markup form.
            if element.kind == 'itemformat':
                if 'command' in element.attrs:
                    command = element.attrs['command']
                    # Typically we can't nest inline markup, but
                    # Sphinx's "samp" supports this syntax:
                    #   :samp:`print 1+{variable}`
                    # (http://sphinx-doc.org/markup/inline.html#role-samp)
                    # which we can use to fake it to one level
                    # of nesting.  Hence given e.g.
                    #   <itemformat command="code">-misel=<var>yes/no</var></itemformat>
                    # we can turn it into:
                    #   <itemformat><samp>-misel={yes/no}</samp></itemformat>
                    if len(element.children) > 1:
                        max_child_len = 0
                        for child in element.children:
                            if isinstance(child, Element):
                                if len(child.children) > max_child_len:
                                    max_child_len = len(child.children)
                        if max_child_len == 1:
                            if 0:
                                old_xml = element.toxml()
                            element.kind = 'samp'
                            new_text = ''
                            for child in element.children:
                                if isinstance(child, Element):
                                    new_text += '{%s}' % child.get_all_text()
                                elif isinstance(child, Text):
                                    new_text += child.data

                            # Fix RTL macros like:
                            # <itemformat command="code">(match_operand:<var>m</var> <var>n</var> ...
                            if new_text.startswith('(') and new_text.endswith(')'):
                                new_text = new_text.replace('}{', '} {')

                            element.children = [Text(new_text)]
                            if 0:
                                print('flattened %s to %s'
                                      % (old_xml, element.toxml()))
                        else:
                            if 0:
                                print('itemformat was too complex to flatten: %s'
                                      % element.toxml())
                    else:
                        element.kind = command
                        text = element.get_all_text().rstrip()
                        element.children = [Text(text)]
                    return

            if element.kind == 'tableentry':
                tableterm = element.first_element_named('tableterm')
                tableitem = element.first_element_named('tableitem')
                if tableterm and tableitem:
                    item = tableterm.first_element_named('item')
                    if item:
                        itemformat = item.first_element_named('itemformat')
                        if itemformat:
                            itemformats = tableterm.get_all_elements('itemformat')
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
                                    note.rst_kind = Directive('note')
                                    note.children = [r]
                                    rtext = r.children[0]
                                    if rtext.data.startswith('(') and rtext.data.endswith(')'):
                                        rtext.data = rtext.data[1:-1]

                                    tableitem.children = \
                                        [note] + tableitem.children

                            if self.convert_to_option(element, tableitem,
                                                      itemformats, parents):
                                return
                            else:
                                self.convert_to_definition_list(tableterm,
                                                                tableitem)

        @staticmethod
        def handle_as_option(text, parents):
            section = parents[-2].first_element_named('sectiontitle')
            if section:
                section_name = section.get_all_text()
                for needle in ('Function Attributes', 'Variable Attributes', 'Type Attributes'):
                    if section_name.endswith(needle):
                        return 'gcc-attr'

            for parent in parents[1:]:
                section = parent.first_element_named('sectiontitle')
                if section:
                    section_name = section.get_all_text()
                    if text.startswith('--') and section_name == 'Configuration':
                        return 'option'
            return None

        @classmethod
        def get_opposite_option(cls, option):
            if 'no-' in option:
                return option.replace('no-', '')
            else:
                return option[:2] + 'no-' + option[2:]

        @classmethod
        def maybe_add_option_to_options(cls, options, default_options, option):
            if option not in options:
                opposite = cls.get_opposite_option(option)
                if opposite in options:
                    default_options.append(option)

        @classmethod
        def get_option_name(cls, option):
            text = ''
            assert option.children
            var_added = False
            for child in option.children:
                if isinstance(child, Element):
                    t = child.get_all_text()
                    if child.kind == 'var' and (' ' in text or '=' in text):
                        t = f'{{{t}}}'
                        var_added = True
                    text += t
                else:
                    text += child.data
            if var_added:
                if not text.startswith('-'):
                    text = option.get_all_text().strip()
            return text.strip()

        def convert_to_option(self, tableentry, tableitem,
                              itemformats, parents):
            itemformats[0].delete_children_named('indexterm')
            text = itemformats[0].get_all_text()
            options = []
            default_options = []

            for itemformat in itemformats:
                itemtext = self.get_option_name(itemformat)
                if itemtext:
                    options.append(itemtext)

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
                                self.maybe_add_option_to_options(options, default_options, option)
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
                # Add negative form as a new option entry:
                if len(default_options) == 1:
                    parent = parents[-1]
                    assert tableentry in parent.children
                    index = parent.children.index(tableentry)
                    negative = Element('negative-option')
                    negative.rst_kind = Directive('option', default_options[0])
                    nopt = Element('opt')
                    nopt.rst_kind = InlineMarkup('option')
                    nopt.children = [Text(self.get_opposite_option(default_options[-1]))]
                    negative.children = [Text('Default setting; overrides '), nopt, Text('.')]
                    parent.children.insert(index + 1, negative)
                else:
                    # FIXME: handle it
                    options += default_options

                # Then it is a description of an option, mark it as such,
                # using all the option names found, and purge the
                # <indexcommand> instances:
                tableentry.kind = 'option'
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
            else:
                directive = self.handle_as_option(text, parents)
                if directive:
                    # For now skip 'vector' and 'const' attributes that are also keywords
                    if text not in ('vector', 'const'):
                        detected_option_directives[text] = directive
                    if directive == 'gcc-attr':
                        text = ', '.join(options)
                    tableentry.rst_kind = Directive(directive, text)
                    tableentry.children = new_children
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

    TableEntryFixer().visit(tree)
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
                  <para>Print the opcode suffix for the size of the current integer operand (one of
                  <code>b</code>/<code>w</code>/<code>l</code>/<code>q</code>).
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
        def previsit_element(self, element, parents):
            if element.kind == 'multitable':
                element.rst_kind = Table(element, ctxt)
            element.delete_children_named('columnprototypes')

        def postvisit_element(self, element, parents):
            if ctxt.debug:
                if element.kind == 'multitable':
                    element.dump(sys.stdout)

    MultitableFixer().visit(tree)
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
            self.default_lang_stack = [args.default_language if args else 'c++']

        @staticmethod
        def is_an_option(text):
            if text.startswith('---'):
                # likely a diff
                return False
            elif text.startswith('-') or text.lstrip().startswith('-W'):
                return True
            elif text.lstrip().startswith('object-file-name'):
                # Linker Options
                return True
            else:
                return False

        def previsit_element(self, element, parents):
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
                    text = pre.get_all_text()
                    if text:
                        if self.is_an_option(text):
                            self.handle_option_listing(element, pre)
                            return
                        lang = self.guess_language(text)
                        example.collapse_to_text()
                        example.rst_kind = Directive('code-block', lang)
                else:
                    exdents = []
                    for child in element.children:
                        if child.kind == 'exdent':
                            exdents.append(child.get_all_text())
                    if exdents:
                        text = '\n'.join(exdents)
                        lang = self.guess_language(text)
                        example.children = [Text(text)]
                        example.rst_kind = Directive('code-block', lang)

        def postvisit_element(self, element, parents):
            if hasattr(element, 'default_language'):
                self.default_lang_stack.pop()

        def guess_language(self, data):
            if 'DO ' in data:
                return 'fortran'
            elif data.startswith('gcc ') or data.startswith('% gcc ') or data.startswith('--'):
                return 'shell-session'

            data = data.strip()
            if data and data[0] == '{' and data[1:].lstrip().startswith('"'):
                # JSON dictionary object {"foo": 123}
                return 'json'
            elif data and data[0] == '[' and data[1:].lstrip().startswith('{'):
                # JSON list of objects [{"foo": 123}]
                return 'json'
            return self.default_lang_stack[-1]

        def handle_option_listing(self, element, pre):
            class OptionWrappingVisitor(NoopVisitor):
                def postvisit_element(self, element, parents):
                    if element.kind == 'var':
                        return
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
                    for m in re.finditer(r'(-\S+)', text.data):
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

    ExampleFixer().visit(tree)
    return tree


def fixup_titles(tree):
    class TitleFixer(NoopVisitor):
        def __init__(self):
            self.cur_section_level = None
            self.section_kinds = {
                'top': '=',
                'chapter': '-',
                'section': '*',
                'subsection': '^',
                'subsubsection': '~',
                'unnumbered': '=',
                'unnumberedsec': '='}

        def previsit_element(self, element, parents):
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
            elif element.kind in ('heading', 'subheading'):
                element.rst_kind = Title(element, '=')
            else:
                return False

            element.collapse_to_text()

    TitleFixer().visit(tree)
    return tree


def fixup_index(tree):
    class IndexFixer(NoopVisitor):
        """
        Look for <cindex><indexterm>TEXT</indexterm></cindex>
        """
        def previsit_element(self, element, parents):
            if isinstance(element, Element):
                if element.kind == 'indexterm':
                    text = element.get_all_text()
                    if text:
                        element.rst_kind = Directive('index', text)
                        element.children = []

    class MoveIndicesFixer(NoopVisitor):
        def previsit_element(self, element, parents):
            if not parents:
                return

            parent = parents[-1]
            if is_movable_index(element):
                i = parent.children.index(element)

                # Move before parent if it is a Directive
                if isinstance(parent.rst_kind, Directive) and i == 0:
                    i2 = parents[-2].children.index(parent)
                    parent.children = parent.children[1:]
                    parents[-2].children.insert(i2, element)
                # Move before a Title if it is our sibling
                elif i > 0:
                    prev = parent.children[i - 1]
                    if isinstance(prev, Element) and isinstance(prev.rst_kind, Title):
                        parent.children[i] = prev
                        parent.children[i - 1] = element

    IndexFixer().visit(tree)
    MoveIndicesFixer().visit(tree)
    return tree


def fixup_urefs(tree):
    class URefFixer(NoopVisitor):
        def previsit_element(self, element, parents):
            if element.kind in ('uref', 'url'):
                url = element.first_element_named('urefurl')
                title = element.first_element_named('urefreplacement')
                if not title:
                    title = element.first_element_named('urefdesc')
                if title and url.get_all_text().startswith('http'):
                    element.rst_kind = EmbeddedUrl(title.get_all_text(), url.get_all_text())
                    element.children = []

    URefFixer().visit(tree)
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
        def previsit_element(self, element, parents):
            if any(p.kind == 'row' for p in parents):
                return

            if element.kind in ('xref', 'pxref', 'ref'):
                xrefnodename = element.first_element_named('xrefnodename')
                if xrefnodename:
                    ref_file = element.first_element_named('xrefinfofile')
                    reftarget = xrefnodename.get_all_text()
                    ref_name = convert_text_to_label(reftarget)
                    if element.kind == 'ref':
                        if reftarget.upper() == reftarget:
                            ref_name = ref_name.upper()

                    ref = Element('ref', {})
                    if ref_file:
                        ref_name = ref_file.get_all_text() + ':' + ref_name
                    ref.rst_kind = Ref(ref_name)
                    if element.kind == 'xref':
                        text = 'See '
                    elif element.kind == 'pxref':
                        text = 'see '
                    else:
                        text = None

                    if text:
                        element.children = [Text(text), ref]
                    else:
                        element.children = [ref]

    XRefFixer().visit(tree)
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
        def previsit_element(self, element, parents):
            if element.kind == 'listitem':
                new_children = []
                indices = []
                element.rst_kind = ListItem('*')
                skip_ws = True
                for child in element.children:
                    if isinstance(child, Element):
                        if child.kind == 'prepend':
                            continue
                        elif child.kind == 'cindex' and not new_children:
                            indices.append(child)
                            continue
                    elif isinstance(child, Text):
                        if child.data.isspace():
                            if skip_ws:
                                continue

                    skip_ws = False
                    new_children.append(child)
                element.children = new_children

                parent = parents[-1]
                index = parent.children.index(element)
                parent.children = parent.children[:index] + indices + parent.children[index:]

    ListFixer().visit(tree)
    return tree


def fixup_inline_markup(tree):
    class InlineMarkupFixer(NoopVisitor):
        """
        Inline markup conversions:
        =========================  ==================
        XML INPUT                  .rst OUTPUT
        =========================  ==================
        <accent>TEXT</accent>      TEXT + diacritic
        <command>TEXT</command>    :command:`TEXT`
        <var>TEXT</var>            ``TEXT``
        <code>TEXT</code>          ``TEXT``
        <dfn>TEXT</dfn>            :dfn:`TEXT`
        <env>TEXT</env>            :envvar:`TEXT`
        <emph>TEXT</emph>          *TEXT*
        <samp>TEXT</samp>          :samp:`TEXT`
        =========================  ==================
        """
        def previsit_element(self, element, parents):
            parent = parents[-1] if parents else None
            if element.kind == 'command':
                element.rst_kind = InlineMarkup('command')
            elif element.kind == 'var':
                element.rst_kind = InlineMarkup('samp')
                if isinstance(parent.rst_kind, InlineMarkup) and parent.kind == 'option':
                    pass
                else:
                    # wrap the variable in braces
                    element.prepend_text('{')
                    element.add_text('}')
            elif element.kind in ('t', 'code'):
                # we cannot support e.g. <var> in a <code> element
                element.collapse_to_text()
                text = element.get_all_text()
                if element.kind == 'code' and text in detected_option_directives:
                    element.rst_kind = InlineMarkup(detected_option_directives[text])
                else:
                    element.rst_kind = MatchedInlineMarkup('``')
            elif element.kind == 'dfn':
                element.rst_kind = InlineMarkup('dfn')
            elif element.kind == 'env':
                element.rst_kind = InlineMarkup('envvar')
            elif element.kind == 'emph':
                element.rst_kind = MatchedInlineMarkup('*')
            elif element.kind == 'strong':
                element.rst_kind = MatchedInlineMarkup('**')
            elif element.kind in ('samp', 'file'):
                element.rst_kind = InlineMarkup('samp')
            elif element.kind == 'verbatim':
                element.rst_kind = Directive('code-block', 'c++')

            new_children = []
            for child in element.children:
                if child.is_element('accent'):
                    if len(child.children) != 1:
                        raise ValueError()
                    grandchild = child.children[0]
                    if not isinstance(grandchild, Text):
                        raise ValueError()
                    new_children.append(grandchild)
                    ACCENTS = {'acute': u'\u0301',
                               'circ': u'\u0302',
                               'grave': u'\u0304',
                               'cedil': u'\u0327',
                               'tilde': u'\u0303',
                               'uml':   u'\u0308'}
                    type_ = child.attrs['type']
                    grandchild.data += ACCENTS[type_]
                    continue
                new_children.append(child)
            element.children = new_children

    InlineMarkupFixer().visit(tree)
    return tree


def fixup_deftype(tree):
    class DefTypeFixup(NoopVisitor):
        MAPPING = {'deftypefn': 'function',
                   'deftypefun': 'function',
                   'deftypefnx': 'function',
                   'defmac': 'c:macro',
                   'defmacx': 'c:macro',
                   'deftypevr': 'c:var',
                   'deftypevrx': 'c:var'}

        def _parse_element(self, element):
            if element.kind in self.MAPPING:
                declaration = ''
                definitionterm = element.first_element_named('definitionterm')
                if not definitionterm:
                    return None
                for child in definitionterm.children:
                    if isinstance(child, Text):
                        declaration += child.data
                    elif child.kind != 'defcategory':
                        declaration += child.get_all_text()
                return declaration
            else:
                return None

        """
        Look for <deftypefn> elements..
        """
        def previsit_element(self, element, parents):
            if isinstance(element, Element):
                declaration = self._parse_element(element)
                lastfn = None
                if declaration:
                    definitionitem = element.first_element_named('definitionitem')
                    lastfn = element
                    element.rst_kind = Directive(self.MAPPING[element.kind], declaration.strip())

                    # process deftypefnx and defmacx elements
                    for fn in (element.get_all_elements('deftypefnx') + element.get_all_elements('defmacx')
                               + element.get_all_elements('deftypevrx')):
                        declaration = self._parse_element(fn)
                        subelement = Element(fn.kind)
                        subelement.rst_kind = Directive(self.MAPPING[subelement.kind], declaration.strip())
                        i = parents[-1].children.index(lastfn)
                        parents[-1].children.insert(i + 1, subelement)
                        lastfn = subelement

                    element.children = []
                    if definitionitem:
                        lastfn.children = [definitionitem]

    DefTypeFixup().visit(tree)
    return tree


# Top-level conversion routine
def convert_to_rst(tree, ctxt):
    tree = ctxt.preprocess(tree)
    tree = fixup_comments(tree)
    tree = prune(tree)
    tree = fixup_nodes(tree, ctxt)
    tree = fixup_menus(tree)
    tree = split(tree)
    tree = fixup_merge_toctree(tree)
    tree = fixup_option_refs(tree)
    tree = fixup_table_entry(tree)
    tree = fixup_multitables(tree, ctxt)
    tree = fixup_examples(tree)
    tree = fixup_titles(tree)
    tree = fixup_index(tree)
    tree = fixup_urefs(tree)
    tree = fixup_xrefs(tree)
    tree = fixup_deftype(tree)
    tree = fixup_lists(tree)
    tree = fixup_inline_markup(tree)
    tree = fixup_empty_texts(tree)
    tree = fixup_ignored_strings(tree)
    tree = fixup_vars_in_samps(tree)
    tree = fixup_wrapped_options(tree)
    tree = fixup_inline_option(tree)
    tree = fixup_element_spacing(tree)
    tree = fixup_machine_dependant_options(tree)
    tree = fixup_params(tree)
    tree = fixup_text_variables(tree)
    tree = fixup_quoting(tree)
    tree = fixup_fortran_functions(tree)
    tree = fixup_libquadmath(tree)
    tree = fixup_merge_functions(tree)
    tree = fixup_option_listing(tree)
    tree = fixup_licenses(tree)
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
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Ref(%r)' % self.name

    def before(self, w):
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
        if self.element.children:
            text = self.element.children[0].data
            assert not text.endswith(':')
            len_ = len(text)
            w.write('\n%s\n\n' % (self.underline * len_))


class Directive(RstKind):
    OPTION_LIMIT = 70

    def __init__(self, name, args=None):
        self.name = name
        self.args = args

    def __repr__(self):
        return 'Directive(%r, %r)' % (self.name, self.args)

    def before(self, w):
        w.write('\n.. %s::' % (self.name, ))
        if self.args:
            w.write(' %s' % (self.args, ))
        w.indent += 1

        if self.name == 'toctree':
            w.write('\n:maxdepth: 2\n')

        w.write('\n\n')

    def after(self, w):
        w.indent -= 1
        w.write('\n\n')


class FnDirective(RstKind):
    def __init__(self, name):
        self.name = name

    def before(self, w):
        w.write('\n:%s:' % (self.name))
        w.indent += 1
        w.write('\n')

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


class EmbeddedUrl(RstKind):
    def __init__(self, title, url):
        self.title = title
        self.url = url

    def __repr__(self):
        return 'EmbeddedUrl(%r, %r)' % (self.title, self.url)

    def before(self, w):
        w.write(f'`{self.title} <{self.url}>`_')


class OutputFile(RstKind):
    def __init__(self, name):
        self.name = name
        self.folder = False
        self.path_components = []

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
        self.has_thead = False
        for child in table_element.children:
            if child.is_element('thead'):
                self.has_thead = True
                self.components.append(child)
            elif child.is_element('tbody'):
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

        self.num_columns = len(self.components[0].rows[0].entries)
        if debug:
            print('self.num_columns: %r' % self.num_columns)
        for comp in self.components:
            comp.columns = []
            for idx in range(self.num_columns):
                column = []
                for row in comp.rows:
                    if idx < len(row.entries):
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
                for entry in comp.columns[x]:
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
        w = RstWriter(io.StringIO())
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
                    for x, _ in enumerate(row.entries):
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
                if comp_idx == 0 and comp.kind == 'thead':
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
        w.write('\n.. list-table::\n')
        if self.has_thead:
            w.write('   :header-rows: 1\n')
        w.write('\n')
        for comp in self.components:
            for row in comp.rows:
                values = []
                for entry in row.entries:
                    texts = [x.strip() for x in self._render_entry(entry).splitlines()]
                    values.append(' '.join(texts))
                for _ in range(len(values), self.num_columns):
                    values.append('')

                for x, text in enumerate(values):
                    c = '*' if x == 0 else ' '
                    output = f'   {c} -'
                    if text:
                        output += ' ' + text
                    w.write(output)
                    w.write('\n')
            w.write('\n')

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
            self.f_out = self.opener.open_file(None)
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

    def previsit_element(self, element, parents):
        if element.rst_kind:
            return element.rst_kind.before(self)
        else:
            if 0:
                print('unhandled element: %r' % (element, ))

    def postvisit_element(self, element, parents):
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
        self.f_out = self.opener.open_file(output_file)
        self.output_file_stack.append(self.f_out)

    def pop_output_file(self, output_file):
        self.opener.close_file(self.f_out)
        self.output_file_stack.pop()
        self.f_out = self.output_file_stack[-1]


class RstOpener:
    """
    Policy for how RstWriter should handle OutputFile instances
    """
    def open_file(self, output_file):
        raise NotImplementedError

    def close_file(self, f_out):
        raise NotImplementedError


class Context:
    def __init__(self):
        self.debug = False

    def preprocess(self, tree):
        return tree


class FileOpener(RstOpener):
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def open_file(self, output_file):
        path_prefix = self.output_dir
        if output_file.path_components:
            prefix = os.path.join(*output_file.path_components)
            path_prefix = os.path.join(path_prefix, prefix)
            if not os.path.exists(path_prefix):
                os.makedirs(path_prefix)
        path = os.path.join(path_prefix, '%s.rst' % output_file.name)
        print(' (%s' % path, end='')
        f_out = open(path, 'w')
        return f_out

    def close_file(self, f_out):
        print(') ', end='')
        f_out.close()


class GccContext(Context):
    def preprocess(self, tree):
        class GccVisitor(NoopVisitor):
            def previsit_element(self, element, parents):
                if element.kind == 'chapter':
                    for child in element.children:
                        if child.is_element('sectiontitle'):
                            text = child.get_sole_text()
                            if text:
                                if text.data == 'GNU Objective-C Features':
                                    element.default_language = 'objective-c'
                # Fixups for issue #1:
                if element.kind == 'option':
                    all_text = element.get_all_text()
                    if all_text in ('-fflag', '-ffoo', '-fno-foo'):
                        element.kind = 'samp'
                        element.children = [Text(all_text)]

        GccVisitor().visit(tree)
        return tree


parser = argparse.ArgumentParser(description='Convert TEXINFO xml file into RST files')
parser.add_argument('xml_file', help='Input XML file')
parser.add_argument('--output', '-o', default='output', help='Output directory')
parser.add_argument('--default-language', default='c++', help='Default language for code blocks')

# Entrypoint
if __name__ == '__main__':
    args = parser.parse_args()
    base, _ = os.path.splitext(os.path.basename(args.xml_file))
    with open(args.xml_file) as f_in:
        xml_src = f_in.read()
        tree = from_xml_string(xml_src)
    tree = convert_to_rst(tree, GccContext())
    if 1:
        if not os.path.exists(args.output):
            os.mkdir(args.output)
        with open(os.path.join(args.output, base + '.rst'), 'w') as f_out:
            print('Creating files:', end='')
            w = RstWriter(f_out, FileOpener(args.output))
            w.visit(tree)
            print()
    else:
        w = RstWriter(sys.stdout)
        w.visit(tree)
