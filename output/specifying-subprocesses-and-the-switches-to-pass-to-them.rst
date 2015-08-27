
Specifying Subprocesses and the Switches to Pass to Them
********************************************************

.. index:: Spec Files

:command:`gcc` is a driver program.  It performs its job by invoking a
sequence of other programs to do the work of compiling, assembling and
linking.  GCC interprets its command-line parameters and uses these to
deduce which programs it should invoke, and which command-line options
it ought to place on their command lines.  This behavior is controlled
by :dfn:`spec strings`.  In most cases there is one spec string for each
program that GCC can invoke, but a few programs have multiple spec
strings to control their behavior.  The spec strings built into GCC can
be overridden by using the :option:`-specs=` command-line switch to specify
a spec file.

:dfn:`Spec files` are plaintext files that are used to construct spec
strings.  They consist of a sequence of directives separated by blank
lines.  The type of directive is determined by the first non-whitespace
character on the line, which can be one of the following:

%``command``
  Issues a ``command`` to the spec file processor.  The commands that can
  appear here are:

  %include <``file``>
    ``%include``Search for ``file`` and insert its text at the current point in the
    specs file.

  %include_noerr <``file``>
    ``%include_noerr``Just like %include, but do not generate an error message if the include
    file cannot be found.

  %rename ``old_name````new_name``
    ``%rename``Rename the spec string ``old_name`` to ``new_name``.

*[``spec_name``]:
  This tells the compiler to create, override or delete the named spec
  string.  All lines after this directive up to the next directive or
  blank line are considered to be the text for the spec string.  If this
  results in an empty string then the spec is deleted.  (Or, if the
  spec did not exist, then nothing happens.)  Otherwise, if the spec
  does not currently exist a new spec is created.  If the spec does
  exist then its contents are overridden by the text of this
  directive, unless the first character of that text is the +
  character, in which case the text is appended to the spec.

[``suffix``]:
  Creates a new [``suffix``] spec pair.  All lines after this directive
  and up to the next directive or blank line are considered to make up the
  spec string for the indicated suffix.  When the compiler encounters an
  input file with the named suffix, it processes the spec string in
  order to work out how to compile that file.  For example:

  .. code-block:: c++

    .ZZ:
    z-compile -input %i

  This says that any input file whose name ends in .ZZ should be
  passed to the program z-compile, which should be invoked with the
  command-line switch :option:`-input` and with the result of performing the
  %i substitution.  (See below.)

  As an alternative to providing a spec string, the text following a
  suffix directive can be one of the following:

  @``language``
    This says that the suffix is an alias for a known ``language``.  This is
    similar to using the :option:`-x` command-line switch to GCC to specify a
    language explicitly.  For example:

    .. code-block:: c++

      .ZZ:
      @c++

    Says that .ZZ files are, in fact, C++ source files.

  #``name``
    This causes an error messages saying:

    .. code-block:: c++

      ``name`` compiler not installed on this system.

    GCC already has an extensive list of suffixes built into it.
  This directive adds an entry to the end of the list of suffixes, but
  since the list is searched from the end backwards, it is effectively
  possible to override earlier entries using this technique.

  GCC has the following spec strings built into it.  Spec files can
override these strings or create their own.  Note that individual
targets can also add their own spec strings to this list.

.. code-block:: c++

  asm          Options to pass to the assembler
  asm_final    Options to pass to the assembler post-processor
  cpp          Options to pass to the C preprocessor
  cc1          Options to pass to the C compiler
  cc1plus      Options to pass to the C++ compiler
  endfile      Object files to include at the end of the link
  link         Options to pass to the linker
  lib          Libraries to include on the command line to the linker
  libgcc       Decides which GCC support library to pass to the linker
  linker       Sets the name of the linker
  predefines   Defines to be passed to the C preprocessor
  signed_char  Defines to pass to CPP to say whether ``char`` is signed
               by default
  startfile    Object files to include at the start of the link

