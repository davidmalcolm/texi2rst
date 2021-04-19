#!/usr/bin/env python3

from collections import deque, OrderedDict
import os
import re
import sys

from node import Node, Element, Comment, Text, NoopVisitor

DTD_LINE = '<!DOCTYPE texinfo PUBLIC "-//GNU//DTD TexinfoML V5.0//EN" "http://www.gnu.org/software/texinfo/dtd/5.0/texinfo.dtd">'

FULL_LINE_COMMANDS = (
    'author',
    'c',
    'chapter',
    'cindex',
    'clear',
    'comment',
    'copying',
    'defcodeindex',
    'display',
    'end',
    'enumerate',
    'findex',
    'group',
    'ifnottex',
    'ifset',
    'iftex',
    'include',
    'item',
    'itemize',
    'macro',
    'menu',
    'node',
    'opindex',
    'page',
    'paragraphindent',
    'section',
    'set',
    'setfilename',
    'settitle',
    'smallexample',
    'syncodeindex',
    'table',
    'titlepage',
    'top',
    'vskip',
)

def add_stripped_text(element, str_, attr_recipient=None):
    '''
    Add str_ to element, stripping any leading spaces,
    and, if so adding 'spaces' attr to "attr_recipient" element,
    using "element" by default.
    '''
    spaces = ''
    while str_ and str_[0].isspace():
        ch = str_[0]
        if ch == '\n':
            ch = '\\n'
        spaces += ch
        str_ = str_[1:]
    element.add_text(str_)
    if attr_recipient is None:
        attr_recipient = element
    if spaces:
        attr_recipient.attrs['spaces'] = spaces

def escape_text(text):
    text = text.replace(' ', '-')
    text = text.replace('\n', '-')
    text = text.replace('+', '_002b')
    return text

class TexiNode(Element):
    """
    An @node within a .texi file.
    """
    def __init__(self):
        Element.__init__(self, 'node')
        # These attrs are all strings, for lookup within Parser.node_dict
        self.next = None
        self.prev = None
        self.up = None
        # This is a list of strings:
        #self.child_nodes = []

    def __repr__(self):
        return ('TexiNode(%r, %r, rst_kind=%r, next=%r, prev=%r, up=%r)'
                % (self.kind, self.attrs, self.rst_kind,
                   self.next, self.prev, self.up))

