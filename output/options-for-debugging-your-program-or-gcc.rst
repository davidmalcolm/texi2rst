  .. _debugging-options:

Options for Debugging Your Program or GCC
*****************************************

.. index:: options, debugging

.. index:: debugging information options

GCC has various special options that are used for debugging
either your program or GCC:

.. option:: -g

  Produce debugging information in the operating system's native format
  (stabs, COFF, XCOFF, or DWARF 2).  GDB can work with this debugging
  information.

  On most systems that use stabs format, :option:`-g` enables use of extra
  debugging information that only GDB can use; this extra information
  makes debugging work better in GDB but probably makes other debuggers
  crash or
  refuse to read the program.  If you want to control for certain whether
  to generate the extra information, use :option:`-gstabs+`, :option:`-gstabs`,
  :option:`-gxcoff+`, :option:`-gxcoff`, or :option:`-gvms` (see below).

  GCC allows you to use :option:`-g` with
  :option:`-O`.  The shortcuts taken by optimized code may occasionally
  produce surprising results: some variables you declared may not exist
  at all; flow of control may briefly move where you did not expect it;
  some statements may not be executed because they compute constant
  results or their values are already at hand; some statements may
  execute in different places because they have been moved out of loops.

  Nevertheless it proves possible to debug optimized output.  This makes
  it reasonable to use the optimizer for programs that might have bugs.

  The following options are useful when GCC is generated with the
  capability for more than one debugging format.

.. option:: -gsplit-dwarf

  Separate as much dwarf debugging information as possible into a
  separate output file with the extension .dwo.  This option allows
  the build system to avoid linking files with debug information.  To
  be useful, this option requires a debugger capable of reading .dwo
  files.

.. option:: -ggdb

  Produce debugging information for use by GDB.  This means to use the
  most expressive format available (DWARF 2, stabs, or the native format
  if neither of those are supported), including GDB extensions if at all
  possible.

.. option:: -gpubnames

  Generate dwarf .debug_pubnames and .debug_pubtypes sections.

.. option:: -ggnu-pubnames

  Generate .debug_pubnames and .debug_pubtypes sections in a format
  suitable for conversion into a GDBindex.  This option is only useful
  with a linker that can produce GDBindex version 7.

.. option:: -gstabs

  Produce debugging information in stabs format (if that is supported),
  without GDB extensions.  This is the format used by DBX on most BSD
  systems.  On MIPS, Alpha and System V Release 4 systems this option
  produces stabs debugging output that is not understood by DBX or SDB.
  On System V Release 4 systems this option requires the GNU assembler.

.. option:: -feliminate-unused-debug-symbols

  Produce debugging information in stabs format (if that is supported),
  for only symbols that are actually used.

.. option:: -femit-class-debug-always

  Instead of emitting debugging information for a C++ class in only one
  object file, emit it in all object files using the class.  This option
  should be used only with debuggers that are unable to handle the way GCC
  normally emits debugging information for classes because using this
  option increases the size of debugging information by as much as a
  factor of two.

.. option:: -fdebug-types-section, -fno-debug-types-section

  When using DWARF Version 4 or higher, type DIEs can be put into
  their own ``.debug_types`` section instead of making them part of the
  ``.debug_info`` section.  It is more efficient to put them in a separate
  comdat sections since the linker can then remove duplicates.
  But not all DWARF consumers support ``.debug_types`` sections yet
  and on some objects ``.debug_types`` produces larger instead of smaller
  debugging information.

.. option:: -gstabs+

  Produce debugging information in stabs format (if that is supported),
  using GNU extensions understood only by the GNU debugger (GDB).  The
  use of these extensions is likely to make other debuggers crash or
  refuse to read the program.

.. option:: -gcoff

  Produce debugging information in COFF format (if that is supported).
  This is the format used by SDB on most System V systems prior to
  System V Release 4.

.. option:: -gxcoff

  Produce debugging information in XCOFF format (if that is supported).
  This is the format used by the DBX debugger on IBM RS/6000 systems.

.. option:: -gxcoff+

  Produce debugging information in XCOFF format (if that is supported),
  using GNU extensions understood only by the GNU debugger (GDB).  The
  use of these extensions is likely to make other debuggers crash or
  refuse to read the program, and may cause assemblers other than the GNU
  assembler (GAS) to fail with an error.

.. option:: -gdwarf-version

  .. index:: gdwarf-version

  Produce debugging information in DWARF format (if that is supported).
  The value of ``version`` may be either 2, 3, 4 or 5; the default version
  for most targets is 4.  DWARF Version 5 is only experimental.

  Note that with DWARF Version 2, some ports require and always
  use some non-conflicting DWARF 3 extensions in the unwind tables.

  Version 4 may require GDB 7.0 and :option:`-fvar-tracking-assignments`
  for maximum benefit.

.. option:: -grecord-gcc-switches

  This switch causes the command-line options used to invoke the
  compiler that may affect code generation to be appended to the
  DW_AT_producer attribute in DWARF debugging information.  The options
  are concatenated with spaces separating them from each other and from
  the compiler version.  See also :option:`-frecord-gcc-switches` for another
  way of storing compiler options into the object file.  This is the default.

.. option:: -gno-record-gcc-switches

  Disallow appending command-line options to the DW_AT_producer attribute
  in DWARF debugging information.

.. option:: -gstrict-dwarf

  Disallow using extensions of later DWARF standard version than selected
  with :option:`-gdwarf-``version```.  On most targets using non-conflicting
  DWARF extensions from later standard versions is allowed.

.. option:: -gno-strict-dwarf

  Allow using extensions of later DWARF standard version than selected with
  :option:`-gdwarf-``version```.

.. option:: -gz[=type]

  Produce compressed debug sections in DWARF format, if that is supported.
  If ``type`` is not given, the default type depends on the capabilities
  of the assembler and linker used.  ``type`` may be one of
  :samp:`none` (don't compress debug sections), :samp:`zlib` (use zlib
  compression in ELF gABI format), or :samp:`zlib-gnu` (use zlib
  compression in traditional GNU format).  If the linker doesn't support
  writing compressed debug sections, the option is rejected.  Otherwise,
  if the assembler does not support them, :option:`-gz` is silently ignored
  when producing object files.

.. option:: -gvms

  Produce debugging information in Alpha/VMS debug format (if that is
  supported).  This is the format used by DEBUG on Alpha/VMS systems.

:samp:`-g{level}` :samp:`-ggdb{level}` :samp:`-gstabs{level}` :samp:`-gcoff{level}` :samp:`-gxcoff{level}` :samp:`-gvms{level}`
  Request debugging information and also use ``level`` to specify how
  much information.  The default level is 2.

  Level 0 produces no debug information at all.  Thus, :option:`-g0` negates
  :option:`-g`.

  Level 1 produces minimal information, enough for making backtraces in
  parts of the program that you don't plan to debug.  This includes
  descriptions of functions and external variables, and line number
  tables, but no information about local variables.

  Level 3 includes extra information, such as all the macro definitions
  present in the program.  Some debuggers support macro expansion when
  you use :option:`-g3`.

  :option:`-gdwarf-2` does not accept a concatenated debug level, because
  GCC used to support an option :option:`-gdwarf` that meant to generate
  debug information in version 1 of the DWARF format (which is very
  different from version 2), and it would have been too confusing.  That
  debug format is long obsolete, but the option cannot be changed now.
  Instead use an additional :option:`-g``level``` option to change the
  debug level for DWARF.

.. option:: -gtoggle

  Turn off generation of debug info, if leaving out this option
  generates it, or turn it on at level 2 otherwise.  The position of this
  argument in the command line does not matter; it takes effect after all
  other options are processed, and it does so only once, no matter how
  many times it is given.  This is mainly intended to be used with
  :option:`-fcompare-debug`.

.. option:: -fsanitize=address

  Enable AddressSanitizer, a fast memory error detector.
  Memory access instructions are instrumented to detect
  out-of-bounds and use-after-free bugs.
  See http://code.google.com/p/address-sanitizer/ for
  more details.  The run-time behavior can be influenced using the
  :envvar:`ASAN_OPTIONS` environment variable; see
  https://code.google.com/p/address-sanitizer/wiki/Flags#Run-time_flags for
  a list of supported options.

.. option:: -fsanitize=kernel-address

  Enable AddressSanitizer for Linux kernel.
  See http://code.google.com/p/address-sanitizer/wiki/AddressSanitizerForKernel for more details.

