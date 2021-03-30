#!/usr/bin/env python3

from texi2xml import *

import unittest

class Texi2XmlTests(unittest.TestCase):
    def assert_xml_conversion(self, texisrc, expectedxmlstr, debug=0, with_dtd=0, filename=None):
        p = Parser('', [],
                   debug=debug,
                   with_dtd=with_dtd,
                   filename=filename)
        tree = p.parse_str(texisrc)
        if with_dtd:
            dtd_line = DTD_LINE
        else:
            dtd_line = None
        if debug:
            tree.dump(sys.stdout)
        xmlstr = tree.toxml(dtd_line)
        self.maxDiff = 10000
        self.assertMultiLineEqual(expectedxmlstr, xmlstr)


class CommentTests(Texi2XmlTests):
    def test_comment(self):
        self.assert_xml_conversion(
            '@c This is a comment.',

            '<texinfo><!-- c This is a comment. -->\n</texinfo>')

    def test_blank_lines(self):
        self.assert_xml_conversion(
            '''
@c -have to add text:  beginning of chapter 8

@c
@c anything else?                       --mew 10feb93
''',
            '''<texinfo>
<!-- c -have to add text:  beginning of chapter 8 -->

<!-- c -->
<!-- c anything else?                       -mew 10feb93 -->
</texinfo>''')

class PreambleTests(Texi2XmlTests):
    def test_preamble(self):
        self.assert_xml_conversion(
            '''
\input texinfo  @c -*-texinfo-*-
@c %**start of header
@setfilename gcc.info
''',
            '''<texinfo>
<preamble>\\input texinfo  @c -*-texinfo-*-
</preamble><!-- c %**start of header -->
<setfilename>gcc.info</setfilename>
</texinfo>''')

    def test_dtd(self):
        self.assert_xml_conversion(
            '',

            '''<?xml version="1.0"?>
<!DOCTYPE texinfo PUBLIC "-//GNU//DTD TexinfoML V5.0//EN" "http://www.gnu.org/software/texinfo/dtd/5.0/texinfo.dtd">
<texinfo xml:lang="en">
<filename file="gcc.xml"></filename>
</texinfo>''',
            with_dtd=1,
            filename='gcc.xml')


class ParaTests(Texi2XmlTests):
    def test_para(self):
        self.assert_xml_conversion(
            'Hello world\n',

            '<texinfo><para>Hello world\n</para>\n</texinfo>')

    def test_paras(self):
        self.assert_xml_conversion(
            '''
Line 1 of para 1.
Line 2 of para 1.

Line 1 of para 2.
Line 2 of para 2.
''',
            '''<texinfo>
<para>Line 1 of para 1.
Line 2 of para 1.
</para>
<para>Line 1 of para 2.
Line 2 of para 2.
</para>
</texinfo>''')


class InlineTests(Texi2XmlTests):
    def test_inline(self):
        self.assert_xml_conversion(
            '''Example of @emph{inline markup}.\n''',

            ('<texinfo><para>Example of <emph>inline markup</emph>.\n</para>\n</texinfo>'))

    def test_multiple_inlines(self):
        self.assert_xml_conversion(
            '''
An amendment to the 1990 standard was published in 1995.  This
amendment added digraphs and @code{__STDC_VERSION__} to the language,
but otherwise concerned the library.  This amendment is commonly known
as @dfn{AMD1}; the amended standard is sometimes known as @dfn{C94} or
@dfn{C95}.  To select this standard in GCC, use the option
@option{-std=iso9899:199409} (with, as for other standard versions,
@option{-pedantic} to receive all required diagnostics).
''',
            '''<texinfo>
<para>An amendment to the 1990 standard was published in 1995.  This
amendment added digraphs and <code>__STDC_VERSION__</code> to the language,
but otherwise concerned the library.  This amendment is commonly known
as <dfn>AMD1</dfn>; the amended standard is sometimes known as <dfn>C94</dfn> or
<dfn>C95</dfn>.  To select this standard in GCC, use the option
<option>-std=iso9899:199409</option> (with, as for other standard versions,
<option>-pedantic</option> to receive all required diagnostics).
</para>
</texinfo>''')

    def test_multiline_inlines(self):
        self.assert_xml_conversion(
            '''
whole standard including all the library facilities; a @dfn{conforming
freestanding implementation} is only required to provide certain
''',
            '''<texinfo>
<para>whole standard including all the library facilities; a <dfn>conforming
freestanding implementation</dfn> is only required to provide certain
</para>
</texinfo>''')

    def test_copyright(self):
        self.assert_xml_conversion(
            '\nCopyright @copyright{} 2015  John Doe.\n',

            '''<texinfo>
<para>Copyright &copyright; 2015  John Doe.
</para>
</texinfo>''')

    def test_email(self):
        self.assert_xml_conversion(
            '''
Send mail to
@email{jdoe@@example.com} or @email{jbloggs@@example.co.uk}.
''',
            '''<texinfo>
<para>Send mail to
<email><emailaddress>jdoe&arobase;example.com</emailaddress></email> or <email><emailaddress>jbloggs&arobase;example.co.uk</emailaddress></email>.
</para>
</texinfo>''')

    def test_uref(self):
        self.assert_xml_conversion(
            "\nsee @uref{http://gcc.gnu.org/projects/@/cxx0x.html}. To select this\n",

            '''<texinfo>
<para>see <uref><urefurl>http://gcc.gnu.org/projects/&slashbreak;cxx0x.html</urefurl></uref>. To select this
</para>
</texinfo>''')


