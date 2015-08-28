
Options Controlling the Kind of Output
**************************************

Compilation can involve up to four stages: preprocessing, compilation
proper, assembly and linking, always in that order.  GCC is capable of
preprocessing and compiling several files either into several
assembler input files, or into one assembler input file; then each
assembler input file produces an object file, and linking combines all
the object files (those newly compiled, and those specified as input)
into an executable file.

.. index:: file name suffix

For any given input file, the file name suffix determines what kind of
compilation is done:

``file``.c
  C source code that must be preprocessed.

``file``.i
  C source code that should not be preprocessed.

``file``.ii
  C++ source code that should not be preprocessed.

``file``.m
  Objective-C source code.  Note that you must link with the libobjc
  library to make an Objective-C program work.

``file``.mi
  Objective-C source code that should not be preprocessed.

``file``.mm ``file``.M
  Objective-C++ source code.  Note that you must link with the libobjc
  library to make an Objective-C++ program work.  Note that .M refers
  to a literal capital M.

``file``.mii
  Objective-C++ source code that should not be preprocessed.

``file``.h
  C, C++, Objective-C or Objective-C++ header file to be turned into a
  precompiled header (default), or C, C++ header file to be turned into an
  Ada spec (via the :option:`-fdump-ada-spec` switch).

``file``.cc ``file``.cp ``file``.cxx ``file``.cpp ``file``.CPP ``file``.c++ ``file``.C
  C++ source code that must be preprocessed.  Note that in .cxx,
  the last two letters must both be literally x.  Likewise,
  .C refers to a literal capital C.

``file``.mm ``file``.M
  Objective-C++ source code that must be preprocessed.

``file``.mii
  Objective-C++ source code that should not be preprocessed.

``file``.hh ``file``.H ``file``.hp ``file``.hxx ``file``.hpp ``file``.HPP ``file``.h++ ``file``.tcc
  C++ header file to be turned into a precompiled header or Ada spec.

``file``.f ``file``.for ``file``.ftn
  Fixed form Fortran source code that should not be preprocessed.

``file``.F ``file``.FOR ``file``.fpp ``file``.FPP ``file``.FTN
  Fixed form Fortran source code that must be preprocessed (with the traditional
  preprocessor).

``file``.f90 ``file``.f95 ``file``.f03 ``file``.f08
  Free form Fortran source code that should not be preprocessed.

``file``.F90 ``file``.F95 ``file``.F03 ``file``.F08
  Free form Fortran source code that must be preprocessed (with the
  traditional preprocessor).

``file``.go
  Go source code.

  .. FIXME: Descriptions of Java file types.
     @var{file}.java
     @var{file}.class
     @var{file}.zip
     @var{file}.jar

``file``.ads
  Ada source code file that contains a library unit declaration (a
  declaration of a package, subprogram, or generic, or a generic
  instantiation), or a library unit renaming declaration (a package,
  generic, or subprogram renaming declaration).  Such files are also
  called :dfn:`specs`.

``file``.adb
  Ada source code file containing a library unit body (a subprogram or
  package body).  Such files are also called :dfn:`bodies`.

  .. GCC also knows about some suffixes for languages not yet included:
     Pascal:
     @var{file}.p
     @var{file}.pas
     Ratfor:
     @var{file}.r

``file``.s
  Assembler code.

``file``.S ``file``.sx
  Assembler code that must be preprocessed.

``other``
  An object file to be fed straight into linking.
  Any file name with no recognized suffix is treated this way.

.. index:: x

You can specify the input language explicitly with the :option:`-x` option:

-x ``language``
  Specify explicitly the ``language`` for the following input files
  (rather than letting the compiler choose a default based on the file
  name suffix).  This option applies to all following input files until
  the next :option:`-x` option.  Possible values for ``language`` are:

  .. code-block:: c++

    c  c-header  cpp-output
    c++  c++-header  c++-cpp-output
    objective-c  objective-c-header  objective-c-cpp-output
    objective-c++ objective-c++-header objective-c++-cpp-output
    assembler  assembler-with-cpp
    ada
    f77  f77-cpp-input f95  f95-cpp-input
    go
    java

-x none
  Turn off any specification of a language, so that subsequent files are
  handled according to their file name suffixes (as they are if :option:`-x`
  has not been used at all).

