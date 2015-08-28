.. _function-attributes:

Declaring Attributes of Functions
*********************************

.. index:: function attributes

.. index:: declaring attributes of functions

.. index:: volatile applied to function

.. index:: const applied to function

In GNU C, you can use function attributes to declare certain things
about functions called in your program which help the compiler
optimize calls and check your code more carefully.  For example, you
can use attributes to declare that a function never returns
(``noreturn``), returns a value depending only on its arguments
(``pure``), or has ``printf``-style arguments (``format``).

You can also use attributes to control memory placement, code
generation options or call/return conventions within the function
being annotated.  Many of these attributes are target-specific.  For
example, many targets support attributes for defining interrupt
handler functions, which typically must follow special register usage
and return conventions.

Function attributes are introduced by the ``__attribute__`` keyword
on a declaration, followed by an attribute specification inside double
parentheses.  You can specify multiple attributes in a declaration by
separating them by commas within the double parentheses or by
immediately following an attribute declaration with another attribute
declaration.  See :ref:`attribute-syntax`, for the exact rules on
attribute syntax and placement.

GCC also supports attributes on
variable declarations (Variable Attributes),
labels (Label Attributes),
and types (Type Attributes).

There is some overlap between the purposes of attributes and pragmas
(PragmasPragmas Accepted by GCC).  It has been
found convenient to use ``__attribute__`` to achieve a natural
attachment of attributes to their corresponding declarations, whereas
``#pragma`` is of use for compatibility with other compilers
or constructs that do not naturally form part of the grammar.

In addition to the attributes documented here,
GCC plugins may provide their own attributes.

.. toctree::

   <common-function-attributes>
   <arc-function-attributes>
   <arm-function-attributes>
   <avr-function-attributes>
   <blackfin-function-attributes>
   <cr16-function-attributes>
   <epiphany-function-attributes>
   <h8-300-function-attributes>
   <ia-64-function-attributes>
   <m32c-function-attributes>
   <m32r-d-function-attributes>
   <m68k-function-attributes>
   <mcore-function-attributes>
   <mep-function-attributes>
   <microblaze-function-attributes>
   <microsoft-windows-function-attributes>
   <mips-function-attributes>
   <msp430-function-attributes>
   <nds32-function-attributes>
   <nios-ii-function-attributes>
   <powerpc-function-attributes>
   <rl78-function-attributes>
   <rx-function-attributes>
   <s-390-function-attributes>
   <sh-function-attributes>
   <spu-function-attributes>
   <symbian-os-function-attributes>
   <visium-function-attributes>
   <x86-function-attributes>
   <xstormy16-function-attributes>

.. _common-function-attributes:

Common Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^

The following attributes are supported on most targets.

.. Keep this table alphabetized by attribute name.  Treat _ as space.

alias ("``target``")

  .. index:: alias function attribute

  The ``alias`` attribute causes the declaration to be emitted as an
  alias for another symbol, which must be specified.  For instance,

  .. code-block:: c++

    void __f () { /* Do something. */; }
    void f () __attribute__ ((weak, alias ("__f")));

  defines f to be a weak alias for __f.  In C++, the
  mangled name for the target must be used.  It is an error if __f
  is not defined in the same translation unit.

  This attribute requires assembler and object file support,
  and may not be available on all targets.

aligned (``alignment``)

  .. index:: aligned function attribute

  This attribute specifies a minimum alignment for the function,
  measured in bytes.

  You cannot use this attribute to decrease the alignment of a function,
  only to increase it.  However, when you explicitly specify a function
  alignment this overrides the effect of the
  :option:`-falign-functions` (Optimize Options) option for this
  function.

  Note that the effectiveness of ``aligned`` attributes may be
  limited by inherent limitations in your linker.  On many systems, the
  linker is only able to arrange for functions to be aligned up to a
  certain maximum alignment.  (For some linkers, the maximum supported
  alignment may be very very small.)  See your linker documentation for
  further information.

  The ``aligned`` attribute can also be used for variables and fields
  (Variable Attributes.)

alloc_align

  .. index:: alloc_align function attribute

  The ``alloc_align`` attribute is used to tell the compiler that the
  function return value points to memory, where the returned pointer minimum
  alignment is given by one of the functions parameters.  GCC uses this
  information to improve pointer alignment analysis.

  The function parameter denoting the allocated alignment is specified by
  one integer argument, whose number is the argument of the attribute.
  Argument numbering starts at one.

  For instance,

  .. code-block:: c++

    void* my_memalign(size_t, size_t) __attribute__((alloc_align(1)))

  declares that ``my_memalign`` returns memory with minimum alignment
  given by parameter 1.

alloc_size

  .. index:: alloc_size function attribute

  The ``alloc_size`` attribute is used to tell the compiler that the
  function return value points to memory, where the size is given by
  one or two of the functions parameters.  GCC uses this
  information to improve the correctness of ``__builtin_object_size``.

  The function parameter(s) denoting the allocated size are specified by
  one or two integer arguments supplied to the attribute.  The allocated size
  is either the value of the single function argument specified or the product
  of the two function arguments specified.  Argument numbering starts at
  one.

  For instance,

  .. code-block:: c++

    void* my_calloc(size_t, size_t) __attribute__((alloc_size(1,2)))
    void* my_realloc(void*, size_t) __attribute__((alloc_size(2)))

  declares that ``my_calloc`` returns memory of the size given by
  the product of parameter 1 and 2 and that ``my_realloc`` returns memory
  of the size given by parameter 2.

always_inline

  .. index:: always_inline function attribute

  Generally, functions are not inlined unless optimization is specified.
  For functions declared inline, this attribute inlines the function
  independent of any restrictions that otherwise apply to inlining.
  Failure to inline such a function is diagnosed as an error.
  Note that if such a function is called indirectly the compiler may
  or may not inline it depending on optimization level and a failure
  to inline an indirect call may or may not be diagnosed.

artificial

  .. index:: artificial function attribute

  This attribute is useful for small inline wrappers that if possible
  should appear during debugging as a unit.  Depending on the debug
  info format it either means marking the function as artificial
  or using the caller location for all instructions within the inlined
  body.

assume_aligned

  .. index:: assume_aligned function attribute

  The ``assume_aligned`` attribute is used to tell the compiler that the
  function return value points to memory, where the returned pointer minimum
  alignment is given by the first argument.
  If the attribute has two arguments, the second argument is misalignment offset.

  For instance

  .. code-block:: c++

    void* my_alloc1(size_t) __attribute__((assume_aligned(16)))
    void* my_alloc2(size_t) __attribute__((assume_aligned(32, 8)))

  declares that ``my_alloc1`` returns 16-byte aligned pointer and
  that ``my_alloc2`` returns a pointer whose value modulo 32 is equal
  to 8.

bnd_instrument

  .. index:: bnd_instrument function attribute

  The ``bnd_instrument`` attribute on functions is used to inform the
  compiler that the function should be instrumented when compiled
  with the :option:`-fchkp-instrument-marked-only` option.

bnd_legacy

  .. index:: bnd_legacy function attribute

  .. index:: Pointer Bounds Checker attributes

  The ``bnd_legacy`` attribute on functions is used to inform the
  compiler that the function should not be instrumented when compiled
  with the :option:`-fcheck-pointer-bounds` option.

cold

  .. index:: cold function attribute

  The ``cold`` attribute on functions is used to inform the compiler that
  the function is unlikely to be executed.  The function is optimized for
  size rather than speed and on many targets it is placed into a special
  subsection of the text section so all cold functions appear close together,
  improving code locality of non-cold parts of program.  The paths leading
  to calls of cold functions within code are marked as unlikely by the branch
  prediction mechanism.  It is thus useful to mark functions used to handle
  unlikely conditions, such as ``perror``, as cold to improve optimization
  of hot functions that do call marked functions in rare occasions.

  When profile feedback is available, via :option:`-fprofile-use`, cold functions
  are automatically detected and this attribute is ignored.

const

  .. index:: const function attribute

  .. index:: functions that have no side effects

  Many functions do not examine any values except their arguments, and
  have no effects except the return value.  Basically this is just slightly
  more strict class than the ``pure`` attribute below, since function is not
  allowed to read global memory.

  .. index:: pointer arguments

  Note that a function that has pointer arguments and examines the data
  pointed to must not be declared ``const``.  Likewise, a
  function that calls a non-``const`` function usually must not be
  ``const``.  It does not make sense for a ``const`` function to
  return ``void``.

constructor destructor constructor (``priority``) destructor (``priority``)

  .. index:: constructor function attribute

  .. index:: destructor function attribute

  The ``constructor`` attribute causes the function to be called
  automatically before execution enters ``main ()``.  Similarly, the
  ``destructor`` attribute causes the function to be called
  automatically after ``main ()`` completes or ``exit ()`` is
  called.  Functions with these attributes are useful for
  initializing data that is used implicitly during the execution of
  the program.

  You may provide an optional integer priority to control the order in
  which constructor and destructor functions are run.  A constructor
  with a smaller priority number runs before a constructor with a larger
  priority number; the opposite relationship holds for destructors.  So,
  if you have a constructor that allocates a resource and a destructor
  that deallocates the same resource, both functions typically have the
  same priority.  The priorities for constructor and destructor
  functions are the same as those specified for namespace-scope C++
  objects (C++ Attributes).

  These attributes are not currently implemented for Objective-C.

deprecated deprecated (``msg``)

  .. index:: deprecated function attribute

  The ``deprecated`` attribute results in a warning if the function
  is used anywhere in the source file.  This is useful when identifying
  functions that are expected to be removed in a future version of a
  program.  The warning also includes the location of the declaration
  of the deprecated function, to enable users to easily find further
  information about why the function is deprecated, or what they should
  do instead.  Note that the warnings only occurs for uses:

  .. code-block:: c++

    int old_fn () __attribute__ ((deprecated));
    int old_fn ();
    int (*fn_ptr)() = old_fn;

  results in a warning on line 3 but not line 2.  The optional ``msg``
  argument, which must be a string, is printed in the warning if
  present.

  The ``deprecated`` attribute can also be used for variables and
  types (Variable Attributes, Type Attributes.)

error ("``message``") warning ("``message``")

  .. index:: error function attribute

  .. index:: warning function attribute

  If the ``error`` or ``warning`` attribute 
  is used on a function declaration and a call to such a function
  is not eliminated through dead code elimination or other optimizations, 
  an error or warning (respectively) that includes ``message`` is diagnosed.  
  This is useful
  for compile-time checking, especially together with ``__builtin_constant_p``
  and inline functions where checking the inline function arguments is not
  possible through ``extern char [(condition) ? 1 : -1];`` tricks.

  While it is possible to leave the function undefined and thus invoke
  a link failure (to define the function with
  a message in ``.gnu.warning*`` section),
  when using these attributes the problem is diagnosed
  earlier and with exact location of the call even in presence of inline
  functions or when not emitting debugging information.

externally_visible

  .. index:: externally_visible function attribute

  This attribute, attached to a global variable or function, nullifies
  the effect of the :option:`-fwhole-program` command-line option, so the
  object remains visible outside the current compilation unit.

  If :option:`-fwhole-program` is used together with :option:`-flto` and 
  :command:`gold` is used as the linker plugin, 
  ``externally_visible`` attributes are automatically added to functions 
  (not variable yet due to a current :command:`gold` issue) 
  that are accessed outside of LTO objects according to resolution file
  produced by :command:`gold`.
  For other linkers that cannot generate resolution file,
  explicit ``externally_visible`` attributes are still necessary.

flatten

  .. index:: flatten function attribute

  Generally, inlining into a function is limited.  For a function marked with
  this attribute, every call inside this function is inlined, if possible.
  Whether the function itself is considered for inlining depends on its size and
  the current inlining parameters.

