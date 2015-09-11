import argparse
from collections import deque
import os
import re
import sys
import unittest

from node import Node, Element, Comment, Text

FULL_LINE_COMMANDS = (
    'author',
    'c',
    'chapter',
    'clear',
    'comment',
    'copying',
    'defcodeindex',
    'end',
    'ifset',
    'include',
    'item',
    'itemize',
    'paragraphindent',
    'section',
    'set',
    'setfilename',
    'settitle',
    'syncodeindex',
    'titlepage',
)

class Parser:
    def __init__(self, path, include_paths, debug=0):
        self.path = path
        self.include_paths = include_paths
        self.debug = debug
        self._stack = []
        self.stack_top = None
        self.have_chapter = False
        self.have_section = False
        self.have_para = False
        self.tokens = deque()

    def parse_file(self, filename):
        with open(filename) as f:
            content = f.read()
        return self.parse_str(content)

    def parse_str(self, content):
        """
        Parse texinfo content, into a Node (and a tree below it).
        """
        self.texinfo = Element('texinfo')
        self.push(self.texinfo)
        self.stack_top.add_text('\n')
        self._parse_content(content)
        while self.stack_top:
            self.pop()
        if 0:
            print
            self.texinfo.dump(sys.stdout)
            print
        return self.texinfo

    def _parse_content(self, text):
        if self.debug:
            print(list(self._tokenize(text)))
        # Add the tokens from "text" to the front of the deque
        # (.extendleft reverses the order, so we need to pre-reverse them
        # to get them in the correct order)
        self.tokens.extendleft(list(self._tokenize(text))[::-1])
        had_newline = 1
        while True:
            tok0 = self.peek_token()
            tok1 = self.peek_token(1)
            tok2 = self.peek_token(2)
            if self.debug:
                print('tok0: %r' % tok0)
                print('  tok1: %r' % tok1)
                print('  tok2: %r' % tok2)
            if tok0 is None:
                break
            if tok0.startswith('\input texinfo'):
                line = tok0
                self.consume_token()
                tok = self.consume_token()
                while tok != '\n':
                    line += tok
                    tok = self.consume_token()
                preamble = self.stack_top.add_element('preamble')
                preamble.add_text(line + '\n')
                had_newline = 1
                continue
            if tok0 == '@':
                if tok2 == '{':
                    if 0:
                        print('got inline markup')
                    command = tok1
                    self.consume_n_tokens(3)
                    inner = ''
                    while 1:
                        tok = self.consume_token()
                        if tok == '}':
                            break
                        inner += tok
                    self._handle_inline_markup(command, inner)
                    had_newline = 0
                    continue
                if tok1 and had_newline:
                    # Do we have a full-line command?
                    m = re.match('^([a-z]*)(\s*.*)$', tok1)
                    if self.debug:
                        print(m.groups())
                    if m and m.group(1) in FULL_LINE_COMMANDS:
                        idx = 2
                        while 1:
                            tok = self.peek_token(idx)
                            if not tok:
                                break
                            if tok == '\n':
                                break
                            idx += 1
                        # Consume everything on the line
                        line = []
                        for i in range(idx):
                            line.append(self.consume_token())
                        self.consume_token() # '\n'
                        if self.debug:
                            print('line: %r' % line)
                        # Drop the '@' tok1:
                        line = line[2:]
                        # Add the rest of tok1:
                        line = [m.group(2)] + line
                        if self.debug:
                            print('line: %r' % line)
                        self._handle_command(m.group(1), ''.join(line))
                        had_newline = 1
                        continue
            elif tok0 == '\n' and (tok1 == '\n' or tok1 is None):
                # Blank line:
                if 0:
                    print('blank line')
                if self.stack_top.kind == 'para':
                    self._handle_text(tok0)
                    self.pop()
                self.consume_n_tokens(2)
                had_newline = 1
                continue
            elif tok0 == '\n':
                if self.have_para:
                    self._handle_text(tok0)
                self.consume_token()
                had_newline = 1
                continue
            had_newline = 0
            self._handle_text(tok0)
            self.consume_token()

    def peek_token(self, n=0):
        if len(self.tokens) >= n + 1:
            return self.tokens[n]
        else:
            return None

    def consume_token(self):
        if self.tokens:
            token = self.tokens.popleft()
            if self.debug:
                print('consuming: %r' % token)
            return token

    def consume_n_tokens(self, n):
        for i in range(n):
            self.consume_token()

    def _tokenize(self, text):
        """
        Split up text into '@', '{', '}', '\n', and runs of everything else,
        yielding the results.
        """
        SPECIAL_CHARS = '@{}\n'
        accum = ''
        for ch in text:
            if ch in SPECIAL_CHARS:
                if accum:
                    yield accum
                accum = ''
                yield ch
            else:
                accum += ch
        if accum:
            yield accum

    def _handle_text(self, text):
        if 0:
            print('_handle_text(%r)' % text)
        if self.stack_top.kind != 'para' and text != '\n':
            para = self.stack_top.add_element('para')
            self.push(para)

        # Entity replacement
        ENTITIES = {"``": 'textldquo',
                    "''": 'textrdquo',
                    "'":  'textrsquo'}
        # Split up "text" into fragments, either text,
        # or things that must become entities
        # Split it up one entity at a time.
        split = [text]
        for splitter in ENTITIES:
            if self.debug:
                print('splitter: %r' % splitter)
                print('old split: %r' % split)
            new_split = []
            for s in split:
                if s in ENTITIES:
                    new_split.append(s)
                    continue
                for frag in s.split(splitter):
                    new_split.append(frag)
                    new_split.append(splitter)
                # Remove stray final splitter:
                new_split = new_split[:-1]
            split = new_split
            if self.debug:
                print('new split: %r' % split)
        if self.debug:
            print(split)

        for frag in split:
            if frag in ENTITIES:
                self.stack_top.add_entity(ENTITIES[frag])
            else:
                self.stack_top.add_text(frag)

    def _handle_command(self, name, line):
        if self.debug:
            print('_handle_command(%r, %r)' % (name, line))
        if name in ('c', 'comment'):
            line = line.replace('--', '-')
            if '--' in line:
                line = '-'
            self.stack_top.add_comment(' ' + name + line + ' ')
            self.stack_top.add_text('\n')
        elif name == 'include':
            self._handle_include(line)
        elif name == 'chapter':
            # Close any existing chapter:
            while self.have_chapter:
                self.pop()
            chapter = self.stack_top.add_element('chapter', spaces=' ')
            self.push(chapter)
            sectiontitle = chapter.add_element('sectiontitle')
            sectiontitle.add_text(line.strip())
            self.stack_top.add_text('\n')
        elif name == 'section':
            # Close any existing section:
            while self.have_section:
                self.pop()
            section = self.stack_top.add_element('section', spaces=' ')
            self.push(section)
            sectiontitle = section.add_element('sectiontitle')
            sectiontitle.add_text(line.strip())
            self.stack_top.add_text('\n')
        elif name in ('copying', 'titlepage', 'itemize'):
            if self.debug:
                print('name: %r' % name)
            env = self.stack_top.add_element(name)
            self.push(env)
            if name == 'itemize':
                line = line.strip()
                if line.startswith('@'):
                    commandarg = line[1:]
                    env.attrs['commandarg'] = commandarg
                    env.attrs['spaces'] = ' '
                    itemprepend = env.add_element('itemprepend')
                    formattingcommand = \
                       itemprepend.add_element('formattingcommand')
                    formattingcommand.attrs['command'] = commandarg
            env.attrs['endspaces'] =' '
            self.stack_top.add_text('\n')
        elif name == 'end':
            env = line.strip()
            if self.debug:
                print('@end of env: %r' % env)
            if env in ('copying', 'titlepage', 'itemize'):
                if self.debug:
                    print('stack: %r' % (self._stack, ))
                while 1:
                    inject_newline = False
                    if env == 'itemize':
                        inject_newline = True
                    old_top = self.pop(inject_newline)
                    if old_top.kind == env:
                        break
        elif name in ('set', 'clear'):
            key, value = self._parse_command_args(line)
            command = self.stack_top.add_element(name)
            command.attrs['name'] = key
            command.attrs['line'] = line
            command.add_text(value)
            self.stack_top.add_text('\n')
        elif name in ('defcodeindex', 'paragraphindent'):
            key, value = self._parse_command_args(line)
            command = self.stack_top.add_element(name)
            command.attrs['value'] = key
            command.attrs['line'] = line
            command.add_text(value)
            self.stack_top.add_text('\n')
        elif name == 'syncodeindex':
            key, value = self._parse_command_args(line)
            command = self.stack_top.add_element(name)
            command.attrs['from'] = key
            command.attrs['to'] = value
            command.attrs['line'] = line
            command.add_text('')
            self.stack_top.add_text('\n')
        elif name == 'item':
            key, value = self._parse_command_args(line)
            if self.stack_top.kind == 'listitem':
                self.pop(inject_newline=False)
            listitem = self.stack_top.add_element('listitem')
            self.push(listitem)
            prepend = listitem.add_element('prepend')
            prepend.add_entity('bullet') # FIXME
            self.stack_top.add_text('\n')
        else:
            m = re.match('^{(.*)}$', line)
            if m:
                line = m.group(1)
            command = self.stack_top.add_element(name)
            command.add_text(line.strip())
            if name in ('settitle', 'author'):
                command.attrs['spaces'] = ' '
            self.stack_top.add_text('\n')

    def _parse_command_args(self, line):
        if self.debug:
            print('line: %r' % line)
        m = re.match('^\s*(\S+)\s+(.*)$', line)
        if m:
            key, value = m.groups()
            value = value.rstrip()
        else:
            key = line.lstrip()
            value = ''
        return key, value

    def _handle_include(self, line):
        """
        For now, always expand included content directly
        inline.
        """
        relpath = line.strip()
        for dirname in [self.path] + self.include_paths:
            candidate_path = os.path.join(dirname, relpath)
            if os.path.exists(candidate_path):
                if 1:
                    print('opening %r (for %r)' % (candidate_path, relpath))
                with open(candidate_path) as f:
                    content = f.read()
                self._parse_content(content)
                if 1:
                    print('end of %r (for %r)' % (candidate_path, relpath))
                return
        if 0:
            raise ValueError('file %r not found' % relpath)
        else:
            print('file %r not found' % relpath)

    def _handle_inline_markup(self, command, inner):
        if command == 'copyright':
            self.stack_top.add_entity('copyright')
            return
        command_el = self.stack_top.add_element(command)
        command_el.add_text(inner)

    def push(self, element):
        if self.debug:
            print('pushing: %r' % element)
        self._stack.append(element)
        self.stack_top = element
        if element.kind == 'chapter':
            self.have_chapter = True
        if element.kind == 'section':
            self.have_section = True
        if element.kind == 'para':
            self.have_para = True

    def pop(self, inject_newline=True):
        old_top = self._stack.pop()
        if self.debug:
            print('popping: %r' % old_top)
        if old_top.kind == 'chapter':
            self.have_chapter = False
        if old_top.kind == 'section':
            self.have_section = False
        if old_top.kind == 'para':
            self.have_para = False
        if old_top.kind == 'listitem':
            inject_newline = False
        if self._stack:
            self.stack_top = self._stack[-1]
            if inject_newline:
                self.stack_top.add_text('\n')
        else:
            self.stack_top = None
        return old_top

