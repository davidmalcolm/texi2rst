.. _code-gen-options:

Options for Code Generation Conventions
***************************************

.. index:: code generation conventions

.. index:: options, code generation

.. index:: run-time options

These machine-independent options control the interface conventions
used in code generation.

Most of them have both positive and negative forms; the negative form
of :option:`-ffoo` is :option:`-fno-foo`.  In the table below, only
one of the forms is listed-the one that is not the default.  You
can figure out the other form by either removing no- or adding
it.

.. option:: -fbounds-check

  For front ends that support it, generate additional code to check that
  indices used to access arrays are within the declared range.  This is
  currently only supported by the Java and Fortran front ends, where
  this option defaults to true and false respectively.

.. option:: -fstack-reuse=reuse-level

  This option controls stack space reuse for user declared local/auto variables
  and compiler generated temporaries.  ``reuse_level`` can be all,
  named_vars, or none. all enables stack reuse for all
  local variables and temporaries, named_vars enables the reuse only for
  user defined local variables with names, and none disables stack reuse
  completely. The default value is all. The option is needed when the
  program extends the lifetime of a scoped local variable or a compiler generated
  temporary beyond the end point defined by the language.  When a lifetime of
  a variable ends, and if the variable lives in memory, the optimizing compiler
  has the freedom to reuse its stack space with other temporaries or scoped
  local variables whose live range does not overlap with it. Legacy code extending
  local lifetime is likely to break with the stack reuse optimization.

  For example,

  .. code-block:: c++

       int *p;
       {
         int local1;

         p = &local1;
         local1 = 10;
         ....
       }
       {
          int local2;
          local2 = 20;
          ...
       }

       if (*p == 10)  // out of scope use of local1
         {

         }

  Another example:

  .. code-block:: c++

       struct A
       {
           A(int k) : i(k), j(k) { }
           int i;
           int j;
       };

       A *ap;

       void foo(const A& ar)
       {
          ap = &ar;
       }

       void bar()
       {
          foo(A(10)); // temp object's lifetime ends when foo returns

          {
            A a(20);
            ....
          }
          ap->i+= 10;  // ap references out of scope temp whose space
                       // is reused with a. What is the value of ap->i?
       }

  The lifetime of a compiler generated temporary is well defined by the C++
  standard. When a lifetime of a temporary ends, and if the temporary lives
  in memory, the optimizing compiler has the freedom to reuse its stack
  space with other temporaries or scoped local variables whose live range
  does not overlap with it. However some of the legacy code relies on
  the behavior of older compilers in which temporaries' stack space is
  not reused, the aggressive stack reuse can lead to runtime errors. This
  option is used to control the temporary stack reuse optimization.

.. option:: -ftrapv

  This option generates traps for signed overflow on addition, subtraction,
  multiplication operations.

.. option:: -fwrapv

  This option instructs the compiler to assume that signed arithmetic
  overflow of addition, subtraction and multiplication wraps around
  using twos-complement representation.  This flag enables some optimizations
  and disables others.  This option is enabled by default for the Java
  front end, as required by the Java language specification.

.. option:: -fexceptions

  Enable exception handling.  Generates extra code needed to propagate
  exceptions.  For some targets, this implies GCC generates frame
  unwind information for all functions, which can produce significant data
  size overhead, although it does not affect execution.  If you do not
  specify this option, GCC enables it by default for languages like
  C++ that normally require exception handling, and disables it for
  languages like C that do not normally require it.  However, you may need
  to enable this option when compiling C code that needs to interoperate
  properly with exception handlers written in C++.  You may also wish to
  disable this option if you are compiling older C++ programs that don't
  use exception handling.

.. option:: -fnon-call-exceptions

  Generate code that allows trapping instructions to throw exceptions.
  Note that this requires platform-specific runtime support that does
  not exist everywhere.  Moreover, it only allows trapping
  instructions to throw exceptions, i.e. memory references or floating-point
  instructions.  It does not allow exceptions to be thrown from
  arbitrary signal handlers such as ``SIGALRM``.

.. option:: -fdelete-dead-exceptions

  Consider that instructions that may throw exceptions but don't otherwise
  contribute to the execution of the program can be optimized away.
  This option is enabled by default for the Ada front end, as permitted by
  the Ada language specification.
  Optimization passes that cause dead exceptions to be removed are enabled independently at different optimization levels.