.. option:: format (archetype, string-index, first-to-check), -Wformat, -ffreestanding, -fno-builtin

  .. index:: format function attribute

  .. index:: functions with printf, scanf, strftime or strfmon style arguments

  The ``format`` attribute specifies that a function takes ``printf``,
  ``scanf``, ``strftime`` or ``strfmon`` style arguments that
  should be type-checked against a format string.  For example, the
  declaration:

  .. code-block:: c++

    extern int
    my_printf (void *my_object, const char *my_format, ...)
          __attribute__ ((format (printf, 2, 3)));

  causes the compiler to check the arguments in calls to ``my_printf``
  for consistency with the ``printf`` style format string argument
  ``my_format``.

  The parameter ``archetype`` determines how the format string is
  interpreted, and should be ``printf``, ``scanf``, ``strftime``,
  ``gnu_printf``, ``gnu_scanf``, ``gnu_strftime`` or
  ``strfmon``.  (You can also use ``__printf__``,
  ``__scanf__``, ``__strftime__`` or ``__strfmon__``.)  On
  MinGW targets, ``ms_printf``, ``ms_scanf``, and
  ``ms_strftime`` are also present.
  ``archetype`` values such as ``printf`` refer to the formats accepted
  by the system's C runtime library,
  while values prefixed with gnu_ always refer
  to the formats accepted by the GNU C Library.  On Microsoft Windows
  targets, values prefixed with ms_ refer to the formats accepted by the
  msvcrt.dll library.
  The parameter ``string-index``
  specifies which argument is the format string argument (starting
  from 1), while ``first-to-check`` is the number of the first
  argument to check against the format string.  For functions
  where the arguments are not available to be checked (such as
  ``vprintf``), specify the third parameter as zero.  In this case the
  compiler only checks the format string for consistency.  For
  ``strftime`` formats, the third parameter is required to be zero.
  Since non-static C++ methods have an implicit ``this`` argument, the
  arguments of such methods should be counted from two, not one, when
  giving values for ``string-index`` and ``first-to-check``.

  In the example above, the format string (``my_format``) is the second
  argument of the function ``my_print``, and the arguments to check
  start with the third argument, so the correct parameters for the format
  attribute are 2 and 3.

  The ``format`` attribute allows you to identify your own functions
  that take format strings as arguments, so that GCC can check the
  calls to these functions for errors.  The compiler always (unless
  :option:`-ffreestanding` or :option:`-fno-builtin` is used) checks formats
  for the standard library functions ``printf``, ``fprintf``,
  ``sprintf``, ``scanf``, ``fscanf``, ``sscanf``, ``strftime``,
  ``vprintf``, ``vfprintf`` and ``vsprintf`` whenever such
  warnings are requested (using :option:`-Wformat`), so there is no need to
  modify the header file stdio.h.  In C99 mode, the functions
  ``snprintf``, ``vsnprintf``, ``vscanf``, ``vfscanf`` and
  ``vsscanf`` are also checked.  Except in strictly conforming C
  standard modes, the X/Open function ``strfmon`` is also checked as
  are ``printf_unlocked`` and ``fprintf_unlocked``.
  See :ref:`Options Controlling C Dialect <c-dialect-options>`.

  For Objective-C dialects, ``NSString`` (or ``__NSString__``) is
  recognized in the same context.  Declarations including these format attributes
  are parsed for correct syntax, however the result of checking of such format
  strings is not yet defined, and is not carried out by this version of the
  compiler.

  The target may also provide additional types of format checks.
  See :ref:`Format Checks Specific to Particular
  Target Machines <target-format-checks>`.

.. option:: format_arg (string-index), -Wformat-nonliteral

  .. index:: format_arg function attribute

  The ``format_arg`` attribute specifies that a function takes a format
  string for a ``printf``, ``scanf``, ``strftime`` or
  ``strfmon`` style function and modifies it (for example, to translate
  it into another language), so the result can be passed to a
  ``printf``, ``scanf``, ``strftime`` or ``strfmon`` style
  function (with the remaining arguments to the format function the same
  as they would have been for the unmodified string).  For example, the
  declaration:

  .. code-block:: c++

    extern char *
    my_dgettext (char *my_domain, const char *my_format)
          __attribute__ ((format_arg (2)));

  causes the compiler to check the arguments in calls to a ``printf``,
  ``scanf``, ``strftime`` or ``strfmon`` type function, whose
  format string argument is a call to the ``my_dgettext`` function, for
  consistency with the format string argument ``my_format``.  If the
  ``format_arg`` attribute had not been specified, all the compiler
  could tell in such calls to format functions would be that the format
  string argument is not constant; this would generate a warning when
  :option:`-Wformat-nonliteral` is used, but the calls could not be checked
  without the attribute.

  The parameter ``string-index`` specifies which argument is the format
  string argument (starting from one).  Since non-static C++ methods have
  an implicit ``this`` argument, the arguments of such methods should
  be counted from two.

  The ``format_arg`` attribute allows you to identify your own
  functions that modify format strings, so that GCC can check the
  calls to ``printf``, ``scanf``, ``strftime`` or ``strfmon``
  type function whose operands are a call to one of your own function.
  The compiler always treats ``gettext``, ``dgettext``, and
  ``dcgettext`` in this manner except when strict ISO C support is
  requested by :option:`-ansi` or an appropriate :option:`-std` option, or
  :option:`-ffreestanding` or :option:`-fno-builtin`
  is used.  See :ref:`Options
  Controlling C Dialect <c-dialect-options>`.

  For Objective-C dialects, the ``format-arg`` attribute may refer to an
  ``NSString`` reference for compatibility with the ``format`` attribute
  above.

  The target may also allow additional types in ``format-arg`` attributes.
  See :ref:`Format Checks Specific to Particular
  Target Machines <target-format-checks>`.

gnu_inline

  .. index:: gnu_inline function attribute

  This attribute should be used with a function that is also declared
  with the ``inline`` keyword.  It directs GCC to treat the function
  as if it were defined in gnu90 mode even when compiling in C99 or
  gnu99 mode.

  If the function is declared ``extern``, then this definition of the
  function is used only for inlining.  In no case is the function
  compiled as a standalone function, not even if you take its address
  explicitly.  Such an address becomes an external reference, as if you
  had only declared the function, and had not defined it.  This has
  almost the effect of a macro.  The way to use this is to put a
  function definition in a header file with this attribute, and put
  another copy of the function, without ``extern``, in a library
  file.  The definition in the header file causes most calls to the
  function to be inlined.  If any uses of the function remain, they
  refer to the single copy in the library.  Note that the two
  definitions of the functions need not be precisely the same, although
  if they do not have the same effect your program may behave oddly.

  In C, if the function is neither ``extern`` nor ``static``, then
  the function is compiled as a standalone function, as well as being
  inlined where possible.

  This is how GCC traditionally handled functions declared
  ``inline``.  Since ISO C99 specifies a different semantics for
  ``inline``, this function attribute is provided as a transition
  measure and as a useful feature in its own right.  This attribute is
  available in GCC 4.1.3 and later.  It is available if either of the
  preprocessor macros ``__GNUC_GNU_INLINE__`` or
  ``__GNUC_STDC_INLINE__`` are defined.  See :ref:`An Inline
  Function is As Fast As a Macro <inline>`.

  In C++, this attribute does not depend on ``extern`` in any way,
  but it still requires the ``inline`` keyword to enable its special
  behavior.

hot

  .. index:: hot function attribute

  The ``hot`` attribute on a function is used to inform the compiler that
  the function is a hot spot of the compiled program.  The function is
  optimized more aggressively and on many targets it is placed into a special
  subsection of the text section so all hot functions appear close together,
  improving locality.

  When profile feedback is available, via :option:`-fprofile-use`, hot functions
  are automatically detected and this attribute is ignored.

ifunc ("``resolver``")

  .. index:: ifunc function attribute

  .. index:: indirect functions

  .. index:: functions that are dynamically resolved

  The ``ifunc`` attribute is used to mark a function as an indirect
  function using the STT_GNU_IFUNC symbol type extension to the ELF
  standard.  This allows the resolution of the symbol value to be
  determined dynamically at load time, and an optimized version of the
  routine can be selected for the particular processor or other system
  characteristics determined then.  To use this attribute, first define
  the implementation functions available, and a resolver function that
  returns a pointer to the selected implementation function.  The
  implementation functions' declarations must match the API of the
  function being implemented, the resolver's declaration is be a
  function returning pointer to void function returning void:

  .. code-block:: c++

    void *my_memcpy (void *dst, const void *src, size_t len)
    {
      ...
    }

    static void (*resolve_memcpy (void)) (void)
    {
      return my_memcpy; // we'll just always select this routine
    }

  The exported header file declaring the function the user calls would
  contain:

  .. code-block:: c++

    extern void *memcpy (void *, const void *, size_t);

  allowing the user to call this as a regular function, unaware of the
  implementation.  Finally, the indirect function needs to be defined in
  the same translation unit as the resolver function:

  .. code-block:: c++

    void *memcpy (void *, const void *, size_t)
         __attribute__ ((ifunc ("resolve_memcpy")));

  Indirect functions cannot be weak.  Binutils version 2.20.1 or higher
  and GNU C Library version 2.11.1 are required to use this feature.

interrupt interrupt_handler
  Many GCC back ends support attributes to indicate that a function is
  an interrupt handler, which tells the compiler to generate function
  entry and exit sequences that differ from those from regular
  functions.  The exact syntax and behavior are target-specific;
  refer to the following subsections for details.

leaf

  .. index:: leaf function attribute

  Calls to external functions with this attribute must return to the current
  compilation unit only by return or by exception handling.  In particular, leaf
  functions are not allowed to call callback function passed to it from the current
  compilation unit or directly call functions exported by the unit or longjmp
  into the unit.  Leaf function might still call functions from other compilation
  units and thus they are not necessarily leaf in the sense that they contain no
  function calls at all.

  The attribute is intended for library functions to improve dataflow analysis.
  The compiler takes the hint that any data not escaping the current compilation unit can
  not be used or modified by the leaf function.  For example, the ``sin`` function
  is a leaf function, but ``qsort`` is not.

  Note that leaf functions might invoke signals and signal handlers might be
  defined in the current compilation unit and use static variables.  The only
  compliant way to write such a signal handler is to declare such variables
  ``volatile``.

  The attribute has no effect on functions defined within the current compilation
  unit.  This is to allow easy merging of multiple compilation units into one,
  for example, by using the link-time optimization.  For this reason the
  attribute is not allowed on types to annotate indirect calls.

malloc

  .. index:: malloc function attribute

  .. index:: functions that behave like malloc

  This tells the compiler that a function is ``malloc``-like, i.e.,
  that the pointer ``P`` returned by the function cannot alias any
  other pointer valid when the function returns, and moreover no
  pointers to valid objects occur in any storage addressed by ``P``.

  Using this attribute can improve optimization.  Functions like
  ``malloc`` and ``calloc`` have this property because they return
  a pointer to uninitialized or zeroed-out storage.  However, functions
  like ``realloc`` do not have this property, as they can return a
  pointer to storage containing pointers.

no_icf

  .. index:: no_icf function attribute

  This function attribute prevents a functions from being merged with another
  semantically equivalent function.

.. option:: no_instrument_function, -finstrument-functions

  .. index:: no_instrument_function function attribute

  If :option:`-finstrument-functions` is given, profiling function calls are
  generated at entry and exit of most user-compiled functions.
  Functions with this attribute are not so instrumented.

no_reorder

  .. index:: no_reorder function attribute

  Do not reorder functions or variables marked ``no_reorder``
  against each other or top level assembler statements the executable.
  The actual order in the program will depend on the linker command
  line. Static variables marked like this are also not removed.
  This has a similar effect
  as the :option:`-fno-toplevel-reorder` option, but only applies to the
  marked symbols.

no_sanitize_address no_address_safety_analysis

  .. index:: no_sanitize_address function attribute

  The ``no_sanitize_address`` attribute on functions is used
  to inform the compiler that it should not instrument memory accesses
  in the function when compiling with the :option:`-fsanitize=address` option.
  The ``no_address_safety_analysis`` is a deprecated alias of the
  ``no_sanitize_address`` attribute, new code should use
  ``no_sanitize_address``.

no_sanitize_thread

  .. index:: no_sanitize_thread function attribute

  The ``no_sanitize_thread`` attribute on functions is used
  to inform the compiler that it should not instrument memory accesses
  in the function when compiling with the :option:`-fsanitize=thread` option.

no_sanitize_undefined

  .. index:: no_sanitize_undefined function attribute

  The ``no_sanitize_undefined`` attribute on functions is used
  to inform the compiler that it should not check for undefined behavior
  in the function when compiling with the :option:`-fsanitize=undefined` option.

.. option:: no_split_stack, -fsplit-stack

  .. index:: no_split_stack function attribute

  If :option:`-fsplit-stack` is given, functions have a small
  prologue which decides whether to split the stack.  Functions with the
  ``no_split_stack`` attribute do not have that prologue, and thus
  may run with only a small amount of stack space available.

noclone

  .. index:: noclone function attribute

  This function attribute prevents a function from being considered for
  cloning-a mechanism that produces specialized copies of functions
  and which is (currently) performed by interprocedural constant
  propagation.