Here is a small example of a spec file:

.. code-block:: c++

  %rename lib                 old_lib

  *lib:
  --start-group -lgcc -lc -leval1 --end-group %(old_lib)

This example renames the spec called lib to old_lib and
then overrides the previous definition of lib with a new one.
The new definition adds in some extra command-line options before
including the text of the old definition.

:dfn:`Spec strings` are a list of command-line options to be passed to their
corresponding program.  In addition, the spec strings can contain
%-prefixed sequences to substitute variable text or to
conditionally insert text into the command line.  Using these constructs
it is possible to generate quite complex command lines.

Here is a table of all defined %-sequences for spec
strings.  Note that spaces are not generated automatically around the
results of expanding these sequences.  Therefore you can concatenate them
together or combine them with constant text in a single argument.

%%
  Substitute one % into the program name or argument.

%i
  Substitute the name of the input file being processed.

%b
  Substitute the basename of the input file being processed.
  This is the substring up to (and not including) the last period
  and not including the directory.

%B
  This is the same as %b, but include the file suffix (text after
  the last period).

%d
  Marks the argument containing or following the %d as a
  temporary file name, so that that file is deleted if GCC exits
  successfully.  Unlike %g, this contributes no text to the
  argument.

%g``suffix``
  Substitute a file name that has suffix ``suffix`` and is chosen
  once per compilation, and mark the argument in the same way as
  %d.  To reduce exposure to denial-of-service attacks, the file
  name is now chosen in a way that is hard to predict even when previously
  chosen file names are known.  For example, %g.s ... %g.o ... %g.s
  might turn into ccUVUUAU.s ccXYAXZ12.o ccUVUUAU.s.  ``suffix`` matches
  the regexp [.A-Za-z]* or the special string %O, which is
  treated exactly as if %O had been preprocessed.  Previously, %g
  was simply substituted with a file name chosen once per compilation,
  without regard to any appended suffix (which was therefore treated
  just like ordinary text), making such attacks more likely to succeed.

%u``suffix``
  Like %g, but generates a new temporary file name
  each time it appears instead of once per compilation.

%U``suffix``
  Substitutes the last file name generated with %u``suffix``, generating a
  new one if there is no such last file name.  In the absence of any
  %u``suffix``, this is just like %g``suffix``, except they don't share
  the same suffix space, so %g.s ... %U.s ... %g.s ... %U.s
  involves the generation of two distinct file names, one
  for each %g.s and another for each %U.s.  Previously, %U was
  simply substituted with a file name chosen for the previous %u,
  without regard to any appended suffix.

%j``suffix``
  Substitutes the name of the ``HOST_BIT_BUCKET``, if any, and if it is
  writable, and if :option:`-save-temps` is not used; 
  otherwise, substitute the name
  of a temporary file, just like %u.  This temporary file is not
  meant for communication between processes, but rather as a junk
  disposal mechanism.

%|``suffix`` %m``suffix``
  Like %g, except if :option:`-pipe` is in effect.  In that case
  %| substitutes a single dash and %m substitutes nothing at
  all.  These are the two most common ways to instruct a program that it
  should read from standard input or write to standard output.  If you
  need something more elaborate you can use an %{pipe:``X``}
  construct: see for example f/lang-specs.h.

%.``SUFFIX``
  Substitutes ``.SUFFIX`` for the suffixes of a matched switch's args
  when it is subsequently output with %*.  ``SUFFIX`` is
  terminated by the next space or %.

%w
  Marks the argument containing or following the %w as the
  designated output file of this compilation.  This puts the argument
  into the sequence of arguments that %o substitutes.

%o
  Substitutes the names of all the output files, with spaces
  automatically placed around them.  You should write spaces
  around the %o as well or the results are undefined.
  %o is for use in the specs for running the linker.
  Input files whose names have no recognized suffix are not compiled
  at all, but they are included among the output files, so they are
  linked.

