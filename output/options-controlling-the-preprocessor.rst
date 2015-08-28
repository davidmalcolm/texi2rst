.. _preprocessor-options:

Options Controlling the Preprocessor
************************************

.. index:: preprocessor options

.. index:: options, preprocessor

These options control the C preprocessor, which is run on each C source
file before actual compilation.

If you use the :option:`-E` option, nothing is done except preprocessing.
Some of these options make sense only together with :option:`-E` because
they cause the preprocessor output to be unsuitable for actual
compilation.

.. option:: -Wp,option, -Wp

  You can use :option:`-Wp,``option``` to bypass the compiler driver
  and pass ``option`` directly through to the preprocessor.  If
  ``option`` contains commas, it is split into multiple options at the
  commas.  However, many options are modified, translated or interpreted
  by the compiler driver before being passed to the preprocessor, and
  :option:`-Wp` forcibly bypasses this phase.  The preprocessor's direct
  interface is undocumented and subject to change, so whenever possible
  you should avoid using :option:`-Wp` and let the driver handle the
  options instead.

.. option:: -Xpreprocessor option, -Xpreprocessor

  Pass ``option`` as an option to the preprocessor.  You can use this to
  supply system-specific preprocessor options that GCC does not 
  recognize.

  If you want to pass an option that takes an argument, you must use
  :option:`-Xpreprocessor` twice, once for the option and once for the argument.

.. option:: -no-integrated-cpp

  Perform preprocessing as a separate pass before compilation.
  By default, GCC performs preprocessing as an integrated part of
  input tokenization and parsing.
  If this option is provided, the appropriate language front end
  (:command:`cc1`, :command:`cc1plus`, or :command:`cc1obj` for C, C++,
  and Objective-C, respectively) is instead invoked twice,
  once for preprocessing only and once for actual compilation
  of the preprocessed input.
  This option may be useful in conjunction with the :option:`-B` or
  :option:`-wrapper` options to specify an alternate preprocessor or
  perform additional processing of the program source between
  normal preprocessing and compilation.

.. Copyright (C) 1999-2015 Free Software Foundation, Inc.
   This is part of the CPP and GCC manuals.
   For copying conditions, see the file gcc.texi.
   -
   Options affecting the preprocessor
   -
   If this file is included with the flag ``cppmanual'' set, it is
   formatted for inclusion in the CPP manual; otherwise the main GCC manual.

.. option:: -D name, -D

  Predefine ``name`` as a macro, with definition ``1``.

-D ``name``=``definition``
  The contents of ``definition`` are tokenized and processed as if
  they appeared during translation phase three in a #define
  directive.  In particular, the definition will be truncated by
  embedded newline characters.

  If you are invoking the preprocessor from a shell or shell-like
  program you may need to use the shell's quoting syntax to protect
  characters such as spaces that have a meaning in the shell syntax.

  If you wish to define a function-like macro on the command line, write
  its argument list with surrounding parentheses before the equals sign
  (if any).  Parentheses are meaningful to most shells, so you will need
  to quote the option.  With :command:`sh` and :command:`csh`,
  :option:`-D'``name``(``args...``)=``definition``'` works.

  :option:`-D` and :option:`-U` options are processed in the order they
  are given on the command line.  All :option:`-imacros ``file``` and
  :option:`-include ``file``` options are processed after all
  :option:`-D` and :option:`-U` options.

.. option:: -U name, -U

  Cancel any previous definition of ``name``, either built in or
  provided with a :option:`-D` option.

.. option:: -undef

  Do not predefine any system-specific or GCC-specific macros.  The
  standard predefined macros remain defined.

.. option:: -I dir, -I

  Add the directory ``dir`` to the list of directories to be searched
  for header files.
  Directories named by :option:`-I` are searched before the standard
  system include directories.  If the directory ``dir`` is a standard
  system include directory, the option is ignored to ensure that the
  default search order for system directories and the special treatment
  of system headers are not defeated
  .
  If ``dir`` begins with ``=``, then the ``=`` will be replaced
  by the sysroot prefix; see :option:`--sysroot` and :option:`-isysroot`.