.. option:: -fsanitize=thread

  Enable ThreadSanitizer, a fast data race detector.
  Memory access instructions are instrumented to detect
  data race bugs.  See http://code.google.com/p/thread-sanitizer/ for more
  details. The run-time behavior can be influenced using the :envvar:`TSAN_OPTIONS`
  environment variable; see
  https://code.google.com/p/thread-sanitizer/wiki/Flags for a list of
  supported options.

.. option:: -fsanitize=leak

  Enable LeakSanitizer, a memory leak detector.
  This option only matters for linking of executables and if neither
  :option:`-fsanitize=address` nor :option:`-fsanitize=thread` is used.  In that
  case the executable is linked against a library that overrides ``malloc``
  and other allocator functions.  See
  https://code.google.com/p/address-sanitizer/wiki/LeakSanitizer for more
  details.  The run-time behavior can be influenced using the
  :envvar:`LSAN_OPTIONS` environment variable.

.. option:: -fsanitize=undefined

  Enable UndefinedBehaviorSanitizer, a fast undefined behavior detector.
  Various computations are instrumented to detect undefined behavior
  at runtime.  Current suboptions are:

  .. option:: -fsanitize=shift

    This option enables checking that the result of a shift operation is
    not undefined.  Note that what exactly is considered undefined differs
    slightly between C and C++, as well as between ISO C90 and C99, etc.

  .. option:: -fsanitize=integer-divide-by-zero

    Detect integer division by zero as well as ``INT_MIN / -1`` division.

  .. option:: -fsanitize=unreachable

    With this option, the compiler turns the ``__builtin_unreachable``
    call into a diagnostics message call instead.  When reaching the
    ``__builtin_unreachable`` call, the behavior is undefined.

  .. option:: -fsanitize=vla-bound

    This option instructs the compiler to check that the size of a variable
    length array is positive.

  .. option:: -fsanitize=null

    This option enables pointer checking.  Particularly, the application
    built with this option turned on will issue an error message when it
    tries to dereference a NULL pointer, or if a reference (possibly an
    rvalue reference) is bound to a NULL pointer, or if a method is invoked
    on an object pointed by a NULL pointer.

  .. option:: -fsanitize=return

    This option enables return statement checking.  Programs
    built with this option turned on will issue an error message
    when the end of a non-void function is reached without actually
    returning a value.  This option works in C++ only.

  .. option:: -fsanitize=signed-integer-overflow

    This option enables signed integer overflow checking.  We check that
    the result of ``+``, ``*``, and both unary and binary ``-``
    does not overflow in the signed arithmetics.  Note, integer promotion
    rules must be taken into account.  That is, the following is not an
    overflow:

    .. code-block:: c++

      signed char a = SCHAR_MAX;
      a++;

  .. option:: -fsanitize=bounds

    This option enables instrumentation of array bounds.  Various out of bounds
    accesses are detected.  Flexible array members, flexible array member-like
    arrays, and initializers of variables with static storage are not instrumented.

  .. option:: -fsanitize=bounds-strict

    This option enables strict instrumentation of array bounds.  Most out of bounds
    accesses are detected, including flexible array members and flexible array
    member-like arrays.  Initializers of variables with static storage are not
    instrumented.

  .. option:: -fsanitize=alignment

    This option enables checking of alignment of pointers when they are
    dereferenced, or when a reference is bound to insufficiently aligned target,
    or when a method or constructor is invoked on insufficiently aligned object.

  .. option:: -fsanitize=object-size

    This option enables instrumentation of memory references using the
    ``__builtin_object_size`` function.  Various out of bounds pointer
    accesses are detected.

  .. option:: -fsanitize=float-divide-by-zero

    Detect floating-point division by zero.  Unlike other similar options,
    :option:`-fsanitize=float-divide-by-zero` is not enabled by
    :option:`-fsanitize=undefined`, since floating-point division by zero can
    be a legitimate way of obtaining infinities and NaNs.

  .. option:: -fsanitize=float-cast-overflow

    This option enables floating-point type to integer conversion checking.
    We check that the result of the conversion does not overflow.
    Unlike other similar options, :option:`-fsanitize=float-cast-overflow` is
    not enabled by :option:`-fsanitize=undefined`.
    This option does not work well with ``FE_INVALID`` exceptions enabled.

  .. option:: -fsanitize=nonnull-attribute

    This option enables instrumentation of calls, checking whether null values
    are not passed to arguments marked as requiring a non-null value by the
    ``nonnull`` function attribute.

  .. option:: -fsanitize=returns-nonnull-attribute

    This option enables instrumentation of return statements in functions
    marked with ``returns_nonnull`` function attribute, to detect returning
    of null values from such functions.

  .. option:: -fsanitize=bool

    This option enables instrumentation of loads from bool.  If a value other
    than 0/1 is loaded, a run-time error is issued.

  .. option:: -fsanitize=enum

    This option enables instrumentation of loads from an enum type.  If
    a value outside the range of values for the enum type is loaded,
    a run-time error is issued.

  .. option:: -fsanitize=vptr

    This option enables instrumentation of C++ member function calls, member
    accesses and some conversions between pointers to base and derived classes,
    to verify the referenced object has the correct dynamic type.

  While :option:`-ftrapv` causes traps for signed overflows to be emitted,
  :option:`-fsanitize=undefined` gives a diagnostic message.
  This currently works only for the C family of languages.

.. option:: -fno-sanitize=all

  This option disables all previously enabled sanitizers.
  :option:`-fsanitize=all` is not allowed, as some sanitizers cannot be used
  together.

.. option:: -fasan-shadow-offset=number

  This option forces GCC to use custom shadow offset in AddressSanitizer checks.
  It is useful for experimenting with different shadow memory layouts in
  Kernel AddressSanitizer.

.. option:: -fsanitize-sections=s1,s2,...

  Sanitize global variables in selected user-defined sections.  ``si`` may
  contain wildcards.

.. option:: -fsanitize-recover[=opts]

  :option:`-fsanitize-recover=` controls error recovery mode for sanitizers
  mentioned in comma-separated list of ``opts``.  Enabling this option
  for a sanitizer component causes it to attempt to continue
  running the program as if no error happened.  This means multiple
  runtime errors can be reported in a single program run, and the exit
  code of the program may indicate success even when errors
  have been reported.  The :option:`-fno-sanitize-recover=` option
  can be used to alter
  this behavior: only the first detected error is reported
  and program then exits with a non-zero exit code.

  Currently this feature only works for :option:`-fsanitize=undefined` (and its suboptions
  except for :option:`-fsanitize=unreachable` and :option:`-fsanitize=return`),
  :option:`-fsanitize=float-cast-overflow`, :option:`-fsanitize=float-divide-by-zero` and
  :option:`-fsanitize=kernel-address`.  For these sanitizers error recovery is turned on by default.
  :option:`-fsanitize-recover=all` and :option:`-fno-sanitize-recover=all` is also
  accepted, the former enables recovery for all sanitizers that support it,
  the latter disables recovery for all sanitizers that support it.

  Syntax without explicit ``opts`` parameter is deprecated.  It is equivalent to

  :option:`-fsanitize-recover=undefined,float-cast-overflow,float-divide-by-zero`
  Similarly :option:`-fno-sanitize-recover` is equivalent to

  :option:`-fno-sanitize-recover=undefined,float-cast-overflow,float-divide-by-zero`

.. option:: -fsanitize-undefined-trap-on-error

  The :option:`-fsanitize-undefined-trap-on-error` option instructs the compiler to
  report undefined behavior using ``__builtin_trap`` rather than
  a ``libubsan`` library routine.  The advantage of this is that the
  ``libubsan`` library is not needed and is not linked in, so this
  is usable even in freestanding environments.