.. option:: -funwind-tables

  Similar to :option:`-fexceptions`, except that it just generates any needed
  static data, but does not affect the generated code in any other way.
  You normally do not need to enable this option; instead, a language processor
  that needs this handling enables it on your behalf.

.. option:: -fasynchronous-unwind-tables

  Generate unwind table in DWARF 2 format, if supported by target machine.  The
  table is exact at each instruction boundary, so it can be used for stack
  unwinding from asynchronous events (such as debugger or garbage collector).

.. option:: -fno-gnu-unique

  On systems with recent GNU assembler and C library, the C++ compiler
  uses the ``STB_GNU_UNIQUE`` binding to make sure that definitions
  of template static data members and static local variables in inline
  functions are unique even in the presence of ``RTLD_LOCAL``; this
  is necessary to avoid problems with a library used by two different
  ``RTLD_LOCAL`` plugins depending on a definition in one of them and
  therefore disagreeing with the other one about the binding of the
  symbol.  But this causes ``dlclose`` to be ignored for affected
  DSOs; if your program relies on reinitialization of a DSO via
  ``dlclose`` and ``dlopen``, you can use
  :option:`-fno-gnu-unique`.

.. option:: -fpcc-struct-return

  Return 'short' ``struct`` and ``union`` values in memory like
  longer ones, rather than in registers.  This convention is less
  efficient, but it has the advantage of allowing intercallability between
  GCC-compiled files and files compiled with other compilers, particularly
  the Portable C Compiler (pcc).

  The precise convention for returning structures in memory depends
  on the target configuration macros.

  Short structures and unions are those whose size and alignment match
  that of some integer type.

  Warning: code compiled with the :option:`-fpcc-struct-return`
  switch is not binary compatible with code compiled with the
  :option:`-freg-struct-return` switch.
  Use it to conform to a non-default application binary interface.

.. option:: -freg-struct-return

  Return ``struct`` and ``union`` values in registers when possible.
  This is more efficient for small structures than
  :option:`-fpcc-struct-return`.

  If you specify neither :option:`-fpcc-struct-return` nor
  :option:`-freg-struct-return`, GCC defaults to whichever convention is
  standard for the target.  If there is no standard convention, GCC
  defaults to :option:`-fpcc-struct-return`, except on targets where GCC is
  the principal compiler.  In those cases, we can choose the standard, and
  we chose the more efficient register return alternative.

  Warning: code compiled with the :option:`-freg-struct-return`
  switch is not binary compatible with code compiled with the
  :option:`-fpcc-struct-return` switch.
  Use it to conform to a non-default application binary interface.

.. option:: -fshort-enums

  Allocate to an ``enum`` type only as many bytes as it needs for the
  declared range of possible values.  Specifically, the ``enum`` type
  is equivalent to the smallest integer type that has enough room.

  Warning: the :option:`-fshort-enums` switch causes GCC to generate
  code that is not binary compatible with code generated without that switch.
  Use it to conform to a non-default application binary interface.

.. option:: -fshort-double

  Use the same size for ``double`` as for ``float``.

  Warning: the :option:`-fshort-double` switch causes GCC to generate
  code that is not binary compatible with code generated without that switch.
  Use it to conform to a non-default application binary interface.

.. option:: -fshort-wchar

  Override the underlying type for ``wchar_t`` to be ``short
  unsigned int`` instead of the default for the target.  This option is
  useful for building programs to run under WINE.

  Warning: the :option:`-fshort-wchar` switch causes GCC to generate
  code that is not binary compatible with code generated without that switch.
  Use it to conform to a non-default application binary interface.

.. option:: -fno-common

  In C code, controls the placement of uninitialized global variables.
  Unix C compilers have traditionally permitted multiple definitions of
  such variables in different compilation units by placing the variables
  in a common block.
  This is the behavior specified by :option:`-fcommon`, and is the default
  for GCC on most targets.
  On the other hand, this behavior is not required by ISO C, and on some
  targets may carry a speed or code size penalty on variable references.
  The :option:`-fno-common` option specifies that the compiler should place
  uninitialized global variables in the data section of the object file,
  rather than generating them as common blocks.
  This has the effect that if the same variable is declared
  (without ``extern``) in two different compilations,
  you get a multiple-definition error when you link them.
  In this case, you must compile with :option:`-fcommon` instead.
  Compiling with :option:`-fno-common` is useful on targets for which
  it provides better performance, or if you wish to verify that the
  program will work on other systems that always treat uninitialized
  variable declarations this way.