noinline

  .. index:: noinline function attribute

  This function attribute prevents a function from being considered for
  inlining.

  .. Don't enumerate the optimizations by name here; we try to be

  .. future-compatible with this mechanism.

  If the function does not have side-effects, there are optimizations
  other than inlining that cause function calls to be optimized away,
  although the function call is live.  To keep such calls from being
  optimized away, put

  .. code-block:: c++

    asm ("");

  (Extended Asm) in the called function, to serve as a special
  side-effect.

nonnull (``arg-index``, ...)

  .. index:: nonnull function attribute

  .. index:: functions with non-null pointer arguments

  The ``nonnull`` attribute specifies that some function parameters should
  be non-null pointers.  For instance, the declaration:

  .. code-block:: c++

    extern void *
    my_memcpy (void *dest, const void *src, size_t len)
            __attribute__((nonnull (1, 2)));

  causes the compiler to check that, in calls to ``my_memcpy``,
  arguments ``dest`` and ``src`` are non-null.  If the compiler
  determines that a null pointer is passed in an argument slot marked
  as non-null, and the :option:`-Wnonnull` option is enabled, a warning
  is issued.  The compiler may also choose to make optimizations based
  on the knowledge that certain function arguments will never be null.

  If no argument index list is given to the ``nonnull`` attribute,
  all pointer arguments are marked as non-null.  To illustrate, the
  following declaration is equivalent to the previous example:

  .. code-block:: c++

    extern void *
    my_memcpy (void *dest, const void *src, size_t len)
            __attribute__((nonnull));

noreturn

  .. index:: noreturn function attribute

  .. index:: functions that never return

  A few standard library functions, such as ``abort`` and ``exit``,
  cannot return.  GCC knows this automatically.  Some programs define
  their own functions that never return.  You can declare them
  ``noreturn`` to tell the compiler this fact.  For example,

  .. code-block:: c++

    void fatal () __attribute__ ((noreturn));

    void
    fatal (/* ... */)
    {
      /* ... */ /* Print error message. */ /* ... */
      exit (1);
    }

  The ``noreturn`` keyword tells the compiler to assume that
  ``fatal`` cannot return.  It can then optimize without regard to what
  would happen if ``fatal`` ever did return.  This makes slightly
  better code.  More importantly, it helps avoid spurious warnings of
  uninitialized variables.

  The ``noreturn`` keyword does not affect the exceptional path when that
  applies: a ``noreturn``-marked function may still return to the caller
  by throwing an exception or calling ``longjmp``.

  Do not assume that registers saved by the calling function are
  restored before calling the ``noreturn`` function.

  It does not make sense for a ``noreturn`` function to have a return
  type other than ``void``.

nothrow

  .. index:: nothrow function attribute

  The ``nothrow`` attribute is used to inform the compiler that a
  function cannot throw an exception.  For example, most functions in
  the standard C library can be guaranteed not to throw an exception
  with the notable exceptions of ``qsort`` and ``bsearch`` that
  take function pointer arguments.

optimize

  .. index:: optimize function attribute

  The ``optimize`` attribute is used to specify that a function is to
  be compiled with different optimization options than specified on the
  command line.  Arguments can either be numbers or strings.  Numbers
  are assumed to be an optimization level.  Strings that begin with
  ``O`` are assumed to be an optimization option, while other options
  are assumed to be used with a ``-f`` prefix.  You can also use the
  #pragma GCC optimize pragma to set the optimization options
  that affect more than one function.
  See :ref:`function-specific-option-pragmas`, for details about the
  #pragma GCC optimize pragma.

  This can be used for instance to have frequently-executed functions
  compiled with more aggressive optimization options that produce faster
  and larger code, while other functions can be compiled with less
  aggressive options.

pure

  .. index:: pure function attribute

  .. index:: functions that have no side effects

  Many functions have no effects except the return value and their
  return value depends only on the parameters and/or global variables.
  Such a function can be subject
  to common subexpression elimination and loop optimization just as an
  arithmetic operator would be.  These functions should be declared
  with the attribute ``pure``.  For example,

  .. code-block:: c++

    int square (int) __attribute__ ((pure));

  says that the hypothetical function ``square`` is safe to call
  fewer times than the program says.

  Some of common examples of pure functions are ``strlen`` or ``memcmp``.
  Interesting non-pure functions are functions with infinite loops or those
  depending on volatile memory or other system resource, that may change between
  two consecutive calls (such as ``feof`` in a multithreading environment).

returns_nonnull

  .. index:: returns_nonnull function attribute

  The ``returns_nonnull`` attribute specifies that the function
  return value should be a non-null pointer.  For instance, the declaration:

  .. code-block:: c++

    extern void *
    mymalloc (size_t len) __attribute__((returns_nonnull));

  lets the compiler optimize callers based on the knowledge
  that the return value will never be null.

returns_twice

  .. index:: returns_twice function attribute

  .. index:: functions that return more than once

  The ``returns_twice`` attribute tells the compiler that a function may
  return more than one time.  The compiler ensures that all registers
  are dead before calling such a function and emits a warning about
  the variables that may be clobbered after the second return from the
  function.  Examples of such functions are ``setjmp`` and ``vfork``.
  The ``longjmp``-like counterpart of such function, if any, might need
  to be marked with the ``noreturn`` attribute.

section ("``section-name``")

  .. index:: section function attribute

  .. index:: functions in arbitrary sections

  Normally, the compiler places the code it generates in the ``text`` section.
  Sometimes, however, you need additional sections, or you need certain
  particular functions to appear in special sections.  The ``section``
  attribute specifies that a function lives in a particular section.
  For example, the declaration:

  .. code-block:: c++

    extern void foobar (void) __attribute__ ((section ("bar")));

  puts the function ``foobar`` in the ``bar`` section.

  Some file formats do not support arbitrary sections so the ``section``
  attribute is not available on all platforms.
  If you need to map the entire contents of a module to a particular
  section, consider using the facilities of the linker instead.

sentinel

  .. index:: sentinel function attribute

  This function attribute ensures that a parameter in a function call is
  an explicit ``NULL``.  The attribute is only valid on variadic
  functions.  By default, the sentinel is located at position zero, the
  last parameter of the function call.  If an optional integer position
  argument P is supplied to the attribute, the sentinel must be located at
  position P counting backwards from the end of the argument list.

  .. code-block:: c++

    __attribute__ ((sentinel))
    is equivalent to
    __attribute__ ((sentinel(0)))

  The attribute is automatically set with a position of 0 for the built-in
  functions ``execl`` and ``execlp``.  The built-in function
  ``execle`` has the attribute set with a position of 1.

  A valid ``NULL`` in this context is defined as zero with any pointer
  type.  If your system defines the ``NULL`` macro with an integer type
  then you need to add an explicit cast.  GCC replaces ``stddef.h``
  with a copy that redefines NULL appropriately.

  The warnings for missing or incorrect sentinels are enabled with
  :option:`-Wformat`.

stack_protect

  .. index:: stack_protect function attribute

  This function attribute make a stack protection of the function if 
  flags fstack-protector or fstack-protector-strong
  or fstack-protector-explicit are set.

target (``options``)

  .. index:: target function attribute

  Multiple target back ends implement the ``target`` attribute
  to specify that a function is to
  be compiled with different target options than specified on the
  command line.  This can be used for instance to have functions
  compiled with a different ISA (instruction set architecture) than the
  default.  You can also use the #pragma GCC target pragma to set
  more than one function to be compiled with specific target options.
  See :ref:`function-specific-option-pragmas`, for details about the
  #pragma GCC target pragma.

  For instance, on an x86, you could declare one function with the
  ``target("sse4.1,arch=core2")`` attribute and another with
  ``target("sse4a,arch=amdfam10")``.  This is equivalent to
  compiling the first function with :option:`-msse4.1` and
  :option:`-march=core2` options, and the second function with
  :option:`-msse4a` and :option:`-march=amdfam10` options.  It is up to you
  to make sure that a function is only invoked on a machine that
  supports the particular ISA it is compiled for (for example by using
  ``cpuid`` on x86 to determine what feature bits and architecture
  family are used).

  .. code-block:: c++

    int core2_func (void) __attribute__ ((__target__ ("arch=core2")));
    int sse3_func (void) __attribute__ ((__target__ ("sse3")));

  You can either use multiple
  strings separated by commas to specify multiple options,
  or separate the options with a comma (,) within a single string.

  The options supported are specific to each target; refer to x86
  Function Attributes, PowerPC Function Attributes, and
  Nios II Function Attributes, for details.

unused

  .. index:: unused function attribute

  This attribute, attached to a function, means that the function is meant
  to be possibly unused.  GCC does not produce a warning for this
  function.

used

  .. index:: used function attribute

  This attribute, attached to a function, means that code must be emitted
  for the function even if it appears that the function is not referenced.
  This is useful, for example, when the function is referenced only in
  inline assembly.

  When applied to a member function of a C++ class template, the
  attribute also means that the function is instantiated if the
  class itself is instantiated.

visibility ("``visibility_type``")

  .. index:: visibility function attribute

  This attribute affects the linkage of the declaration to which it is attached.
  There are four supported ``visibility_type`` values: default,
  hidden, protected or internal visibility.

  .. code-block:: c++

    void __attribute__ ((visibility ("protected")))
    f () { /* Do something. */; }
    int i __attribute__ ((visibility ("hidden")));

  The possible values of ``visibility_type`` correspond to the
  visibility settings in the ELF gABI.

  .. keep this list of visibilities in alphabetical order.

  default
    Default visibility is the normal case for the object file format.
    This value is available for the visibility attribute to override other
    options that may change the assumed visibility of entities.

    On ELF, default visibility means that the declaration is visible to other
    modules and, in shared libraries, means that the declared entity may be
    overridden.

    On Darwin, default visibility means that the declaration is visible to
    other modules.

    Default visibility corresponds to 'external linkage' in the language.

  hidden
    Hidden visibility indicates that the entity declared has a new
    form of linkage, which we call 'hidden linkage'.  Two
    declarations of an object with hidden linkage refer to the same object
    if they are in the same shared object.

  internal
    Internal visibility is like hidden visibility, but with additional
    processor specific semantics.  Unless otherwise specified by the
    psABI, GCC defines internal visibility to mean that a function is
    never called from another module.  Compare this with hidden
    functions which, while they cannot be referenced directly by other
    modules, can be referenced indirectly via function pointers.  By
    indicating that a function cannot be called from outside the module,
    GCC may for instance omit the load of a PIC register since it is known
    that the calling function loaded the correct value.

  protected
    Protected visibility is like default visibility except that it
    indicates that references within the defining module bind to the
    definition in that module.  That is, the declared entity cannot be
    overridden by another module.

    All visibilities are supported on many, but not all, ELF targets
  (supported when the assembler supports the .visibility
  pseudo-op).  Default visibility is supported everywhere.  Hidden
  visibility is supported on Darwin targets.

  The visibility attribute should be applied only to declarations that
  would otherwise have external linkage.  The attribute should be applied
  consistently, so that the same entity should not be declared with
  different settings of the attribute.

  In C++, the visibility attribute applies to types as well as functions
  and objects, because in C++ types have linkage.  A class must not have
  greater visibility than its non-static data member types and bases,
  and class members default to the visibility of their class.  Also, a
  declaration without explicit visibility is limited to the visibility
  of its type.

  In C++, you can mark member functions and static member variables of a
  class with the visibility attribute.  This is useful if you know a
  particular method or static member variable should only be used from
  one shared object; then you can mark it hidden while the rest of the
  class has default visibility.  Care must be taken to avoid breaking
  the One Definition Rule; for example, it is usually not useful to mark
  an inline method as hidden without marking the whole class as hidden.

  A C++ namespace declaration can also have the visibility attribute.

  .. code-block:: c++

    namespace nspace1 __attribute__ ((visibility ("protected")))
    { /* Do something. */; }

  This attribute applies only to the particular namespace body, not to
  other definitions of the same namespace; it is equivalent to using
  #pragma GCC visibility before and after the namespace
  definition (Visibility Pragmas).

  In C++, if a template argument has limited visibility, this
  restriction is implicitly propagated to the template instantiation.
  Otherwise, template instantiations and specializations default to the
  visibility of their template.

  If both the template and enclosing class have explicit visibility, the
  visibility from the template is used.