.. option:: -fcheck-pointer-bounds, -fno-check-pointer-bounds

  .. index:: Pointer Bounds Checker options

  Enable Pointer Bounds Checker instrumentation.  Each memory reference
  is instrumented with checks of the pointer used for memory access against
  bounds associated with that pointer.

  Currently there
  is only an implementation for Intel MPX available, thus x86 target
  and :option:`-mmpx` are required to enable this feature.  
  MPX-based instrumentation requires
  a runtime library to enable MPX in hardware and handle bounds
  violation signals.  By default when :option:`-fcheck-pointer-bounds`
  and :option:`-mmpx` options are used to link a program, the GCC driver
  links against the libmpx runtime library and libmpxwrappers
  library.  It also passes '-z bndplt' to a linker in case it supports this
  option (which is checked on libmpx configuration).  Note that old versions
  of linker may ignore option.  Gold linker doesn't support '-z bndplt'
  option.  With no '-z bndplt' support in linker all calls to dynamic libraries
  lose passed bounds reducing overall protection level.  It's highly
  recommended to use linker with '-z bndplt' support.  In case such linker
  is not available it is adviced to always use :option:`-static-libmpxwrappers`
  for better protection level or use :option:`-static` to completely avoid
  external calls to dynamic libraries.  MPX-based instrumentation
  may be used for debugging and also may be included in production code
  to increase program security.  Depending on usage, you may
  have different requirements for the runtime library.  The current version
  of the MPX runtime library is more oriented for use as a debugging
  tool.  MPX runtime library usage implies :option:`-lpthread`.  See
  also :option:`-static-libmpx`.  The runtime library  behavior can be
  influenced using various :envvar:`CHKP_RT_*` environment variables.  See
  https://gcc.gnu.org/wiki/Intel%20MPX%20support%20in%20the%20GCC%20compiler
  for more details.

  Generated instrumentation may be controlled by various
  :option:`-fchkp-*` options and by the ``bnd_variable_size``
  structure field attribute (see :ref:`type-attributes`) and
  ``bnd_legacy``, and ``bnd_instrument`` function attributes
  (see :ref:`function-attributes`).  GCC also provides a number of built-in
  functions for controlling the Pointer Bounds Checker.  See :ref:`pointer-bounds-checker-builtins`, for more information.

.. option:: -fchkp-check-incomplete-type, -fno-chkp-check-incomplete-type

  Generate pointer bounds checks for variables with incomplete type.
  Enabled by default.

.. option:: -fchkp-narrow-bounds, -fno-chkp-narrow-bounds

  Controls bounds used by Pointer Bounds Checker for pointers to object
  fields.  If narrowing is enabled then field bounds are used.  Otherwise
  object bounds are used.  See also :option:`-fchkp-narrow-to-innermost-array`
  and :option:`-fchkp-first-field-has-own-bounds`.  Enabled by default.

.. option:: -fchkp-first-field-has-own-bounds, -fno-chkp-first-field-has-own-bounds

  Forces Pointer Bounds Checker to use narrowed bounds for the address of the
  first field in the structure.  By default a pointer to the first field has
  the same bounds as a pointer to the whole structure.

.. option:: -fchkp-narrow-to-innermost-array, -fno-chkp-narrow-to-innermost-array

  Forces Pointer Bounds Checker to use bounds of the innermost arrays in
  case of nested static array access.  By default this option is disabled and
  bounds of the outermost array are used.

.. option:: -fchkp-optimize, -fno-chkp-optimize

  Enables Pointer Bounds Checker optimizations.  Enabled by default at
  optimization levels :option:`-O`, :option:`-O2`, :option:`-O3`.

.. option:: -fchkp-use-fast-string-functions, -fno-chkp-use-fast-string-functions

  Enables use of ``*_nobnd`` versions of string functions (not copying bounds)
  by Pointer Bounds Checker.  Disabled by default.

.. option:: -fchkp-use-nochk-string-functions, -fno-chkp-use-nochk-string-functions

  Enables use of ``*_nochk`` versions of string functions (not checking bounds)
  by Pointer Bounds Checker.  Disabled by default.

.. option:: -fchkp-use-static-bounds, -fno-chkp-use-static-bounds

  Allow Pointer Bounds Checker to generate static bounds holding
  bounds of static variables.  Enabled by default.

.. option:: -fchkp-use-static-const-bounds, -fno-chkp-use-static-const-bounds

  Use statically-initialized bounds for constant bounds instead of
  generating them each time they are required.  By default enabled when
  :option:`-fchkp-use-static-bounds` is enabled.

.. option:: -fchkp-treat-zero-dynamic-size-as-infinite, -fno-chkp-treat-zero-dynamic-size-as-infinite

  With this option, objects with incomplete type whose
  dynamically-obtained size is zero are treated as having infinite size
  instead by Pointer Bounds
  Checker.  This option may be helpful if a program is linked with a library
  missing size information for some symbols.  Disabled by default.

.. option:: -fchkp-check-read, -fno-chkp-check-read

  Instructs Pointer Bounds Checker to generate checks for all read
  accesses to memory.  Enabled by default.

.. option:: -fchkp-check-write, -fno-chkp-check-write

  Instructs Pointer Bounds Checker to generate checks for all write
  accesses to memory.  Enabled by default.

.. option:: -fchkp-store-bounds, -fno-chkp-store-bounds

  Instructs Pointer Bounds Checker to generate bounds stores for
  pointer writes.  Enabled by default.

.. option:: -fchkp-instrument-calls, -fno-chkp-instrument-calls

  Instructs Pointer Bounds Checker to pass pointer bounds to calls.
  Enabled by default.

.. option:: -fchkp-instrument-marked-only, -fno-chkp-instrument-marked-only

  Instructs Pointer Bounds Checker to instrument only functions
  marked with the ``bnd_instrument`` attribute
  (see :ref:`function-attributes`).  Disabled by default.

.. option:: -fchkp-use-wrappers, -fno-chkp-use-wrappers

  Allows Pointer Bounds Checker to replace calls to built-in functions
  with calls to wrapper functions.  When :option:`-fchkp-use-wrappers`
  is used to link a program, the GCC driver automatically links
  against libmpxwrappers.  See also :option:`-static-libmpxwrappers`.
  Enabled by default.

.. option:: -fdump-final-insns[=file]

  Dump the final internal representation (RTL) to ``file``.  If the
  optional argument is omitted (or if ``file`` is ``.``), the name
  of the dump file is determined by appending ``.gkd`` to the
  compilation output file name.

.. option:: -fcompare-debug[=opts]

  If no error occurs during compilation, run the compiler a second time,
  adding ``opts`` and :option:`-fcompare-debug-second` to the arguments
  passed to the second compilation.  Dump the final internal
  representation in both compilations, and print an error if they differ.

  If the equal sign is omitted, the default :option:`-gtoggle` is used.

  The environment variable :envvar:`GCC_COMPARE_DEBUG`, if defined, non-empty
  and nonzero, implicitly enables :option:`-fcompare-debug`.  If
  :envvar:`GCC_COMPARE_DEBUG` is defined to a string starting with a dash,
  then it is used for ``opts``, otherwise the default :option:`-gtoggle`
  is used.

  :option:`-fcompare-debug=`, with the equal sign but without ``opts``,
  is equivalent to :option:`-fno-compare-debug`, which disables the dumping
  of the final representation and the second compilation, preventing even
  :envvar:`GCC_COMPARE_DEBUG` from taking effect.

  To verify full coverage during :option:`-fcompare-debug` testing, set
  :envvar:`GCC_COMPARE_DEBUG` to say :option:`-fcompare-debug-not-overridden`,
  which GCC rejects as an invalid option in any actual compilation
  (rather than preprocessing, assembly or linking).  To get just a
  warning, setting :envvar:`GCC_COMPARE_DEBUG` to :samp:`-w%n-fcompare-debug
  not overridden` will do.

.. option:: -fcompare-debug-second

  This option is implicitly passed to the compiler for the second
  compilation requested by :option:`-fcompare-debug`, along with options to
  silence warnings, and omitting other options that would cause
  side-effect compiler outputs to files or to the standard output.  Dump
  files and preserved temporary files are renamed so as to contain the
  ``.gk`` additional extension during the second compilation, to avoid
  overwriting those generated by the first.

  When this option is passed to the compiler driver, it causes the
  *first* compilation to be skipped, which makes it useful for little
  other than debugging the compiler proper.

.. option:: -feliminate-dwarf2-dups

  Compress DWARF 2 debugging information by eliminating duplicated
  information about each symbol.  This option only makes sense when
  generating DWARF 2 debugging information with :option:`-gdwarf-2`.

.. option:: -femit-struct-debug-baseonly

  Emit debug information for struct-like types
  only when the base name of the compilation source file
  matches the base name of file in which the struct is defined.

  This option substantially reduces the size of debugging information,
  but at significant potential loss in type information to the debugger.
  See :option:`-femit-struct-debug-reduced` for a less aggressive option.
  See :option:`-femit-struct-debug-detailed` for more detailed control.

  This option works only with DWARF 2.