.. option:: -fno-ident

  Ignore the ``#ident`` directive.

.. option:: -finhibit-size-directive

  Don't output a ``.size`` assembler directive, or anything else that
  would cause trouble if the function is split in the middle, and the
  two halves are placed at locations far apart in memory.  This option is
  used when compiling crtstuff.c; you should not need to use it
  for anything else.

.. option:: -fverbose-asm

  Put extra commentary information in the generated assembly code to
  make it more readable.  This option is generally only of use to those
  who actually need to read the generated assembly code (perhaps while
  debugging the compiler itself).

  :option:`-fno-verbose-asm`, the default, causes the
  extra information to be omitted and is useful when comparing two assembler
  files.

.. option:: -frecord-gcc-switches

  This switch causes the command line used to invoke the
  compiler to be recorded into the object file that is being created.
  This switch is only implemented on some targets and the exact format
  of the recording is target and binary file format dependent, but it
  usually takes the form of a section containing ASCII text.  This
  switch is related to the :option:`-fverbose-asm` switch, but that
  switch only records information in the assembler output file as
  comments, so it never reaches the object file.
  See also :option:`-grecord-gcc-switches` for another
  way of storing compiler options into the object file.

.. option:: -fpic

  .. index:: global offset table

  .. index:: PIC

  Generate position-independent code (PIC) suitable for use in a shared
  library, if supported for the target machine.  Such code accesses all
  constant addresses through a global offset table (GOT).  The dynamic
  loader resolves the GOT entries when the program starts (the dynamic
  loader is not part of GCC; it is part of the operating system).  If
  the GOT size for the linked executable exceeds a machine-specific
  maximum size, you get an error message from the linker indicating that
  :option:`-fpic` does not work; in that case, recompile with :option:`-fPIC`
  instead.  (These maximums are 8k on the SPARC and 32k
  on the m68k and RS/6000.  The x86 has no such limit.)

  Position-independent code requires special support, and therefore works
  only on certain machines.  For the x86, GCC supports PIC for System V
  but not for the Sun 386i.  Code generated for the IBM RS/6000 is always
  position-independent.

  When this flag is set, the macros ``__pic__`` and ``__PIC__``
  are defined to 1.

.. option:: -fPIC

  If supported for the target machine, emit position-independent code,
  suitable for dynamic linking and avoiding any limit on the size of the
  global offset table.  This option makes a difference on the m68k,
  PowerPC and SPARC.

  Position-independent code requires special support, and therefore works
  only on certain machines.

  When this flag is set, the macros ``__pic__`` and ``__PIC__``
  are defined to 2.

.. option:: -fpie, -fPIE

  These options are similar to :option:`-fpic` and :option:`-fPIC`, but
  generated position independent code can be only linked into executables.
  Usually these options are used when :option:`-pie` GCC option is
  used during linking.

  :option:`-fpie` and :option:`-fPIE` both define the macros
  ``__pie__`` and ``__PIE__``.  The macros have the value 1
  for :option:`-fpie` and 2 for :option:`-fPIE`.

.. option:: -fno-plt

  Do not use PLT for external function calls in position-independent code.
  Instead, load callee address at call site from GOT and branch to it.
  This leads to more efficient code by eliminating PLT stubs and exposing
  GOT load to optimizations.  On architectures such as 32-bit x86 where
  PLT stubs expect GOT pointer in a specific register, this gives more
  register allocation freedom to the compiler.  Lazy binding requires PLT:
  with :option:`-fno-plt` all external symbols are resolved at load time.

.. option:: -fno-jump-tables

  Do not use jump tables for switch statements even where it would be
  more efficient than other code generation strategies.  This option is
  of use in conjunction with :option:`-fpic` or :option:`-fPIC` for
  building code that forms part of a dynamic linker and cannot
  reference the address of a jump table.  On some targets, jump tables
  do not require a GOT and this option is not needed.

