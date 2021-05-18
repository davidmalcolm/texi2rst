#!/usr/bin/env python3

from texi2rst import *

import unittest

class Texi2RstTests(unittest.TestCase):
    def setUp(self):
        self.ctxt = Context()

    def make_rst_string(self, doc):
        w = RstWriter(io.StringIO())
        w.visit(doc)
        w.finish()
        return w.f_out.getvalue()

    def make_rst_strings(self, doc):
        class StringOpener(RstOpener):
            def __init__(self):
                self.dict_ = OrderedDict()
            def open_file(self, output_file):
                f_out = io.StringIO()
                self.dict_[output_file] = f_out
                return f_out
            def close_file(self, f_out):
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

  g++-and-gcc
  standards
  invoking-gcc
  c-implementation
  c++-implementation
  c-extensions
  c++-extensions

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
        self.assertEqual(u'Before :samp:`{gcc}` after', out)

    def test_code(self):
        xml_src = '<texinfo>Before <code>gcc</code> after</texinfo>'
        doc = from_xml_string(xml_src)
        doc = fixup_inline_markup(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'Before ``gcc`` after', out)

    def test_code_with_vars(self):
        xml_src = '<para>Target has the <code>_Float<var>n</var></code> type.</para>'
        doc = from_xml_string(xml_src)
        doc = fixup_inline_markup(doc)
        out = self.make_rst_string(doc)
        self.assertEqual(u'Target has the ``_Floatn`` type.\n\n', out)

    def test_code_spacing(self):
        xml_src = '<para><var>$&lbrace;tool&rbrace;</var><code>-torture-execute</code>, where <var>tool</var> is <code>c</code></para>'
        doc = from_xml_string(xml_src)
        doc = convert_to_rst(doc, self.ctxt)
        out = self.make_rst_string(doc)
        self.assertEqual(u':samp:`{${tool}}` ``-torture-execute``, where :samp:`{tool}` is ``c``\n\n', out)

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

    def test_gcc_variable_replacement(self):
        xml_src = '<para>$$VERSION_PACKAGE$$</para>'
        doc = from_xml_string(xml_src)
        doc = convert_to_rst(doc, self.ctxt)
        out = self.make_rst_string(doc)
        self.assertEqual('|package_version|\n\n', out)


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

    def test_option_ref_with_var(self):
        xml_src = '<para>This is similar to how <option>-Walloca-larger-than=</option><var>byte-size</var> works.</para>'
        doc = from_xml_string(xml_src)
        doc = convert_to_rst(doc, self.ctxt)
        out = self.make_rst_string(doc)
        self.assertEqual('This is similar to how :option:`-Walloca-larger-than`:samp:`={byte-size}` works.\n\n', out)

    def test_option_ref_with_var2(self):
        xml_src = '<para>See also <option>-Walloca-larger-than=<var>byte-size</var></option>.</para>'
        doc = from_xml_string(xml_src)
        doc = convert_to_rst(doc, self.ctxt)
        out = self.make_rst_string(doc)
        self.assertEqual('See also :option:`-Walloca-larger-than`:samp:`={byte-size}`.\n\n', out)

    def test_option_with_var_and_space(self):
        xml_src = '<para>same <option>-G <var>num</var></option> value</para>'
        doc = from_xml_string(xml_src)
        doc = convert_to_rst(doc, self.ctxt)
        out = self.make_rst_string(doc)
        self.assertEqual('same :option:`-G `:samp:`{num}` value\n\n', out)

    def test_option_with_var_and_space2(self):
        xml_src = "<para><option>-fmodule-mapper='|ncat <var>ipv4host</var> <var>port</var>'</option>.</para>"
        doc = from_xml_string(xml_src)
        doc = convert_to_rst(doc, self.ctxt)
        out = self.make_rst_string(doc)
        self.assertEqual(":option:`-fmodule-mapper='|ncat `:samp:`{ipv4host}`:samp:`{port}` '.\n\n", out)

    def test_samp_with_var(self):
        xml_src = '<para>form <samp><var>n</var>f2_1</samp></para>'
        doc = from_xml_string(xml_src)
        doc = convert_to_rst(doc, self.ctxt)
        out = self.make_rst_string(doc)
        self.assertEqual('form :samp:`{n}f2_1`\n\n', out)

    def test_man_options_and_variables(self):
        xml_src = '<para>[@option{-f}@var{option}@dots{}] [@option{-m}@var{machine-option}@dots{}]</para>'
        doc = from_xml_string(xml_src)
        doc = convert_to_rst(doc, self.ctxt)
        out = self.make_rst_string(doc)
        self.assertEqual('[ :option:`-f`:samp:`{option}`...] [ :option:`-m`:samp:`{machine-option}`...]\n\n', out)

    def test_heading(self):
        xml_src = '<heading spaces=" ">Tools/packages necessary for building GCC</heading>'
        doc = from_xml_string(xml_src)
        doc = convert_to_rst(doc, self.ctxt)
        out = self.make_rst_string(doc)
        self.assertEqual("""Tools/packages necessary for building GCC
=========================================

""", out)

    def test_section_with_asterisk(self):
        xml_src = '<heading spaces=" ">powerpcle-*-eabi</heading>'
        doc = from_xml_string(xml_src)
        doc = convert_to_rst(doc, self.ctxt)
        out = self.make_rst_string(doc)
        self.assertEqual("""powerpcle-\\*-eabi
=================

""", out)


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
</tableterm><tableitem><indexcommand command="opindex" index="op" spaces=" "><indexterm index="op" number="417" incode="1">Wstrict-prototypes-foo-foo-foo-foo</indexterm></indexcommand>
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
            u'''.. option:: -Wstrict-prototypes , -Wstrict-prototypes-foo-foo-foo-foo
.. option:: -Wno-strict-prototypes

  .. note::

    C and Objective-C only

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

    def test_option_listing_with_vars(self):
        xml_src = ('''