.. option:: -femit-struct-debug-reduced

  Emit debug information for struct-like types
  only when the base name of the compilation source file
  matches the base name of file in which the type is defined,
  unless the struct is a template or defined in a system header.

  This option significantly reduces the size of debugging information,
  with some potential loss in type information to the debugger.
  See :option:`-femit-struct-debug-baseonly` for a more aggressive option.
  See :option:`-femit-struct-debug-detailed` for more detailed control.

  This option works only with DWARF 2.

.. option:: -femit-struct-debug-detailed[=spec-list]

  Specify the struct-like types
  for which the compiler generates debug information.
  The intent is to reduce duplicate struct debug information
  between different object files within the same program.

  This option is a detailed version of
  :option:`-femit-struct-debug-reduced` and :option:`-femit-struct-debug-baseonly`,
  which serves for most needs.

  A specification has the syntax

  [:samp:`dir:`|:samp:`ind:`][:samp:`ord:`|:samp:`gen:`](:samp:`any`|:samp:`sys`|:samp:`base`|:samp:`none`)

  The optional first word limits the specification to
  structs that are used directly (:samp:`dir:`) or used indirectly (:samp:`ind:`).
  A struct type is used directly when it is the type of a variable, member.
  Indirect uses arise through pointers to structs.
  That is, when use of an incomplete struct is valid, the use is indirect.
  An example is
  :samp:`struct one direct; struct two * indirect;`.

  The optional second word limits the specification to
  ordinary structs (:samp:`ord:`) or generic structs (:samp:`gen:`).
  Generic structs are a bit complicated to explain.
  For C++, these are non-explicit specializations of template classes,
  or non-template classes within the above.
  Other programming languages have generics,
  but :option:`-femit-struct-debug-detailed` does not yet implement them.

  The third word specifies the source files for those
  structs for which the compiler should emit debug information.
  The values :samp:`none` and :samp:`any` have the normal meaning.
  The value :samp:`base` means that
  the base of name of the file in which the type declaration appears
  must match the base of the name of the main compilation file.
  In practice, this means that when compiling foo.c, debug information
  is generated for types declared in that file and foo.h,
  but not other header files.
  The value :samp:`sys` means those types satisfying :samp:`base`
  or declared in system or compiler headers.

  You may need to experiment to determine the best settings for your application.

  The default is :option:`-femit-struct-debug-detailed=all`.

  This option works only with DWARF 2.

.. option:: -fno-merge-debug-strings, -fmerge-debug-strings

  Direct the linker to not merge together strings in the debugging
  information that are identical in different object files.  Merging is
  not supported by all assemblers or linkers.  Merging decreases the size
  of the debug information in the output file at the cost of increasing
  link processing time.  Merging is enabled by default.

.. option:: -fdebug-prefix-map=old=new

  When compiling files in directory ``old``, record debugging
  information describing them as in ``new`` instead.

.. option:: -fno-dwarf2-cfi-asm, -fdwarf2-cfi-asm

  Emit DWARF 2 unwind info as compiler generated ``.eh_frame`` section
  instead of using GAS ``.cfi_*`` directives.

  .. index:: prof

.. option:: -p

  Generate extra code to write profile information suitable for the
  analysis program :command:`prof`.  You must use this option when compiling
  the source files you want data about, and you must also use it when
  linking.

  .. index:: gprof

.. option:: -pg

  Generate extra code to write profile information suitable for the
  analysis program :command:`gprof`.  You must use this option when compiling
  the source files you want data about, and you must also use it when
  linking.

.. option:: -Q

  Makes the compiler print out each function name as it is compiled, and
  print some statistics about each pass when it finishes.

.. option:: -ftime-report

  Makes the compiler print some statistics about the time consumed by each
  pass when it finishes.

.. option:: -fmem-report

  Makes the compiler print some statistics about permanent memory
  allocation when it finishes.

.. option:: -fmem-report-wpa

  Makes the compiler print some statistics about permanent memory
  allocation for the WPA phase only.

.. option:: -fpre-ipa-mem-report

.. option:: -fpost-ipa-mem-report

  Makes the compiler print some statistics about permanent memory
  allocation before or after interprocedural optimization.

.. option:: -fprofile-report

  Makes the compiler print some statistics about consistency of the
  (estimated) profile and effect of individual passes.

.. option:: -fstack-usage

  Makes the compiler output stack usage information for the program, on a
  per-function basis.  The filename for the dump is made by appending
  .su to the ``auxname``.  ``auxname`` is generated from the name of
  the output file, if explicitly specified and it is not an executable,
  otherwise it is the basename of the source file.  An entry is made up
  of three fields:

  * The name of the function.

  * A number of bytes.

  * One or more qualifiers: ``static``, ``dynamic``, ``bounded``.

  The qualifier ``static`` means that the function manipulates the stack
  statically: a fixed number of bytes are allocated for the frame on function
  entry and released on function exit; no stack adjustments are otherwise made
  in the function.  The second field is this fixed number of bytes.

  The qualifier ``dynamic`` means that the function manipulates the stack
  dynamically: in addition to the static allocation described above, stack
  adjustments are made in the body of the function, for example to push/pop
  arguments around function calls.  If the qualifier ``bounded`` is also
  present, the amount of these adjustments is bounded at compile time and
  the second field is an upper bound of the total amount of stack used by
  the function.  If it is not present, the amount of these adjustments is
  not bounded at compile time and the second field only represents the
  bounded part.

.. option:: -fprofile-arcs

  Add code so that program flow :dfn:`arcs` are instrumented.  During
  execution the program records how many times each branch and call is
  executed and how many times it is taken or returns.  When the compiled
  program exits it saves this data to a file called
  ``auxname``.gcda for each source file.  The data may be used for
  profile-directed optimizations (:option:`-fbranch-probabilities`), or for
  test coverage analysis (:option:`-ftest-coverage`).  Each object file's
  ``auxname`` is generated from the name of the output file, if
  explicitly specified and it is not the final executable, otherwise it is
  the basename of the source file.  In both cases any suffix is removed
  (e.g. foo.gcda for input file dir/foo.c, or
  dir/foo.gcda for output file specified as :option:`-o dir/foo.o`).
  See :ref:`cross-profiling`.

  .. index:: gcov

.. option:: --coverage, -coverage

  This option is used to compile and link code instrumented for coverage
  analysis.  The option is a synonym for :option:`-fprofile-arcs`
  :option:`-ftest-coverage` (when compiling) and :option:`-lgcov` (when
  linking).  See the documentation for those options for more details.

  * Compile the source files with :option:`-fprofile-arcs` plus optimization
    and code generation options.  For test coverage analysis, use the
    additional :option:`-ftest-coverage` option.  You do not need to profile
    every source file in a program.

  * Link your object files with :option:`-lgcov` or :option:`-fprofile-arcs`
    (the latter implies the former).

  * Run the program on a representative workload to generate the arc profile
    information.  This may be repeated any number of times.  You can run
    concurrent instances of your program, and provided that the file system
    supports locking, the data files will be correctly updated.  Also
    ``fork`` calls are detected and correctly handled (double counting
    will not happen).

  * For profile-directed optimizations, compile the source files again with
    the same optimization and code generation options plus
    :option:`-fbranch-probabilities` (see :ref:`Options that
    Control Optimization <optimize-options>`).

  * For test coverage analysis, use :command:`gcov` to produce human readable
    information from the .gcno and .gcda files.  Refer to the
    :command:`gcov` documentation for further information.

  With :option:`-fprofile-arcs`, for each function of your program GCC
  creates a program flow graph, then finds a spanning tree for the graph.
  Only arcs that are not on the spanning tree have to be instrumented: the
  compiler adds code to count the number of times that these arcs are
  executed.  When an arc is the only exit or only entrance to a block, the
  instrumentation code can be added to the block; otherwise, a new basic
  block must be created to hold the instrumentation code.

.. option:: -ftest-coverage

  Produce a notes file that the :command:`gcov` code-coverage utility
  (see :ref:`gcov`) can use to
  show program coverage.  Each source file's note file is called
  ``auxname``.gcno.  Refer to the :option:`-fprofile-arcs` option
  above for a description of ``auxname`` and instructions on how to
  generate test coverage data.  Coverage data matches the source files
  more closely if you do not optimize.