class StructuralTests(Texi2XmlTests):
    def test_sections(self):
        self.assert_xml_conversion(
            '''
@section Section 1
Text in section 1.

@section Section 2
Text in section 2.
''',
            '''<texinfo>
<section spaces=" "><sectiontitle>Section 1</sectiontitle>
<para>Text in section 1.
</para>
</section>
<section spaces=" "><sectiontitle>Section 2</sectiontitle>
<para>Text in section 2.
</para>
</section>
</texinfo>''')

    def test_chapters(self):
        self.assert_xml_conversion(
            '''
@chapter Chapter 1
@section Chapter 1 Section 1
Text in chapter 1 section 1.

@section Chapter 1 Section 2
Text in chapter 1 section 2.

@chapter Chapter 2
@section Chapter 2 Section 1
Text in chapter 2 section 1.

@section Chapter 2 Section 2
Text in chapter 2 section 2.
''',
            '''<texinfo>
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
</texinfo>''')

    def test_settitle(self):
        self.assert_xml_conversion(
            '\n@settitle Using the GNU Compiler Collection (GCC)\n',

            '''<texinfo>
<settitle spaces=" ">Using the GNU Compiler Collection (GCC)</settitle>
</texinfo>''')


class IndexTests(Texi2XmlTests):
    def test_cindex(self):
        self.assert_xml_conversion(
            '\n@cindex first\n@cindex second\n',

            '''<texinfo>
<cindex index="cp" spaces=" "><indexterm index="cp" number="1">first</indexterm></cindex>
<cindex index="cp" spaces=" "><indexterm index="cp" number="2">second</indexterm></cindex>
</texinfo>''')

    def test_findex(self):
        self.assert_xml_conversion(
            '\n@findex first\n@findex second\n',

            '''<texinfo>
<findex index="fn" spaces=" "><indexterm index="fn" number="1" mergedindex="cp">first</indexterm></findex>
<findex index="fn" spaces=" "><indexterm index="fn" number="2" mergedindex="cp">second</indexterm></findex>
</texinfo>''')

    def test_opindex(self):
        self.assert_xml_conversion(
            '\n@opindex first\n@opindex second\n',

            '''<texinfo>
<indexcommand command="opindex" index="op" spaces=" "><indexterm index="op" number="1" incode="1">first</indexterm></indexcommand>
<indexcommand command="opindex" index="op" spaces=" "><indexterm index="op" number="2" incode="1">second</indexterm></indexcommand>
</texinfo>''')

    def test_defcodeindex(self):
        self.assert_xml_conversion(
            '''
@defcodeindex op
@syncodeindex fn cp
''',
            '''<texinfo>
<defcodeindex value="op" line=" op"></defcodeindex>
<syncodeindex from="fn" to="cp" line=" fn cp"></syncodeindex>
</texinfo>''')