%O
  Substitutes the suffix for object files.  Note that this is
  handled specially when it immediately follows %g, %u, or %U,
  because of the need for those to form complete file names.  The
  handling is such that %O is treated exactly as if it had already
  been substituted, except that %g, %u, and %U do not currently
  support additional ``suffix`` characters following %O as they do
  following, for example, .o.

%p
  Substitutes the standard macro predefinitions for the
  current target machine.  Use this when running :command:`cpp`.

%P
  Like %p, but puts __ before and after the name of each
  predefined macro, except for macros that start with __ or with
  _``L``, where ``L`` is an uppercase letter.  This is for ISO
  C.

%I
  Substitute any of :option:`-iprefix` (made from :envvar:`GCC_EXEC_PREFIX`),
  :option:`-isysroot` (made from :envvar:`TARGET_SYSTEM_ROOT`),
  :option:`-isystem` (made from :envvar:`COMPILER_PATH` and :option:`-B` options)
  and :option:`-imultilib` as necessary.

%s
  Current argument is the name of a library or startup file of some sort.
  Search for that file in a standard list of directories and substitute
  the full name found.  The current working directory is included in the
  list of directories scanned.

%T
  Current argument is the name of a linker script.  Search for that file
  in the current list of directories to scan for libraries. If the file
  is located insert a :option:`--script` option into the command line
  followed by the full path name found.  If the file is not found then
  generate an error message.  Note: the current working directory is not
  searched.

%e``str``
  Print ``str`` as an error message.  ``str`` is terminated by a newline.
  Use this when inconsistent options are detected.

%(``name``)
  Substitute the contents of spec string ``name`` at this point.

%x{``option``}
  Accumulate an option for %X.

%X
  Output the accumulated linker options specified by :option:`-Wl` or a %x
  spec string.

%Y
  Output the accumulated assembler options specified by :option:`-Wa`.

%Z
  Output the accumulated preprocessor options specified by :option:`-Wp`.

%a
  Process the ``asm`` spec.  This is used to compute the
  switches to be passed to the assembler.

%A
  Process the ``asm_final`` spec.  This is a spec string for
  passing switches to an assembler post-processor, if such a program is
  needed.

%l
  Process the ``link`` spec.  This is the spec for computing the
  command line passed to the linker.  Typically it makes use of the
  %L %G %S %D and %E sequences.

%D
  Dump out a :option:`-L` option for each directory that GCC believes might
  contain startup files.  If the target supports multilibs then the
  current multilib directory is prepended to each of these paths.

%L
  Process the ``lib`` spec.  This is a spec string for deciding which
  libraries are included on the command line to the linker.

%G
  Process the ``libgcc`` spec.  This is a spec string for deciding
  which GCC support library is included on the command line to the linker.

%S
  Process the ``startfile`` spec.  This is a spec for deciding which
  object files are the first ones passed to the linker.  Typically
  this might be a file named crt0.o.

%E
  Process the ``endfile`` spec.  This is a spec string that specifies
  the last object files that are passed to the linker.

%C
  Process the ``cpp`` spec.  This is used to construct the arguments
  to be passed to the C preprocessor.

%1
  Process the ``cc1`` spec.  This is used to construct the options to be
  passed to the actual C compiler (:command:`cc1`).

%2
  Process the ``cc1plus`` spec.  This is used to construct the options to be
  passed to the actual C++ compiler (:command:`cc1plus`).

%*
  Substitute the variable part of a matched option.  See below.
  Note that each comma in the substituted string is replaced by
  a single space.

%<``S``
  Remove all occurrences of ``-S`` from the command line.  Note-this
  command is position dependent.  % commands in the spec string
  before this one see ``-S``, % commands in the spec string
  after this one do not.