warn_unused_result

  .. index:: warn_unused_result function attribute

  The ``warn_unused_result`` attribute causes a warning to be emitted
  if a caller of the function with this attribute does not use its
  return value.  This is useful for functions where not checking
  the result is either a security problem or always a bug, such as
  ``realloc``.

  .. code-block:: c++

    int fn () __attribute__ ((warn_unused_result));
    int foo ()
    {
      if (fn () < 0) return -1;
      fn ();
      return 0;
    }

  results in warning on line 5.

weak

  .. index:: weak function attribute

  The ``weak`` attribute causes the declaration to be emitted as a weak
  symbol rather than a global.  This is primarily useful in defining
  library functions that can be overridden in user code, though it can
  also be used with non-function declarations.  Weak symbols are supported
  for ELF targets, and also for a.out targets when using the GNU assembler
  and linker.

weakref weakref ("``target``")

  .. index:: weakref function attribute

  The ``weakref`` attribute marks a declaration as a weak reference.
  Without arguments, it should be accompanied by an ``alias`` attribute
  naming the target symbol.  Optionally, the ``target`` may be given as
  an argument to ``weakref`` itself.  In either case, ``weakref``
  implicitly marks the declaration as ``weak``.  Without a
  ``target``, given as an argument to ``weakref`` or to ``alias``,
  ``weakref`` is equivalent to ``weak``.

  .. code-block:: c++

    static int x() __attribute__ ((weakref ("y")));
    /* is equivalent to... */
    static int x() __attribute__ ((weak, weakref, alias ("y")));
    /* and to... */
    static int x() __attribute__ ((weakref));
    static int x() __attribute__ ((alias ("y")));

  A weak reference is an alias that does not by itself require a
  definition to be given for the target symbol.  If the target symbol is
  only referenced through weak references, then it becomes a ``weak``
  undefined symbol.  If it is directly referenced, however, then such
  strong references prevail, and a definition is required for the
  symbol, not necessarily in the same translation unit.

  The effect is equivalent to moving all references to the alias to a
  separate translation unit, renaming the alias to the aliased symbol,
  declaring it as weak, compiling the two separate translation units and
  performing a reloadable link on them.

  At present, a declaration to which ``weakref`` is attached can
  only be ``static``.

lower upper either

  .. index:: lower memory region on the MSP430

  .. index:: upper memory region on the MSP430

  .. index:: either memory region on the MSP430

  On the MSP430 target these attributes can be used to specify whether
  the function or variable should be placed into low memory, high
  memory, or the placement should be left to the linker to decide.  The
  attributes are only significant if compiling for the MSP430X
  architecture.

  The attributes work in conjunction with a linker script that has been
  augmented to specify where to place sections with a ``.lower`` and
  a ``.upper`` prefix.  So for example as well as placing the
  ``.data`` section the script would also specify the placement of a
  ``.lower.data`` and a ``.upper.data`` section.  The intention
  being that ``lower`` sections are placed into a small but easier to
  access memory region and the upper sections are placed into a larger, but
  slower to access region.

  The ``either`` attribute is special.  It tells the linker to place
  the object into the corresponding ``lower`` section if there is
  room for it.  If there is insufficient room then the object is placed
  into the corresponding ``upper`` section instead.  Note - the
  placement algorithm is not very sophisticated.  It will not attempt to
  find an optimal packing of the ``lower`` sections.  It just makes
  one pass over the objects and does the best that it can.  Using the
  :option:`-ffunction-sections` and :option:`-fdata-sections` command line
  options can help the packing however, since they produce smaller,
  easier to pack regions.

.. This is the end of the target-independent attribute table

.. _arc-function-attributes:

ARC Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the ARC back end:

interrupt

  .. index:: interrupt function attribute, ARC

  Use this attribute to indicate
  that the specified function is an interrupt handler.  The compiler generates
  function entry and exit sequences suitable for use in an interrupt handler
  when this attribute is present.

  On the ARC, you must specify the kind of interrupt to be handled
  in a parameter to the interrupt attribute like this:

  .. code-block:: c++

    void f () __attribute__ ((interrupt ("ilink1")));

  Permissible values for this parameter are: ``ilink1`` and
  ``ilink2``.

long_call medium_call short_call

  .. index:: long_call function attribute, ARC

  .. index:: medium_call function attribute, ARC

  .. index:: short_call function attribute, ARC

  .. index:: indirect calls, ARC

  These attributes specify how a particular function is called.
  These attributes override the
  :option:`-mlong-calls` and :option:`-mmedium-calls` (ARC Options)
  command-line switches and ``#pragma long_calls`` settings.

  For ARC, a function marked with the ``long_call`` attribute is
  always called using register-indirect jump-and-link instructions,
  thereby enabling the called function to be placed anywhere within the
  32-bit address space.  A function marked with the ``medium_call``
  attribute will always be close enough to be called with an unconditional
  branch-and-link instruction, which has a 25-bit offset from
  the call site.  A function marked with the ``short_call``
  attribute will always be close enough to be called with a conditional
  branch-and-link instruction, which has a 21-bit offset from
  the call site.

  .. _arm-function-attributes:

ARM Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported for ARM targets:

interrupt

  .. index:: interrupt function attribute, ARM

  Use this attribute to indicate
  that the specified function is an interrupt handler.  The compiler generates
  function entry and exit sequences suitable for use in an interrupt handler
  when this attribute is present.

  You can specify the kind of interrupt to be handled by
  adding an optional parameter to the interrupt attribute like this:

  .. code-block:: c++

    void f () __attribute__ ((interrupt ("IRQ")));

  Permissible values for this parameter are: ``IRQ``, ``FIQ``,
  ``SWI``, ``ABORT`` and ``UNDEF``.

  On ARMv7-M the interrupt type is ignored, and the attribute means the function
  may be called with a word-aligned stack pointer.

isr

  .. index:: isr function attribute, ARM

  Use this attribute on ARM to write Interrupt Service Routines. This is an
  alias to the ``interrupt`` attribute above.

long_call short_call

  .. index:: long_call function attribute, ARM

  .. index:: short_call function attribute, ARM

  .. index:: indirect calls, ARM

  These attributes specify how a particular function is called.
  These attributes override the
  :option:`-mlong-calls` (ARM Options)
  command-line switch and ``#pragma long_calls`` settings.  For ARM, the
  ``long_call`` attribute indicates that the function might be far
  away from the call site and require a different (more expensive)
  calling sequence.   The ``short_call`` attribute always places
  the offset to the function from the call site into the BL
  instruction directly.

naked

  .. index:: naked function attribute, ARM

  This attribute allows the compiler to construct the
  requisite function declaration, while allowing the body of the
  function to be assembly code. The specified function will not have
  prologue/epilogue sequences generated by the compiler. Only basic
  ``asm`` statements can safely be included in naked functions
  (Basic Asm). While using extended ``asm`` or a mixture of
  basic ``asm`` and C code may appear to work, they cannot be
  depended upon to work reliably and are not supported.

pcs

  .. index:: pcs function attribute, ARM

  The ``pcs`` attribute can be used to control the calling convention
  used for a function on ARM.  The attribute takes an argument that specifies
  the calling convention to use.

  When compiling using the AAPCS ABI (or a variant of it) then valid
  values for the argument are ``"aapcs"`` and ``"aapcs-vfp"``.  In
  order to use a variant other than ``"aapcs"`` then the compiler must
  be permitted to use the appropriate co-processor registers (i.e., the
  VFP registers must be available in order to use ``"aapcs-vfp"``).
  For example,

  .. code-block:: c++

    /* Argument passed in r0, and result returned in r0+r1.  */
    double f2d (float) __attribute__((pcs("aapcs")));

  Variadic functions always use the ``"aapcs"`` calling convention and
  the compiler rejects attempts to specify an alternative.

  .. _avr-function-attributes:

AVR Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the AVR back end:

interrupt

  .. index:: interrupt function attribute, AVR

  Use this attribute to indicate
  that the specified function is an interrupt handler.  The compiler generates
  function entry and exit sequences suitable for use in an interrupt handler
  when this attribute is present.

  On the AVR, the hardware globally disables interrupts when an
  interrupt is executed.  The first instruction of an interrupt handler
  declared with this attribute is a ``SEI`` instruction to
  re-enable interrupts.  See also the ``signal`` function attribute
  that does not insert a ``SEI`` instruction.  If both ``signal`` and
  ``interrupt`` are specified for the same function, ``signal``
  is silently ignored.

naked

  .. index:: naked function attribute, AVR

  This attribute allows the compiler to construct the
  requisite function declaration, while allowing the body of the
  function to be assembly code. The specified function will not have
  prologue/epilogue sequences generated by the compiler. Only basic
  ``asm`` statements can safely be included in naked functions
  (Basic Asm). While using extended ``asm`` or a mixture of
  basic ``asm`` and C code may appear to work, they cannot be
  depended upon to work reliably and are not supported.

OS_main OS_task

  .. index:: OS_main function attribute, AVR

  .. index:: OS_task function attribute, AVR

  On AVR, functions with the ``OS_main`` or ``OS_task`` attribute
  do not save/restore any call-saved register in their prologue/epilogue.

  The ``OS_main`` attribute can be used when there is
  guarantee that interrupts are disabled at the time when the function
  is entered.  This saves resources when the stack pointer has to be
  changed to set up a frame for local variables.

  The ``OS_task`` attribute can be used when there is no
  guarantee that interrupts are disabled at that time when the function
  is entered like for, e.g. task functions in a multi-threading operating
  system. In that case, changing the stack pointer register is
  guarded by save/clear/restore of the global interrupt enable flag.

  The differences to the ``naked`` function attribute are:

  * ``naked`` functions do not have a return instruction whereas 
    ``OS_main`` and ``OS_task`` functions have a ``RET`` or
    ``RETI`` return instruction.

  * ``naked`` functions do not set up a frame for local variables
    or a frame pointer whereas ``OS_main`` and ``OS_task`` do this
    as needed.

signal

  .. index:: signal function attribute, AVR

  Use this attribute on the AVR to indicate that the specified
  function is an interrupt handler.  The compiler generates function
  entry and exit sequences suitable for use in an interrupt handler when this
  attribute is present.

  See also the ``interrupt`` function attribute. 

  The AVR hardware globally disables interrupts when an interrupt is executed.
  Interrupt handler functions defined with the ``signal`` attribute
  do not re-enable interrupts.  It is save to enable interrupts in a
  ``signal`` handler.  This 'save' only applies to the code
  generated by the compiler and not to the IRQ layout of the
  application which is responsibility of the application.

  If both ``signal`` and ``interrupt`` are specified for the same
  function, ``signal`` is silently ignored.

  .. _blackfin-function-attributes:

Blackfin Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the Blackfin back end:

exception_handler

  .. index:: exception_handler function attribute

  .. index:: exception handler functions, Blackfin

  Use this attribute on the Blackfin to indicate that the specified function
  is an exception handler.  The compiler generates function entry and
  exit sequences suitable for use in an exception handler when this
  attribute is present.

interrupt_handler

  .. index:: interrupt_handler function attribute, Blackfin

  Use this attribute to
  indicate that the specified function is an interrupt handler.  The compiler
  generates function entry and exit sequences suitable for use in an
  interrupt handler when this attribute is present.

kspisusp

  .. index:: kspisusp function attribute, Blackfin

  .. index:: User stack pointer in interrupts on the Blackfin

  When used together with ``interrupt_handler``, ``exception_handler``
  or ``nmi_handler``, code is generated to load the stack pointer
  from the USP register in the function prologue.

l1_text

  .. index:: l1_text function attribute, Blackfin

  This attribute specifies a function to be placed into L1 Instruction
  SRAM. The function is put into a specific section named ``.l1.text``.
  With :option:`-mfdpic`, function calls with a such function as the callee
  or caller uses inlined PLT.

l2

  .. index:: l2 function attribute, Blackfin

  This attribute specifies a function to be placed into L2
  SRAM. The function is put into a specific section named
  ``.l2.text``. With :option:`-mfdpic`, callers of such functions use
  an inlined PLT.

longcall shortcall

  .. index:: indirect calls, Blackfin

  .. index:: longcall function attribute, Blackfin

  .. index:: shortcall function attribute, Blackfin

  The ``longcall`` attribute
  indicates that the function might be far away from the call site and
  require a different (more expensive) calling sequence.  The
  ``shortcall`` attribute indicates that the function is always close
  enough for the shorter calling sequence to be used.  These attributes
  override the :option:`-mlongcall` switch.

nesting

  .. index:: nesting function attribute, Blackfin

  .. index:: Allow nesting in an interrupt handler on the Blackfin processor

  Use this attribute together with ``interrupt_handler``,
  ``exception_handler`` or ``nmi_handler`` to indicate that the function
  entry code should enable nested interrupts or exceptions.