.. option:: -ffixed-reg, -ffixed

  Treat the register named ``reg`` as a fixed register; generated code
  should never refer to it (except perhaps as a stack pointer, frame
  pointer or in some other fixed role).

  ``reg`` must be the name of a register.  The register names accepted
  are machine-specific and are defined in the ``REGISTER_NAMES``
  macro in the machine description macro file.

  This flag does not have a negative form, because it specifies a
  three-way choice.

.. option:: -fcall-used-reg, -fcall-used

  Treat the register named ``reg`` as an allocable register that is
  clobbered by function calls.  It may be allocated for temporaries or
  variables that do not live across a call.  Functions compiled this way
  do not save and restore the register ``reg``.

  It is an error to use this flag with the frame pointer or stack pointer.
  Use of this flag for other registers that have fixed pervasive roles in
  the machine's execution model produces disastrous results.

  This flag does not have a negative form, because it specifies a
  three-way choice.

.. option:: -fcall-saved-reg, -fcall-saved

  Treat the register named ``reg`` as an allocable register saved by
  functions.  It may be allocated even for temporaries or variables that
  live across a call.  Functions compiled this way save and restore
  the register ``reg`` if they use it.

  It is an error to use this flag with the frame pointer or stack pointer.
  Use of this flag for other registers that have fixed pervasive roles in
  the machine's execution model produces disastrous results.

  A different sort of disaster results from the use of this flag for
  a register in which function values may be returned.

  This flag does not have a negative form, because it specifies a
  three-way choice.