.. option:: -pass-exit-codes

  Normally the :command:`gcc` program exits with the code of 1 if any
  phase of the compiler returns a non-success return code.  If you specify
  :option:`-pass-exit-codes`, the :command:`gcc` program instead returns with
  the numerically highest error produced by any phase returning an error
  indication.  The C, C++, and Fortran front ends return 4 if an internal
  compiler error is encountered.

If you only want some of the stages of compilation, you can use
:option:`-x` (or filename suffixes) to tell :command:`gcc` where to start, and
one of the options :option:`-c`, :option:`-S`, or :option:`-E` to say where
:command:`gcc` is to stop.  Note that some combinations (for example,
-x cpp-output -E) instruct :command:`gcc` to do nothing at all.

.. option:: -c

  Compile or assemble the source files, but do not link.  The linking
  stage simply is not done.  The ultimate output is in the form of an
  object file for each source file.

  By default, the object file name for a source file is made by replacing
  the suffix .c, .i, .s, etc., with .o.

  Unrecognized input files, not requiring compilation or assembly, are
  ignored.

.. option:: -S

  Stop after the stage of compilation proper; do not assemble.  The output
  is in the form of an assembler code file for each non-assembler input
  file specified.

  By default, the assembler file name for a source file is made by
  replacing the suffix .c, .i, etc., with .s.

  Input files that don't require compilation are ignored.

.. option:: -E

  Stop after the preprocessing stage; do not run the compiler proper.  The
  output is in the form of preprocessed source code, which is sent to the
  standard output.

  Input files that don't require preprocessing are ignored.

  .. index:: output file option

.. option:: -o file, -o

  Place output in file ``file``.  This applies to whatever
  sort of output is being produced, whether it be an executable file,
  an object file, an assembler file or preprocessed C code.

  If :option:`-o` is not specified, the default is to put an executable
  file in a.out, the object file for
  ``source``.``suffix`` in ``source``.o, its
  assembler file in ``source``.s, a precompiled header file in
  ``source``.``suffix``.gch, and all preprocessed C source on
  standard output.

.. option:: -v

  Print (on standard error output) the commands executed to run the stages
  of compilation.  Also print the version number of the compiler driver
  program and of the preprocessor and the compiler proper.

.. option:: -###

  Like :option:`-v` except the commands are not executed and arguments
  are quoted unless they contain only alphanumeric characters or ``./-_``.
  This is useful for shell scripts to capture the driver-generated command lines.

.. option:: -pipe

  Use pipes rather than temporary files for communication between the
  various stages of compilation.  This fails to work on some systems where
  the assembler is unable to read from a pipe; but the GNU assembler has
  no trouble.

.. option:: --help, -help

  Print (on the standard output) a description of the command-line options
  understood by :command:`gcc`.  If the :option:`-v` option is also specified
  then :option:`--help` is also passed on to the various processes
  invoked by :command:`gcc`, so that they can display the command-line options
  they accept.  If the :option:`-Wextra` option has also been specified
  (prior to the :option:`--help` option), then command-line options that
  have no documentation associated with them are also displayed.

.. option:: --target-help, -target-help

  Print (on the standard output) a description of target-specific command-line
  options for each tool.  For some targets extra target-specific
  information may also be printed.