nmi_handler

  .. index:: nmi_handler function attribute, Blackfin

  .. index:: NMI handler functions on the Blackfin processor

  Use this attribute on the Blackfin to indicate that the specified function
  is an NMI handler.  The compiler generates function entry and
  exit sequences suitable for use in an NMI handler when this
  attribute is present.

saveall

  .. index:: saveall function attribute, Blackfin

  .. index:: save all registers on the Blackfin

  Use this attribute to indicate that
  all registers except the stack pointer should be saved in the prologue
  regardless of whether they are used or not.

  .. _cr16-function-attributes:

CR16 Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the CR16 back end:

interrupt

  .. index:: interrupt function attribute, CR16

  Use this attribute to indicate
  that the specified function is an interrupt handler.  The compiler generates
  function entry and exit sequences suitable for use in an interrupt handler
  when this attribute is present.

  .. _epiphany-function-attributes:

Epiphany Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the Epiphany back end:

disinterrupt

  .. index:: disinterrupt function attribute, Epiphany

  This attribute causes the compiler to emit
  instructions to disable interrupts for the duration of the given
  function.

forwarder_section

  .. index:: forwarder_section function attribute, Epiphany

  This attribute modifies the behavior of an interrupt handler.
  The interrupt handler may be in external memory which cannot be
  reached by a branch instruction, so generate a local memory trampoline
  to transfer control.  The single parameter identifies the section where
  the trampoline is placed.

interrupt

  .. index:: interrupt function attribute, Epiphany

  Use this attribute to indicate
  that the specified function is an interrupt handler.  The compiler generates
  function entry and exit sequences suitable for use in an interrupt handler
  when this attribute is present.  It may also generate
  a special section with code to initialize the interrupt vector table.

  On Epiphany targets one or more optional parameters can be added like this:

  .. code-block:: c++

    void __attribute__ ((interrupt ("dma0, dma1"))) universal_dma_handler ();

  Permissible values for these parameters are: ``reset``,
  ``software_exception``, ``page_miss``,
  ``timer0``, ``timer1``, ``message``,
  ``dma0``, ``dma1``, ``wand`` and ``swi``.
  Multiple parameters indicate that multiple entries in the interrupt
  vector table should be initialized for this function, i.e. for each
  parameter ``name``, a jump to the function is emitted in
  the section ivt_entry_``name``.  The parameter(s) may be omitted
  entirely, in which case no interrupt vector table entry is provided.

  Note that interrupts are enabled inside the function
  unless the ``disinterrupt`` attribute is also specified.

  The following examples are all valid uses of these attributes on
  Epiphany targets:

  .. code-block:: c++

    void __attribute__ ((interrupt)) universal_handler ();
    void __attribute__ ((interrupt ("dma1"))) dma1_handler ();
    void __attribute__ ((interrupt ("dma0, dma1"))) 
      universal_dma_handler ();
    void __attribute__ ((interrupt ("timer0"), disinterrupt))
      fast_timer_handler ();
    void __attribute__ ((interrupt ("dma0, dma1"), 
                         forwarder_section ("tramp")))
      external_dma_handler ();

long_call short_call

  .. index:: long_call function attribute, Epiphany

  .. index:: short_call function attribute, Epiphany

  .. index:: indirect calls, Epiphany

  These attributes specify how a particular function is called.
  These attributes override the
  :option:`-mlong-calls` (Adapteva Epiphany Options)
  command-line switch and ``#pragma long_calls`` settings.

  .. _h8-300-function-attributes:

H8/300 Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are available for H8/300 targets:

function_vector

  .. index:: function_vector function attribute, H8/300

  Use this attribute on the H8/300, H8/300H, and H8S to indicate 
  that the specified function should be called through the function vector.
  Calling a function through the function vector reduces code size; however,
  the function vector has a limited size (maximum 128 entries on the H8/300
  and 64 entries on the H8/300H and H8S)
  and shares space with the interrupt vector.

interrupt_handler

  .. index:: interrupt_handler function attribute, H8/300

  Use this attribute on the H8/300, H8/300H, and H8S to
  indicate that the specified function is an interrupt handler.  The compiler
  generates function entry and exit sequences suitable for use in an
  interrupt handler when this attribute is present.

saveall

  .. index:: saveall function attribute, H8/300

  .. index:: save all registers on the H8/300, H8/300H, and H8S

  Use this attribute on the H8/300, H8/300H, and H8S to indicate that
  all registers except the stack pointer should be saved in the prologue
  regardless of whether they are used or not.

  .. _ia-64-function-attributes:

IA-64 Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported on IA-64 targets:

syscall_linkage

  .. index:: syscall_linkage function attribute, IA-64

  This attribute is used to modify the IA-64 calling convention by marking
  all input registers as live at all function exits.  This makes it possible
  to restart a system call after an interrupt without having to save/restore
  the input registers.  This also prevents kernel data from leaking into
  application code.

version_id

  .. index:: version_id function attribute, IA-64

  This IA-64 HP-UX attribute, attached to a global variable or function, renames a
  symbol to contain a version string, thus allowing for function level
  versioning.  HP-UX system header files may use function level versioning
  for some system calls.

  .. code-block:: c++

    extern int foo () __attribute__((version_id ("20040821")));

  Calls to ``foo`` are mapped to calls to ``foo{20040821}``.

  .. _m32c-function-attributes:

M32C Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the M32C back end:

bank_switch

  .. index:: bank_switch function attribute, M32C

  When added to an interrupt handler with the M32C port, causes the
  prologue and epilogue to use bank switching to preserve the registers
  rather than saving them on the stack.

fast_interrupt

  .. index:: fast_interrupt function attribute, M32C

  Use this attribute on the M32C port to indicate that the specified
  function is a fast interrupt handler.  This is just like the
  ``interrupt`` attribute, except that ``freit`` is used to return
  instead of ``reit``.

function_vector

  .. index:: function_vector function attribute, M16C/M32C

  On M16C/M32C targets, the ``function_vector`` attribute declares a
  special page subroutine call function. Use of this attribute reduces
  the code size by 2 bytes for each call generated to the
  subroutine. The argument to the attribute is the vector number entry
  from the special page vector table which contains the 16 low-order
  bits of the subroutine's entry address. Each vector table has special
  page number (18 to 255) that is used in ``jsrs`` instructions.
  Jump addresses of the routines are generated by adding 0x0F0000 (in
  case of M16C targets) or 0xFF0000 (in case of M32C targets), to the
  2-byte addresses set in the vector table. Therefore you need to ensure
  that all the special page vector routines should get mapped within the
  address range 0x0F0000 to 0x0FFFFF (for M16C) and 0xFF0000 to 0xFFFFFF
  (for M32C).

  In the following example 2 bytes are saved for each call to
  function ``foo``.

  .. code-block:: c++

    void foo (void) __attribute__((function_vector(0x18)));
    void foo (void)
    {
    }

    void bar (void)
    {
        foo();
    }

  If functions are defined in one file and are called in another file,
  then be sure to write this declaration in both files.

  This attribute is ignored for R8C target.

interrupt

  .. index:: interrupt function attribute, M32C

  Use this attribute to indicate
  that the specified function is an interrupt handler.  The compiler generates
  function entry and exit sequences suitable for use in an interrupt handler
  when this attribute is present.

  .. _m32r-d-function-attributes:

M32R/D Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the M32R/D back end:

interrupt

  .. index:: interrupt function attribute, M32R/D

  Use this attribute to indicate
  that the specified function is an interrupt handler.  The compiler generates
  function entry and exit sequences suitable for use in an interrupt handler
  when this attribute is present.

model (``model-name``)

  .. index:: model function attribute, M32R/D

  .. index:: function addressability on the M32R/D

  On the M32R/D, use this attribute to set the addressability of an
  object, and of the code generated for a function.  The identifier
  ``model-name`` is one of ``small``, ``medium``, or
  ``large``, representing each of the code models.

  Small model objects live in the lower 16MB of memory (so that their
  addresses can be loaded with the ``ld24`` instruction), and are
  callable with the ``bl`` instruction.

  Medium model objects may live anywhere in the 32-bit address space (the
  compiler generates ``seth/add3`` instructions to load their addresses),
  and are callable with the ``bl`` instruction.

  Large model objects may live anywhere in the 32-bit address space (the
  compiler generates ``seth/add3`` instructions to load their addresses),
  and may not be reachable with the ``bl`` instruction (the compiler
  generates the much slower ``seth/add3/jl`` instruction sequence).

  .. _m68k-function-attributes:

m68k Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the m68k back end:

interrupt interrupt_handler

  .. index:: interrupt function attribute, m68k

  .. index:: interrupt_handler function attribute, m68k

  Use this attribute to
  indicate that the specified function is an interrupt handler.  The compiler
  generates function entry and exit sequences suitable for use in an
  interrupt handler when this attribute is present.  Either name may be used.

interrupt_thread

  .. index:: interrupt_thread function attribute, fido

  Use this attribute on fido, a subarchitecture of the m68k, to indicate
  that the specified function is an interrupt handler that is designed
  to run as a thread.  The compiler omits generate prologue/epilogue
  sequences and replaces the return instruction with a ``sleep``
  instruction.  This attribute is available only on fido.

  .. _mcore-function-attributes:

MCORE Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the MCORE back end:

naked

  .. index:: naked function attribute, MCORE

  This attribute allows the compiler to construct the
  requisite function declaration, while allowing the body of the
  function to be assembly code. The specified function will not have
  prologue/epilogue sequences generated by the compiler. Only basic
  ``asm`` statements can safely be included in naked functions
  (Basic Asm). While using extended ``asm`` or a mixture of
  basic ``asm`` and C code may appear to work, they cannot be
  depended upon to work reliably and are not supported.

  .. _mep-function-attributes:

MeP Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the MeP back end:

disinterrupt

  .. index:: disinterrupt function attribute, MeP

  On MeP targets, this attribute causes the compiler to emit
  instructions to disable interrupts for the duration of the given
  function.

interrupt

  .. index:: interrupt function attribute, MeP

  Use this attribute to indicate
  that the specified function is an interrupt handler.  The compiler generates
  function entry and exit sequences suitable for use in an interrupt handler
  when this attribute is present.

near

  .. index:: near function attribute, MeP

  This attribute causes the compiler to assume the called
  function is close enough to use the normal calling convention,
  overriding the :option:`-mtf` command-line option.

far

  .. index:: far function attribute, MeP

  On MeP targets this causes the compiler to use a calling convention
  that assumes the called function is too far away for the built-in
  addressing modes.

vliw

  .. index:: vliw function attribute, MeP

  The ``vliw`` attribute tells the compiler to emit
  instructions in VLIW mode instead of core mode.  Note that this
  attribute is not allowed unless a VLIW coprocessor has been configured
  and enabled through command-line options.

  .. _microblaze-function-attributes:

MicroBlaze Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported on MicroBlaze targets:

save_volatiles

  .. index:: save_volatiles function attribute, MicroBlaze

  Use this attribute to indicate that the function is
  an interrupt handler.  All volatile registers (in addition to non-volatile
  registers) are saved in the function prologue.  If the function is a leaf
  function, only volatiles used by the function are saved.  A normal function
  return is generated instead of a return from interrupt.

break_handler

  .. index:: break_handler function attribute, MicroBlaze

  .. index:: break handler functions

  Use this attribute to indicate that
  the specified function is a break handler.  The compiler generates function
  entry and exit sequences suitable for use in an break handler when this
  attribute is present. The return from ``break_handler`` is done through
  the ``rtbd`` instead of ``rtsd``.

  .. code-block:: c++

    void f () __attribute__ ((break_handler));

  .. _microsoft-windows-function-attributes:

Microsoft Windows Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following attributes are available on Microsoft Windows and Symbian OS
targets.