class EnvironmentTests(Texi2XmlTests):
    def test_copying(self):
        self.assert_xml_conversion(
            '''
@copying
Text goes here.
@end copying
''',
            '''<texinfo>
<copying endspaces=" ">
<para>Text goes here.
</para></copying></texinfo>''')

    def test_itemize(self):
        self.assert_xml_conversion(
            '''
@itemize @bullet
@item
This is item 1

@item
This is item 2
@end itemize
''',
            '''<texinfo>
<itemize commandarg="bullet" spaces=" " endspaces=" "><itemprepend><formattingcommand command="bullet"/></itemprepend>
<listitem><prepend>&bullet;</prepend>
<para>This is item 1
</para>
</listitem><listitem><prepend>&bullet;</prepend>
<para>This is item 2
</para>
</listitem></itemize>
</texinfo>''')

    def test_enumerate(self):
        self.assert_xml_conversion(
            '''
@enumerate
@item If @var{X} is @code{0xf},
then the @var{n}-th bit of @var{val} is returned unaltered.

@item If X is in the range 0@dots{}7,
then the @var{n}-th result bit is set to the @var{X}-th bit of @var{bits}

@item If X is in the range 8@dots{}@code{0xe},
then the @var{n}-th result bit is undefined.
@end enumerate
''',
            '''<texinfo>
<enumerate first="1" endspaces=" ">
<listitem spaces=" "><para>If <var>X</var> is <code>0xf</code>,
then the <var>n</var>-th bit of <var>val</var> is returned unaltered.
</para>
</listitem><listitem spaces=" "><para>If X is in the range 0&dots;7,
then the <var>n</var>-th result bit is set to the <var>X</var>-th bit of <var>bits</var>
</para>
</listitem><listitem spaces=" "><para>If X is in the range 8&dots;<code>0xe</code>,
then the <var>n</var>-th result bit is undefined.
</para></listitem></enumerate>
</texinfo>''')

    def test_smallexample(self):
        self.assert_xml_conversion(
            '''
@smallexample
#define foo() bar
foo
baz
@end smallexample
''',
            '''<texinfo>
<smallexample endspaces=" ">
<pre xml:space="preserve">#define foo() bar
foo
baz
</pre></smallexample>
</texinfo>''')

    def test_code_example(self):
        self.assert_xml_conversion(
            '''
@smallexample
int a;
@dots{}
if (!a > 1) @{ @dots{} @}
@end smallexample
''',
            '''<texinfo>
<smallexample endspaces=" ">
<pre xml:space="preserve">int a;
&dots;
if (!a &gt; 1) &lbrace; &dots; &rbrace;
</pre></smallexample>
</texinfo>''')

    def test_code_with_group(self):
        self.assert_xml_conversion(
            '''
@smallexample
@group
float area(float radius)
@{
   return 3.14159 * radius * radius;
@}
@end group
@end smallexample
''',
            '''<texinfo>
<smallexample endspaces=" ">
<group endspaces=" ">
<pre xml:space="preserve">float area(float radius)
&lbrace;
   return 3.14159 * radius * radius;
&rbrace;
</pre></group>
</smallexample>
</texinfo>''')

    def test_display(self):
        self.assert_xml_conversion(
            '''
@display
This is an example...

...of multiline text
@end display
''',
            '''<texinfo>
<display endspaces=" ">
<pre xml:space="preserve">This is an example...

...of multiline text
</pre></display>
</texinfo>''')

class VariableTests(Texi2XmlTests):
    def test_set(self):
        self.assert_xml_conversion(
            '''
@set version-GCC 6.0.0
@set DEVELOPMENT
@set VERSION_PACKAGE (GCC)''' + ' ' + '''
''',
            '''<texinfo>
<set name="version-GCC" line=" version-GCC 6.0.0">6.0.0</set>
<set name="DEVELOPMENT" line=" DEVELOPMENT"></set>
<set name="VERSION_PACKAGE" line=" VERSION_PACKAGE (GCC) ">(GCC)</set>
</texinfo>''')

    def test_clear(self):
        self.assert_xml_conversion(
            '\n@clear INTERNALS\n',

            '''<texinfo>
<clear name="INTERNALS" line=" INTERNALS"></clear>
</texinfo>''')

    def test_variable(self):
        self.assert_xml_conversion(
            '''It corresponds to the compilers
@ifset VERSION_PACKAGE
@value{VERSION_PACKAGE}
@end ifset
version @value{version-GCC}.
''',
            '''<texinfo><para>It corresponds to the compilers
<ifset>VERSION_PACKAGE</ifset>
<value>VERSION_PACKAGE</value>
version <value>version-GCC</value>.
</para>
</texinfo>''')