--help={``class``|[^]``qualifier``}[,...]
  Print (on the standard output) a description of the command-line
  options understood by the compiler that fit into all specified classes
  and qualifiers.  These are the supported classes:

  optimizers
    Display all of the optimization options supported by the
    compiler.

  warnings
    Display all of the options controlling warning messages
    produced by the compiler.

  target
    Display target-specific options.  Unlike the
    :option:`--target-help` option however, target-specific options of the
    linker and assembler are not displayed.  This is because those
    tools do not currently support the extended :option:`--help=` syntax.

  params
    Display the values recognized by the :option:`--param`
    option.

  ``language``
    Display the options supported for ``language``, where
    ``language`` is the name of one of the languages supported in this
    version of GCC.

  common
    Display the options that are common to all languages.

    These are the supported qualifiers:

  undocumented
    Display only those options that are undocumented.

  joined
    Display options taking an argument that appears after an equal
    sign in the same continuous piece of text, such as:
    --help=target.

  separate
    Display options taking an argument that appears as a separate word
    following the original option, such as: -o output-file.

    Thus for example to display all the undocumented target-specific
  switches supported by the compiler, use:

  :option:`--help=target,undocumented`
  The sense of a qualifier can be inverted by prefixing it with the
  ^ character, so for example to display all binary warning
  options (i.e., ones that are either on or off and that do not take an
  argument) that have a description, use:

  :option:`--help=warnings,^joined,^undocumented`
  The argument to :option:`--help=` should not consist solely of inverted
  qualifiers.

  Combining several classes is possible, although this usually
  restricts the output so much that there is nothing to display.  One
  case where it does work, however, is when one of the classes is
  ``target``.  For example, to display all the target-specific
  optimization options, use:

  :option:`--help=target,optimizers`
  The :option:`--help=` option can be repeated on the command line.  Each
  successive use displays its requested class of options, skipping
  those that have already been displayed.

  If the :option:`-Q` option appears on the command line before the
  :option:`--help=` option, then the descriptive text displayed by
  :option:`--help=` is changed.  Instead of describing the displayed
  options, an indication is given as to whether the option is enabled,
  disabled or set to a specific value (assuming that the compiler
  knows this at the point where the :option:`--help=` option is used).

  Here is a truncated example from the ARM port of :command:`gcc`:

  .. code-block:: c++

      % gcc -Q -mabi=2 --help=target -c
      The following options are target specific:
      -mabi=                                2
      -mabort-on-noreturn                   [disabled]
      -mapcs                                [disabled]

  The output is sensitive to the effects of previous command-line
  options, so for example it is possible to find out which optimizations
  are enabled at :option:`-O2` by using:

  :option:`-Q` :option:`-O2` :option:`--help=optimizers`
  Alternatively you can discover which binary optimizations are enabled
  by :option:`-O3` by using:

  .. code-block:: bash

    gcc -c -Q -O3 --help=optimizers > /tmp/O3-opts
    gcc -c -Q -O2 --help=optimizers > /tmp/O2-opts
    diff /tmp/O2-opts /tmp/O3-opts | grep enabled

.. option:: -no-canonical-prefixes

  Do not expand any symbolic links, resolve references to /../
  or /./, or make the path absolute when generating a relative
  prefix.

.. option:: --version, -version

  Display the version number and copyrights of the invoked GCC.

.. option:: -wrapper

  Invoke all subcommands under a wrapper program.  The name of the
  wrapper program and its parameters are passed as a comma separated
  list.

  .. code-block:: bash

    gcc -c t.c -wrapper gdb,--args

  This invokes all subprograms of :command:`gcc` under
  gdb --args, thus the invocation of :command:`cc1` is
  gdb --args cc1 ....

.. option:: -fplugin=name.so

  Load the plugin code in file ``name``.so, assumed to be a
  shared object to be dlopen'd by the compiler.  The base name of
  the shared object file is used to identify the plugin for the
  purposes of argument parsing (See
  :option:`-fplugin-arg-``name``-``key``=``value``` below).
  Each plugin should define the callback functions specified in the
  Plugins API.

.. option:: -fplugin-arg-name-key=value

  Define an argument called ``key`` with a value of ``value``
  for the plugin called ``name``.

.. option:: -fdump-ada-spec[-slim], -fdump-ada-spec

  For C and C++ source and include files, generate corresponding Ada specs.
  See :ref:`generating-ada-bindings-for-c-and-c++-headers`, which provides detailed documentation on this feature.

.. option:: -fada-spec-parent=unit

  In conjunction with :option:`-fdump-ada-spec[-slim]` above, generate
  Ada specs as child units of parent ``unit``.

.. option:: -fdump-go-spec=file

  For input files in any language, generate corresponding Go
  declarations in ``file``.  This generates Go ``const``,
  ``type``, ``var``, and ``func`` declarations which may be a
  useful way to start writing a Go interface to code written in some
  other language.

  .. This file is designed to be included in manuals that use
     expandargv.

@``file``
  Read command-line options from ``file``.  The options read are
  inserted in place of the original @``file`` option.  If ``file``
  does not exist, or cannot be read, then the option will be treated
  literally, and not removed.  

  Options in ``file`` are separated by whitespace.  A whitespace
  character may be included in an option by surrounding the entire
  option in either single or double quotes.  Any character (including a
  backslash) may be included by prefixing the character to be included
  with a backslash.  The ``file`` may itself contain additional
  @``file`` options; any such options will be processed recursively.