dllexport

  .. index:: dllexport function attribute

  .. index:: __declspec(dllexport)

  On Microsoft Windows targets and Symbian OS targets the
  ``dllexport`` attribute causes the compiler to provide a global
  pointer to a pointer in a DLL, so that it can be referenced with the
  ``dllimport`` attribute.  On Microsoft Windows targets, the pointer
  name is formed by combining ``_imp__`` and the function or variable
  name.

  You can use ``__declspec(dllexport)`` as a synonym for
  ``__attribute__ ((dllexport))`` for compatibility with other
  compilers.

  On systems that support the ``visibility`` attribute, this
  attribute also implies 'default' visibility.  It is an error to
  explicitly specify any other visibility.

  GCC's default behavior is to emit all inline functions with the
  ``dllexport`` attribute.  Since this can cause object file-size bloat,
  you can use :option:`-fno-keep-inline-dllexport`, which tells GCC to
  ignore the attribute for inlined functions unless the 
  :option:`-fkeep-inline-functions` flag is used instead.

  The attribute is ignored for undefined symbols.

  When applied to C++ classes, the attribute marks defined non-inlined
  member functions and static data members as exports.  Static consts
  initialized in-class are not marked unless they are also defined
  out-of-class.

  For Microsoft Windows targets there are alternative methods for
  including the symbol in the DLL's export table such as using a
  .def file with an ``EXPORTS`` section or, with GNU ld, using
  the :option:`--export-all` linker flag.

dllimport

  .. index:: dllimport function attribute

  .. index:: __declspec(dllimport)

  On Microsoft Windows and Symbian OS targets, the ``dllimport``
  attribute causes the compiler to reference a function or variable via
  a global pointer to a pointer that is set up by the DLL exporting the
  symbol.  The attribute implies ``extern``.  On Microsoft Windows
  targets, the pointer name is formed by combining ``_imp__`` and the
  function or variable name.

  You can use ``__declspec(dllimport)`` as a synonym for
  ``__attribute__ ((dllimport))`` for compatibility with other
  compilers.

  On systems that support the ``visibility`` attribute, this
  attribute also implies 'default' visibility.  It is an error to
  explicitly specify any other visibility.

  Currently, the attribute is ignored for inlined functions.  If the
  attribute is applied to a symbol definition, an error is reported.
  If a symbol previously declared ``dllimport`` is later defined, the
  attribute is ignored in subsequent references, and a warning is emitted.
  The attribute is also overridden by a subsequent declaration as
  ``dllexport``.

  When applied to C++ classes, the attribute marks non-inlined
  member functions and static data members as imports.  However, the
  attribute is ignored for virtual methods to allow creation of vtables
  using thunks.

  On the SH Symbian OS target the ``dllimport`` attribute also has
  another affect-it can cause the vtable and run-time type information
  for a class to be exported.  This happens when the class has a
  dllimported constructor or a non-inline, non-pure virtual function
  and, for either of those two conditions, the class also has an inline
  constructor or destructor and has a key function that is defined in
  the current translation unit.

  For Microsoft Windows targets the use of the ``dllimport``
  attribute on functions is not necessary, but provides a small
  performance benefit by eliminating a thunk in the DLL.  The use of the
  ``dllimport`` attribute on imported variables can be avoided by passing the
  :option:`--enable-auto-import` switch to the GNU linker.  As with
  functions, using the attribute for a variable eliminates a thunk in
  the DLL.

  One drawback to using this attribute is that a pointer to a
  variable marked as ``dllimport`` cannot be used as a constant
  address. However, a pointer to a function with the
  ``dllimport`` attribute can be used as a constant initializer; in
  this case, the address of a stub function in the import lib is
  referenced.  On Microsoft Windows targets, the attribute can be disabled
  for functions by setting the :option:`-mnop-fun-dllimport` flag.

  .. _mips-function-attributes:

MIPS Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the MIPS back end:

interrupt

  .. index:: interrupt function attribute, MIPS

  Use this attribute to indicate
  that the specified function is an interrupt handler.  The compiler generates
  function entry and exit sequences suitable for use in an interrupt handler
  when this attribute is present.

  You can use the following attributes to modify the behavior
  of an interrupt handler:

  use_shadow_register_set

    .. index:: use_shadow_register_set function attribute, MIPS

    Assume that the handler uses a shadow register set, instead of
    the main general-purpose registers.

  keep_interrupts_masked

    .. index:: keep_interrupts_masked function attribute, MIPS

    Keep interrupts masked for the whole function.  Without this attribute,
    GCC tries to reenable interrupts for as much of the function as it can.

  use_debug_exception_return

    .. index:: use_debug_exception_return function attribute, MIPS

    Return using the ``deret`` instruction.  Interrupt handlers that don't
    have this attribute return using ``eret`` instead.

    You can use any combination of these attributes, as shown below:

  .. code-block:: c++

    void __attribute__ ((interrupt)) v0 ();
    void __attribute__ ((interrupt, use_shadow_register_set)) v1 ();
    void __attribute__ ((interrupt, keep_interrupts_masked)) v2 ();
    void __attribute__ ((interrupt, use_debug_exception_return)) v3 ();
    void __attribute__ ((interrupt, use_shadow_register_set,
                         keep_interrupts_masked)) v4 ();
    void __attribute__ ((interrupt, use_shadow_register_set,
                         use_debug_exception_return)) v5 ();
    void __attribute__ ((interrupt, keep_interrupts_masked,
                         use_debug_exception_return)) v6 ();
    void __attribute__ ((interrupt, use_shadow_register_set,
                         keep_interrupts_masked,
                         use_debug_exception_return)) v7 ();

long_call near far

  .. index:: indirect calls, MIPS

  .. index:: long_call function attribute, MIPS

  .. index:: near function attribute, MIPS

  .. index:: far function attribute, MIPS

  These attributes specify how a particular function is called on MIPS.
  The attributes override the :option:`-mlong-calls` (MIPS Options)
  command-line switch.  The ``long_call`` and ``far`` attributes are
  synonyms, and cause the compiler to always call
  the function by first loading its address into a register, and then using
  the contents of that register.  The ``near`` attribute has the opposite
  effect; it specifies that non-PIC calls should be made using the more
  efficient ``jal`` instruction.

mips16 nomips16

  .. index:: mips16 function attribute, MIPS

  .. index:: nomips16 function attribute, MIPS

  On MIPS targets, you can use the ``mips16`` and ``nomips16``
  function attributes to locally select or turn off MIPS16 code generation.
  A function with the ``mips16`` attribute is emitted as MIPS16 code,
  while MIPS16 code generation is disabled for functions with the
  ``nomips16`` attribute.  These attributes override the
  :option:`-mips16` and :option:`-mno-mips16` options on the command line
  (MIPS Options).

  When compiling files containing mixed MIPS16 and non-MIPS16 code, the
  preprocessor symbol ``__mips16`` reflects the setting on the command line,
  not that within individual functions.  Mixed MIPS16 and non-MIPS16 code
  may interact badly with some GCC extensions such as ``__builtin_apply``
  (Constructing Calls).

micromips, MIPS nomicromips, MIPS

  .. index:: micromips function attribute

  .. index:: nomicromips function attribute

  On MIPS targets, you can use the ``micromips`` and ``nomicromips``
  function attributes to locally select or turn off microMIPS code generation.
  A function with the ``micromips`` attribute is emitted as microMIPS code,
  while microMIPS code generation is disabled for functions with the
  ``nomicromips`` attribute.  These attributes override the
  :option:`-mmicromips` and :option:`-mno-micromips` options on the command line
  (MIPS Options).

  When compiling files containing mixed microMIPS and non-microMIPS code, the
  preprocessor symbol ``__mips_micromips`` reflects the setting on the
  command line,
  not that within individual functions.  Mixed microMIPS and non-microMIPS code
  may interact badly with some GCC extensions such as ``__builtin_apply``
  (Constructing Calls).

nocompression

  .. index:: nocompression function attribute, MIPS

  On MIPS targets, you can use the ``nocompression`` function attribute
  to locally turn off MIPS16 and microMIPS code generation.  This attribute
  overrides the :option:`-mips16` and :option:`-mmicromips` options on the
  command line (MIPS Options).

  .. _msp430-function-attributes:

MSP430 Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the MSP430 back end:

critical

  .. index:: critical function attribute, MSP430

  Critical functions disable interrupts upon entry and restore the
  previous interrupt state upon exit.  Critical functions cannot also
  have the ``naked`` or ``reentrant`` attributes.  They can have
  the ``interrupt`` attribute.

interrupt

  .. index:: interrupt function attribute, MSP430

  Use this attribute to indicate
  that the specified function is an interrupt handler.  The compiler generates
  function entry and exit sequences suitable for use in an interrupt handler
  when this attribute is present.

  You can provide an argument to the interrupt
  attribute which specifies a name or number.  If the argument is a
  number it indicates the slot in the interrupt vector table (0 - 31) to
  which this handler should be assigned.  If the argument is a name it
  is treated as a symbolic name for the vector slot.  These names should
  match up with appropriate entries in the linker script.  By default
  the names ``watchdog`` for vector 26, ``nmi`` for vector 30 and
  ``reset`` for vector 31 are recognized.

naked

  .. index:: naked function attribute, MSP430

  This attribute allows the compiler to construct the
  requisite function declaration, while allowing the body of the
  function to be assembly code. The specified function will not have
  prologue/epilogue sequences generated by the compiler. Only basic
  ``asm`` statements can safely be included in naked functions
  (Basic Asm). While using extended ``asm`` or a mixture of
  basic ``asm`` and C code may appear to work, they cannot be
  depended upon to work reliably and are not supported.

reentrant

  .. index:: reentrant function attribute, MSP430

  Reentrant functions disable interrupts upon entry and enable them
  upon exit.  Reentrant functions cannot also have the ``naked``
  or ``critical`` attributes.  They can have the ``interrupt``
  attribute.

wakeup

  .. index:: wakeup function attribute, MSP430

  This attribute only applies to interrupt functions.  It is silently
  ignored if applied to a non-interrupt function.  A wakeup interrupt
  function will rouse the processor from any low-power state that it
  might be in when the function exits.

  .. _nds32-function-attributes:

NDS32 Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the NDS32 back end:

exception

  .. index:: exception function attribute

  .. index:: exception handler functions, NDS32

  Use this attribute on the NDS32 target to indicate that the specified function
  is an exception handler.  The compiler will generate corresponding sections
  for use in an exception handler.

interrupt

  .. index:: interrupt function attribute, NDS32

  On NDS32 target, this attribute indicates that the specified function
  is an interrupt handler.  The compiler generates corresponding sections
  for use in an interrupt handler.  You can use the following attributes
  to modify the behavior:

  nested

    .. index:: nested function attribute, NDS32

    This interrupt service routine is interruptible.

  not_nested

    .. index:: not_nested function attribute, NDS32

    This interrupt service routine is not interruptible.

  nested_ready

    .. index:: nested_ready function attribute, NDS32

    This interrupt service routine is interruptible after ``PSW.GIE``
    (global interrupt enable) is set.  This allows interrupt service routine to
    finish some short critical code before enabling interrupts.

  save_all

    .. index:: save_all function attribute, NDS32

    The system will help save all registers into stack before entering
    interrupt handler.

  partial_save

    .. index:: partial_save function attribute, NDS32

    The system will help save caller registers into stack before entering
    interrupt handler.

naked

  .. index:: naked function attribute, NDS32

  This attribute allows the compiler to construct the
  requisite function declaration, while allowing the body of the
  function to be assembly code. The specified function will not have
  prologue/epilogue sequences generated by the compiler. Only basic
  ``asm`` statements can safely be included in naked functions
  (Basic Asm). While using extended ``asm`` or a mixture of
  basic ``asm`` and C code may appear to work, they cannot be
  depended upon to work reliably and are not supported.

reset

  .. index:: reset function attribute, NDS32

  .. index:: reset handler functions

  Use this attribute on the NDS32 target to indicate that the specified function
  is a reset handler.  The compiler will generate corresponding sections
  for use in a reset handler.  You can use the following attributes
  to provide extra exception handling:

  nmi

    .. index:: nmi function attribute, NDS32

    Provide a user-defined function to handle NMI exception.

  warm

    .. index:: warm function attribute, NDS32

    Provide a user-defined function to handle warm reset exception.

    .. _nios-ii-function-attributes:

Nios II Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the Nios II back end:

target (``options``)

  .. index:: target function attribute

  As discussed in Common Function Attributes, this attribute 
  allows specification of target-specific compilation options.

  When compiling for Nios II, the following options are allowed:

  custom-``insn``=``N`` no-custom-``insn``

    .. index:: target("custom-insn=N") function attribute, Nios II

    .. index:: target("no-custom-insn") function attribute, Nios II

    Each custom-``insn``=``N`` attribute locally enables use of a
    custom instruction with encoding ``N`` when generating code that uses 
    ``insn``.  Similarly, no-custom-``insn`` locally inhibits use of
    the custom instruction ``insn``.
    These target attributes correspond to the
    :option:`-mcustom-``insn``=``N``` and :option:`-mno-custom-``insn```
    command-line options, and support the same set of ``insn`` keywords.
    See :ref:`nios-ii-options`, for more information.

  custom-fpu-cfg=``name``

    .. index:: target("custom-fpu-cfg=name") function attribute, Nios II

    This attribute corresponds to the :option:`-mcustom-fpu-cfg=``name```
    command-line option, to select a predefined set of custom instructions
    named ``name``.
    See :ref:`nios-ii-options`, for more information.

    .. _powerpc-function-attributes:

