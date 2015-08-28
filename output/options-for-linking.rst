.. _link-options:

Options for Linking
*******************

.. index:: link options

.. index:: options, linking

These options come into play when the compiler links object files into
an executable output file.  They are meaningless if the compiler is
not doing a link step.

.. index:: file names

``object-file-name``
  A file name that does not end in a special recognized suffix is
  considered to name an object file or library.  (Object files are
  distinguished from libraries by the linker according to the file
  contents.)  If linking is done, these object files are used as input
  to the linker.

.. option:: -c, -S, -E

  If any of these options is used, then the linker is not run, and
  object file names should not be used as arguments.  See :ref:`overall-options`.

.. option:: -fuse-ld=bfd

  Use the :command:`bfd` linker instead of the default linker.

.. option:: -fuse-ld=gold

  Use the :command:`gold` linker instead of the default linker.

  .. index:: Libraries

.. option:: -llibrary, -l

  Search the library named ``library`` when linking.  (The second
  alternative with the library as a separate argument is only for
  POSIX compliance and is not recommended.)

  It makes a difference where in the command you write this option; the
  linker searches and processes libraries and object files in the order they
  are specified.  Thus, foo.o -lz bar.o searches library z
  after file foo.o but before bar.o.  If bar.o refers
  to functions in z, those functions may not be loaded.

  The linker searches a standard list of directories for the library,
  which is actually a file named lib``library``.a.  The linker
  then uses this file as if it had been specified precisely by name.

  The directories searched include several standard system directories
  plus any that you specify with :option:`-L`.

  Normally the files found this way are library files-archive files
  whose members are object files.  The linker handles an archive file by
  scanning through it for members which define symbols that have so far
  been referenced but not defined.  But if the file that is found is an
  ordinary object file, it is linked in the usual fashion.  The only
  difference between using an :option:`-l` option and specifying a file name
  is that :option:`-l` surrounds ``library`` with lib and .a
  and searches several directories.

.. option:: -lobjc

  You need this special case of the :option:`-l` option in order to
  link an Objective-C or Objective-C++ program.

.. option:: -nostartfiles

  Do not use the standard system startup files when linking.
  The standard system libraries are used normally, unless :option:`-nostdlib`
  or :option:`-nodefaultlibs` is used.

.. option:: -nodefaultlibs

  Do not use the standard system libraries when linking.
  Only the libraries you specify are passed to the linker, and options
  specifying linkage of the system libraries, such as :option:`-static-libgcc`
  or :option:`-shared-libgcc`, are ignored.  
  The standard startup files are used normally, unless :option:`-nostartfiles`
  is used.  

  The compiler may generate calls to ``memcmp``,
  ``memset``, ``memcpy`` and ``memmove``.
  These entries are usually resolved by entries in
  libc.  These entry points should be supplied through some other
  mechanism when this option is specified.

.. option:: -nostdlib

  Do not use the standard system startup files or libraries when linking.
  No startup files and only the libraries you specify are passed to
  the linker, and options specifying linkage of the system libraries, such as
  :option:`-static-libgcc` or :option:`-shared-libgcc`, are ignored.

  The compiler may generate calls to ``memcmp``, ``memset``,
  ``memcpy`` and ``memmove``.
  These entries are usually resolved by entries in
  libc.  These entry points should be supplied through some other
  mechanism when this option is specified.

  :option:`-lgcc`, use with :option:`-nostdlib`:option:`-nostdlib` and unresolved referencesunresolved references and :option:`-nostdlib`:option:`-lgcc`, use with :option:`-nodefaultlibs`:option:`-nodefaultlibs` and unresolved referencesunresolved references and :option:`-nodefaultlibs`One of the standard libraries bypassed by :option:`-nostdlib` and
  :option:`-nodefaultlibs` is libgcc.a, a library of internal subroutines
  which GCC uses to overcome shortcomings of particular machines, or special
  needs for some languages.
  (See :ref:`Interfacing to GCC Output <interface>`,
  for more discussion of libgcc.a.)
  In most cases, you need libgcc.a even when you want to avoid
  other standard libraries.  In other words, when you specify :option:`-nostdlib`
  or :option:`-nodefaultlibs` you should usually specify :option:`-lgcc` as well.
  This ensures that you have no unresolved references to internal GCC
  library subroutines.
  (An example of such an internal subroutine is ``__main``, used to ensure C++
  constructors are called; Collect2``collect2``gccintGNU Compiler Collection (GCC) Internals.)