.. option:: -fpack-struct[=n]

  Without a value specified, pack all structure members together without
  holes.  When a value is specified (which must be a small power of two), pack
  structure members according to this value, representing the maximum
  alignment (that is, objects with default alignment requirements larger than
  this are output potentially unaligned at the next fitting location.

  Warning: the :option:`-fpack-struct` switch causes GCC to generate
  code that is not binary compatible with code generated without that switch.
  Additionally, it makes the code suboptimal.
  Use it to conform to a non-default application binary interface.

.. option:: -finstrument-functions

  Generate instrumentation calls for entry and exit to functions.  Just
  after function entry and just before function exit, the following
  profiling functions are called with the address of the current
  function and its call site.  (On some platforms,
  ``__builtin_return_address`` does not work beyond the current
  function, so the call site information may not be available to the
  profiling functions otherwise.)

  .. code-block:: c++

    void __cyg_profile_func_enter (void *this_fn,
                                   void *call_site);
    void __cyg_profile_func_exit  (void *this_fn,
                                   void *call_site);

  The first argument is the address of the start of the current function,
  which may be looked up exactly in the symbol table.

  This instrumentation is also done for functions expanded inline in other
  functions.  The profiling calls indicate where, conceptually, the
  inline function is entered and exited.  This means that addressable
  versions of such functions must be available.  If all your uses of a
  function are expanded inline, this may mean an additional expansion of
  code size.  If you use ``extern inline`` in your C code, an
  addressable version of such functions must be provided.  (This is
  normally the case anyway, but if you get lucky and the optimizer always
  expands the functions inline, you might have gotten away without
  providing static copies.)

  A function may be given the attribute ``no_instrument_function``, in
  which case this instrumentation is not done.  This can be used, for
  example, for the profiling functions listed above, high-priority
  interrupt routines, and any functions from which the profiling functions
  cannot safely be called (perhaps signal handlers, if the profiling
  routines generate output or allocate memory).

.. option:: -finstrument-functions-exclude-file-list=file,file,...

  Set the list of functions that are excluded from instrumentation (see
  the description of :option:`-finstrument-functions`).  If the file that
  contains a function definition matches with one of ``file``, then
  that function is not instrumented.  The match is done on substrings:
  if the ``file`` parameter is a substring of the file name, it is
  considered to be a match.

  For example:

  :option:`-finstrument-functions-exclude-file-list=/bits/stl,include/sys`
  excludes any inline function defined in files whose pathnames
  contain /bits/stl or include/sys.

  If, for some reason, you want to include letter , in one of
  ``sym``, write \,. For example,
  :option:`-finstrument-functions-exclude-file-list='\,\,tmp'`
  (note the single quote surrounding the option).

.. option:: -finstrument-functions-exclude-function-list=sym,sym,...

  This is similar to :option:`-finstrument-functions-exclude-file-list`,
  but this option sets the list of function names to be excluded from
  instrumentation.  The function name to be matched is its user-visible
  name, such as ``vector<int> blah(const vector<int> &)``, not the
  internal mangled name (e.g., ``_Z4blahRSt6vectorIiSaIiEE``).  The
  match is done on substrings: if the ``sym`` parameter is a substring
  of the function name, it is considered to be a match.  For C99 and C++
  extended identifiers, the function name must be given in UTF-8, not
  using universal character names.

.. option:: -fstack-check

  Generate code to verify that you do not go beyond the boundary of the
  stack.  You should specify this flag if you are running in an
  environment with multiple threads, but you only rarely need to specify it in
  a single-threaded environment since stack overflow is automatically
  detected on nearly all systems if there is only one stack.

  Note that this switch does not actually cause checking to be done; the
  operating system or the language runtime must do that.  The switch causes
  generation of code to ensure that they see the stack being extended.

  You can additionally specify a string parameter: no means no
  checking, generic means force the use of old-style checking,
  specific means use the best checking method and is equivalent
  to bare :option:`-fstack-check`.

  Old-style checking is a generic mechanism that requires no specific
  target support in the compiler but comes with the following drawbacks:

  * Modified allocation strategy for large objects: they are always
    allocated dynamically if their size exceeds a fixed threshold.

  * Fixed limit on the size of the static frame of functions: when it is
    topped by a particular function, stack checking is not reliable and
    a warning is issued by the compiler.

  * Inefficiency: because of both the modified allocation strategy and the
    generic implementation, code performance is hampered.

  Note that old-style stack checking is also the fallback method for
  specific if no target support has been added in the compiler.

.. option:: -fstack-limit-register=reg

  Generate code to ensure that the stack does not grow beyond a certain value,
  either the value of a register or the address of a symbol.  If a larger
  stack is required, a signal is raised at run time.  For most targets,
  the signal is raised before the stack overruns the boundary, so
  it is possible to catch the signal without taking special precautions.

  For instance, if the stack starts at absolute address 0x80000000
  and grows downwards, you can use the flags
  :option:`-fstack-limit-symbol=__stack_limit` and
  :option:`-Wl,--defsym,__stack_limit=0x7ffe0000` to enforce a stack limit
  of 128KB.  Note that this may only work with the GNU linker.

.. option:: -fsplit-stack

  Generate code to automatically split the stack before it overflows.
  The resulting program has a discontiguous stack which can only
  overflow if the program is unable to allocate any more memory.  This
  is most useful when running threaded programs, as it is no longer
  necessary to calculate a good stack size to use for each thread.  This
  is currently only implemented for the x86 targets running
  GNU/Linux.

  When code compiled with :option:`-fsplit-stack` calls code compiled
  without :option:`-fsplit-stack`, there may not be much stack space
  available for the latter code to run.  If compiling all code,
  including library code, with :option:`-fsplit-stack` is not an option,
  then the linker can fix up these calls so that the code compiled
  without :option:`-fsplit-stack` always has a large stack.  Support for
  this is implemented in the gold linker in GNU binutils release 2.21
  and later.

.. option:: -fleading-underscore

  This option and its counterpart, :option:`-fno-leading-underscore`, forcibly
  change the way C symbols are represented in the object file.  One use
  is to help link with legacy assembly code.

  Warning: the :option:`-fleading-underscore` switch causes GCC to
  generate code that is not binary compatible with code generated without that
  switch.  Use it to conform to a non-default application binary interface.
  Not all targets provide complete support for this switch.

.. option:: -ftls-model=model

  Alter the thread-local storage model to be used (Thread-Local).
  The ``model`` argument should be one of global-dynamic,
  local-dynamic, initial-exec or local-exec.
  Note that the choice is subject to optimization: the compiler may use
  a more efficient model for symbols not visible outside of the translation
  unit, or if :option:`-fpic` is not given on the command line.

  The default without :option:`-fpic` is initial-exec; with
  :option:`-fpic` the default is global-dynamic.

.. option:: -fvisibility=[default|internal|hidden|protected]

  Set the default ELF image symbol visibility to the specified option-all
  symbols are marked with this unless overridden within the code.
  Using this feature can very substantially improve linking and
  load times of shared object libraries, produce more optimized
  code, provide near-perfect API export and prevent symbol clashes.
  It is strongly recommended that you use this in any shared objects
  you distribute.

  Despite the nomenclature, default always means public; i.e.,
  available to be linked against from outside the shared object.
  protected and internal are pretty useless in real-world
  usage so the only other commonly used option is hidden.
  The default if :option:`-fvisibility` isn't specified is
  default, i.e., make every symbol public.

  A good explanation of the benefits offered by ensuring ELF
  symbols have the correct visibility is given by 'How To Write
  Shared Libraries' by Ulrich Drepper (which can be found at
  http://www.akkadia.org/drepper/)-however a superior
  solution made possible by this option to marking things hidden when
  the default is public is to make the default hidden and mark things
  public.  This is the norm with DLLs on Windows and with :option:`-fvisibility=hidden`
  and ``__attribute__ ((visibility("default")))`` instead of
  ``__declspec(dllexport)`` you get almost identical semantics with
  identical syntax.  This is a great boon to those working with
  cross-platform projects.

  For those adding visibility support to existing code, you may find
  ``#pragma GCC visibility`` of use.  This works by you enclosing
  the declarations you wish to set visibility for with (for example)
  ``#pragma GCC visibility push(hidden)`` and
  ``#pragma GCC visibility pop``.
  Bear in mind that symbol visibility should be viewed as
  part of the API interface contract and thus all new code should
  always specify visibility when it is not the default; i.e., declarations
  only for use within the local DSO should always be marked explicitly
  as hidden as so to avoid PLT indirection overheads-making this
  abundantly clear also aids readability and self-documentation of the code.
  Note that due to ISO C++ specification requirements, ``operator new`` and
  ``operator delete`` must always be of default visibility.

  Be aware that headers from outside your project, in particular system
  headers and headers from any other library you use, may not be
  expecting to be compiled with visibility other than the default.  You
  may need to explicitly say ``#pragma GCC visibility push(default)``
  before including any such headers.

  ``extern`` declarations are not affected by :option:`-fvisibility`, so
  a lot of code can be recompiled with :option:`-fvisibility=hidden` with
  no modifications.  However, this means that calls to ``extern``
  functions with no explicit visibility use the PLT, so it is more
  effective to use ``__attribute ((visibility))`` and/or
  ``#pragma GCC visibility`` to tell the compiler which ``extern``
  declarations should be treated as hidden.

  Note that :option:`-fvisibility` does affect C++ vague linkage
  entities. This means that, for instance, an exception class that is
  be thrown between DSOs must be explicitly marked with default
  visibility so that the type_info nodes are unified between
  the DSOs.

  An overview of these techniques, their benefits and how to use them
  is at http://gcc.gnu.org//wiki//Visibility.

.. option:: -fstrict-volatile-bitfields

  This option should be used if accesses to volatile bit-fields (or other
  structure fields, although the compiler usually honors those types
  anyway) should use a single access of the width of the
  field's type, aligned to a natural alignment if possible.  For
  example, targets with memory-mapped peripheral registers might require
  all such accesses to be 16 bits wide; with this flag you can
  declare all peripheral bit-fields as ``unsigned short`` (assuming short
  is 16 bits on these targets) to force GCC to use 16-bit accesses
  instead of, perhaps, a more efficient 32-bit access.

  If this option is disabled, the compiler uses the most efficient
  instruction.  In the previous example, that might be a 32-bit load
  instruction, even though that accesses bytes that do not contain
  any portion of the bit-field, or memory-mapped registers unrelated to
  the one being updated.

  In some cases, such as when the ``packed`` attribute is applied to a 
  structure field, it may not be possible to access the field with a single
  read or write that is correctly aligned for the target machine.  In this
  case GCC falls back to generating multiple accesses rather than code that 
  will fault or truncate the result at run time.

  Note:  Due to restrictions of the C/C++11 memory model, write accesses are
  not allowed to touch non bit-field members.  It is therefore recommended
  to define all bits of the field's type as bit-field members.

  The default value of this option is determined by the application binary
  interface for the target processor.

.. option:: -fsync-libcalls

  This option controls whether any out-of-line instance of the ``__sync``
  family of functions may be used to implement the C++11 ``__atomic``
  family of functions.

  The default value of this option is enabled, thus the only useful form
  of the option is :option:`-fno-sync-libcalls`.  This option is used in
  the implementation of the libatomic runtime library.

.. man end