PowerPC Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the PowerPC back end:

longcall shortcall

  .. index:: indirect calls, PowerPC

  .. index:: longcall function attribute, PowerPC

  .. index:: shortcall function attribute, PowerPC

  The ``longcall`` attribute
  indicates that the function might be far away from the call site and
  require a different (more expensive) calling sequence.  The
  ``shortcall`` attribute indicates that the function is always close
  enough for the shorter calling sequence to be used.  These attributes
  override both the :option:`-mlongcall` switch and
  the ``#pragma longcall`` setting.

  See :ref:`rs-6000-and-powerpc-options`, for more information on whether long
  calls are necessary.

target (``options``)

  .. index:: target function attribute

  As discussed in Common Function Attributes, this attribute 
  allows specification of target-specific compilation options.

  On the PowerPC, the following options are allowed:

  altivec no-altivec

    .. index:: target("altivec") function attribute, PowerPC

    Generate code that uses (does not use) AltiVec instructions.  In
    32-bit code, you cannot enable AltiVec instructions unless
    :option:`-mabi=altivec` is used on the command line.

  cmpb no-cmpb

    .. index:: target("cmpb") function attribute, PowerPC

    Generate code that uses (does not use) the compare bytes instruction
    implemented on the POWER6 processor and other processors that support
    the PowerPC V2.05 architecture.

  dlmzb no-dlmzb

    .. index:: target("dlmzb") function attribute, PowerPC

    Generate code that uses (does not use) the string-search dlmzb
    instruction on the IBM 405, 440, 464 and 476 processors.  This instruction is
    generated by default when targeting those processors.

  fprnd no-fprnd

    .. index:: target("fprnd") function attribute, PowerPC

    Generate code that uses (does not use) the FP round to integer
    instructions implemented on the POWER5+ processor and other processors
    that support the PowerPC V2.03 architecture.

  hard-dfp no-hard-dfp

    .. index:: target("hard-dfp") function attribute, PowerPC

    Generate code that uses (does not use) the decimal floating-point
    instructions implemented on some POWER processors.

  isel no-isel

    .. index:: target("isel") function attribute, PowerPC

    Generate code that uses (does not use) ISEL instruction.

  mfcrf no-mfcrf

    .. index:: target("mfcrf") function attribute, PowerPC

    Generate code that uses (does not use) the move from condition
    register field instruction implemented on the POWER4 processor and
    other processors that support the PowerPC V2.01 architecture.

  mfpgpr no-mfpgpr

    .. index:: target("mfpgpr") function attribute, PowerPC

    Generate code that uses (does not use) the FP move to/from general
    purpose register instructions implemented on the POWER6X processor and
    other processors that support the extended PowerPC V2.05 architecture.

  mulhw no-mulhw

    .. index:: target("mulhw") function attribute, PowerPC

    Generate code that uses (does not use) the half-word multiply and
    multiply-accumulate instructions on the IBM 405, 440, 464 and 476 processors.
    These instructions are generated by default when targeting those
    processors.

  multiple no-multiple

    .. index:: target("multiple") function attribute, PowerPC

    Generate code that uses (does not use) the load multiple word
    instructions and the store multiple word instructions.

  update no-update

    .. index:: target("update") function attribute, PowerPC

    Generate code that uses (does not use) the load or store instructions
    that update the base register to the address of the calculated memory
    location.

  popcntb no-popcntb

    .. index:: target("popcntb") function attribute, PowerPC

    Generate code that uses (does not use) the popcount and double-precision
    FP reciprocal estimate instruction implemented on the POWER5
    processor and other processors that support the PowerPC V2.02
    architecture.

  popcntd no-popcntd

    .. index:: target("popcntd") function attribute, PowerPC

    Generate code that uses (does not use) the popcount instruction
    implemented on the POWER7 processor and other processors that support
    the PowerPC V2.06 architecture.

  powerpc-gfxopt no-powerpc-gfxopt

    .. index:: target("powerpc-gfxopt") function attribute, PowerPC

    Generate code that uses (does not use) the optional PowerPC
    architecture instructions in the Graphics group, including
    floating-point select.

  powerpc-gpopt no-powerpc-gpopt

    .. index:: target("powerpc-gpopt") function attribute, PowerPC

    Generate code that uses (does not use) the optional PowerPC
    architecture instructions in the General Purpose group, including
    floating-point square root.

  recip-precision no-recip-precision

    .. index:: target("recip-precision") function attribute, PowerPC

    Assume (do not assume) that the reciprocal estimate instructions
    provide higher-precision estimates than is mandated by the PowerPC
    ABI.

  string no-string

    .. index:: target("string") function attribute, PowerPC

    Generate code that uses (does not use) the load string instructions
    and the store string word instructions to save multiple registers and
    do small block moves.

  vsx no-vsx

    .. index:: target("vsx") function attribute, PowerPC

    Generate code that uses (does not use) vector/scalar (VSX)
    instructions, and also enable the use of built-in functions that allow
    more direct access to the VSX instruction set.  In 32-bit code, you
    cannot enable VSX or AltiVec instructions unless
    :option:`-mabi=altivec` is used on the command line.

  friz no-friz

    .. index:: target("friz") function attribute, PowerPC

    Generate (do not generate) the ``friz`` instruction when the
    :option:`-funsafe-math-optimizations` option is used to optimize
    rounding a floating-point value to 64-bit integer and back to floating
    point.  The ``friz`` instruction does not return the same value if
    the floating-point number is too large to fit in an integer.

  avoid-indexed-addresses no-avoid-indexed-addresses

    .. index:: target("avoid-indexed-addresses") function attribute, PowerPC

    Generate code that tries to avoid (not avoid) the use of indexed load
    or store instructions.

  paired no-paired

    .. index:: target("paired") function attribute, PowerPC

    Generate code that uses (does not use) the generation of PAIRED simd
    instructions.

  longcall no-longcall

    .. index:: target("longcall") function attribute, PowerPC

    Generate code that assumes (does not assume) that all calls are far
    away so that a longer more expensive calling sequence is required.

  cpu=``CPU``

    .. index:: target("cpu=CPU") function attribute, PowerPC

    Specify the architecture to generate code for when compiling the
    function.  If you select the ``target("cpu=power7")`` attribute when
    generating 32-bit code, VSX and AltiVec instructions are not generated
    unless you use the :option:`-mabi=altivec` option on the command line.

  tune=``TUNE``

    .. index:: target("tune=TUNE") function attribute, PowerPC

    Specify the architecture to tune for when compiling the function.  If
    you do not specify the ``target("tune=``TUNE``")`` attribute and
    you do specify the ``target("cpu=``CPU``")`` attribute,
    compilation tunes for the ``CPU`` architecture, and not the
    default tuning specified on the command line.

    On the PowerPC, the inliner does not inline a
  function that has different target options than the caller, unless the
  callee has a subset of the target options of the caller.

  .. _rl78-function-attributes:

RL78 Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the RL78 back end:

interrupt brk_interrupt

  .. index:: interrupt function attribute, RL78

  .. index:: brk_interrupt function attribute, RL78

  These attributes indicate
  that the specified function is an interrupt handler.  The compiler generates
  function entry and exit sequences suitable for use in an interrupt handler
  when this attribute is present.

  Use ``brk_interrupt`` instead of ``interrupt`` for
  handlers intended to be used with the ``BRK`` opcode (i.e. those
  that must end with ``RETB`` instead of ``RETI``).

naked

  .. index:: naked function attribute, RL78

  This attribute allows the compiler to construct the
  requisite function declaration, while allowing the body of the
  function to be assembly code. The specified function will not have
  prologue/epilogue sequences generated by the compiler. Only basic
  ``asm`` statements can safely be included in naked functions
  (Basic Asm). While using extended ``asm`` or a mixture of
  basic ``asm`` and C code may appear to work, they cannot be
  depended upon to work reliably and are not supported.

  .. _rx-function-attributes:

RX Function Attributes
^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the RX back end:

fast_interrupt

  .. index:: fast_interrupt function attribute, RX

  Use this attribute on the RX port to indicate that the specified
  function is a fast interrupt handler.  This is just like the
  ``interrupt`` attribute, except that ``freit`` is used to return
  instead of ``reit``.

interrupt

  .. index:: interrupt function attribute, RX

  Use this attribute to indicate
  that the specified function is an interrupt handler.  The compiler generates
  function entry and exit sequences suitable for use in an interrupt handler
  when this attribute is present.

  On RX targets, you may specify one or more vector numbers as arguments
  to the attribute, as well as naming an alternate table name.
  Parameters are handled sequentially, so one handler can be assigned to
  multiple entries in multiple tables.  One may also pass the magic
  string ``"$default"`` which causes the function to be used for any
  unfilled slots in the current table.

  This example shows a simple assignment of a function to one vector in
  the default table (note that preprocessor macros may be used for
  chip-specific symbolic vector names):

  .. code-block:: c++

    void __attribute__ ((interrupt (5))) txd1_handler ();

  This example assigns a function to two slots in the default table
  (using preprocessor macros defined elsewhere) and makes it the default
  for the ``dct`` table:

  .. code-block:: c++

    void __attribute__ ((interrupt (RXD1_VECT,RXD2_VECT,"dct","$default")))
    	txd1_handler ();

naked

  .. index:: naked function attribute, RX

  This attribute allows the compiler to construct the
  requisite function declaration, while allowing the body of the
  function to be assembly code. The specified function will not have
  prologue/epilogue sequences generated by the compiler. Only basic
  ``asm`` statements can safely be included in naked functions
  (Basic Asm). While using extended ``asm`` or a mixture of
  basic ``asm`` and C code may appear to work, they cannot be
  depended upon to work reliably and are not supported.

vector

  .. index:: vector function attribute, RX

  This RX attribute is similar to the ``interrupt`` attribute, including its
  parameters, but does not make the function an interrupt-handler type
  function (i.e. it retains the normal C function calling ABI).  See the
  ``interrupt`` attribute for a description of its arguments.

  .. _s-390-function-attributes:

S/390 Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported on the S/390:

hotpatch (``halfwords-before-function-label``,``halfwords-after-function-label``)

  .. index:: hotpatch function attribute, S/390

  On S/390 System z targets, you can use this function attribute to
  make GCC generate a 'hot-patching' function prologue.  If the
  :option:`-mhotpatch=` command-line option is used at the same time,
  the ``hotpatch`` attribute takes precedence.  The first of the
  two arguments specifies the number of halfwords to be added before
  the function label.  A second argument can be used to specify the
  number of halfwords to be added after the function label.  For
  both arguments the maximum allowed value is 1000000.

  If both arguments are zero, hotpatching is disabled.

  .. _sh-function-attributes:

SH Function Attributes
^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported on the SH family of processors:

function_vector

  .. index:: function_vector function attribute, SH

  .. index:: calling functions through the function vector on SH2A

  On SH2A targets, this attribute declares a function to be called using the
  TBR relative addressing mode.  The argument to this attribute is the entry
  number of the same function in a vector table containing all the TBR
  relative addressable functions.  For correct operation the TBR must be setup
  accordingly to point to the start of the vector table before any functions with
  this attribute are invoked.  Usually a good place to do the initialization is
  the startup routine.  The TBR relative vector table can have at max 256 function
  entries.  The jumps to these functions are generated using a SH2A specific,
  non delayed branch instruction JSR/N @(disp8,TBR).  You must use GAS and GLD
  from GNU binutils version 2.7 or later for this attribute to work correctly.

  In an application, for a function being called once, this attribute
  saves at least 8 bytes of code; and if other successive calls are being
  made to the same function, it saves 2 bytes of code per each of these
  calls.

interrupt_handler

  .. index:: interrupt_handler function attribute, SH

  Use this attribute to
  indicate that the specified function is an interrupt handler.  The compiler
  generates function entry and exit sequences suitable for use in an
  interrupt handler when this attribute is present.

nosave_low_regs

  .. index:: nosave_low_regs function attribute, SH

  Use this attribute on SH targets to indicate that an ``interrupt_handler``
  function should not save and restore registers R0..R7.  This can be used on SH3*
  and SH4* targets that have a second R0..R7 register bank for non-reentrant
  interrupt handlers.