.. option:: -fdbg-cnt-list

  Print the name and the counter upper bound for all debug counters.

.. option:: -fdbg-cnt=counter-value-list

  Set the internal debug counter upper bound.  ``counter-value-list``
  is a comma-separated list of ``name``:``value`` pairs
  which sets the upper bound of each debug counter ``name`` to ``value``.
  All debug counters have the initial upper bound of ``UINT_MAX``;
  thus ``dbg_cnt`` returns true always unless the upper bound
  is set by this option.
  For example, with :option:`-fdbg-cnt=dce:10,tail_call:0`,
  ``dbg_cnt(dce)`` returns true only for first 10 invocations.

.. option:: -fenable-kind-pass, -fdisable-, -fenable-

  This is a set of options that are used to explicitly disable/enable
  optimization passes.  These options are intended for use for debugging GCC.
  Compiler users should use regular options for enabling/disabling
  passes instead.

  :samp:`-fdisable-ipa-{pass}`
    Disable IPA pass ``pass``. ``pass`` is the pass name.  If the same pass is
    statically invoked in the compiler multiple times, the pass name should be
    appended with a sequential number starting from 1.

  :samp:`-fdisable-rtl-{pass}` :samp:`-fdisable-rtl-{pass}={range-list}`
    Disable RTL pass ``pass``.  ``pass`` is the pass name.  If the same pass is
    statically invoked in the compiler multiple times, the pass name should be
    appended with a sequential number starting from 1.  ``range-list`` is a 
    comma-separated list of function ranges or assembler names.  Each range is a number
    pair separated by a colon.  The range is inclusive in both ends.  If the range
    is trivial, the number pair can be simplified as a single number.  If the
    function's call graph node's ``uid`` falls within one of the specified ranges,
    the ``pass`` is disabled for that function.  The ``uid`` is shown in the
    function header of a dump file, and the pass names can be dumped by using
    option :option:`-fdump-passes`.

  :samp:`-fdisable-tree-{pass}` :samp:`-fdisable-tree-{pass}={range-list}`
    Disable tree pass ``pass``.  See :option:`-fdisable-rtl` for the description of
    option arguments.

  :samp:`-fenable-ipa-{pass}`
    Enable IPA pass ``pass``.  ``pass`` is the pass name.  If the same pass is
    statically invoked in the compiler multiple times, the pass name should be
    appended with a sequential number starting from 1.

  :samp:`-fenable-rtl-{pass}` :samp:`-fenable-rtl-{pass}={range-list}`
    Enable RTL pass ``pass``.  See :option:`-fdisable-rtl` for option argument
    description and examples.

  :samp:`-fenable-tree-{pass}` :samp:`-fenable-tree-{pass}={range-list}`
    Enable tree pass ``pass``.  See :option:`-fdisable-rtl` for the description
    of option arguments.

    Here are some examples showing uses of these options.

  .. code-block:: c++

    # disable ccp1 for all functions
       -fdisable-tree-ccp1
    # disable complete unroll for function whose cgraph node uid is 1
       -fenable-tree-cunroll=1
    # disable gcse2 for functions at the following ranges [1,1],
    # [300,400], and [400,1000]
    # disable gcse2 for functions foo and foo2
       -fdisable-rtl-gcse2=foo,foo2
    # disable early inlining
       -fdisable-tree-einline
    # disable ipa inlining
       -fdisable-ipa-inline
    # enable tree full unroll
       -fenable-tree-unroll

.. option:: -dletters, -d

  .. index:: fdump-rtl-pass

  Says to make debugging dumps during compilation at times specified by
  ``letters``.  This is used for debugging the RTL-based passes of the
  compiler.  The file names for most of the dumps are made by appending
  a pass number and a word to the ``dumpname``, and the files are
  created in the directory of the output file. In case of
  =``filename`` option, the dump is output on the given file
  instead of the pass numbered dump files. Note that the pass number is
  computed statically as passes get registered into the pass manager.
  Thus the numbering is not related to the dynamic order of execution of
  passes.  In particular, a pass installed by a plugin could have a
  number over 200 even if it executed quite early.  ``dumpname`` is
  generated from the name of the output file, if explicitly specified
  and it is not an executable, otherwise it is the basename of the
  source file. These switches may have different effects when
  :option:`-E` is used for preprocessing.

  Debug dumps can be enabled with a :option:`-fdump-rtl` switch or some
  :option:`-d` option ``letters``.  Here are the possible
  letters for use in ``pass`` and ``letters``, and their meanings:

  .. option:: -fdump-rtl-alignments

    Dump after branch alignments have been computed.

  .. option:: -fdump-rtl-asmcons

    Dump after fixing rtl statements that have unsatisfied in/out constraints.

  .. option:: -fdump-rtl-auto_inc_dec

    Dump after auto-inc-dec discovery.  This pass is only run on
    architectures that have auto inc or auto dec instructions.

  .. option:: -fdump-rtl-barriers

    Dump after cleaning up the barrier instructions.

  .. option:: -fdump-rtl-bbpart

    Dump after partitioning hot and cold basic blocks.

  .. option:: -fdump-rtl-bbro

    Dump after block reordering.

  .. option:: -fdump-rtl-btl1, -fdump-rtl-btl2

    :option:`-fdump-rtl-btl1` and :option:`-fdump-rtl-btl2` enable dumping
    after the two branch
    target load optimization passes.

  .. option:: -fdump-rtl-bypass

    Dump after jump bypassing and control flow optimizations.

  .. option:: -fdump-rtl-combine

    Dump after the RTL instruction combination pass.

  .. option:: -fdump-rtl-compgotos

    Dump after duplicating the computed gotos.

  .. option:: -fdump-rtl-ce1, -fdump-rtl-ce2, -fdump-rtl-ce3

    :option:`-fdump-rtl-ce1`, :option:`-fdump-rtl-ce2`, and
    :option:`-fdump-rtl-ce3` enable dumping after the three
    if conversion passes.

  .. option:: -fdump-rtl-cprop_hardreg

    Dump after hard register copy propagation.

  .. option:: -fdump-rtl-csa

    Dump after combining stack adjustments.

  .. option:: -fdump-rtl-cse1, -fdump-rtl-cse2

    :option:`-fdump-rtl-cse1` and :option:`-fdump-rtl-cse2` enable dumping after
    the two common subexpression elimination passes.

  .. option:: -fdump-rtl-dce

    Dump after the standalone dead code elimination passes.

  .. option:: -fdump-rtl-dbr

    Dump after delayed branch scheduling.

  .. option:: -fdump-rtl-dce1, -fdump-rtl-dce2

    :option:`-fdump-rtl-dce1` and :option:`-fdump-rtl-dce2` enable dumping after
    the two dead store elimination passes.

  .. option:: -fdump-rtl-eh

    Dump after finalization of EH handling code.

  .. option:: -fdump-rtl-eh_ranges

    Dump after conversion of EH handling range regions.

  .. option:: -fdump-rtl-expand

    Dump after RTL generation.

  .. option:: -fdump-rtl-fwprop1, -fdump-rtl-fwprop2

    :option:`-fdump-rtl-fwprop1` and :option:`-fdump-rtl-fwprop2` enable
    dumping after the two forward propagation passes.

  .. option:: -fdump-rtl-gcse1, -fdump-rtl-gcse2

    :option:`-fdump-rtl-gcse1` and :option:`-fdump-rtl-gcse2` enable dumping
    after global common subexpression elimination.

  .. option:: -fdump-rtl-init-regs

    Dump after the initialization of the registers.

  .. option:: -fdump-rtl-initvals

    Dump after the computation of the initial value sets.

  .. option:: -fdump-rtl-into_cfglayout

    Dump after converting to cfglayout mode.

  .. option:: -fdump-rtl-ira

    Dump after iterated register allocation.

  .. option:: -fdump-rtl-jump

    Dump after the second jump optimization.

  .. option:: -fdump-rtl-loop2

    :option:`-fdump-rtl-loop2` enables dumping after the rtl
    loop optimization passes.

  .. option:: -fdump-rtl-mach

    Dump after performing the machine dependent reorganization pass, if that
    pass exists.

  .. option:: -fdump-rtl-mode_sw

    Dump after removing redundant mode switches.

  .. option:: -fdump-rtl-rnreg

    Dump after register renumbering.

  .. option:: -fdump-rtl-outof_cfglayout

    Dump after converting from cfglayout mode.

  .. option:: -fdump-rtl-peephole2

    Dump after the peephole pass.

  .. option:: -fdump-rtl-postreload

    Dump after post-reload optimizations.

  .. option:: -fdump-rtl-pro_and_epilogue

    Dump after generating the function prologues and epilogues.

  .. option:: -fdump-rtl-sched1, -fdump-rtl-sched2

    :option:`-fdump-rtl-sched1` and :option:`-fdump-rtl-sched2` enable dumping
    after the basic block scheduling passes.

  .. option:: -fdump-rtl-ree

    Dump after sign/zero extension elimination.

  .. option:: -fdump-rtl-seqabstr

    Dump after common sequence discovery.

  .. option:: -fdump-rtl-shorten

    Dump after shortening branches.

  .. option:: -fdump-rtl-sibling

    Dump after sibling call optimizations.

  .. option:: -fdump-rtl-split1, -fdump-rtl-split2, -fdump-rtl-split3, -fdump-rtl-split4, -fdump-rtl-split5

    These options enable dumping after five rounds of
    instruction splitting.

  .. option:: -fdump-rtl-sms

    Dump after modulo scheduling.  This pass is only run on some
    architectures.

  .. option:: -fdump-rtl-stack

    Dump after conversion from GCC's 'flat register file' registers to the
    x87's stack-like registers.  This pass is only run on x86 variants.

  .. option:: -fdump-rtl-subreg1, -fdump-rtl-subreg2

    :option:`-fdump-rtl-subreg1` and :option:`-fdump-rtl-subreg2` enable dumping after
    the two subreg expansion passes.

  .. option:: -fdump-rtl-unshare

    Dump after all rtl has been unshared.

  .. option:: -fdump-rtl-vartrack

    Dump after variable tracking.

  .. option:: -fdump-rtl-vregs

    Dump after converting virtual registers to hard registers.

  .. option:: -fdump-rtl-web

    Dump after live range splitting.

  .. option:: -fdump-rtl-regclass, -fdump-rtl-subregs_of_mode_init, -fdump-rtl-subregs_of_mode_finish, -fdump-rtl-dfinit, -fdump-rtl-dfinish

    These dumps are defined but always produce empty files.

  .. option:: -da, -fdump-rtl-all

    Produce all the dumps listed above.

  .. option:: -dA

    Annotate the assembler output with miscellaneous debugging information.

  .. option:: -dD

    Dump all macro definitions, at the end of preprocessing, in addition to
    normal output.

  .. option:: -dH

    Produce a core dump whenever an error occurs.

  .. option:: -dp

    Annotate the assembler output with a comment indicating which
    pattern and alternative is used.  The length of each instruction is
    also printed.

  .. option:: -dP

    Dump the RTL in the assembler output as a comment before each instruction.
    Also turns on :option:`-dp` annotation.

  .. option:: -dx

    Just generate RTL for a function instead of compiling it.  Usually used
    with :option:`-fdump-rtl-expand`.