class MenuTests(Texi2XmlTests):
    def test_menu(self):
        self.assert_xml_conversion(
            '''
@menu
* Item one::       Description one.
* Item two::       Description two.
* Item three::     Description three.
@end menu
''',
            '''<texinfo>
<menu endspaces=" ">
<menuentry leadingtext="* "><menunode separator="::       ">Item one</menunode><menudescription><pre xml:space="preserve">Description one.
</pre></menudescription></menuentry><menuentry leadingtext="* "><menunode separator="::       ">Item two</menunode><menudescription><pre xml:space="preserve">Description two.
</pre></menudescription></menuentry><menuentry leadingtext="* "><menunode separator="::     ">Item three</menunode><menudescription><pre xml:space="preserve">Description three.
</pre></menudescription></menuentry></menu>
</texinfo>''')

    def test_menu_with_multiline_item(self):
        self.assert_xml_conversion(
            '''
@menu
* Item one::       Description one.
* Item two::       Description two
                   continues here.
* Item three::     Description three.
@end menu
''',
            '''<texinfo>
<menu endspaces=" ">
<menuentry leadingtext="* "><menunode separator="::       ">Item one</menunode><menudescription><pre xml:space="preserve">Description one.
</pre></menudescription></menuentry><menuentry leadingtext="* "><menunode separator="::       ">Item two</menunode><menudescription><pre xml:space="preserve">Description two
                   continues here.
</pre></menudescription></menuentry><menuentry leadingtext="* "><menunode separator="::     ">Item three</menunode><menudescription><pre xml:space="preserve">Description three.
</pre></menudescription></menuentry></menu>
</texinfo>''')


class TextTests(Texi2XmlTests):
    def test_arobase_at_line_start(self):
        self.assert_xml_conversion(
            '''
enumeration (only for Objective-C), method attributes and the
@@optional and @@required keywords in protocols.  GCC supports
Objective-C++ and features available in Objective-C are also available
''',
            '''<texinfo>
<para>enumeration (only for Objective-C), method attributes and the
&arobase;optional and &arobase;required keywords in protocols.  GCC supports
Objective-C++ and features available in Objective-C are also available
</para>
</texinfo>''')

    def test_text_quotes(self):
        self.assert_xml_conversion(
            "\nfoo ``bar'' baz\n",

            '''<texinfo>
<para>foo &textldquo;bar&textrdquo; baz
</para>
</texinfo>''')

    def test_text_quote(self):
        self.assert_xml_conversion(
            "\nfoo's bar\n",

            '''<texinfo>
<para>foo&textrsquo;s bar
</para>
</texinfo>''')

    def test_eosperiod(self):
        self.assert_xml_conversion(
            "\nHello world@.\n",

            '''<texinfo>
<para>Hello world&eosperiod;
</para>
</texinfo>''')

    def test_eosperiod_2(self):
        self.assert_xml_conversion(
            "\ncompiler by its own name, or as GCC@.  Either is correct.\n",

            '''<texinfo>
<para>compiler by its own name, or as GCC&eosperiod;  Either is correct.
</para>
</texinfo>''')

    def test_mdash(self):
        self.assert_xml_conversion(
            '''
Many options have long names starting with @samp{-f} or with
@samp{-W}---for example,
''',

            '''<texinfo>
<para>Many options have long names starting with <samp>-f</samp> or with
<samp>-W</samp>&textmdash;for example,
</para>
</texinfo>''')


    def test_noeos(self):
        self.assert_xml_conversion(
            '''
Warn about ISO C constructs that are outside of the common subset of
ISO C and ISO C++, e.g.@: request for implicit conversion from
''',

            '''<texinfo>
<para>Warn about ISO C constructs that are outside of the common subset of
ISO C and ISO C++, e.g.&noeos; request for implicit conversion from
</para>
</texinfo>''')