renesas

  .. index:: renesas function attribute, SH

  On SH targets this attribute specifies that the function or struct follows the
  Renesas ABI.

resbank

  .. index:: resbank function attribute, SH

  On the SH2A target, this attribute enables the high-speed register
  saving and restoration using a register bank for ``interrupt_handler``
  routines.  Saving to the bank is performed automatically after the CPU
  accepts an interrupt that uses a register bank.

  The nineteen 32-bit registers comprising general register R0 to R14,
  control register GBR, and system registers MACH, MACL, and PR and the
  vector table address offset are saved into a register bank.  Register
  banks are stacked in first-in last-out (FILO) sequence.  Restoration
  from the bank is executed by issuing a RESBANK instruction.

sp_switch

  .. index:: sp_switch function attribute, SH

  Use this attribute on the SH to indicate an ``interrupt_handler``
  function should switch to an alternate stack.  It expects a string
  argument that names a global variable holding the address of the
  alternate stack.

  .. code-block:: c++

    void *alt_stack;
    void f () __attribute__ ((interrupt_handler,
                              sp_switch ("alt_stack")));

trap_exit

  .. index:: trap_exit function attribute, SH

  Use this attribute on the SH for an ``interrupt_handler`` to return using
  ``trapa`` instead of ``rte``.  This attribute expects an integer
  argument specifying the trap number to be used.

trapa_handler

  .. index:: trapa_handler function attribute, SH

  On SH targets this function attribute is similar to ``interrupt_handler``
  but it does not save and restore all registers.

  .. _spu-function-attributes:

SPU Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the SPU back end:

naked

  .. index:: naked function attribute, SPU

  This attribute allows the compiler to construct the
  requisite function declaration, while allowing the body of the
  function to be assembly code. The specified function will not have
  prologue/epilogue sequences generated by the compiler. Only basic
  ``asm`` statements can safely be included in naked functions
  (Basic Asm). While using extended ``asm`` or a mixture of
  basic ``asm`` and C code may appear to work, they cannot be
  depended upon to work reliably and are not supported.

  .. _symbian-os-function-attributes:

Symbian OS Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`microsoft-windows-function-attributes`, for discussion of the
``dllexport`` and ``dllimport`` attributes.

.. _visium-function-attributes:

Visium Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the Visium back end:

interrupt

  .. index:: interrupt function attribute, Visium

  Use this attribute to indicate
  that the specified function is an interrupt handler.  The compiler generates
  function entry and exit sequences suitable for use in an interrupt handler
  when this attribute is present.

  .. _x86-function-attributes:

x86 Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the x86 back end:

.. option:: cdecl, -mrtd

  .. index:: cdecl function attribute, x86-32

  .. index:: functions that pop the argument stack on x86-32

  On the x86-32 targets, the ``cdecl`` attribute causes the compiler to
  assume that the calling function pops off the stack space used to
  pass arguments.  This is
  useful to override the effects of the :option:`-mrtd` switch.

fastcall

  .. index:: fastcall function attribute, x86-32

  .. index:: functions that pop the argument stack on x86-32

  On x86-32 targets, the ``fastcall`` attribute causes the compiler to
  pass the first argument (if of integral type) in the register ECX and
  the second argument (if of integral type) in the register EDX.  Subsequent
  and other typed arguments are passed on the stack.  The called function
  pops the arguments off the stack.  If the number of arguments is variable all
  arguments are pushed on the stack.

thiscall

  .. index:: thiscall function attribute, x86-32

  .. index:: functions that pop the argument stack on x86-32

  On x86-32 targets, the ``thiscall`` attribute causes the compiler to
  pass the first argument (if of integral type) in the register ECX.
  Subsequent and other typed arguments are passed on the stack. The called
  function pops the arguments off the stack.
  If the number of arguments is variable all arguments are pushed on the
  stack.
  The ``thiscall`` attribute is intended for C++ non-static member functions.
  As a GCC extension, this calling convention can be used for C functions
  and for static member methods.

ms_abi sysv_abi

  .. index:: ms_abi function attribute, x86

  .. index:: sysv_abi function attribute, x86

  On 32-bit and 64-bit x86 targets, you can use an ABI attribute
  to indicate which calling convention should be used for a function.  The
  ``ms_abi`` attribute tells the compiler to use the Microsoft ABI,
  while the ``sysv_abi`` attribute tells the compiler to use the ABI
  used on GNU/Linux and other systems.  The default is to use the Microsoft ABI
  when targeting Windows.  On all other systems, the default is the x86/AMD ABI.

  Note, the ``ms_abi`` attribute for Microsoft Windows 64-bit targets currently
  requires the :option:`-maccumulate-outgoing-args` option.

callee_pop_aggregate_return (``number``)

  .. index:: callee_pop_aggregate_return function attribute, x86

  On x86-32 targets, you can use this attribute to control how
  aggregates are returned in memory.  If the caller is responsible for
  popping the hidden pointer together with the rest of the arguments, specify
  ``number`` equal to zero.  If callee is responsible for popping the
  hidden pointer, specify ``number`` equal to one.  

  The default x86-32 ABI assumes that the callee pops the
  stack for hidden pointer.  However, on x86-32 Microsoft Windows targets,
  the compiler assumes that the
  caller pops the stack for hidden pointer.

ms_hook_prologue

  .. index:: ms_hook_prologue function attribute, x86

  On 32-bit and 64-bit x86 targets, you can use
  this function attribute to make GCC generate the 'hot-patching' function
  prologue used in Win32 API functions in Microsoft Windows XP Service Pack 2
  and newer.

regparm (``number``)

  .. index:: regparm function attribute, x86

  .. index:: functions that are passed arguments in registers on x86-32

  On x86-32 targets, the ``regparm`` attribute causes the compiler to
  pass arguments number one to ``number`` if they are of integral type
  in registers EAX, EDX, and ECX instead of on the stack.  Functions that
  take a variable number of arguments continue to be passed all of their
  arguments on the stack.

  Beware that on some ELF systems this attribute is unsuitable for
  global functions in shared libraries with lazy binding (which is the
  default).  Lazy binding sends the first call via resolving code in
  the loader, which might assume EAX, EDX and ECX can be clobbered, as
  per the standard calling conventions.  Solaris 8 is affected by this.
  Systems with the GNU C Library version 2.1 or higher
  and FreeBSD are believed to be
  safe since the loaders there save EAX, EDX and ECX.  (Lazy binding can be
  disabled with the linker or the loader if desired, to avoid the
  problem.)

sseregparm

  .. index:: sseregparm function attribute, x86

  On x86-32 targets with SSE support, the ``sseregparm`` attribute
  causes the compiler to pass up to 3 floating-point arguments in
  SSE registers instead of on the stack.  Functions that take a
  variable number of arguments continue to pass all of their
  floating-point arguments on the stack.

force_align_arg_pointer

  .. index:: force_align_arg_pointer function attribute, x86

  On x86 targets, the ``force_align_arg_pointer`` attribute may be
  applied to individual function definitions, generating an alternate
  prologue and epilogue that realigns the run-time stack if necessary.
  This supports mixing legacy codes that run with a 4-byte aligned stack
  with modern codes that keep a 16-byte stack for SSE compatibility.

stdcall

  .. index:: stdcall function attribute, x86-32

  .. index:: functions that pop the argument stack on x86-32

  On x86-32 targets, the ``stdcall`` attribute causes the compiler to
  assume that the called function pops off the stack space used to
  pass arguments, unless it takes a variable number of arguments.

target (``options``)

  .. index:: target function attribute

  As discussed in Common Function Attributes, this attribute 
  allows specification of target-specific compilation options.

  On the x86, the following options are allowed:

  abm no-abm

    .. index:: target("abm") function attribute, x86

    Enable/disable the generation of the advanced bit instructions.

  aes no-aes

    .. index:: target("aes") function attribute, x86

    Enable/disable the generation of the AES instructions.

  default

    .. index:: target("default") function attribute, x86

    See :ref:`function-multiversioning`, where it is used to specify the
    default function version.

  mmx no-mmx

    .. index:: target("mmx") function attribute, x86

    Enable/disable the generation of the MMX instructions.

  pclmul no-pclmul

    .. index:: target("pclmul") function attribute, x86

    Enable/disable the generation of the PCLMUL instructions.

  popcnt no-popcnt

    .. index:: target("popcnt") function attribute, x86

    Enable/disable the generation of the POPCNT instruction.

  sse no-sse

    .. index:: target("sse") function attribute, x86

    Enable/disable the generation of the SSE instructions.

  sse2 no-sse2

    .. index:: target("sse2") function attribute, x86

    Enable/disable the generation of the SSE2 instructions.

  sse3 no-sse3

    .. index:: target("sse3") function attribute, x86

    Enable/disable the generation of the SSE3 instructions.

  sse4 no-sse4

    .. index:: target("sse4") function attribute, x86

    Enable/disable the generation of the SSE4 instructions (both SSE4.1
    and SSE4.2).

  sse4.1 no-sse4.1

    .. index:: target("sse4.1") function attribute, x86

    Enable/disable the generation of the sse4.1 instructions.

  sse4.2 no-sse4.2

    .. index:: target("sse4.2") function attribute, x86

    Enable/disable the generation of the sse4.2 instructions.

  sse4a no-sse4a

    .. index:: target("sse4a") function attribute, x86

    Enable/disable the generation of the SSE4A instructions.

  fma4 no-fma4

    .. index:: target("fma4") function attribute, x86

    Enable/disable the generation of the FMA4 instructions.

  xop no-xop

    .. index:: target("xop") function attribute, x86

    Enable/disable the generation of the XOP instructions.

  lwp no-lwp

    .. index:: target("lwp") function attribute, x86

    Enable/disable the generation of the LWP instructions.

  ssse3 no-ssse3

    .. index:: target("ssse3") function attribute, x86

    Enable/disable the generation of the SSSE3 instructions.

  cld no-cld

    .. index:: target("cld") function attribute, x86

    Enable/disable the generation of the CLD before string moves.

  fancy-math-387 no-fancy-math-387

    .. index:: target("fancy-math-387") function attribute, x86

    Enable/disable the generation of the ``sin``, ``cos``, and
    ``sqrt`` instructions on the 387 floating-point unit.

  fused-madd no-fused-madd

    .. index:: target("fused-madd") function attribute, x86

    Enable/disable the generation of the fused multiply/add instructions.

  ieee-fp no-ieee-fp

    .. index:: target("ieee-fp") function attribute, x86

    Enable/disable the generation of floating point that depends on IEEE arithmetic.

  inline-all-stringops no-inline-all-stringops

    .. index:: target("inline-all-stringops") function attribute, x86

    Enable/disable inlining of string operations.

  inline-stringops-dynamically no-inline-stringops-dynamically

    .. index:: target("inline-stringops-dynamically") function attribute, x86

    Enable/disable the generation of the inline code to do small string
    operations and calling the library routines for large operations.

  align-stringops no-align-stringops

    .. index:: target("align-stringops") function attribute, x86

    Do/do not align destination of inlined string operations.

  recip no-recip

    .. index:: target("recip") function attribute, x86

    Enable/disable the generation of RCPSS, RCPPS, RSQRTSS and RSQRTPS
    instructions followed an additional Newton-Raphson step instead of
    doing a floating-point division.

  arch=``ARCH``

    .. index:: target("arch=ARCH") function attribute, x86

    Specify the architecture to generate code for in compiling the function.

  tune=``TUNE``

    .. index:: target("tune=TUNE") function attribute, x86

    Specify the architecture to tune for in compiling the function.

  fpmath=``FPMATH``

    .. index:: target("fpmath=FPMATH") function attribute, x86

    Specify which floating-point unit to use.  You must specify the
    ``target("fpmath=sse,387")`` option as
    ``target("fpmath=sse+387")`` because the comma would separate
    different options.

    On the x86, the inliner does not inline a
  function that has different target options than the caller, unless the
  callee has a subset of the target options of the caller.  For example
  a function declared with ``target("sse3")`` can inline a function
  with ``target("sse2")``, since ``-msse3`` implies ``-msse2``.

  .. _xstormy16-function-attributes:

Xstormy16 Function Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These function attributes are supported by the Xstormy16 back end:

interrupt

  .. index:: interrupt function attribute, Xstormy16

  Use this attribute to indicate
  that the specified function is an interrupt handler.  The compiler generates
  function entry and exit sequences suitable for use in an interrupt handler
  when this attribute is present.