%:``function``(``args``)
  Call the named function ``function``, passing it ``args``.
  ``args`` is first processed as a nested spec string, then split
  into an argument vector in the usual fashion.  The function returns
  a string which is processed as if it had appeared literally as part
  of the current spec.

  The following built-in spec functions are provided:

  ``getenv``
    The ``getenv`` spec function takes two arguments: an environment
    variable name and a string.  If the environment variable is not
    defined, a fatal error is issued.  Otherwise, the return value is the
    value of the environment variable concatenated with the string.  For
    example, if :envvar:`TOPDIR` is defined as /path/to/top, then:

    .. code-block:: c++

      %:getenv(TOPDIR /include)

    expands to /path/to/top/include.

  ``if-exists``
    The ``if-exists`` spec function takes one argument, an absolute
    pathname to a file.  If the file exists, ``if-exists`` returns the
    pathname.  Here is a small example of its usage:

    .. code-block:: c++

      *startfile:
      crt0%O%s %:if-exists(crti%O%s) crtbegin%O%s

  ``if-exists-else``
    The ``if-exists-else`` spec function is similar to the ``if-exists``
    spec function, except that it takes two arguments.  The first argument is
    an absolute pathname to a file.  If the file exists, ``if-exists-else``
    returns the pathname.  If it does not exist, it returns the second argument.
    This way, ``if-exists-else`` can be used to select one file or another,
    based on the existence of the first.  Here is a small example of its usage:

    .. code-block:: c++

      *startfile:
      crt0%O%s %:if-exists(crti%O%s) \
      %:if-exists-else(crtbeginT%O%s crtbegin%O%s)

  ``replace-outfile``
    The ``replace-outfile`` spec function takes two arguments.  It looks for the
    first argument in the outfiles array and replaces it with the second argument.  Here
    is a small example of its usage:

    .. code-block:: c++

      %{fgnu-runtime:%:replace-outfile(-lobjc -lobjc-gnu)}

  ``remove-outfile``
    The ``remove-outfile`` spec function takes one argument.  It looks for the
    first argument in the outfiles array and removes it.  Here is a small example
    its usage:

    .. code-block:: c++

      %:remove-outfile(-lm)

  ``pass-through-libs``
    The ``pass-through-libs`` spec function takes any number of arguments.  It
    finds any :option:`-l` options and any non-options ending in .a (which it
    assumes are the names of linker input library archive files) and returns a
    result containing all the found arguments each prepended by
    :option:`-plugin-opt=-pass-through=` and joined by spaces.  This list is
    intended to be passed to the LTO linker plugin.

    .. code-block:: c++

      %:pass-through-libs(%G %L %G)

  ``print-asm-header``
    The ``print-asm-header`` function takes no arguments and simply
    prints a banner like:

    .. code-block:: c++

      Assembler options
      =================

      Use "-Wa,OPTION" to pass "OPTION" to the assembler.

    It is used to separate compiler options from assembler options
    in the :option:`--target-help` output.

%{``S``}
  Substitutes the ``-S`` switch, if that switch is given to GCC.
  If that switch is not specified, this substitutes nothing.  Note that
  the leading dash is omitted when specifying this option, and it is
  automatically inserted if the substitution is performed.  Thus the spec
  string %{foo} matches the command-line option :option:`-foo`
  and outputs the command-line option :option:`-foo`.

%W{``S``}
  Like %{``S``} but mark last argument supplied within as a file to be
  deleted on failure.

%{``S``*}
  Substitutes all the switches specified to GCC whose names start
  with ``-S``, but which also take an argument.  This is used for
  switches like :option:`-o`, :option:`-D`, :option:`-I`, etc.
  GCC considers :option:`-o foo` as being
  one switch whose name starts with o.  %{o*} substitutes this
  text, including the space.  Thus two arguments are generated.

%{``S``*&``T``*}
  Like %{``S``*}, but preserve order of ``S`` and ``T`` options
  (the order of ``S`` and ``T`` in the spec is not significant).
  There can be any number of ampersand-separated variables; for each the
  wild card is optional.  Useful for CPP as %{D*&U*&A*}.