<smallexample endspaces=" ">
<pre xml:space="preserve">-Walloca-larger-than=<var>byte-size</var></pre></smallexample>
''')
        doc = from_xml_string(xml_src)
        doc = convert_to_rst(doc, self.ctxt)
        out = self.make_rst_string(doc)
        self.assertEqual(':option:`-Walloca-larger-than`:samp:`={byte-size}`', out)

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
            u''':samp:`{file}.c`
  C source code that must be preprocessed.

:samp:`{file}.i`
  C source code that should not be preprocessed.

:samp:`{file}.ii`
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
        self.assertEqual(u''':samp:`c90` :samp:`c89` :samp:`iso9899:1990`
  Support all ISO C90 programs (certain GNU extensions that conflict
  with ISO C90 are disabled). Same as :option:`-ansi` for C code.

''', out)

    def test_itemformat_command_flattening(self):
        xml_src = u'''<texinfo>
<para><itemformat command="code">-misel=<var>yes/no</var></itemformat></para>
<para><itemformat command="samp">default </itemformat>
</para>
</texinfo>'''
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual(
            u''':samp:`-misel={yes/no}`

:samp:`default`

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

   /* Control comes here from access
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

    def test_xref_with_var(self):
        xml_src = '<xref label="Range-checks-on-poly_005fints"><xrefnodename>Range checks on <code>poly_int</code>s</xrefnodename></xref>'
        doc = from_xml_string(xml_src)
        doc = fixup_xrefs(doc)
        out = self.make_rst_string(doc)
        self.assertEqual('See :ref:`range-checks-on-poly_ints`', out)

class IntegrationTests(Texi2RstTests):
    def test_empty(self):
        xml_src = '''<texinfo/>'''
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual(u'', out)

    def test_accents(self):
        xml_src = '''<texinfo>
<para>Fran<accent type="cedil">c</accent>ois
</para>
<para>L<accent type="acute" bracketed="off">o</accent>pez-Ib<accent type="acute" bracketed="off">a</accent><accent type="tilde" bracketed="off">n</accent>ez
</para>
<para>von L<accent type="uml" bracketed="off">o</accent>wis
</para>
</texinfo>'''
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual(u'''Franc\u0327ois

Lo\u0301pez-Iba\u0301n\u0303ez

von Lo\u0308wis

''', out)

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

    def test_subsection_with_code(self):
        xml_src = '''<subsection spaces=" "><sectiontitle><code>GIMPLE_ASM</code></sectiontitle>
<cindex index="cp" spaces=" "><indexterm index="cp" number="116"><code>GIMPLE_ASM</code></indexterm></cindex>
</subsection>'''
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual('''GIMPLE_ASM
^^^^^^^^^^

.. index:: GIMPLE_ASM

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
        self.assertTrue(dfs[0].is_element('document'))
        self.assertTrue(dfs[1].is_element('A'))
        self.assertTrue(dfs[2].is_element('B-1'))
        self.assertTrue(dfs[3].is_element('C-1'))
        self.assertTrue(dfs[4].is_element('C-2'))
        self.assertTrue(dfs[5].is_element('B-2'))
        self.assertTrue(dfs[6].is_element('C-3'))
        self.assertTrue(dfs[7].is_element('C-4'))

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

    def test_table_with_variable_number_of_columns(self):
        xml_src = '''
<multitable spaces=" " endspaces=" "><columnprototypes><columnprototype bracketed="on">Modifier</columnprototype> <columnprototype bracketed="on">Print the opcode suffix for the size of th</columnprototype> <columnprototype bracketed="on">Operand</columnprototype> <columnprototype bracketed="on"><samp>att</samp></columnprototype> <columnprototype bracketed="on"><samp>intel</samp></columnprototype></columnprototypes>
<thead><row><entry command="headitem" spaces=" "><para>Modifier </para></entry><entry command="tab" spaces=" "><para>Description </para></entry><entry command="tab" spaces=" "><para>Operand </para></entry><entry command="tab" spaces=" "><para><samp>att</samp> </para></entry><entry command="tab" spaces=" "><para><samp>intel</samp>
</para></entry></row></thead>
<tbody><row><entry command="item" spaces=" "><para><code>P</code>
</para></entry><entry command="tab" spaces=" "><para>If used for a function, print the PLT suffix and generate PIC code.
For example, emit <code>foo&arobase;PLT</code> instead of &textrsquo;foo&textrsquo; for the function
foo(). If used for a constant, drop all syntax-specific prefixes and
issue the bare constant. See <code>p</code> above.
</para></entry></row><row><entry command="item" spaces=" "><para><code>q</code>
</para></entry><entry command="tab" spaces=" "><para>Print the DImode name of the register.
</para></entry><entry command="tab" spaces=" "><para><code>%q0</code>
</para></entry><entry command="tab" spaces=" "><para><code>%rax</code>
</para></entry><entry command="tab" spaces=" "><para><code>rax</code>
</para></entry></row><row><entry command="item" spaces=" "><para><code>Q</code>
</para></entry><entry command="tab" spaces=" "><para>print the opcode suffix of q.
</para></entry><entry command="tab" spaces=" "><para><code>%Q0</code>
</para></entry><entry command="tab" spaces=" "><para><code>q</code>
</para></entry><entry command="tab">
</entry></row></tbody></multitable>'''
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual(
            u'''========  ====================================================================  =======  ===========  =============
Modifier  Description                                                           Operand  :samp:`att`  :samp:`intel`
========  ====================================================================  =======  ===========  =============
``P``     If used for a function, print the PLT suffix and generate PIC code.
          For example, emit ``foo@PLT`` instead of 'foo' for the function
          foo(). If used for a constant, drop all syntax-specific prefixes and
          issue the bare constant. See ``p`` above.
``q``     Print the DImode name of the register.                                ``%q0``  ``%rax``     ``rax``
``Q``     print the opcode suffix of q.                                         ``%Q0``  ``q``
========  ====================================================================  =======  ===========  =============
''', out)

class TestFunctionDefinitions(Texi2RstTests):
    def test_spacing_in_between_nodes(self):
        xml_src = '<definitionitem><deftype>tree</deftype> <deffunction>gimple_asm_clobber_op</deffunction> <defdelimiter>(</defdelimiter><defparamtype>const</defparamtype></definitionitem>'
        tree = from_xml_string(xml_src)
        for child in tree.children[0].children:
            assert isinstance(child, Element)

    def test_function(self):
        xml_src = '''
<deftypefn spaces=" " endspaces=" "><definitionterm><indexterm index="fn" number="1924" mergedindex="cp">gimple_asm_clobber_op</indexterm><defcategory bracketed="on">GIMPLE function</defcategory> <deftype>tree</deftype> <deffunction>gimple_asm_clobber_op</deffunction> <defdelimiter>(</defdelimiter><defparamtype>const</defparamtype> <defparam>gasm</defparam> <defparamtype>*g</defparamtype><defdelimiter>,</defdelimiter> <defparamtype>unsigned</defparamtype> <defparam>index</defparam><defdelimiter>)</defdelimiter></definitionterm>
<definitionitem><para>Return clobber operand <code>INDEX</code> of <code>GIMPLE_ASM</code> <code>G</code>.
</para></definitionitem></deftypefn>'''
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual(
            '''.. function:: tree gimple_asm_clobber_op (const gasm *g, unsigned index)

  Return clobber operand ``INDEX`` of ``GIMPLE_ASM`` ``G``.

''', out)


    def test_function_deftypefun(self):
        xml_src = '''
<defmac spaces=" " endspaces=" "><definitionterm><indexterm index="fn" number="3744" mergedindex="cp">HANDLE_PRAGMA_PACK_WITH_EXPANSION</indexterm><defcategory automatic="on" bracketed="on">Macro</defcategory> <deffunction>HANDLE_PRAGMA_PACK_WITH_EXPANSION</deffunction></definitionterm>
<definitionitem><para>Define this macro if macros should be expanded in the
arguments of <samp>#pragma pack</samp>.
</para></definitionitem></defmac>'''
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual(
            '''.. macro:: HANDLE_PRAGMA_PACK_WITH_EXPANSION

  Define this macro if macros should be expanded in the
  arguments of :samp:`#pragma pack`.

''', out)

    def test_deftypevr(self):
        xml_src = '''
<deftypevr spaces=" " endspaces=" "><definitionterm><indexterm index="vr" number="65" mergedindex="cp">TARGET_HAVE_COUNT_REG_DECR_P</indexterm><defcategory bracketed="on">Target Hook</defcategory> <deftype>bool</deftype> <defvariable>TARGET_HAVE_COUNT_REG_DECR_P</defvariable></definitionterm>
<definitionitem><para>Return true if the target supports hardware count register for decrement
and branch.
The default value is false.
</para></definitionitem></deftypevr>'''
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual(
            '''.. c:var:: bool TARGET_HAVE_COUNT_REG_DECR_P

  Return true if the target supports hardware count register for decrement
  and branch.
  The default value is false.

''', out)

    def test_deftypefun(self):
        xml_src = '''
<deftypefun spaces=" " endspaces=" "><definitionterm><indexterm index="fn" number="2697" mergedindex="cp">constraint_satisfied_p</indexterm><defcategory automatic="on" bracketed="on">Function</defcategory> <deftype>bool</deftype> <deffunction>constraint_satisfied_p</deffunction> <defdelimiter>(</defdelimiter><defparamtype>rtx</defparamtype> <defparam><var>exp</var></defparam><defdelimiter>,</defdelimiter> <defparamtype>enum</defparamtype> <defparam>constraint_num</defparam> <defparam><var>c</var></defparam><defdelimiter>)</defdelimiter></definitionterm>
<definitionitem><para>Like the <code>satisfies_constraint_<var>m</var></code> functions, but the
constraint to test is given as an argument, <var>c</var>.  If <var>c</var>
specifies a register constraint, this function will always return
<code>false</code>.
</para></definitionitem></deftypefun>'''
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual(
            '''.. function:: bool constraint_satisfied_p (rtx exp, enum constraint_num c)

  Like the ``satisfies_constraint_m`` functions, but the
  constraint to test is given as an argument, :samp:`{c}`.  If :samp:`{c}`
  specifies a register constraint, this function will always return
  ``false``.

''', out)


class TestLinks(Texi2RstTests):
    def test_url(self):
        xml_src = '<para>The <uref><urefurl>https://sourceware.org/cygwin/</urefurl><urefreplacement>Cygwin</urefreplacement></uref> project;</para>'
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual(
                '''The `Cygwin <https://sourceware.org/cygwin/>`_ project;

''', out)


    def test_url_urefdesc(self):
        xml_src = '<para><uref><urefurl>https://www.openacc.org</urefurl><urefdesc spaces=" ">OpenACC</urefdesc></uref> Application Programming</para>'
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual(
                '''`OpenACC <https://www.openacc.org>`_ Application Programming

''', out)

class TestBullets(Texi2RstTests):
    def test_bullets(self):
        xml_src = '<itemize commandarg="bullet" endspaces=" "><itemprepend>&bullet;</itemprepend><listitem><prepend>&bullet;</prepend><para><uref><urefurl>https://example.com</urefurl></uref></para></listitem></itemize>'
        tree = from_xml_string(xml_src)
        tree = convert_to_rst(tree, self.ctxt)
        out = self.make_rst_string(tree)
        self.assertEqual(
                '''* https://example.com

''', out)