class Texi2XmlTests(unittest.TestCase):
    def test_comment(self):
        texisrc = '@c This is a comment.'
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        dom_doc = tree.to_dom_doc()
        xmlstr = dom_doc.toxml()
        self.assertMultiLineEqual(
            ('<?xml version="1.0" ?><texinfo>\n'
             + '<!-- c This is a comment. -->\n</texinfo>'),
            xmlstr)

    def test_preamble(self):
        texisrc = '''\input texinfo  @c -*-texinfo-*-
@c %**start of header
@setfilename gcc.info
'''
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        dom_doc = tree.to_dom_doc()
        xmlstr = dom_doc.toxml()
        self.assertMultiLineEqual(
            '''<?xml version="1.0" ?><texinfo>
<preamble>\\input texinfo  @c -*-texinfo-*-
</preamble><!-- c %**start of header -->
<setfilename>gcc.info</setfilename>
</texinfo>''',
            xmlstr)

    def test_para(self):
        texisrc = 'Hello world\n'
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        dom_doc = tree.to_dom_doc()
        xmlstr = dom_doc.toxml()
        self.assertMultiLineEqual(
            ('<?xml version="1.0" ?><texinfo>\n'
             + '<para>Hello world\n</para>\n</texinfo>'),
            xmlstr)

    def test_paras(self):
        texisrc = '''Line 1 of para 1.
Line 2 of para 1.

Line 1 of para 2.
Line 2 of para 2.
'''
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        dom_doc = tree.to_dom_doc()
        xmlstr = dom_doc.toxml()
        self.assertMultiLineEqual('''<?xml version="1.0" ?><texinfo>
<para>Line 1 of para 1.
Line 2 of para 1.
</para>
<para>Line 1 of para 2.
Line 2 of para 2.
</para>
</texinfo>''',
                                        xmlstr)

    def test_inline(self):
        texisrc = '''Example of @emph{inline markup}.\n'''
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        dom_doc = tree.to_dom_doc()
        xmlstr = dom_doc.toxml()
        self.assertMultiLineEqual(
            ('<?xml version="1.0" ?><texinfo>\n'
             '<para>Example of <emph>inline markup</emph>.\n</para>\n</texinfo>'),
            xmlstr)

    def test_multiple_inlines(self):
        texisrc = '''
An amendment to the 1990 standard was published in 1995.  This
amendment added digraphs and @code{__STDC_VERSION__} to the language,
but otherwise concerned the library.  This amendment is commonly known
as @dfn{AMD1}; the amended standard is sometimes known as @dfn{C94} or
@dfn{C95}.  To select this standard in GCC, use the option
@option{-std=iso9899:199409} (with, as for other standard versions,
@option{-pedantic} to receive all required diagnostics).
'''
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        dom_doc = tree.to_dom_doc()
        xmlstr = dom_doc.toxml()
        self.maxDiff = 2000
        self.assertMultiLineEqual(
            ('''<?xml version="1.0" ?><texinfo>
<para>An amendment to the 1990 standard was published in 1995.  This
amendment added digraphs and <code>__STDC_VERSION__</code> to the language,
but otherwise concerned the library.  This amendment is commonly known
as <dfn>AMD1</dfn>; the amended standard is sometimes known as <dfn>C94</dfn> or
<dfn>C95</dfn>.  To select this standard in GCC, use the option
<option>-std=iso9899:199409</option> (with, as for other standard versions,
<option>-pedantic</option> to receive all required diagnostics).
</para>
</texinfo>'''),
            xmlstr)

    def test_multiline_inlines(self):
        texisrc = '''
whole standard including all the library facilities; a @dfn{conforming
freestanding implementation} is only required to provide certain
'''
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        dom_doc = tree.to_dom_doc()
        xmlstr = dom_doc.toxml()
        self.maxDiff = 2000
        self.assertMultiLineEqual(
            ('''<?xml version="1.0" ?><texinfo>
<para>whole standard including all the library facilities; a <dfn>conforming
freestanding implementation</dfn> is only required to provide certain
</para>
</texinfo>'''),
            xmlstr)

    def test_sections(self):
        texisrc = '''@section Section 1
Text in section 1.

@section Section 2
Text in section 2.
'''

        p = Parser('', [])
        tree = p.parse_str(texisrc)
        dom_doc = tree.to_dom_doc()
        xmlstr = dom_doc.toxml()
        self.assertMultiLineEqual(
            ('''<?xml version="1.0" ?><texinfo>
<section spaces=" "><sectiontitle>Section 1</sectiontitle>
<para>Text in section 1.
</para>
</section>
<section spaces=" "><sectiontitle>Section 2</sectiontitle>
<para>Text in section 2.
</para>
</section>
</texinfo>'''),
            xmlstr)

    def test_chapters(self):
        texisrc = '''@chapter Chapter 1
@section Chapter 1 Section 1
Text in chapter 1 section 1.

@section Chapter 1 Section 2
Text in chapter 1 section 2.

@chapter Chapter 2
@section Chapter 2 Section 1
Text in chapter 2 section 1.

@section Chapter 2 Section 2
Text in chapter 2 section 2.
'''

        p = Parser('', [])
        tree = p.parse_str(texisrc)
        dom_doc = tree.to_dom_doc()
        xmlstr = dom_doc.toxml()
        self.maxDiff = 2000
        self.assertMultiLineEqual(
            ('''<?xml version="1.0" ?><texinfo>
<chapter spaces=" "><sectiontitle>Chapter 1</sectiontitle>
<section spaces=" "><sectiontitle>Chapter 1 Section 1</sectiontitle>
<para>Text in chapter 1 section 1.
</para>
</section>
<section spaces=" "><sectiontitle>Chapter 1 Section 2</sectiontitle>
<para>Text in chapter 1 section 2.
</para>
</section>
</chapter>
<chapter spaces=" "><sectiontitle>Chapter 2</sectiontitle>
<section spaces=" "><sectiontitle>Chapter 2 Section 1</sectiontitle>
<para>Text in chapter 2 section 1.
</para>
</section>
<section spaces=" "><sectiontitle>Chapter 2 Section 2</sectiontitle>
<para>Text in chapter 2 section 2.
</para>
</section>
</chapter>
</texinfo>'''),
            xmlstr)

    def test_settitle(self):
        texisrc = '@settitle Using the GNU Compiler Collection (GCC)\n'
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        xmlstr = tree.toxml()
        self.maxDiff = 2000
        self.assertMultiLineEqual('''<texinfo>
<settitle spaces=" ">Using the GNU Compiler Collection (GCC)</settitle>
</texinfo>''',
                         xmlstr)

    def test_paragraphindent(self):
        texisrc = '@paragraphindent 1\n'
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        xmlstr = tree.toxml()
        self.maxDiff = 2000
        self.assertMultiLineEqual('''<texinfo>
<paragraphindent value="1" line=" 1"></paragraphindent>
</texinfo>''',
                         xmlstr)

    def test_defcodeindex(self):
        texisrc = '''@defcodeindex op
@syncodeindex fn cp
'''
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        xmlstr = tree.toxml()
        self.maxDiff = 2000
        self.assertMultiLineEqual('''<texinfo>
<defcodeindex value="op" line=" op"></defcodeindex>
<syncodeindex from="fn" to="cp" line=" fn cp"></syncodeindex>
</texinfo>''',
                         xmlstr)

    def test_copying(self):
        texisrc = '''
@copying
Text goes here.
@end copying
'''
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        xmlstr = tree.toxml()
        self.maxDiff = 2000
        self.assertMultiLineEqual('''<texinfo>
<copying endspaces=" ">
<para>Text goes here.
</para></copying></texinfo>''',
                         xmlstr)

    def test_itemize(self):
        texisrc = '''
@itemize @bullet
@item
This is item 1

@item
This is item 2
@end itemize
'''
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        xmlstr = tree.toxml()
        self.maxDiff = 2000
        self.assertMultiLineEqual(
            '''<texinfo>
<itemize commandarg="bullet" spaces=" " endspaces=" "><itemprepend><formattingcommand command="bullet"/></itemprepend>
<listitem><prepend>&bullet;</prepend>
<para>This is item 1
</para>
</listitem><listitem><prepend>&bullet;</prepend>
<para>This is item 2
</para>
</listitem></itemize>
</texinfo>''',
            xmlstr)

    def test_set(self):
        texisrc = '''
@set version-GCC 6.0.0
@set DEVELOPMENT
@set VERSION_PACKAGE (GCC)''' + ' ' + '''
'''
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        xmlstr = tree.toxml()
        self.maxDiff = 2000
        self.assertMultiLineEqual('''<texinfo>
<set name="version-GCC" line=" version-GCC 6.0.0">6.0.0</set>
<set name="DEVELOPMENT" line=" DEVELOPMENT"></set>
<set name="VERSION_PACKAGE" line=" VERSION_PACKAGE (GCC) ">(GCC)</set>
</texinfo>''',
                         xmlstr)


    def test_clear(self):
        texisrc = '@clear INTERNALS\n'
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        xmlstr = tree.toxml()
        self.maxDiff = 2000
        self.assertMultiLineEqual(
            '''<texinfo>
<clear name="INTERNALS" line=" INTERNALS"></clear>
</texinfo>''',
            xmlstr)

    def test_copyright(self):
        texisrc = '\nCopyright @copyright{} 2015  John Doe.\n'
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        xmlstr = tree.toxml()
        self.maxDiff = 2000
        self.assertMultiLineEqual(
            '''<texinfo>
<para>Copyright &copyright; 2015  John Doe.
</para>
</texinfo>''',
            xmlstr)

    def test_text_quotes(self):
        texisrc = "\nfoo ``bar'' baz\n"
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        xmlstr = tree.toxml()
        self.maxDiff = 2000
        self.assertMultiLineEqual(
            '''<texinfo>
<para>foo &textldquo;bar&textrdquo; baz
</para>
</texinfo>''',
            xmlstr)

    def test_text_quote(self):
        texisrc = "\nfoo's bar\n"
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        xmlstr = tree.toxml()
        self.maxDiff = 2000
        self.assertMultiLineEqual(
            '''<texinfo>
<para>foo&textrsquo;s bar
</para>
</texinfo>''',
            xmlstr)

    def test_variable(self):
        texisrc = '''It corresponds to the compilers
@ifset VERSION_PACKAGE
@value{VERSION_PACKAGE}
@end ifset
version @value{version-GCC}.
'''
        p = Parser('', [])
        tree = p.parse_str(texisrc)
        dom_doc = tree.to_dom_doc()
        xmlstr = dom_doc.toxml()
        self.assertMultiLineEqual('''<?xml version="1.0" ?><texinfo>
<para>It corresponds to the compilers
<ifset>VERSION_PACKAGE</ifset>
<value>VERSION_PACKAGE</value>
version <value>version-GCC</value>.
</para>
</texinfo>''',
                         xmlstr)

if __name__ == '__main__':
    unittest.main()