%{``S``:``X``}
  Substitutes ``X``, if the :option:`-S` switch is given to GCC.

%{!``S``:``X``}
  Substitutes ``X``, if the :option:`-S` switch is not given to GCC.

%{``S``*:``X``}
  Substitutes ``X`` if one or more switches whose names start with
  ``-S`` are specified to GCC.  Normally ``X`` is substituted only
  once, no matter how many such switches appeared.  However, if ``%*``
  appears somewhere in ``X``, then ``X`` is substituted once
  for each matching switch, with the ``%*`` replaced by the part of
  that switch matching the ``*``.

  If ``%*`` appears as the last part of a spec sequence then a space
  is added after the end of the last substitution.  If there is more
  text in the sequence, however, then a space is not generated.  This
  allows the ``%*`` substitution to be used as part of a larger
  string.  For example, a spec string like this:

  .. code-block:: c++

    %{mcu=*:--script=%*/memory.ld}

  when matching an option like :option:`-mcu=newchip` produces:

  :option:`--script=newchip/memory.ld`

%{.``S``:``X``}
  Substitutes ``X``, if processing a file with suffix ``S``.

%{!.``S``:``X``}
  Substitutes ``X``, if not processing a file with suffix ``S``.

%{,``S``:``X``}
  Substitutes ``X``, if processing a file for language ``S``.

%{!,``S``:``X``}
  Substitutes ``X``, if not processing a file for language ``S``.

%{``S``|``P``:``X``}
  Substitutes ``X`` if either ``-S`` or ``-P`` is given to
  GCC.  This may be combined with !, ., ,, and
  ``*`` sequences as well, although they have a stronger binding than
  the |.  If ``%*`` appears in ``X``, all of the
  alternatives must be starred, and only the first matching alternative
  is substituted.

  For example, a spec string like this:

  .. code-block:: c++

    %{.c:-foo} %{!.c:-bar} %{.c|d:-baz} %{!.c|d:-boggle}

  outputs the following command-line options from the following input
  command-line options:

  .. code-block:: c++

    fred.c        -foo -baz
    jim.d         -bar -boggle
    -d fred.c     -foo -baz -boggle
    -d jim.d      -bar -baz -boggle

%{S:X; T:Y; :D}
  If ``S`` is given to GCC, substitutes ``X``; else if ``T`` is
  given to GCC, substitutes ``Y``; else substitutes ``D``.  There can
  be as many clauses as you need.  This may be combined with ``.``,
  ``,``, ``!``, ``|``, and ``*`` as needed.

  The conditional text ``X`` in a %{``S``:``X``} or similar
construct may contain other nested % constructs or spaces, or
even newlines.  They are processed as usual, as described above.
Trailing white space in ``X`` is ignored.  White space may also
appear anywhere on the left side of the colon in these constructs,
except between ``.`` or ``*`` and the corresponding word.

The :option:`-O`, :option:`-f`, :option:`-m`, and :option:`-W` switches are
handled specifically in these constructs.  If another value of
:option:`-O` or the negated form of a :option:`-f`, :option:`-m`, or
:option:`-W` switch is found later in the command line, the earlier
switch value is ignored, except with {``S``*} where ``S`` is
just one letter, which passes all matching options.

The character | at the beginning of the predicate text is used to
indicate that a command should be piped to the following command, but
only if :option:`-pipe` is specified.

It is built into GCC which switches take arguments and which do not.
(You might think it would be useful to generalize this to allow each
compiler's spec to say which switches take arguments.  But this cannot
be done in a consistent fashion.  GCC cannot even decide which input
files have been specified without knowing which switches take arguments,
and it must know which input files to compile in order to tell which
compilers to run).

GCC also knows implicitly that arguments starting in :option:`-l` are to be
treated as compiler output files, and passed to the linker in their
proper position among the other output files.

.. man begin OPTIONS