.. option:: -fdump-noaddr

  When doing debugging dumps, suppress address output.  This makes it more
  feasible to use diff on debugging dumps for compiler invocations with
  different compiler binaries and/or different
  text / bss / data / heap / stack / dso start locations.

.. option:: -freport-bug

  Collect and dump debug information into temporary file if ICE in C/C++
  compiler occured.

.. option:: -fdump-unnumbered

  When doing debugging dumps, suppress instruction numbers and address output.
  This makes it more feasible to use diff on debugging dumps for compiler
  invocations with different options, in particular with and without
  :option:`-g`.

.. option:: -fdump-unnumbered-links

  When doing debugging dumps (see :option:`-d` option above), suppress
  instruction numbers for the links to the previous and next instructions
  in a sequence.

.. option:: -fdump-translation-unit , -fdump-translation-unit

  .. note::

    (C++ only)

  Dump a representation of the tree structure for the entire translation
  unit to a file.  The file name is made by appending .tu to the
  source file name, and the file is created in the same directory as the
  output file.  If the :samp:`-``options``` form is used, ``options``
  controls the details of the dump as described for the
  :option:`-fdump-tree` options.

.. option:: -fdump-class-hierarchy , -fdump-class-hierarchy

  .. note::

    (C++ only)

  Dump a representation of each class's hierarchy and virtual function
  table layout to a file.  The file name is made by appending
  .class to the source file name, and the file is created in the
  same directory as the output file.  If the :samp:`-``options``` form
  is used, ``options`` controls the details of the dump as described
  for the :option:`-fdump-tree` options.

.. option:: -fdump-ipa-switch, -fdump-ipa

  Control the dumping at various stages of inter-procedural analysis
  language tree to a file.  The file name is generated by appending a
  switch specific suffix to the source file name, and the file is created
  in the same directory as the output file.  The following dumps are
  possible:

  :samp:`all`
    Enables all inter-procedural analysis dumps.

  :samp:`cgraph`
    Dumps information about call-graph optimization, unused function removal,
    and inlining decisions.

  :samp:`inline`
    Dump after function inlining.

.. option:: -fdump-passes

  Dump the list of optimization passes that are turned on and off by
  the current command-line options.

.. option:: -fdump-statistics-option, -fdump-statistics

  Enable and control dumping of pass statistics in a separate file.  The
  file name is generated by appending a suffix ending in
  :samp:`.statistics` to the source file name, and the file is created in
  the same directory as the output file.  If the :samp:`-``option```
  form is used, :samp:`-stats` causes counters to be summed over the
  whole compilation unit while :samp:`-details` dumps every event as
  the passes generate them.  The default with no option is to sum
  counters for each function compiled.