class Parser:
    def __init__(self, path, include_paths, debug=0, with_dtd=0, filename=None):
        self.path = path
        self.include_paths = include_paths
        self.debug = debug
        self.with_dtd = with_dtd
        self.filename = filename
        self._stack = []
        self.stack_top = None
        self.have_chapter = False
        self.have_section = False
        self.have_para = False
        self.tokens = deque()
        self.index_count = {}
        self.last_node = None
        self.top_node = None
        self.node_dict = OrderedDict()
        self.cur_macro_defn = None
        self.macros = OrderedDict()
        self.need_pre = False

    def parse_file(self, filename):
        with open(filename) as f:
            content = f.read()
        return self.parse_str(content)

    def parse_str(self, content):
        """
        Parse texinfo content, into a Node (and a tree below it).
        """
        self.texinfo = Element('texinfo')
        if self.with_dtd:
            self.texinfo.attrs['xml:lang'] = "en"
        self.push(self.texinfo)
        if self.filename:
            self.stack_top.add_text('\n')
            filename = self.texinfo.add_element('filename')
            filename.attrs['file'] = self.filename
            filename.add_text('')
            self.stack_top.add_text('\n')
        self._parse_content(content)
        while self.stack_top:
            self.pop()
        self._fixup_nodes()
        self._strip_conditionals()
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
            if tok0.startswith('\\input texinfo'):
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
                nextch = tok1[0]
                if nextch in ('.', ':', '{', '}', '*', '/'):
                    ENTITIES = {'.': 'eosperiod',
                                '{': 'lbrace',
                                '*': 'linebreak',
                                '}': 'rbrace',
                                '/': 'slashbreak',
                                ':': 'noeos'}
                    self.stack_top.add_entity(ENTITIES[nextch])
                    self.consume_n_tokens(2)
                    tok1 = tok1[1:]
                    if tok1:
                        self.tokens.appendleft(tok1)
                    had_newline = 0
                    continue
                if nextch == ' ':
                    spacecmd = self.stack_top.add_element('spacecmd')
                    spacecmd.attrs['type'] = 'spc'
                    self.consume_n_tokens(2)
                    tok1 = tok1[1:]
                    if tok1:
                        self.tokens.appendleft(tok1)
                    had_newline = 0
                    continue
                if tok1 == '@':
                    self.stack_top.add_entity('arobase')
                    self.consume_n_tokens(2)
                    had_newline = 0
                    continue
                if tok1 == '\n':
                    # '@' on the end of a line: line continuation
                    # http://www.gnu.org/software/texinfo/manual/texinfo/html_node/Def-Cmd-Continuation-Lines.html
                    spacecmd = self.stack_top.add_element('spacecmd')
                    spacecmd.attrs['type'] = 'nl'
                    self.consume_n_tokens(2)
                    had_newline = 0
                    continue
                if tok1 and had_newline:
                    # Do we have a full-line command?
                    m = re.match(r'^([a-z]*)(\s*.*)$', tok1)
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
                if tok2 == '{':
                    if 0:
                        print('got inline markup')
                    command = tok1
                    self.consume_n_tokens(3)
                    inner = ''
                    nesting = 1
                    while 1:
                        tok = self.consume_token()
                        if tok == '{':
                            nesting += 1
                        if tok == '}':
                            nesting -= 1
                            if nesting == 0:
                                break
                        inner += tok
                    self._handle_inline_markup(command, inner)
                    if command not in self.macros:
                        had_newline = 0
                    continue
                # inline markup without braces
                self.consume_n_tokens(2)
                if self.debug:
                    print('tok1: %r' % tok1)
                m = re.match(r'(\S+)(.*)', tok1)
                if not m:
                    raise ValueError('tok1: %r' % tok1)
                command = m.group(1)
                rest_of_tok1 = m.group(2)
                if rest_of_tok1:
                    self.tokens.appendleft(rest_of_tok1)
                self._handle_inline_markup(command, '')
                had_newline = 0
                continue

            if self.need_pre:
                pre = self.stack_top.add_element('pre')
                pre.attrs['xml:space'] = 'preserve'
                self.push(pre)
                self.need_pre = False

            if self.stack_top.kind == 'pre':
                self.stack_top.add_text(tok0)
                self.consume_token()
                had_newline = tok0 == '\n'
                continue
            elif tok0 == '\n' and (tok1 == '\n' or tok1 is None):
                # Blank line:
                if self.debug:
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
                else:
                    self.stack_top.add_text(tok0)
                self.consume_token()
                had_newline = 1
                continue
            elif self.stack_top.kind == 'menu':
                line = tok0
                self.consume_token()
                tok = self.consume_token()
                while tok != '\n':
                    line += tok
                    tok = self.consume_token()
                leadingtext = '* '
                m = re.match(r'\* (.*)(::\s*)(.*)', line)
                if m:
                    title, separator, desc = m.groups()
                    menuentry = self.stack_top.add_element('menuentry')
                    menuentry.attrs['leadingtext'] = leadingtext
                    menunode = menuentry.add_element('menunode')
                    menunode.add_text(title)
                    menunode.attrs['separator'] = separator
                    menudescription = menuentry.add_element('menudescription')
                    pre = menudescription.add_element('pre')
                    pre.attrs['xml:space'] = 'preserve'
                    pre.add_text(desc + '\n')
                    self._pre = pre
                else:
                    assert self._pre
                    self._pre.add_text(line + '\n')
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

    def _insert_text_with_entities(self, element, text):
        """
        Add text (a string) to the given element, converting
        certain character sequences to entities.
        """
        if self.debug:
            print('_insert_text_with_entities: %r' % text)
        # Entity replacement
        ENTITIES = {"@{": 'lbrace',
                    "@}": 'rbrace',
                    "@/": 'slashbreak',
                    "@:": 'noeos',
                    "---": 'textmdash',
                    "``": 'textldquo',
                    "''": 'textrdquo',
                    "'":  'textrsquo',
                    "@@": 'arobase'}
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
                element.add_entity(ENTITIES[frag])
            else:
                element.add_text(frag)

    def _handle_text(self, text):
        if 0:
            print('_handle_text(%r)' % text)
        if self.stack_top.kind != 'para' and text != '\n':
            para = self.stack_top.add_element('para')
            self.push(para)
        self._insert_text_with_entities(self.stack_top, text)

    def _handle_command(self, name, line):
        if self.debug:
            print('_handle_command(%r, %r)' % (name, line))
        if name in ('c', 'comment'):
            line = line.replace('--', '-')
            if '--' in line:
                line = '-'
            self.stack_top.add_comment(' ' + name + line + ' ')
            self.stack_top.add_text('\n')
        elif name in ('cindex', 'findex', 'opindex'):
            kind = name
            if name == 'opindex':
                kind = 'indexcommand'
            outer = self.stack_top.add_element(kind)
            index = {'cindex': 'cp',
                     'findex': 'fn',
                     'opindex': 'op'}
            if name == 'opindex':
                outer.attrs['command'] = name
            outer.attrs['index'] = index[name]
            indexterm = outer.add_element('indexterm')
            indexterm.attrs['index'] = index[name]
            if name in self.index_count:
                self.index_count[name] += 1
            else:
                self.index_count[name] = 1
            indexterm.attrs['number'] = '%i' % self.index_count[name]
            if name == 'findex':
                indexterm.attrs['mergedindex'] = 'cp'
            if name == 'opindex':
                indexterm.attrs['incode'] = '1'
            add_stripped_text(indexterm, line, outer)
            self.stack_top.add_text('\n')
        elif name == 'include':
            self._handle_include(line)
        elif name == 'chapter':
            # Close any existing chapter:
            while self.have_chapter:
                self.pop(why='chapter')
            chapter = self.stack_top.add_element('chapter')
            self.push(chapter)
            sectiontitle = chapter.add_element('sectiontitle')
            add_stripped_text(sectiontitle, line, chapter)
            self.stack_top.add_text('\n')
        elif name == 'section':
            # Close any existing section:
            while self.have_section:
                self.pop()
            section = self.stack_top.add_element('section')
            self.push(section)
            sectiontitle = section.add_element('sectiontitle')
            add_stripped_text(sectiontitle, line, section)
            self.stack_top.add_text('\n')
        elif name == 'macro':
            m = re.match(r'\s*(\S+)\{(.*)\}', line)
            if m:
                macro_name, formalarg = m.groups()
            else:
                m = re.match(r'\s*(\S+)\s*', line)
                macro_name = m.group(1)
                formalarg = None

            # Capture tokens up to the next "@end macro"
            tokens = []
            while 1:
                tok0 = self.peek_token()
                tok1 = self.peek_token(1)
                tok2 = self.peek_token(2)
                if tok0 == '@' and tok1 == 'end macro' and tok2 == '\n':
                    break
                tokens.append(tok0)
                self.consume_token()
            macro_el = self.stack_top.add_element('macro')
            macro_el.attrs['name'] = macro_name
            macro_el.attrs['line'] = line
            if formalarg:
                formalarg_el = macro_el.add_element('formalarg')
                formalarg_el.add_text(formalarg)
            macro_el.add_text(''.join(tokens))
            if self.debug:
                print('defined macro %r as %r' % (macro_name, tokens))
            self.macros[macro_name] = tokens
            return
        elif name in ('copying', 'titlepage', 'itemize', 'enumerate', 'menu',
                      'smallexample', 'table', 'group', 'display',
                      'iftex', 'ifnottex'):
            if self.debug:
                print('name: %r' % name)
            env = self.stack_top.add_element(name)
            self.push(env)
            if name in ('itemize', 'table', 'enumerate'):
                line = line.strip()
                if line.startswith('@'):
                    commandarg = line[1:]
                    env.attrs['commandarg'] = commandarg
                    env.attrs['spaces'] = ' '
                    if name == 'itemize':
                        itemprepend = env.add_element('itemprepend')
                        formattingcommand = \
                                            itemprepend.add_element('formattingcommand')
                        formattingcommand.attrs['command'] = commandarg
                if name == 'enumerate':
                    env.attrs['first'] = '1'
            env.attrs['endspaces'] =' '
            self.stack_top.add_text('\n')
            if name in ('smallexample', 'display'):
                self.need_pre = True
        elif name == 'end':
            env = line.strip()
            if self.debug:
                print('@end of env: %r' % env)
            if env in ('copying', 'titlepage', 'itemize', 'enumerate', 'menu',
                       'smallexample', 'table', 'iftex', 'ifnottex',
                       'group', 'display'):
                if self.debug:
                    print('stack: %r' % (self._stack, ))
                while 1:
                    inject_newline = False
                    if env in ('itemize', 'enumerate', 'menu', 'smallexample'):
                        inject_newline = True
                    old_top = self.pop(inject_newline, why=env)
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
            if self.stack_top.kind == 'tableitem':
                self.pop(inject_newline=False)
                self.pop(inject_newline=False)
            if self.stack_top.kind == 'itemize':
                listitem = self.stack_top.add_element('listitem')
                self.push(listitem)
                prepend = listitem.add_element('prepend')
                prepend.add_entity('bullet') # FIXME
                self.stack_top.add_text('\n')
            if self.stack_top.kind == 'enumerate':
                listitem = self.stack_top.add_element('listitem')
                self.push(listitem)
                if self.debug:
                    print('line: %r' % line)
                    print(key, value)
                if line.startswith(' '):
                    listitem.attrs['spaces'] = ' '
                    line = line[1:]
                line += '\n'
                self.tokens.extendleft(list(self._tokenize(line))[::-1])
                return
            elif self.stack_top.kind == 'table':
                table = self.stack_top
                tableentry = self.stack_top.add_element('tableentry')
                self.push(tableentry)
                tableterm = tableentry.add_element('tableterm')
                item = tableterm.add_element('item')
                itemformat = item.add_element('itemformat')
                itemformat.attrs['command'] = table.attrs['commandarg']
                add_stripped_text(itemformat, line, item)
                tableterm.add_text('\n')
                tableitem = self.stack_top.add_element('tableitem')
                self.push(tableitem)
                return
        elif name == 'node':
            args = line.split(',')
            if self.debug:
                print('node args: %r' % args)
            node = TexiNode()
            self.stack_top.children.append(node)
            node.attrs['name'] = escape_text(args[0].strip())
            self.stack_top.add_text('\n')
            self.last_node = node
            nodename = node.add_element('nodename')
            add_stripped_text(nodename, args[0], node)
            self.node_dict[args[0].strip()] = node
            node.name = args[0].strip()
            node.args = args
            # (we create the other child elements in _fixup_nodes)
        elif name == 'top':
            self.top_node = self.last_node
        else:
            m = re.match('^{(.*)}$', line)
            if m:
                line = m.group(1)
            command = self.stack_top.add_element(name)
            if name != 'vskip':
                line = line.strip()
            command.add_text(line)
            if name in ('settitle', 'author'):
                command.attrs['spaces'] = ' '
            self.stack_top.add_text('\n')

    def _parse_command_args(self, line):
        if self.debug:
            print('line: %r' % line)
        m = re.match(r'^\s*(\S+)\s+(.*)$', line)
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
        if self.debug:
            print('_handle_inline_markup: command: %r inner: %r'
                  % (command, inner))
        if command in self.macros:
            if self.debug:
                print('expanding macro: %r' % command)
            macro_def = self.macros[command]
            new_tokens = []
            for token in macro_def:
                if token == '\\body\\': # FIXME
                    new_tokens += self._tokenize(inner)
                else:
                    new_tokens.append(token)
            if self.debug:
                print('adding tokens: %r' % new_tokens)
            self.tokens.extendleft(new_tokens[::-1])
            return
        if command in ('copyright', 'dots'):
            self.stack_top.add_entity(command)
            return
        ACCENTS = {"'": 'acute',
                   ',': 'cedil',
                   '~': 'tilde',
                   '"': 'uml'}
        if command in ACCENTS:
            accent = self.stack_top.add_element('accent', type=ACCENTS[command])
            accent.add_text(inner)
            return
        if not inner:
            ch = command[0]
            if ch in ACCENTS:
                accent = self.stack_top.add_element('accent', type=ACCENTS[ch])
                accent.attrs['bracketed'] = 'off'
                accent.add_text(command[1])
                self.tokens.appendleft(command[2:])
                return
        command_el = self.stack_top.add_element(command)
        if command == 'email':
            command_el = command_el.add_element('emailaddress')
        if command == 'uref':
            command_el = command_el.add_element('urefurl')
        if command in ('xref', 'pxref'):
            args = inner.split(',')
            if self.debug:
                print('xref args: %r' % args)
            label = escape_text(args[0])
            command_el.attrs['label'] = label
            if len(args) == 1:
                command_el.add_element('xrefnodename').add_text(args[0])
                return
            if len(args) == 2:
                command_el.add_element('xrefnodename').add_text(args[0])
                command_el.add_element('xrefinfoname').add_text(args[1])
                return
            if len(args) >= 3:
                name = args[1]
                desc = args[2]
            if name == '' or name.isspace():
                name = args[0]
            command_el.add_element('xrefnodename').add_text(name)
            xrefprinteddesc = command_el.add_element('xrefprinteddesc')
            add_stripped_text(xrefprinteddesc, desc)
            if len(args) == 5:
                xrefinfofile = command_el.add_element('xrefinfofile')
                add_stripped_text(xrefinfofile, args[3])
                xrefprintedname = command_el.add_element('xrefprintedname')
                add_stripped_text(xrefprintedname, args[4])
                command_el.attrs['manual'] = args[3].lstrip()
            return
        self._insert_text_with_entities(command_el, inner)

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

    def pop(self, inject_newline=True, why=None):
        old_top = self._stack.pop()
        if self._stack:
            self.stack_top = self._stack[-1]
        else:
            self.stack_top = None
        new_top = self.stack_top
        if self.debug:
            print('popping: %r, inject_newline=%r new top=%r'
                  % (old_top, inject_newline, new_top))
        if old_top.kind == 'chapter':
            self.have_chapter = False
        if old_top.kind == 'section':
            self.have_section = False
        if old_top.kind == 'para':
            if why == 'enumerate':
                inject_newline = False
            self.have_para = False
        if old_top.kind == 'listitem':
            inject_newline = False
        if old_top.kind == 'pre':
            inject_newline = False
        if old_top.kind == 'group':
            inject_newline = True
        if old_top.kind == 'display':
            inject_newline = True
        if self.stack_top:
            if inject_newline:
                self.stack_top.add_text('\n')
        return old_top

    def _fixup_nodes(self):
        # Automatic wiring up of next/prev/up for @node
        node_names = list(self.node_dict)
        for i, name in enumerate(node_names):
            node = self.node_dict[name]
            #print repr(name), repr(node)
            def add_ptr(node, name, arg_idx, auto_name):
                """
                Add <nodenext>, <nodeprev>, <nodeup>
                """
                if arg_idx < len(node.args):
                    arg = arg = node.args[arg_idx]
                    ptrnode = node.add_element(name)
                    add_stripped_text(ptrnode, arg)
                else:
                    if auto_name:
                        ptrnode = node.add_element(name)
                        ptrnode.attrs['automatic'] = 'on'
                        ptrnode.add_text(auto_name)

            # For now, put everything after top in one list below the
            # top node:

            if i + 1 < len(node_names):
                auto_next_name = node_names[i + 1]
            else:
                auto_next_name = None
            add_ptr(node, 'nodenext', 1, auto_next_name)

            if i > 1:
                auto_prev_name = node_names[i - 1]
            else:
                auto_prev_name = None
            add_ptr(node, 'nodeprev', 2, auto_prev_name)

            add_ptr(node, 'nodeup', 3, self.top_node.name)

        if self.debug:
            for k in self.node_dict:
                print(repr(k), repr(self.node_dict[k]))

    def _strip_conditionals(self):
        """
        Postprocessing step to (optionally) eliminate things like
        <iftex> entirely, and eliminate e.g. <ifnottex>
        """
        class ConditionalFixer(NoopVisitor):
            def previsit_element(self, element, parents):
                new_children = []
                for child in element.children:
                    if child.is_element('iftex'):
                        # Drop this entirely
                        continue
                    elif child.is_element('ifnottex'):
                        # Eliminate the element, moving
                        # the grandchildren up:
                        for grandchild in child.children:
                            new_children.append(grandchild)
                    else:
                        new_children.append(child)
                element.children = new_children

        v = ConditionalFixer()
        v.visit(self.texinfo)