.. option:: -pie

  Produce a position independent executable on targets that support it.
  For predictable results, you must also specify the same set of options
  used for compilation (:option:`-fpie`, :option:`-fPIE`,
  or model suboptions) when you specify this linker option.

.. option:: -rdynamic

  Pass the flag :option:`-export-dynamic` to the ELF linker, on targets
  that support it. This instructs the linker to add all symbols, not
  only used ones, to the dynamic symbol table. This option is needed
  for some uses of ``dlopen`` or to allow obtaining backtraces
  from within a program.

.. option:: -s

  Remove all symbol table and relocation information from the executable.

.. option:: -static

  On systems that support dynamic linking, this prevents linking with the shared
  libraries.  On other systems, this option has no effect.

.. option:: -shared

  Produce a shared object which can then be linked with other objects to
  form an executable.  Not all systems support this option.  For predictable
  results, you must also specify the same set of options used for compilation
  (:option:`-fpic`, :option:`-fPIC`, or model suboptions) when
  you specify this linker option.On some systems, gcc -shared
  needs to build supplementary stub code for constructors to work.  On
  multi-libbed systems, gcc -shared must select the correct support
  libraries to link against.  Failing to supply the correct flags may lead
  to subtle defects.  Supplying them in cases where they are not necessary
  is innocuous.

.. option:: -shared-libgcc, -static-libgcc

  On systems that provide libgcc as a shared library, these options
  force the use of either the shared or static version, respectively.
  If no shared version of libgcc was built when the compiler was
  configured, these options have no effect.

  There are several situations in which an application should use the
  shared libgcc instead of the static version.  The most common
  of these is when the application wishes to throw and catch exceptions
  across different shared libraries.  In that case, each of the libraries
  as well as the application itself should use the shared libgcc.

  Therefore, the G++ and GCJ drivers automatically add
  :option:`-shared-libgcc` whenever you build a shared library or a main
  executable, because C++ and Java programs typically use exceptions, so
  this is the right thing to do.

  If, instead, you use the GCC driver to create shared libraries, you may
  find that they are not always linked with the shared libgcc.
  If GCC finds, at its configuration time, that you have a non-GNU linker
  or a GNU linker that does not support option :option:`--eh-frame-hdr`,
  it links the shared version of libgcc into shared libraries
  by default.  Otherwise, it takes advantage of the linker and optimizes
  away the linking with the shared version of libgcc, linking with
  the static version of libgcc by default.  This allows exceptions to
  propagate through such shared libraries, without incurring relocation
  costs at library load time.

  However, if a library or main executable is supposed to throw or catch
  exceptions, you must link it using the G++ or GCJ driver, as appropriate
  for the languages used in the program, or using the option
  :option:`-shared-libgcc`, such that it is linked with the shared
  libgcc.

.. option:: -static-libasan

  When the :option:`-fsanitize=address` option is used to link a program,
  the GCC driver automatically links against libasan.  If
  libasan is available as a shared library, and the :option:`-static`
  option is not used, then this links against the shared version of
  libasan.  The :option:`-static-libasan` option directs the GCC
  driver to link libasan statically, without necessarily linking
  other libraries statically.

.. option:: -static-libtsan

  When the :option:`-fsanitize=thread` option is used to link a program,
  the GCC driver automatically links against libtsan.  If
  libtsan is available as a shared library, and the :option:`-static`
  option is not used, then this links against the shared version of
  libtsan.  The :option:`-static-libtsan` option directs the GCC
  driver to link libtsan statically, without necessarily linking
  other libraries statically.

.. option:: -static-liblsan

  When the :option:`-fsanitize=leak` option is used to link a program,
  the GCC driver automatically links against liblsan.  If
  liblsan is available as a shared library, and the :option:`-static`
  option is not used, then this links against the shared version of
  liblsan.  The :option:`-static-liblsan` option directs the GCC
  driver to link liblsan statically, without necessarily linking
  other libraries statically.