class NodeTests(Texi2XmlTests):
    def test_four_args(self):
        self.assert_xml_conversion(
            '''
@node Top, G++ and GCC,, (DIR)
@top Introduction
''',
            '''<texinfo>
<node name="Top" spaces=" "><nodename>Top</nodename><nodenext spaces=" ">G++ and GCC</nodenext><nodeprev></nodeprev><nodeup spaces=" ">(DIR)</nodeup></node>
</texinfo>''')

    def test_automatic(self):
        self.assert_xml_conversion(
            '''
@node Top, G++ and GCC,, (DIR)
@top Introduction

@node G++ and GCC

@node Standards
''',
            '''<texinfo>
<node name="Top" spaces=" "><nodename>Top</nodename><nodenext spaces=" ">G++ and GCC</nodenext><nodeprev></nodeprev><nodeup spaces=" ">(DIR)</nodeup></node>

<node name="G_002b_002b-and-GCC" spaces=" "><nodename>G++ and GCC</nodename><nodenext automatic="on">Standards</nodenext><nodeup automatic="on">Top</nodeup></node>

<node name="Standards" spaces=" "><nodename>Standards</nodename><nodeprev automatic="on">G++ and GCC</nodeprev><nodeup automatic="on">Top</nodeup></node>
</texinfo>''')

class XrefTests(Texi2XmlTests):
    def test_one_arg(self):
        self.assert_xml_conversion(
            '''
@xref{Option Index}, for an index to GCC's options.
''',
            '''<texinfo>
<xref label="Option-Index"><xrefnodename>Option Index</xrefnodename></xref><para>, for an index to GCC&textrsquo;s options.
</para>
</texinfo>''')

    def test_two_args(self):
        self.assert_xml_conversion(
            '''
By default, GCC provides some extensions to the C++ language; @xref{C++
Dialect Options,Options Controlling C++ Dialect}.  Use of the
''',

            '''<texinfo>
<para>By default, GCC provides some extensions to the C++ language; <xref label="C_002b_002b-Dialect-Options"><xrefnodename>C++
Dialect Options</xrefnodename><xrefinfoname>Options Controlling C++ Dialect</xrefinfoname></xref>.  Use of the
</para>
</texinfo>''')

    def test_three_args_with_empty_second_arg(self):
        self.assert_xml_conversion(
            '''
errors rather than warnings).  @xref{C Dialect Options,,Options
Controlling C Dialect}.
''',

            '''<texinfo>
<para>errors rather than warnings).  <xref label="C-Dialect-Options"><xrefnodename>C Dialect Options</xrefnodename><xrefprinteddesc>Options
Controlling C Dialect</xrefprinteddesc></xref>.
</para>
</texinfo>''')

    def test_five_args(self):
        self.assert_xml_conversion(
            '''
@xref{Top,,
Introduction, gccint, GNU Compiler Collection (GCC) Internals}''',

            '''<texinfo>
<xref label="Top" manual="gccint"><xrefnodename>Top</xrefnodename><xrefprinteddesc spaces="\\n">Introduction</xrefprinteddesc><xrefinfofile spaces=" ">gccint</xrefinfofile><xrefprintedname spaces=" ">GNU Compiler Collection (GCC) Internals</xrefprintedname></xref></texinfo>''')

    def test_pxref(self):
        self.assert_xml_conversion(
            '''
Using this option is roughly equivalent to adding the
@code{gnu_inline} function attribute to all inline functions
(@pxref{Function Attributes}).
''',
            '''<texinfo>
<para>Using this option is roughly equivalent to adding the
<code>gnu_inline</code> function attribute to all inline functions
(<pxref label="Function-Attributes"><xrefnodename>Function Attributes</xrefnodename></pxref>).
</para>
</texinfo>''')


class TableTests(Texi2XmlTests):
    def test_dfn_table(self):
        self.assert_xml_conversion(
            '''
@table @dfn
@item first item
Description of first item.

@item second item
Description of second item.
@end table
''',
            '''<texinfo>
<table commandarg="dfn" spaces=" " endspaces=" ">
<tableentry><tableterm><item spaces=" "><itemformat command="dfn">first item</itemformat></item>
</tableterm><tableitem><para>Description of first item.
</para>
</tableitem></tableentry><tableentry><tableterm><item spaces=" "><itemformat command="dfn">second item</itemformat></item>
</tableterm><tableitem><para>Description of second item.
</para></tableitem></tableentry></table></texinfo>''')


