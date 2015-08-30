.. _c-extensions:

Extensions to the C Language Family
-----------------------------------

.. index:: extensions, C language

.. index:: C language extensions

.. index:: pedantic

GNU C provides several language features not found in ISO standard C.
(The :option:`-pedantic` option directs GCC to print a warning message if
any of these features is used.)  To test for the availability of these
features in conditional compilation, check for a predefined macro
``__GNUC__``, which is always defined under GCC.

These extensions are available in C and Objective-C.  Most of them are
also available in C++.  See :ref:`Extensions to the
C++ Language <c++-extensions>`, for extensions that apply *only* to C++.

Some features that are in ISO C99 but not C90 or C++ are also, as
extensions, accepted by GCC in C90 mode and in C++.

.. toctree::

  Putting statements and declarations inside expressions. <statement-exprs>
  Labels local to a block. <local-labels>
  Getting pointers to labels, and computed gotos. <labels-as-values>
  As in Algol and Pascal, lexical scoping of functions. <nested-functions>
  Dispatching a call to another function. <constructing-calls>
  ``typeof``: referring to the type of an expression. <typeof>
  Omitting the middle operand of a ?: expression. <conditionals>
  128-bit integers-``__int128``. <__int128>
  Double-word integers-``long long int``. <long-long>
  Data types for complex numbers. <complex>
  Additional Floating Types. <floating-types>
  Half-Precision Floating Point. <half-precision>
  Decimal Floating Types. <decimal-float>
  Hexadecimal floating-point constants. <hex-floats>
  Fixed-Point Types. <fixed-point>
  Named address spaces. <named-address-spaces>
  Zero-length arrays. <zero-length>
  Structures with no members. <empty-structures>
  Arrays whose length is computed at run time. <variable-length>
  Macros with a variable number of arguments. <variadic-macros>
  Slightly looser rules for escaped newlines. <escaped-newlines>
  Any array can be subscripted, even if not an lvalue. <subscripting>
  Arithmetic on ``void``-pointers and function pointers. <pointer-arith>
  Pointers to arrays with qualifiers work as expected. <pointers-to-arrays>
  Non-constant initializers. <initializers>
  Compound literals give structures, unions
                          or arrays as values. <compound-literals>
  Labeling elements of initializers. <designated-inits>
  'case 1 ... 9' and such. <case-ranges>
  Casting to union type from any member of the union. <cast-to-union>
  Mixing declarations and code. <mixed-declarations>
  Declaring that functions have no side effects,
                          or that they can never return. <function-attributes>
  Specifying attributes of variables. <variable-attributes>
  Specifying attributes of types. <type-attributes>
  Specifying attributes on labels. <label-attributes>
  Formal syntax for attributes. <attribute-syntax>
  Prototype declarations and old-style definitions. <function-prototypes>
  C++ comments are recognized. <c++-comments>
  Dollar sign is allowed in identifiers. <dollar-signs>
  \e stands for the character ESC. <character-escapes>
  Inquiring about the alignment of a type or variable. <alignment>
  Defining inline functions (as fast as macros). <inline>
  What constitutes an access to a volatile object. <volatiles>
  Instructions and extensions for interfacing C with assembler. <using-assembly-language-with-c>
  ``__const__``, ``__asm__``, etc., for header files. <alternate-keywords>
  ``enum foo;``, with details to follow. <incomplete-enums>
  Printable strings which are the name of the current
                          function. <function-names>
  Getting the return or frame address of a function. <return-address>
  Using vector instructions through built-in functions. <vector-extensions>
  Special syntax for implementing ``offsetof``. <offsetof>
  Legacy built-in functions for atomic memory access. <__sync-builtins>
  Atomic built-in functions with memory model. <__atomic-builtins>
  Built-in functions to perform arithmetics and
                          arithmetic overflow checking. <integer-overflow-builtins>
  x86 memory models. <x86-specific-memory-model-extensions-for-transactional-memory>
  Built-in functions for limited buffer overflow
                          checking. <object-size-checking>
  Built-in functions for Pointer Bounds Checker. <pointer-bounds-checker-builtins>
  Built-in functions for the Cilk Plus language extension. <cilk-plus-builtins>
  Other built-in functions. <other-builtins>
  Built-in functions specific to particular targets. <target-builtins>
  Format checks specific to particular targets. <target-format-checks>
  Pragmas accepted by GCC. <pragmas>
  Unnamed struct/union fields within structs/unions. <unnamed-fields>
  Per-thread variables. <thread-local>
  Binary constants using the 0b prefix. <binary-constants>

.. toctree::

  statements-and-declarations-in-expressions
  locally-declared-labels
  labels-as-values
  nested-functions
  constructing-function-calls
  referring-to-a-type-with-typeof
  conditionals-with-omitted-operands
  128-bit-integers
  double-word-integers
  complex-numbers
  additional-floating-types
  half-precision-floating-point
  decimal-floating-types
  hex-floats
  fixed-point-types
  named-address-spaces
  arrays-of-length-zero
  structures-with-no-members
  arrays-of-variable-length
  macros-with-a-variable-number-of-arguments.
  slightly-looser-rules-for-escaped-newlines
  non-lvalue-arrays-may-have-subscripts
  arithmetic-on-void--and-function-pointers
  pointers-to-arrays-with-qualifiers-work-as-expected
  non-constant-initializers
  compound-literals
  designated-initializers
  case-ranges
  cast-to-a-union-type
  mixed-declarations-and-code
  declaring-attributes-of-functions
  specifying-attributes-of-variables
  specifying-attributes-of-types
  label-attributes
  attribute-syntax
  prototypes-and-old-style-function-definitions
  c++-style-comments
  dollar-signs-in-identifier-names
  the-character-esc-in-constants
  inquiring-on-alignment-of-types-or-variables
  an-inline-function-is-as-fast-as-a-macro
  when-is-a-volatile-object-accessed?
  how-to-use-inline-assembly-language-in-c-code
  alternate-keywords
  incomplete-enum-types
  function-names-as-strings
  getting-the-return-or-frame-address-of-a-function
  using-vector-instructions-through-built-in-functions
  support-for-offsetof
  legacy-__sync-built-in-functions-for-atomic-memory-access
  built-in-functions-for-memory-model-aware-atomic-operations
  built-in-functions-to-perform-arithmetic-with-overflow-checking
  x86-specific-memory-model-extensions-for-transactional-memory
  object-size-checking-built-in-functions
  pointer-bounds-checker-built-in-functions
  cilk-plus-c-c++-language-extension-built-in-functions
  other-built-in-functions-provided-by-gcc
  built-in-functions-specific-to-particular-target-machines
  format-checks-specific-to-particular-target-machines
  pragmas-accepted-by-gcc
  unnamed-structure-and-union-fields
  thread-local-storage
  binary-constants-using-the-0b-prefix