.. option:: -static-libubsan

  When the :option:`-fsanitize=undefined` option is used to link a program,
  the GCC driver automatically links against libubsan.  If
  libubsan is available as a shared library, and the :option:`-static`
  option is not used, then this links against the shared version of
  libubsan.  The :option:`-static-libubsan` option directs the GCC
  driver to link libubsan statically, without necessarily linking
  other libraries statically.

.. option:: -static-libmpx

  When the :option:`-fcheck-pointer bounds` and :option:`-mmpx` options are
  used to link a program, the GCC driver automatically links against
  libmpx.  If libmpx is available as a shared library,
  and the :option:`-static` option is not used, then this links against
  the shared version of libmpx.  The :option:`-static-libmpx`
  option directs the GCC driver to link libmpx statically,
  without necessarily linking other libraries statically.

.. option:: -static-libmpxwrappers

  When the :option:`-fcheck-pointer bounds` and :option:`-mmpx` options are used
  to link a program without also using :option:`-fno-chkp-use-wrappers`, the
  GCC driver automatically links against libmpxwrappers.  If
  libmpxwrappers is available as a shared library, and the
  :option:`-static` option is not used, then this links against the shared
  version of libmpxwrappers.  The :option:`-static-libmpxwrappers`
  option directs the GCC driver to link libmpxwrappers statically,
  without necessarily linking other libraries statically.

.. option:: -static-libstdc++

  When the :command:`g++` program is used to link a C++ program, it
  normally automatically links against libstdc++.  If
  libstdc++ is available as a shared library, and the
  :option:`-static` option is not used, then this links against the
  shared version of libstdc++.  That is normally fine.  However, it
  is sometimes useful to freeze the version of libstdc++ used by
  the program without going all the way to a fully static link.  The
  :option:`-static-libstdc++` option directs the :command:`g++` driver to
  link libstdc++ statically, without necessarily linking other
  libraries statically.

.. option:: -symbolic

  Bind references to global symbols when building a shared object.  Warn
  about any unresolved references (unless overridden by the link editor
  option :option:`-Xlinker -z -Xlinker defs`).  Only a few systems support
  this option.

.. option:: -T script, -T

  .. index:: linker script

  Use ``script`` as the linker script.  This option is supported by most
  systems using the GNU linker.  On some targets, such as bare-board
  targets without an operating system, the :option:`-T` option may be required
  when linking to avoid references to undefined symbols.

.. option:: -Xlinker option, -Xlinker

  Pass ``option`` as an option to the linker.  You can use this to
  supply system-specific linker options that GCC does not recognize.

  If you want to pass an option that takes a separate argument, you must use
  :option:`-Xlinker` twice, once for the option and once for the argument.
  For example, to pass :option:`-assert definitions`, you must write
  :option:`-Xlinker -assert -Xlinker definitions`.  It does not work to write
  :option:`-Xlinker "-assert definitions"`, because this passes the entire
  string as a single argument, which is not what the linker expects.

  When using the GNU linker, it is usually more convenient to pass
  arguments to linker options using the ``option``=``value``
  syntax than as separate arguments.  For example, you can specify
  :option:`-Xlinker -Map=output.map` rather than
  :option:`-Xlinker -Map -Xlinker output.map`.  Other linkers may not support
  this syntax for command-line options.

.. option:: -Wl,option, -Wl

  Pass ``option`` as an option to the linker.  If ``option`` contains
  commas, it is split into multiple options at the commas.  You can use this
  syntax to pass an argument to the option.
  For example, :option:`-Wl,-Map,output.map` passes :option:`-Map output.map` to the
  linker.  When using the GNU linker, you can also get the same effect with
  :option:`-Wl,-Map=output.map`.

.. option:: -u symbol, -u

  Pretend the symbol ``symbol`` is undefined, to force linking of
  library modules to define it.  You can use :option:`-u` multiple times with
  different symbols to force loading of additional library modules.

.. option:: -z keyword, -z

  :option:`-z` is passed directly on to the linker along with the keyword
  ``keyword``. See the section in the documentation of your linker for
  permitted values and their meanings.

