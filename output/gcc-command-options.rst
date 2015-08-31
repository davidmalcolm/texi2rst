.. _invoking-gcc:

GCC Command Options
-------------------

.. index:: GCC command options

.. index:: command options

.. index:: options, GCC command

.. man begin DESCRIPTION

When you invoke GCC, it normally does preprocessing, compilation,
assembly and linking.  The 'overall options' allow you to stop this
process at an intermediate stage.  For example, the :option:`-c` option
says not to run the linker.  Then the output consists of object files
output by the assembler.

Other options are passed on to one stage of processing.  Some options
control the preprocessor and others the compiler itself.  Yet other
options control the assembler and linker; most of these are not
documented here, since you rarely need to use any of them.

.. index:: C compilation options

Most of the command-line options that you can use with GCC are useful
for C programs; when an option is only useful with another language
(usually C++), the explanation says so explicitly.  If the description
for a particular option does not mention a source language, you can use
that option with all supported languages.

.. index:: C++ compilation options

See :ref:`Compiling C++ Programs <invoking-g++>`, for a summary of special
options for compiling C++ programs.

.. index:: grouping options

.. index:: options, grouping

The :command:`gcc` program accepts options and file names as operands.  Many
options have multi-letter names; therefore multiple single-letter options
may *not* be grouped: :option:`-dv` is very different from :samp:`-d
-v`.

.. index:: order of options

.. index:: options, order

You can mix options and other arguments.  For the most part, the order
you use doesn't matter.  Order does matter when you use several
options of the same kind; for example, if you specify :option:`-L` more
than once, the directories are searched in the order specified.  Also,
the placement of the :option:`-l` option is significant.

Many options have long names starting with :samp:`-f` or with
:samp:`-W`-for example,
:option:`-fmove-loop-invariants`, :option:`-Wformat` and so on.  Most of
these have both positive and negative forms; the negative form of
:samp:`-ffoo` is :samp:`-fno-foo`.  This manual documents
only one of these two forms, whichever one is not the default.

.. man end

See :ref:`option-index`, for an index to GCC's options.

.. toctree::

  Brief list of all options, without explanations. <option-summary>
  Controlling the kind of output:
                          an executable, object files, assembler files,
                          or preprocessed source. <overall-options>
  Compiling C++ programs. <invoking-g++>
  Controlling the variant of C language compiled. <c-dialect-options>
  Variations on C++. <c++-dialect-options>
  Variations on Objective-C
                          and Objective-C++. <objective-c-and-objective-c++-dialect-options>
  Controlling how diagnostics should be
                          formatted. <language-independent-options>
  How picky should the compiler be? <warning-options>
  Symbol tables, measurements, and debugging dumps. <debugging-options>
  How much optimization? <optimize-options>
  Controlling header files and macro definitions.
                           Also, getting dependency information for Make. <preprocessor-options>
  Passing options to the assembler. <assembler-options>
  Specifying libraries and so on. <link-options>
  Where to find header files and libraries.
                          Where to find the compiler executable files. <directory-options>
  How to pass switches to sub-processes. <spec-files>
  Running a cross-compiler, or an old version of GCC. <target-options>
  Specifying minor hardware or convention variations,
                          such as 68010 vs 68020. <submodel-options>
  Specifying conventions for function calls, data layout
                          and register usage. <code-gen-options>
  Env vars that affect GCC. <environment-variables>
  Compiling a header once, and using it many times. <precompiled-headers>

.. man begin OPTIONS

.. toctree::

  option-summary
  options-controlling-the-kind-of-output
  compiling-c++-programs
  options-controlling-c-dialect
  options-controlling-c++-dialect
  options-controlling-objective-c-and-objective-c++-dialects
  options-to-control-diagnostic-messages-formatting
  options-to-request-or-suppress-warnings
  options-for-debugging-your-program-or-gcc
  options-that-control-optimization
  options-controlling-the-preprocessor
  passing-options-to-the-assembler
  options-for-linking
  options-for-directory-search
  specifying-subprocesses-and-the-switches-to-pass-to-them
  specifying-target-machine-and-compiler-version
  hardware-models-and-configurations
  options-for-code-generation-conventions
  environment-variables-affecting-gcc
  using-precompiled-headers