class MacroTests(Texi2XmlTests):
    def test_macro(self):
        self.assert_xml_conversion(
            r'''
@macro gccoptlist{body}
@smallexample
\body\
@end smallexample
@end macro

@iftex
@alias gol = *
@end iftex
@ifnottex
@macro gol
@end macro
@end ifnottex

@gccoptlist{-c  -S  -E  -o @var{file}  -no-canonical-prefixes  @gol
-pipe  -pass-exit-codes  @gol
-x @var{language}  -v  -###  --help@r{[}=@var{class}@r{[},@dots{}@r{]]}  --target-help  @gol
--version -wrapper @@@var{file} -fplugin=@var{file} -fplugin-arg-@var{name}=@var{arg}  @gol
-fdump-ada-spec@r{[}-slim@r{]} -fada-spec-parent=@var{unit} -fdump-go-spec=@var{file}}
''',

            '''<texinfo>
<macro name="gccoptlist" line=" gccoptlist{body}"><formalarg>body</formalarg>@smallexample
\\body\\
@end smallexample
</macro>

<macro name="gol" line=" gol"></macro>
<smallexample endspaces=" ">
<pre xml:space="preserve">-c  -S  -E  -o <var>file</var>  -no-canonical-prefixes  
-pipe  -pass-exit-codes  
-x <var>language</var>  -v  -###  --help<r>[</r>=<var>class</var><r>[</r>,&dots;<r>]]</r>  --target-help  
--version -wrapper &arobase;<var>file</var> -fplugin=<var>file</var> -fplugin-arg-<var>name</var>=<var>arg</var>  
-fdump-ada-spec<r>[</r>-slim<r>]</r> -fada-spec-parent=<var>unit</var> -fdump-go-spec=<var>file</var>
</pre></smallexample>
</texinfo>''')


class OtherTests(Texi2XmlTests):
    def test_page(self):
        self.assert_xml_conversion(
            '\n@page\n',

            '''<texinfo>
<page></page>
</texinfo>''')

    def test_vskip(self):
        self.assert_xml_conversion(
            "\n@vskip 0pt plus 1filll\n",

            '''<texinfo>
<vskip> 0pt plus 1filll</vskip>
</texinfo>''')

    def test_paragraphindent(self):
        self.assert_xml_conversion(
            '@paragraphindent 1\n',

            '<texinfo><paragraphindent value="1" line=" 1"></paragraphindent>\n</texinfo>')

    def test_trailing_at(self):
        self.assert_xml_conversion(
            '''
Warn for suspicious calls to the @code{memset} built-in function, if the
second argument is not zero and the third argument is zero.  This warns e.g.@
about @code{memset (buf, sizeof buf, 0)} where most probably
@code{memset (buf, 0, sizeof buf)} was meant instead.
''',
           '''<texinfo>
<para>Warn for suspicious calls to the <code>memset</code> built-in function, if the
second argument is not zero and the third argument is zero.  This warns e.g.<spacecmd type="nl"/>about <code>memset (buf, sizeof buf, 0)</code> where most probably
<code>memset (buf, 0, sizeof buf)</code> was meant instead.
</para>
</texinfo>''')

    def test_at_space(self):
        self.assert_xml_conversion(
            '''
Generate .debug_pubnames and .debug_pubtypes sections in a format
suitable for conversion into a GDB@ index.  This option is only useful
with a linker that can produce GDB@ index version 7.
''',
           '''<texinfo>
<para>Generate .debug_pubnames and .debug_pubtypes sections in a format
suitable for conversion into a GDB<spacecmd type="spc"/>index.  This option is only useful
with a linker that can produce GDB<spacecmd type="spc"/>index version 7.
</para>
</texinfo>''')

    def test_linebreak(self):
        self.assert_xml_conversion(
            '''
Last printed October 2003 for GCC 3.3.1.@*
Printed copies are available for $45 each.
''',
            '''<texinfo>
<para>Last printed October 2003 for GCC 3.3.1.&linebreak;
Printed copies are available for $45 each.
</para>
</texinfo>''')

    def test_slashbreak(self):
        self.assert_xml_conversion(
            '''
Produce code optimized for the most common IA32/@/AMD64/@/EM64T processors.
''',
            '''<texinfo>
<para>Produce code optimized for the most common IA32/&slashbreak;AMD64/&slashbreak;EM64T processors.
</para>
</texinfo>''')

    def test_accents(self):
        self.assert_xml_conversion(
            '''
Fran@,{c}ois

L@'opez-Ib@'a@~nez

von L@"owis
''',
            '''<texinfo>
<para>Fran<accent type="cedil">c</accent>ois
</para>
<para>L<accent type="acute" bracketed="off">o</accent>pez-Ib<accent type="acute" bracketed="off">a</accent><accent type="tilde" bracketed="off">n</accent>ez
</para>
<para>von L<accent type="uml" bracketed="off">o</accent>wis
</para>
</texinfo>''')