.. option:: -o file, -o

  Write output to ``file``.  This is the same as specifying ``file``
  as the second non-option argument to :command:`cpp`.  :command:`gcc` has a
  different interpretation of a second non-option argument, so you must
  use :option:`-o` to specify the output file.

.. option:: -Wall

  Turns on all optional warnings which are desirable for normal code.
  At present this is :option:`-Wcomment`, :option:`-Wtrigraphs`,
  :option:`-Wmultichar` and a warning about integer promotion causing a
  change of sign in ``#if`` expressions.  Note that many of the
  preprocessor's warnings are on by default and have no options to
  control them.

.. option:: -Wcomment, -Wcomments

  Warn whenever a comment-start sequence /* appears in a /*
  comment, or whenever a backslash-newline appears in a // comment.
  (Both forms have the same effect.)

.. option:: -Wtrigraphs

  WtrigraphsMost trigraphs in comments cannot affect the meaning of the program.
  However, a trigraph that would form an escaped newline (??/ at
  the end of a line) can, by changing where the comment begins or ends.
  Therefore, only trigraphs that would form escaped newlines produce
  warnings inside a comment.

  This option is implied by :option:`-Wall`.  If :option:`-Wall` is not
  given, this option is still enabled unless trigraphs are enabled.  To
  get trigraph conversion without warnings, but get the other
  :option:`-Wall` warnings, use -trigraphs -Wall -Wno-trigraphs.

.. option:: -Wtraditional

  Warn about certain constructs that behave differently in traditional and
  ISO C.  Also warn about ISO C constructs that have no traditional C
  equivalent, and problematic constructs which should be avoided.

.. option:: -Wundef

  Warn whenever an identifier which is not a macro is encountered in an
  #if directive, outside of defined.  Such identifiers are
  replaced with zero.

.. option:: -Wunused-macros

  Warn about macros defined in the main file that are unused.  A macro
  is :dfn:`used` if it is expanded or tested for existence at least once.
  The preprocessor will also warn if the macro has not been used at the
  time it is redefined or undefined.

  Built-in macros, macros defined on the command line, and macros
  defined in include files are not warned about.

  Note: If a macro is actually used, but only used in skipped
  conditional blocks, then CPP will report it as unused.  To avoid the
  warning in such a case, you might improve the scope of the macro's
  definition by, for example, moving it into the first skipped block.
  Alternatively, you could provide a dummy use with something like:

  .. code-block:: c++

    #if defined the_macro_causing_the_warning
    #endif

.. option:: -Wendif-labels

  Warn whenever an #else or an #endif are followed by text.
  This usually happens in code of the form

  .. code-block:: c++

    #if FOO
    ...
    #else FOO
    ...
    #endif FOO

  The second and third ``FOO`` should be in comments, but often are not
  in older programs.  This warning is on by default.

.. option:: -Werror

  Make all warnings into hard errors.  Source code which triggers warnings
  will be rejected.

.. option:: -Wsystem-headers

  Issue warnings for code in system headers.  These are normally unhelpful
  in finding bugs in your own code, therefore suppressed.  If you are
  responsible for the system library, you may want to see them.

.. option:: -w

  Suppress all warnings, including those which GNU CPP issues by default.

.. option:: -pedantic

  Issue all the mandatory diagnostics listed in the C standard.  Some of
  them are left out by default, since they trigger frequently on harmless
  code.

.. option:: -pedantic-errors

  Issue all the mandatory diagnostics, and make all mandatory diagnostics
  into errors.  This includes mandatory diagnostics that GCC issues
  without -pedantic but treats as warnings.

.. option:: -M

  :command:`make`dependencies, :command:`make`Instead of outputting the result of preprocessing, output a rule
  suitable for :command:`make` describing the dependencies of the main
  source file.  The preprocessor outputs one :command:`make` rule containing
  the object file name for that source file, a colon, and the names of all
  the included files, including those coming from :option:`-include` or
  :option:`-imacros` command-line options.

  Unless specified explicitly (with :option:`-MT` or :option:`-MQ`), the
  object file name consists of the name of the source file with any
  suffix replaced with object file suffix and with any leading directory
  parts removed.  If there are many included files then the rule is
  split into several lines using \-newline.  The rule has no
  commands.

  This option does not suppress the preprocessor's debug output, such as
  :option:`-dM`.  To avoid mixing such debug output with the dependency
  rules you should explicitly specify the dependency output file with
  :option:`-MF`, or use an environment variable like
  :envvar:`DEPENDENCIES_OUTPUT` (Environment Variables).  Debug output
  will still be sent to the regular output stream as normal.

  Passing :option:`-M` to the driver implies :option:`-E`, and suppresses
  warnings with an implicit :option:`-w`.

.. option:: -MM

  Like :option:`-M` but do not mention header files that are found in
  system header directories, nor header files that are included,
  directly or indirectly, from such a header.

  This implies that the choice of angle brackets or double quotes in an
  #include directive does not in itself determine whether that
  header will appear in :option:`-MM` dependency output.  This is a
  slight change in semantics from GCC versions 3.0 and earlier.

  dashMF

.. option:: -MF file, -MF

  When used with :option:`-M` or :option:`-MM`, specifies a
  file to write the dependencies to.  If no :option:`-MF` switch is given
  the preprocessor sends the rules to the same place it would have sent
  preprocessed output.

  When used with the driver options :option:`-MD` or :option:`-MMD`,
  :option:`-MF` overrides the default dependency output file.

.. option:: -MG

  In conjunction with an option such as :option:`-M` requesting
  dependency generation, :option:`-MG` assumes missing header files are
  generated files and adds them to the dependency list without raising
  an error.  The dependency filename is taken directly from the
  ``#include`` directive without prepending any path.  :option:`-MG`
  also suppresses preprocessed output, as a missing header file renders
  this useless.

  This feature is used in automatic updating of makefiles.

.. option:: -MP

  This option instructs CPP to add a phony target for each dependency
  other than the main file, causing each to depend on nothing.  These
  dummy rules work around errors :command:`make` gives if you remove header
  files without updating the Makefile to match.

  This is typical output:

  .. code-block:: c++

    test.o: test.c test.h

    test.h:

.. option:: -MT target, -MT

  Change the target of the rule emitted by dependency generation.  By
  default CPP takes the name of the main input file, deletes any
  directory components and any file suffix such as .c, and
  appends the platform's usual object suffix.  The result is the target.

  An :option:`-MT` option will set the target to be exactly the string you
  specify.  If you want multiple targets, you can specify them as a single
  argument to :option:`-MT`, or use multiple :option:`-MT` options.

  For example, -MT '$(objpfx)foo.o' might give

  .. code-block:: c++

    $(objpfx)foo.o: foo.c

.. option:: -MQ target, -MQ

  Same as :option:`-MT`, but it quotes any characters which are special to
  Make.  -MQ '$(objpfx)foo.o' gives

  .. code-block:: c++

    $$(objpfx)foo.o: foo.c

  The default target is automatically quoted, as if it were given with
  :option:`-MQ`.

.. option:: -MD

  :option:`-MD` is equivalent to :option:`-M -MF ``file```, except that
  :option:`-E` is not implied.  The driver determines ``file`` based on
  whether an :option:`-o` option is given.  If it is, the driver uses its
  argument but with a suffix of .d, otherwise it takes the name
  of the input file, removes any directory components and suffix, and
  applies a .d suffix.

  If :option:`-MD` is used in conjunction with :option:`-E`, any
  :option:`-o` switch is understood to specify the dependency output file
  (dashMF-MF), but if used without :option:`-E`, each :option:`-o`
  is understood to specify a target object file.

  Since :option:`-E` is not implied, :option:`-MD` can be used to generate
  a dependency output file as a side-effect of the compilation process.

.. option:: -MMD

  Like :option:`-MD` except mention only user header files, not system
  header files.

.. option:: -fpch-deps

  When using precompiled headers (Precompiled Headers), this flag
  will cause the dependency-output flags to also list the files from the
  precompiled header's dependencies.  If not specified only the
  precompiled header would be listed and not the files that were used to
  create it because those files are not consulted when a precompiled
  header is used.

.. option:: -fpch-preprocess

  This option allows use of a precompiled header (Precompiled
  Headers) together with :option:`-E`.  It inserts a special ``#pragma``,
  ``#pragma GCC pch_preprocess "``filename``"`` in the output to mark
  the place where the precompiled header was found, and its ``filename``.
  When :option:`-fpreprocessed` is in use, GCC recognizes this ``#pragma``
  and loads the PCH.

  This option is off by default, because the resulting preprocessed output
  is only really suitable as input to GCC.  It is switched on by
  :option:`-save-temps`.

  You should not write this ``#pragma`` in your own code, but it is
  safe to edit the filename if the PCH file is available in a different
  location.  The filename may be absolute or it may be relative to GCC's
  current directory.

.. option:: -x c, -x

  Specify the source language: C, C++, Objective-C, or assembly.  This has
  nothing to do with standards conformance or extensions; it merely
  selects which base syntax to expect.  If you give none of these options,
  cpp will deduce the language from the extension of the source file:
  .c, .cc, .m, or .S.  Some other common
  extensions for C++ and assembly are also recognized.  If cpp does not
  recognize the extension, it will treat the file as C; this is the most
  generic mode.

  Note: Previous versions of cpp accepted a :option:`-lang` option
  which selected both the language and the standards conformance level.
  This option has been removed, because it conflicts with the :option:`-l`
  option.

.. option:: -std=standard

  Specify the standard to which the code should conform.  Currently CPP
  knows about C and C++ standards; others may be added in the future.

  ``standard``
  may be one of:

  c90 c89 iso9899:1990
    The ISO C standard from 1990.  c90 is the customary shorthand for
    this version of the standard.

    The :option:`-ansi` option is equivalent to :option:`-std=c90`.

  iso9899:199409
    The 1990 C standard, as amended in 1994.

  iso9899:1999 c99 iso9899:199x c9x
    The revised ISO C standard, published in December 1999.  Before
    publication, this was known as C9X.

  iso9899:2011 c11 c1x
    The revised ISO C standard, published in December 2011.  Before
    publication, this was known as C1X.

  gnu90 gnu89
    The 1990 C standard plus GNU extensions.  This is the default.

  gnu99 gnu9x
    The 1999 C standard plus GNU extensions.

  gnu11 gnu1x
    The 2011 C standard plus GNU extensions.

  c++98
    The 1998 ISO C++ standard plus amendments.

  gnu++98
    The same as :option:`-std=c++98` plus GNU extensions.  This is the
    default for C++ code.

.. option:: -I-

  Split the include path.  Any directories specified with :option:`-I`
  options before :option:`-I-` are searched only for headers requested with
  ``#include "``file``"``; they are not searched for
  ``#include <``file``>``.  If additional directories are
  specified with :option:`-I` options after the :option:`-I-`, those
  directories are searched for all #include directives.

  In addition, :option:`-I-` inhibits the use of the directory of the current
  file directory as the first search directory for ``#include
  "``file``"``.
  This option has been deprecated.

.. option:: -nostdinc

  Do not search the standard system directories for header files.
  Only the directories you have specified with :option:`-I` options
  (and the directory of the current file, if appropriate) are searched.

.. option:: -nostdinc++

  Do not search for header files in the C++-specific standard directories,
  but do still search the other standard directories.  (This option is
  used when building the C++ library.)

.. option:: -include file, -include

  Process ``file`` as if ``#include "file"`` appeared as the first
  line of the primary source file.  However, the first directory searched
  for ``file`` is the preprocessor's working directory instead of
  the directory containing the main source file.  If not found there, it
  is searched for in the remainder of the ``#include "..."`` search
  chain as normal.

  If multiple :option:`-include` options are given, the files are included
  in the order they appear on the command line.

.. option:: -imacros file, -imacros

  Exactly like :option:`-include`, except that any output produced by
  scanning ``file`` is thrown away.  Macros it defines remain defined.
  This allows you to acquire all the macros from a header without also
  processing its declarations.

  All files specified by :option:`-imacros` are processed before all files
  specified by :option:`-include`.

.. option:: -idirafter dir, -idirafter

  Search ``dir`` for header files, but do it after all
  directories specified with :option:`-I` and the standard system directories
  have been exhausted.  ``dir`` is treated as a system include directory.
  If ``dir`` begins with ``=``, then the ``=`` will be replaced
  by the sysroot prefix; see :option:`--sysroot` and :option:`-isysroot`.

.. option:: -iprefix prefix, -iprefix

  Specify ``prefix`` as the prefix for subsequent :option:`-iwithprefix`
  options.  If the prefix represents a directory, you should include the
  final /.

.. option:: -iwithprefix dir, -iwithprefix, -iwithprefixbefore

  Append ``dir`` to the prefix specified previously with
  :option:`-iprefix`, and add the resulting directory to the include search
  path.  :option:`-iwithprefixbefore` puts it in the same place :option:`-I`
  would; :option:`-iwithprefix` puts it where :option:`-idirafter` would.

.. option:: -isysroot dir, -isysroot

  This option is like the :option:`--sysroot` option, but applies only to
  header files (except for Darwin targets, where it applies to both header
  files and libraries).  See the :option:`--sysroot` option for more
  information.

.. option:: -imultilib dir, -imultilib

  Use ``dir`` as a subdirectory of the directory containing
  target-specific C++ headers.

.. option:: -isystem dir, -isystem

  Search ``dir`` for header files, after all directories specified by
  :option:`-I` but before the standard system directories.  Mark it
  as a system directory, so that it gets the same special treatment as
  is applied to the standard system directories.
  If ``dir`` begins with ``=``, then the ``=`` will be replaced
  by the sysroot prefix; see :option:`--sysroot` and :option:`-isysroot`.

.. option:: -iquote dir, -iquote

  Search ``dir`` only for header files requested with
  ``#include "``file``"``; they are not searched for
  ``#include <``file``>``, before all directories specified by
  :option:`-I` and before the standard system directories.
  If ``dir`` begins with ``=``, then the ``=`` will be replaced
  by the sysroot prefix; see :option:`--sysroot` and :option:`-isysroot`.

.. option:: -fdirectives-only

  When preprocessing, handle directives, but do not expand macros.

  The option's behavior depends on the :option:`-E` and :option:`-fpreprocessed`
  options.

  With :option:`-E`, preprocessing is limited to the handling of directives
  such as ``#define``, ``#ifdef``, and ``#error``.  Other
  preprocessor operations, such as macro expansion and trigraph
  conversion are not performed.  In addition, the :option:`-dD` option is
  implicitly enabled.

  With :option:`-fpreprocessed`, predefinition of command line and most
  builtin macros is disabled.  Macros such as ``__LINE__``, which are
  contextually dependent, are handled normally.  This enables compilation of
  files previously preprocessed with ``-E -fdirectives-only``.

  With both :option:`-E` and :option:`-fpreprocessed`, the rules for
  :option:`-fpreprocessed` take precedence.  This enables full preprocessing of
  files previously preprocessed with ``-E -fdirectives-only``.

.. option:: -fdollars-in-identifiers

  fdollars-in-identifiersAccept $ in identifiers.

.. option:: -fextended-identifiers

  Accept universal character names in identifiers.  This option is
  enabled by default for C99 (and later C standard versions) and C++.

.. option:: -fno-canonical-system-headers

  When preprocessing, do not shorten system header paths with canonicalization.

.. option:: -fpreprocessed

  Indicate to the preprocessor that the input file has already been
  preprocessed.  This suppresses things like macro expansion, trigraph
  conversion, escaped newline splicing, and processing of most directives.
  The preprocessor still recognizes and removes comments, so that you can
  pass a file preprocessed with :option:`-C` to the compiler without
  problems.  In this mode the integrated preprocessor is little more than
  a tokenizer for the front ends.

  :option:`-fpreprocessed` is implicit if the input file has one of the
  extensions .i, .ii or .mi.  These are the
  extensions that GCC uses for preprocessed files created by
  :option:`-save-temps`.

.. option:: -ftabstop=width

  Set the distance between tab stops.  This helps the preprocessor report
  correct column numbers in warnings or errors, even if tabs appear on the
  line.  If the value is less than 1 or greater than 100, the option is
  ignored.  The default is 8.

.. option:: -fdebug-cpp

  This option is only useful for debugging GCC.  When used with
  :option:`-E`, dumps debugging information about location maps.  Every
  token in the output is preceded by the dump of the map its location
  belongs to.  The dump of the map holding the location of a token would
  be:

  .. code-block:: c++

    {P:/file/path;F:/includer/path;L:``line_num``;C:``col_num``;S:``system_header_p``;M:``map_address``;E:``macro_expansion_p``,loc:``location``}

  When used without :option:`-E`, this option has no effect.

.. option:: -ftrack-macro-expansion[=level]

  Track locations of tokens across macro expansions. This allows the
  compiler to emit diagnostic about the current macro expansion stack
  when a compilation error occurs in a macro expansion. Using this
  option makes the preprocessor and the compiler consume more
  memory. The ``level`` parameter can be used to choose the level of
  precision of token location tracking thus decreasing the memory
  consumption if necessary. Value 0 of ``level`` de-activates
  this option just as if no :option:`-ftrack-macro-expansion` was present
  on the command line. Value 1 tracks tokens locations in a
  degraded mode for the sake of minimal memory overhead. In this mode
  all tokens resulting from the expansion of an argument of a
  function-like macro have the same location. Value 2 tracks
  tokens locations completely. This value is the most memory hungry.
  When this option is given no argument, the default parameter value is
  2.

  Note that ``-ftrack-macro-expansion=2`` is activated by default.

.. option:: -fexec-charset=charset

  .. index:: character set, execution

  Set the execution character set, used for string and character
  constants.  The default is UTF-8.  ``charset`` can be any encoding
  supported by the system's ``iconv`` library routine.

.. option:: -fwide-exec-charset=charset

  .. index:: character set, wide execution

  Set the wide execution character set, used for wide string and
  character constants.  The default is UTF-32 or UTF-16, whichever
  corresponds to the width of ``wchar_t``.  As with
  :option:`-fexec-charset`, ``charset`` can be any encoding supported
  by the system's ``iconv`` library routine; however, you will have
  problems with encodings that do not fit exactly in ``wchar_t``.

.. option:: -finput-charset=charset

  .. index:: character set, input

  Set the input character set, used for translation from the character
  set of the input file to the source character set used by GCC.  If the
  locale does not specify, or GCC cannot get this information from the
  locale, the default is UTF-8.  This can be overridden by either the locale
  or this command-line option.  Currently the command-line option takes
  precedence if there's a conflict.  ``charset`` can be any encoding
  supported by the system's ``iconv`` library routine.

.. option:: -fworking-directory, -fno-working-directory

  Enable generation of linemarkers in the preprocessor output that will
  let the compiler know the current working directory at the time of
  preprocessing.  When this option is enabled, the preprocessor will
  emit, after the initial linemarker, a second linemarker with the
  current working directory followed by two slashes.  GCC will use this
  directory, when it's present in the preprocessed input, as the
  directory emitted as the current working directory in some debugging
  information formats.  This option is implicitly enabled if debugging
  information is enabled, but this can be inhibited with the negated
  form :option:`-fno-working-directory`.  If the :option:`-P` flag is
  present in the command line, this option has no effect, since no
  ``#line`` directives are emitted whatsoever.

.. option:: -fno-show-column

  Do not print column numbers in diagnostics.  This may be necessary if
  diagnostics are being scanned by a program that does not understand the
  column numbers, such as :command:`dejagnu`.

.. option:: -A predicate=answer

  Make an assertion with the predicate ``predicate`` and answer
  ``answer``.  This form is preferred to the older form :option:`-A
  ``predicate``(``answer``)`, which is still supported, because
  it does not use shell special characters.

-A -``predicate``=``answer``
  Cancel an assertion with the predicate ``predicate`` and answer
  ``answer``.

-dCHARS
  ``CHARS`` is a sequence of one or more of the following characters,
  and must not be preceded by a space.  Other characters are interpreted
  by the compiler proper, or reserved for future versions of GCC, and so
  are silently ignored.  If you specify characters whose behavior
  conflicts, the result is undefined.

  .. option:: M, -dM

    Instead of the normal output, generate a list of #define
    directives for all the macros defined during the execution of the
    preprocessor, including predefined macros.  This gives you a way of
    finding out what is predefined in your version of the preprocessor.
    Assuming you have no file foo.h, the command

    .. code-block:: c++

      touch foo.h; cpp -dM foo.h

    will show all the predefined macros.

    If you use :option:`-dM` without the :option:`-E` option, :option:`-dM` is
    interpreted as a synonym for :option:`-fdump-rtl-mach`.
    See :ref:`debugging-options`.

  .. option:: D, -dD

    Like M except in two respects: it does not include the
    predefined macros, and it outputs both the #define
    directives and the result of preprocessing.  Both kinds of output go to
    the standard output file.

  .. option:: N, -dN

    Like D, but emit only the macro names, not their expansions.

  .. option:: I, -dI

    Output #include directives in addition to the result of
    preprocessing.

  .. option:: U, -dU

    Like D except that only macros that are expanded, or whose
    definedness is tested in preprocessor directives, are output; the
    output is delayed until the use or test of the macro; and
    #undef directives are also output for macros tested but
    undefined at the time.

.. option:: -P

  Inhibit generation of linemarkers in the output from the preprocessor.
  This might be useful when running the preprocessor on something that is
  not C code, and will be sent to a program which might be confused by the
  linemarkers.

.. option:: -C

  Do not discard comments.  All comments are passed through to the output
  file, except for comments in processed directives, which are deleted
  along with the directive.

  You should be prepared for side effects when using :option:`-C`; it
  causes the preprocessor to treat comments as tokens in their own right.
  For example, comments appearing at the start of what would be a
  directive line have the effect of turning that line into an ordinary
  source line, since the first token on the line is no longer a #.

-CC
  Do not discard comments, including during macro expansion.  This is
  like :option:`-C`, except that comments contained within macros are
  also passed through to the output file where the macro is expanded.

  In addition to the side-effects of the :option:`-C` option, the
  :option:`-CC` option causes all C++-style comments inside a macro
  to be converted to C-style comments.  This is to prevent later use
  of that macro from inadvertently commenting out the remainder of
  the source line.

  The :option:`-CC` option is generally used to support lint comments.

.. option:: -traditional-cpp

  Try to imitate the behavior of old-fashioned C preprocessors, as
  opposed to ISO C preprocessors.

.. option:: -trigraphs

  Process trigraph sequences.
  These are three-character sequences, all starting with ??, that
  are defined by ISO C to stand for single characters.  For example,
  ??/ stands for \, so '??/n' is a character
  constant for a newline.  By default, GCC ignores trigraphs, but in
  standard-conforming modes it converts them.  See the :option:`-std` and
  :option:`-ansi` options.

  The nine trigraphs and their replacements are

  .. code-block:: c++

    Trigraph:       ??(  ??)  ??<  ??>  ??=  ??/  ??'  ??!  ??-
    Replacement:      [    ]    {    }    #    \    ^    |    ~

.. option:: -remap

  Enable special code to work around file systems which only permit very
  short file names, such as MS-DOS.

.. option:: --help, -help, -target-help

  Print text describing all the command-line options instead of
  preprocessing anything.

.. option:: -v

  Verbose mode.  Print out GNU CPP's version number at the beginning of
  execution, and report the final form of the include path.

.. option:: -H

  Print the name of each header file used, in addition to other normal
  activities.  Each name is indented to show how deep in the
  #include stack it is.  Precompiled header files are also
  printed, even if they are found to be invalid; an invalid precompiled
  header file is printed with ...x and a valid one with ...! .

.. option:: -version

  Print out GNU CPP's version number.  With one dash, proceed to
  preprocess as normal.  With two dashes, exit immediately.