.. option:: -fdump-tree-switch, -fdump-tree

  Control the dumping at various stages of processing the intermediate
  language tree to a file.  The file name is generated by appending a
  switch-specific suffix to the source file name, and the file is
  created in the same directory as the output file. In case of
  =``filename`` option, the dump is output on the given file
  instead of the auto named dump files.  If the :samp:`-``options```
  form is used, ``options`` is a list of :samp:`-` separated options
  which control the details of the dump.  Not all options are applicable
  to all dumps; those that are not meaningful are ignored.  The
  following options are available

  :samp:`address`
    Print the address of each node.  Usually this is not meaningful as it
    changes according to the environment and source file.  Its primary use
    is for tying up a dump file with a debug environment.

  :samp:`asmname`
    If ``DECL_ASSEMBLER_NAME`` has been set for a given decl, use that
    in the dump instead of ``DECL_NAME``.  Its primary use is ease of
    use working backward from mangled names in the assembly file.

  :samp:`slim`
    When dumping front-end intermediate representations, inhibit dumping
    of members of a scope or body of a function merely because that scope
    has been reached.  Only dump such items when they are directly reachable
    by some other path.

    When dumping pretty-printed trees, this option inhibits dumping the
    bodies of control structures.

    When dumping RTL, print the RTL in slim (condensed) form instead of
    the default LISP-like representation.

  :samp:`raw`
    Print a raw representation of the tree.  By default, trees are
    pretty-printed into a C-like representation.

  :samp:`details`
    Enable more detailed dumps (not honored by every dump option). Also
    include information from the optimization passes.

  :samp:`stats`
    Enable dumping various statistics about the pass (not honored by every dump
    option).

  :samp:`blocks`
    Enable showing basic block boundaries (disabled in raw dumps).

  :samp:`graph`
    For each of the other indicated dump files (:option:`-fdump-rtl-``pass```),
    dump a representation of the control flow graph suitable for viewing with
    GraphViz to ``file``.``passid``.``pass``.dot.  Each function in
    the file is pretty-printed as a subgraph, so that GraphViz can render them
    all in a single plot.

    This option currently only works for RTL dumps, and the RTL is always
    dumped in slim form.

  :samp:`vops`
    Enable showing virtual operands for every statement.

  :samp:`lineno`
    Enable showing line numbers for statements.

  :samp:`uid`
    Enable showing the unique ID (``DECL_UID``) for each variable.

  :samp:`verbose`
    Enable showing the tree dump for each statement.

  :samp:`eh`
    Enable showing the EH region number holding each statement.

  :samp:`scev`
    Enable showing scalar evolution analysis details.

  :samp:`optimized`
    Enable showing optimization information (only available in certain
    passes).

  :samp:`missed`
    Enable showing missed optimization information (only available in certain
    passes).

  :samp:`note`
    Enable other detailed optimization information (only available in
    certain passes).

  :samp:`={filename}`
    Instead of an auto named dump file, output into the given file
    name. The file names stdout and stderr are treated
    specially and are considered already open standard streams. For
    example,

    .. code-block:: bash

      gcc -O2 -ftree-vectorize -fdump-tree-vect-blocks=foo.dump
           -fdump-tree-pre=stderr file.c

    outputs vectorizer dump into foo.dump, while the PRE dump is
    output on to stderr. If two conflicting dump filenames are
    given for the same pass, then the latter option overrides the earlier
    one.

  :samp:`all`
    Turn on all options, except raw, slim, verbose
    and lineno.

  :samp:`optall`
    Turn on all optimization options, i.e., optimized,
    missed, and note.

    The following tree dumps are possible:

  .. option:: original, -fdump-tree-original

    Dump before any tree based optimization, to ``file``.original.

  .. option:: optimized, -fdump-tree-optimized

    Dump after all tree based optimization, to ``file``.optimized.

  .. option:: gimple, -fdump-tree-gimple

    Dump each function before and after the gimplification pass to a file.  The
    file name is made by appending .gimple to the source file name.

  .. option:: cfg, -fdump-tree-cfg

    Dump the control flow graph of each function to a file.  The file name is
    made by appending .cfg to the source file name.

  .. option:: ch, -fdump-tree-ch

    Dump each function after copying loop headers.  The file name is made by
    appending .ch to the source file name.

  .. option:: ssa, -fdump-tree-ssa

    Dump SSA related information to a file.  The file name is made by appending
    .ssa to the source file name.

  .. option:: alias, -fdump-tree-alias

    Dump aliasing information for each function.  The file name is made by
    appending .alias to the source file name.

  .. option:: ccp, -fdump-tree-ccp

    Dump each function after CCP.  The file name is made by appending
    .ccp to the source file name.

  .. option:: storeccp, -fdump-tree-storeccp

    Dump each function after STORE-CCP.  The file name is made by appending
    .storeccp to the source file name.

  .. option:: pre, -fdump-tree-pre

    Dump trees after partial redundancy elimination.  The file name is made
    by appending .pre to the source file name.

  .. option:: fre, -fdump-tree-fre

    Dump trees after full redundancy elimination.  The file name is made
    by appending .fre to the source file name.

  .. option:: copyprop, -fdump-tree-copyprop

    Dump trees after copy propagation.  The file name is made
    by appending .copyprop to the source file name.

  .. option:: store_copyprop, -fdump-tree-store_copyprop

    Dump trees after store copy-propagation.  The file name is made
    by appending .store_copyprop to the source file name.

  .. option:: dce, -fdump-tree-dce

    Dump each function after dead code elimination.  The file name is made by
    appending .dce to the source file name.

  .. option:: sra, -fdump-tree-sra

    Dump each function after performing scalar replacement of aggregates.  The
    file name is made by appending .sra to the source file name.

  .. option:: sink, -fdump-tree-sink

    Dump each function after performing code sinking.  The file name is made
    by appending .sink to the source file name.

  .. option:: dom, -fdump-tree-dom

    Dump each function after applying dominator tree optimizations.  The file
    name is made by appending .dom to the source file name.

  .. option:: dse, -fdump-tree-dse

    Dump each function after applying dead store elimination.  The file
    name is made by appending .dse to the source file name.

  .. option:: phiopt, -fdump-tree-phiopt

    Dump each function after optimizing PHI nodes into straightline code.  The file
    name is made by appending .phiopt to the source file name.

  .. option:: forwprop, -fdump-tree-forwprop

    Dump each function after forward propagating single use variables.  The file
    name is made by appending .forwprop to the source file name.

  .. option:: copyrename, -fdump-tree-copyrename

    Dump each function after applying the copy rename optimization.  The file
    name is made by appending .copyrename to the source file name.

  .. option:: nrv, -fdump-tree-nrv

    Dump each function after applying the named return value optimization on
    generic trees.  The file name is made by appending .nrv to the source
    file name.

  .. option:: vect, -fdump-tree-vect

    Dump each function after applying vectorization of loops.  The file name is
    made by appending .vect to the source file name.

  .. option:: slp, -fdump-tree-slp

    Dump each function after applying vectorization of basic blocks.  The file name
    is made by appending .slp to the source file name.

  .. option:: vrp, -fdump-tree-vrp

    Dump each function after Value Range Propagation (VRP).  The file name
    is made by appending .vrp to the source file name.

  .. option:: all, -fdump-tree-all

    Enable all the available tree dumps with the flags provided in this option.

.. option:: -fopt-info

  Controls optimization dumps from various optimization passes. If the
  :samp:`-``options``` form is used, ``options`` is a list of
  :samp:`-` separated option keywords to select the dump details and
  optimizations.  

  The ``options`` can be divided into two groups: options describing the
  verbosity of the dump, and options describing which optimizations
  should be included. The options from both the groups can be freely
  mixed as they are non-overlapping. However, in case of any conflicts,
  the later options override the earlier options on the command
  line. 

  The following options control the dump verbosity:

  :samp:`optimized`
    Print information when an optimization is successfully applied. It is
    up to a pass to decide which information is relevant. For example, the
    vectorizer passes print the source location of loops which are
    successfully vectorized.

  :samp:`missed`
    Print information about missed optimizations. Individual passes
    control which information to include in the output.

  :samp:`note`
    Print verbose information about optimizations, such as certain
    transformations, more detailed messages about decisions etc.

  :samp:`all`
    Print detailed optimization information. This includes
    :samp:`optimized`, :samp:`missed`, and :samp:`note`.

    One or more of the following option keywords can be used to describe a
  group of optimizations:

  :samp:`ipa`
    Enable dumps from all interprocedural optimizations.

  :samp:`loop`
    Enable dumps from all loop optimizations.

  :samp:`inline`
    Enable dumps from all inlining optimizations.

  :samp:`vec`
    Enable dumps from all vectorization optimizations.

  :samp:`optall`
    Enable dumps from all optimizations. This is a superset of
    the optimization groups listed above.

    If ``options`` is
  omitted, it defaults to :samp:`optimized-optall`, which means to dump all
  info about successful optimizations from all the passes.  

  If the ``filename`` is provided, then the dumps from all the
  applicable optimizations are concatenated into the ``filename``.
  Otherwise the dump is output onto stderr. Though multiple
  :option:`-fopt-info` options are accepted, only one of them can include
  a ``filename``. If other filenames are provided then all but the
  first such option are ignored.

  Note that the output ``filename`` is overwritten
  in case of multiple translation units. If a combined output from
  multiple translation units is desired, stderr should be used
  instead.

  In the following example, the optimization info is output to
  stderr:

  .. code-block:: bash

    gcc -O3 -fopt-info

  This example:

  .. code-block:: bash

    gcc -O3 -fopt-info-missed=missed.all

  outputs missed optimization report from all the passes into
  missed.all, and this one:

  .. code-block:: bash

    gcc -O2 -ftree-vectorize -fopt-info-vec-missed

  prints information about missed optimization opportunities from
  vectorization passes on stderr.  
  Note that :option:`-fopt-info-vec-missed` is equivalent to 
  :option:`-fopt-info-missed-vec`.

  As another example,

  .. code-block:: bash

    gcc -O3 -fopt-info-inline-optimized-missed=inline.txt

  outputs information about missed optimizations as well as
  optimized locations from all the inlining passes into
  inline.txt.

  Finally, consider:

  .. code-block:: bash

    gcc -fopt-info-vec-missed=vec.miss -fopt-info-loop-optimized=loop.opt

  Here the two output filenames vec.miss and loop.opt are
  in conflict since only one output file is allowed. In this case, only
  the first option takes effect and the subsequent options are
  ignored. Thus only vec.miss is produced which contains
  dumps from the vectorizer about missed opportunities.

.. option:: -frandom-seed=number

  This option provides a seed that GCC uses in place of
  random numbers in generating certain symbol names
  that have to be different in every compiled file.  It is also used to
  place unique stamps in coverage data files and the object files that
  produce them.  You can use the :option:`-frandom-seed` option to produce
  reproducibly identical object files.

  The ``number`` should be different for every file you compile.

.. option:: -fsched-verbose=n

  On targets that use instruction scheduling, this option controls the
  amount of debugging output the scheduler prints.  This information is
  written to standard error, unless :option:`-fdump-rtl-sched1` or
  :option:`-fdump-rtl-sched2` is specified, in which case it is output
  to the usual dump listing file, .sched1 or .sched2
  respectively.  However for ``n`` greater than nine, the output is
  always printed to standard error.

  For ``n`` greater than zero, :option:`-fsched-verbose` outputs the
  same information as :option:`-fdump-rtl-sched1` and :option:`-fdump-rtl-sched2`.
  For ``n`` greater than one, it also output basic block probabilities,
  detailed ready list information and unit/insn info.  For ``n`` greater
  than two, it includes RTL at abort point, control-flow and regions info.
  And for ``n`` over four, :option:`-fsched-verbose` also includes
  dependence info.

.. option:: -save-temps

  Store the usual 'temporary' intermediate files permanently; place them
  in the current directory and name them based on the source file.  Thus,
  compiling foo.c with :option:`-c -save-temps` produces files
  foo.i and foo.s, as well as foo.o.  This creates a
  preprocessed foo.i output file even though the compiler now
  normally uses an integrated preprocessor.

  When used in combination with the :option:`-x` command-line option,
  :option:`-save-temps` is sensible enough to avoid over writing an
  input source file with the same extension as an intermediate file.
  The corresponding intermediate file may be obtained by renaming the
  source file before using :option:`-save-temps`.

  If you invoke GCC in parallel, compiling several different source
  files that share a common base name in different subdirectories or the
  same source file compiled for multiple output destinations, it is
  likely that the different parallel compilers will interfere with each
  other, and overwrite the temporary files.  For instance:

  .. code-block:: bash

    gcc -save-temps -o outdir1/foo.o indir1/foo.c&
    gcc -save-temps -o outdir2/foo.o indir2/foo.c&

  may result in foo.i and foo.o being written to
  simultaneously by both compilers.

.. option:: -save-temps=obj

  Store the usual 'temporary' intermediate files permanently.  If the
  :option:`-o` option is used, the temporary files are based on the
  object file.  If the :option:`-o` option is not used, the
  :option:`-save-temps=obj` switch behaves like :option:`-save-temps`.

  For example:

  .. code-block:: bash

    gcc -save-temps=obj -c foo.c
    gcc -save-temps=obj -c bar.c -o dir/xbar.o
    gcc -save-temps=obj foobar.c -o dir2/yfoobar

  creates foo.i, foo.s, dir/xbar.i,
  dir/xbar.s, dir2/yfoobar.i, dir2/yfoobar.s, and
  dir2/yfoobar.o.

.. option:: -time[=file]

  Report the CPU time taken by each subprocess in the compilation
  sequence.  For C source files, this is the compiler proper and assembler
  (plus the linker if linking is done).

  Without the specification of an output file, the output looks like this:

  .. code-block:: c++

    # cc1 0.12 0.01
    # as 0.00 0.01

  The first number on each line is the 'user time', that is time spent
  executing the program itself.  The second number is 'system time',
  time spent executing operating system routines on behalf of the program.
  Both numbers are in seconds.

  With the specification of an output file, the output is appended to the
  named file, and it looks like this:

  .. code-block:: c++

    0.12 0.01 cc1 ``options``
    0.00 0.01 as ``options``

  The 'user time' and the 'system time' are moved before the program
  name, and the options passed to the program are displayed, so that one
  can later tell what file was being compiled, and with which options.

.. option:: -fvar-tracking

  Run variable tracking pass.  It computes where variables are stored at each
  position in code.  Better debugging information is then generated
  (if the debugging information format supports this information).

  It is enabled by default when compiling with optimization (:option:`-Os`,
  :option:`-O`, :option:`-O2`, ...), debugging information (:option:`-g`) and
  the debug info format supports it.

.. option:: -fvar-tracking-assignments, -fno-var-tracking-assignments

  Annotate assignments to user variables early in the compilation and
  attempt to carry the annotations over throughout the compilation all the
  way to the end, in an attempt to improve debug information while
  optimizing.  Use of :option:`-gdwarf-4` is recommended along with it.

  It can be enabled even if var-tracking is disabled, in which case
  annotations are created and maintained, but discarded at the end.
  By default, this flag is enabled together with :option:`-fvar-tracking`,
  except when selective scheduling is enabled.

.. option:: -fvar-tracking-assignments-toggle, -fno-var-tracking-assignments-toggle

  Toggle :option:`-fvar-tracking-assignments`, in the same way that
  :option:`-gtoggle` toggles :option:`-g`.

.. option:: -print-file-name=library

  Print the full absolute name of the library file ``library`` that
  would be used when linking-and don't do anything else.  With this
  option, GCC does not compile or link anything; it just prints the
  file name.

.. option:: -print-multi-directory

  Print the directory name corresponding to the multilib selected by any
  other switches present in the command line.  This directory is supposed
  to exist in :envvar:`GCC_EXEC_PREFIX`.

.. option:: -print-multi-lib

  Print the mapping from multilib directory names to compiler switches
  that enable them.  The directory name is separated from the switches by
  :samp:`;`, and each switch starts with an :samp:`@` instead of the
  :samp:`-`, without spaces between multiple switches.  This is supposed to
  ease shell processing.

.. option:: -print-multi-os-directory

  Print the path to OS libraries for the selected
  multilib, relative to some lib subdirectory.  If OS libraries are
  present in the lib subdirectory and no multilibs are used, this is
  usually just ., if OS libraries are present in lib``suffix``
  sibling directories this prints e.g. ../lib64, ../lib or
  ../lib32, or if OS libraries are present in lib/``subdir``
  subdirectories it prints e.g. amd64, sparcv9 or ev6.

.. option:: -print-multiarch

  Print the path to OS libraries for the selected multiarch,
  relative to some lib subdirectory.

.. option:: -print-prog-name=program

  Like :option:`-print-file-name`, but searches for a program such as :command:`cpp`.

.. option:: -print-libgcc-file-name

  Same as :option:`-print-file-name=libgcc.a`.

  This is useful when you use :option:`-nostdlib` or :option:`-nodefaultlibs`
  but you do want to link with libgcc.a.  You can do:

  .. code-block:: bash

    gcc -nostdlib ``files``... `gcc -print-libgcc-file-name`

.. option:: -print-search-dirs

  Print the name of the configured installation directory and a list of
  program and library directories :command:`gcc` searches-and don't do anything else.

  This is useful when :command:`gcc` prints the error message
  :samp:`installation problem, cannot exec cpp0: No such file or directory`.
  To resolve this you either need to put cpp0 and the other compiler
  components where :command:`gcc` expects to find them, or you can set the environment
  variable :envvar:`GCC_EXEC_PREFIX` to the directory where you installed them.
  Don't forget the trailing :samp:`/`.
  See :ref:`environment-variables`.

.. option:: -print-sysroot

  Print the target sysroot directory that is used during
  compilation.  This is the target sysroot specified either at configure
  time or using the :option:`--sysroot` option, possibly with an extra
  suffix that depends on compilation options.  If no target sysroot is
  specified, the option prints nothing.

.. option:: -print-sysroot-headers-suffix

  Print the suffix added to the target sysroot when searching for
  headers, or give an error if the compiler is not configured with such
  a suffix-and don't do anything else.

.. option:: -dumpmachine

  Print the compiler's target machine (for example,
  :samp:`i686-pc-linux-gnu`)-and don't do anything else.

.. option:: -dumpversion

  Print the compiler version (for example, ``3.0``)-and don't do
  anything else.

.. option:: -dumpspecs

  Print the compiler's built-in specs-and don't do anything else.  (This
  is used when GCC itself is being built.)  See :ref:`spec-files`.

.. option:: -fno-eliminate-unused-debug-types, -feliminate-unused-debug-types

  Normally, when producing DWARF 2 output, GCC avoids producing debug symbol 
  output for types that are nowhere used in the source file being compiled.
  Sometimes it is useful to have GCC emit debugging
  information for all types declared in a compilation
  unit, regardless of whether or not they are actually used
  in that compilation unit, for example 
  if, in the debugger, you want to cast a value to a type that is
  not actually used in your program (but is declared).  More often,
  however, this results in a significant amount of wasted space.

