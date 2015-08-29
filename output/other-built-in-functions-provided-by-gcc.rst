.. _other-builtins:

Other Built-in Functions Provided by GCC
****************************************

.. index:: built-in functions

.. index:: __builtin_call_with_static_chain

.. index:: __builtin_fpclassify

.. index:: __builtin_isfinite

.. index:: __builtin_isnormal

.. index:: __builtin_isgreater

.. index:: __builtin_isgreaterequal

.. index:: __builtin_isinf_sign

.. index:: __builtin_isless

.. index:: __builtin_islessequal

.. index:: __builtin_islessgreater

.. index:: __builtin_isunordered

.. index:: __builtin_powi

.. index:: __builtin_powif

.. index:: __builtin_powil

.. index:: _Exit

.. index:: _exit

.. index:: abort

.. index:: abs

.. index:: acos

.. index:: acosf

.. index:: acosh

.. index:: acoshf

.. index:: acoshl

.. index:: acosl

.. index:: alloca

.. index:: asin

.. index:: asinf

.. index:: asinh

.. index:: asinhf

.. index:: asinhl

.. index:: asinl

.. index:: atan

.. index:: atan2

.. index:: atan2f

.. index:: atan2l

.. index:: atanf

.. index:: atanh

.. index:: atanhf

.. index:: atanhl

.. index:: atanl

.. index:: bcmp

.. index:: bzero

.. index:: cabs

.. index:: cabsf

.. index:: cabsl

.. index:: cacos

.. index:: cacosf

.. index:: cacosh

.. index:: cacoshf

.. index:: cacoshl

.. index:: cacosl

.. index:: calloc

.. index:: carg

.. index:: cargf

.. index:: cargl

.. index:: casin

.. index:: casinf

.. index:: casinh

.. index:: casinhf

.. index:: casinhl

.. index:: casinl

.. index:: catan

.. index:: catanf

.. index:: catanh

.. index:: catanhf

.. index:: catanhl

.. index:: catanl

.. index:: cbrt

.. index:: cbrtf

.. index:: cbrtl

.. index:: ccos

.. index:: ccosf

.. index:: ccosh

.. index:: ccoshf

.. index:: ccoshl

.. index:: ccosl

.. index:: ceil

.. index:: ceilf

.. index:: ceill

.. index:: cexp

.. index:: cexpf

.. index:: cexpl

.. index:: cimag

.. index:: cimagf

.. index:: cimagl

.. index:: clog

.. index:: clogf

.. index:: clogl

.. index:: conj

.. index:: conjf

.. index:: conjl

.. index:: copysign

.. index:: copysignf

.. index:: copysignl

.. index:: cos

.. index:: cosf

.. index:: cosh

.. index:: coshf

.. index:: coshl

.. index:: cosl

.. index:: cpow

.. index:: cpowf

.. index:: cpowl

.. index:: cproj

.. index:: cprojf

.. index:: cprojl

.. index:: creal

.. index:: crealf

.. index:: creall

.. index:: csin

.. index:: csinf

.. index:: csinh

.. index:: csinhf

.. index:: csinhl

.. index:: csinl

.. index:: csqrt

.. index:: csqrtf

.. index:: csqrtl

.. index:: ctan

.. index:: ctanf

.. index:: ctanh

.. index:: ctanhf

.. index:: ctanhl

.. index:: ctanl

.. index:: dcgettext

.. index:: dgettext

.. index:: drem

.. index:: dremf

.. index:: dreml

.. index:: erf

.. index:: erfc

.. index:: erfcf

.. index:: erfcl

.. index:: erff

.. index:: erfl

.. index:: exit

.. index:: exp

.. index:: exp10

.. index:: exp10f

.. index:: exp10l

.. index:: exp2

.. index:: exp2f

.. index:: exp2l

.. index:: expf

.. index:: expl

.. index:: expm1

.. index:: expm1f

.. index:: expm1l

.. index:: fabs

.. index:: fabsf

.. index:: fabsl

.. index:: fdim

.. index:: fdimf

.. index:: fdiml

.. index:: ffs

.. index:: floor

.. index:: floorf

.. index:: floorl

.. index:: fma

.. index:: fmaf

.. index:: fmal

.. index:: fmax

.. index:: fmaxf

.. index:: fmaxl

.. index:: fmin

.. index:: fminf

.. index:: fminl

.. index:: fmod

.. index:: fmodf

.. index:: fmodl

.. index:: fprintf

.. index:: fprintf_unlocked

.. index:: fputs

.. index:: fputs_unlocked

.. index:: frexp

.. index:: frexpf

.. index:: frexpl

.. index:: fscanf

.. index:: gamma

.. index:: gammaf

.. index:: gammal

.. index:: gamma_r

.. index:: gammaf_r

.. index:: gammal_r

.. index:: gettext

.. index:: hypot

.. index:: hypotf

.. index:: hypotl

.. index:: ilogb

.. index:: ilogbf

.. index:: ilogbl

.. index:: imaxabs

.. index:: index

.. index:: isalnum

.. index:: isalpha

.. index:: isascii

.. index:: isblank

.. index:: iscntrl

.. index:: isdigit

.. index:: isgraph

.. index:: islower

.. index:: isprint

.. index:: ispunct

.. index:: isspace

.. index:: isupper

.. index:: iswalnum

.. index:: iswalpha

.. index:: iswblank

.. index:: iswcntrl

.. index:: iswdigit

.. index:: iswgraph

.. index:: iswlower

.. index:: iswprint

.. index:: iswpunct

.. index:: iswspace

.. index:: iswupper

.. index:: iswxdigit

.. index:: isxdigit

.. index:: j0

.. index:: j0f

.. index:: j0l

.. index:: j1

.. index:: j1f

.. index:: j1l

.. index:: jn

.. index:: jnf

.. index:: jnl

.. index:: labs

.. index:: ldexp

.. index:: ldexpf

.. index:: ldexpl

.. index:: lgamma

.. index:: lgammaf

.. index:: lgammal

.. index:: lgamma_r

.. index:: lgammaf_r

.. index:: lgammal_r

.. index:: llabs

.. index:: llrint

.. index:: llrintf

.. index:: llrintl

.. index:: llround

.. index:: llroundf

.. index:: llroundl

.. index:: log

.. index:: log10

.. index:: log10f

.. index:: log10l

.. index:: log1p

.. index:: log1pf

.. index:: log1pl

.. index:: log2

.. index:: log2f

.. index:: log2l

.. index:: logb

.. index:: logbf

.. index:: logbl

.. index:: logf

.. index:: logl

.. index:: lrint

.. index:: lrintf

.. index:: lrintl

.. index:: lround

.. index:: lroundf

.. index:: lroundl

.. index:: malloc

.. index:: memchr

.. index:: memcmp

.. index:: memcpy

.. index:: mempcpy

.. index:: memset

.. index:: modf

.. index:: modff

.. index:: modfl

.. index:: nearbyint

.. index:: nearbyintf

.. index:: nearbyintl

.. index:: nextafter

.. index:: nextafterf

.. index:: nextafterl

.. index:: nexttoward

.. index:: nexttowardf

.. index:: nexttowardl

.. index:: pow

.. index:: pow10

.. index:: pow10f

.. index:: pow10l

.. index:: powf

.. index:: powl

.. index:: printf

.. index:: printf_unlocked

.. index:: putchar

.. index:: puts

.. index:: remainder

.. index:: remainderf

.. index:: remainderl

.. index:: remquo

.. index:: remquof

.. index:: remquol

.. index:: rindex

.. index:: rint

.. index:: rintf

.. index:: rintl

.. index:: round

.. index:: roundf

.. index:: roundl

.. index:: scalb

.. index:: scalbf

.. index:: scalbl

.. index:: scalbln

.. index:: scalblnf

.. index:: scalblnf

.. index:: scalbn

.. index:: scalbnf

.. index:: scanfnl

.. index:: signbit

.. index:: signbitf

.. index:: signbitl

.. index:: signbitd32

.. index:: signbitd64

.. index:: signbitd128

.. index:: significand

.. index:: significandf

.. index:: significandl

.. index:: sin

.. index:: sincos

.. index:: sincosf

.. index:: sincosl

.. index:: sinf

.. index:: sinh

.. index:: sinhf

.. index:: sinhl

.. index:: sinl

.. index:: snprintf

.. index:: sprintf

.. index:: sqrt

.. index:: sqrtf

.. index:: sqrtl

.. index:: sscanf

.. index:: stpcpy

.. index:: stpncpy

.. index:: strcasecmp

.. index:: strcat

.. index:: strchr

.. index:: strcmp

.. index:: strcpy

.. index:: strcspn

.. index:: strdup

.. index:: strfmon

.. index:: strftime

.. index:: strlen

.. index:: strncasecmp

.. index:: strncat

.. index:: strncmp

.. index:: strncpy

.. index:: strndup

.. index:: strpbrk

.. index:: strrchr

.. index:: strspn

.. index:: strstr

.. index:: tan

.. index:: tanf

.. index:: tanh

.. index:: tanhf

.. index:: tanhl

.. index:: tanl

.. index:: tgamma

.. index:: tgammaf

.. index:: tgammal

.. index:: toascii

.. index:: tolower

.. index:: toupper

.. index:: towlower

.. index:: towupper

.. index:: trunc

.. index:: truncf

.. index:: truncl

.. index:: vfprintf

.. index:: vfscanf

.. index:: vprintf

.. index:: vscanf

.. index:: vsnprintf

.. index:: vsprintf

.. index:: vsscanf

.. index:: y0

.. index:: y0f

.. index:: y0l

.. index:: y1

.. index:: y1f

.. index:: y1l

.. index:: yn

.. index:: ynf

.. index:: ynl

GCC provides a large number of built-in functions other than the ones
mentioned above.  Some of these are for internal use in the processing
of exceptions or variable-length argument lists and are not
documented here because they may change from time to time; we do not
recommend general use of these functions.

The remaining functions are provided for optimization purposes.

.. index:: fno-builtin

GCC includes built-in versions of many of the functions in the standard
C library.  The versions prefixed with ``__builtin_`` are always
treated as having the same meaning as the C library function even if you
specify the :option:`-fno-builtin` option.  (see :ref:`c-dialect-options`)
Many of these functions are only optimized in certain cases; if they are
not optimized in a particular case, a call to the library function is
emitted.

.. index:: ansi

.. index:: std

Outside strict ISO C mode (:option:`-ansi`, :option:`-std=c90`,
:option:`-std=c99` or :option:`-std=c11`), the functions
``_exit``, ``alloca``, ``bcmp``, ``bzero``,
``dcgettext``, ``dgettext``, ``dremf``, ``dreml``,
``drem``, ``exp10f``, ``exp10l``, ``exp10``, ``ffsll``,
``ffsl``, ``ffs``, ``fprintf_unlocked``,
``fputs_unlocked``, ``gammaf``, ``gammal``, ``gamma``,
``gammaf_r``, ``gammal_r``, ``gamma_r``, ``gettext``,
``index``, ``isascii``, ``j0f``, ``j0l``, ``j0``,
``j1f``, ``j1l``, ``j1``, ``jnf``, ``jnl``, ``jn``,
``lgammaf_r``, ``lgammal_r``, ``lgamma_r``, ``mempcpy``,
``pow10f``, ``pow10l``, ``pow10``, ``printf_unlocked``,
``rindex``, ``scalbf``, ``scalbl``, ``scalb``,
``signbit``, ``signbitf``, ``signbitl``, ``signbitd32``,
``signbitd64``, ``signbitd128``, ``significandf``,
``significandl``, ``significand``, ``sincosf``,
``sincosl``, ``sincos``, ``stpcpy``, ``stpncpy``,
``strcasecmp``, ``strdup``, ``strfmon``, ``strncasecmp``,
``strndup``, ``toascii``, ``y0f``, ``y0l``, ``y0``,
``y1f``, ``y1l``, ``y1``, ``ynf``, ``ynl`` and
``yn``
may be handled as built-in functions.
All these functions have corresponding versions
prefixed with ``__builtin_``, which may be used even in strict C90
mode.

The ISO C99 functions
``_Exit``, ``acoshf``, ``acoshl``, ``acosh``, ``asinhf``,
``asinhl``, ``asinh``, ``atanhf``, ``atanhl``, ``atanh``,
``cabsf``, ``cabsl``, ``cabs``, ``cacosf``, ``cacoshf``,
``cacoshl``, ``cacosh``, ``cacosl``, ``cacos``,
``cargf``, ``cargl``, ``carg``, ``casinf``, ``casinhf``,
``casinhl``, ``casinh``, ``casinl``, ``casin``,
``catanf``, ``catanhf``, ``catanhl``, ``catanh``,
``catanl``, ``catan``, ``cbrtf``, ``cbrtl``, ``cbrt``,
``ccosf``, ``ccoshf``, ``ccoshl``, ``ccosh``, ``ccosl``,
``ccos``, ``cexpf``, ``cexpl``, ``cexp``, ``cimagf``,
``cimagl``, ``cimag``, ``clogf``, ``clogl``, ``clog``,
``conjf``, ``conjl``, ``conj``, ``copysignf``, ``copysignl``,
``copysign``, ``cpowf``, ``cpowl``, ``cpow``, ``cprojf``,
``cprojl``, ``cproj``, ``crealf``, ``creall``, ``creal``,
``csinf``, ``csinhf``, ``csinhl``, ``csinh``, ``csinl``,
``csin``, ``csqrtf``, ``csqrtl``, ``csqrt``, ``ctanf``,
``ctanhf``, ``ctanhl``, ``ctanh``, ``ctanl``, ``ctan``,
``erfcf``, ``erfcl``, ``erfc``, ``erff``, ``erfl``,
``erf``, ``exp2f``, ``exp2l``, ``exp2``, ``expm1f``,
``expm1l``, ``expm1``, ``fdimf``, ``fdiml``, ``fdim``,
``fmaf``, ``fmal``, ``fmaxf``, ``fmaxl``, ``fmax``,
``fma``, ``fminf``, ``fminl``, ``fmin``, ``hypotf``,
``hypotl``, ``hypot``, ``ilogbf``, ``ilogbl``, ``ilogb``,
``imaxabs``, ``isblank``, ``iswblank``, ``lgammaf``,
``lgammal``, ``lgamma``, ``llabs``, ``llrintf``, ``llrintl``,
``llrint``, ``llroundf``, ``llroundl``, ``llround``,
``log1pf``, ``log1pl``, ``log1p``, ``log2f``, ``log2l``,
``log2``, ``logbf``, ``logbl``, ``logb``, ``lrintf``,
``lrintl``, ``lrint``, ``lroundf``, ``lroundl``,
``lround``, ``nearbyintf``, ``nearbyintl``, ``nearbyint``,
``nextafterf``, ``nextafterl``, ``nextafter``,
``nexttowardf``, ``nexttowardl``, ``nexttoward``,
``remainderf``, ``remainderl``, ``remainder``, ``remquof``,
``remquol``, ``remquo``, ``rintf``, ``rintl``, ``rint``,
``roundf``, ``roundl``, ``round``, ``scalblnf``,
``scalblnl``, ``scalbln``, ``scalbnf``, ``scalbnl``,
``scalbn``, ``snprintf``, ``tgammaf``, ``tgammal``,
``tgamma``, ``truncf``, ``truncl``, ``trunc``,
``vfscanf``, ``vscanf``, ``vsnprintf`` and ``vsscanf``
are handled as built-in functions
except in strict ISO C90 mode (:option:`-ansi` or :option:`-std=c90`).

There are also built-in versions of the ISO C99 functions
``acosf``, ``acosl``, ``asinf``, ``asinl``, ``atan2f``,
``atan2l``, ``atanf``, ``atanl``, ``ceilf``, ``ceill``,
``cosf``, ``coshf``, ``coshl``, ``cosl``, ``expf``,
``expl``, ``fabsf``, ``fabsl``, ``floorf``, ``floorl``,
``fmodf``, ``fmodl``, ``frexpf``, ``frexpl``, ``ldexpf``,
``ldexpl``, ``log10f``, ``log10l``, ``logf``, ``logl``,
``modfl``, ``modf``, ``powf``, ``powl``, ``sinf``,
``sinhf``, ``sinhl``, ``sinl``, ``sqrtf``, ``sqrtl``,
``tanf``, ``tanhf``, ``tanhl`` and ``tanl``
that are recognized in any mode since ISO C90 reserves these names for
the purpose to which ISO C99 puts them.  All these functions have
corresponding versions prefixed with ``__builtin_``.

The ISO C94 functions
``iswalnum``, ``iswalpha``, ``iswcntrl``, ``iswdigit``,
``iswgraph``, ``iswlower``, ``iswprint``, ``iswpunct``,
``iswspace``, ``iswupper``, ``iswxdigit``, ``towlower`` and
``towupper``
are handled as built-in functions
except in strict ISO C90 mode (:option:`-ansi` or :option:`-std=c90`).

The ISO C90 functions
``abort``, ``abs``, ``acos``, ``asin``, ``atan2``,
``atan``, ``calloc``, ``ceil``, ``cosh``, ``cos``,
``exit``, ``exp``, ``fabs``, ``floor``, ``fmod``,
``fprintf``, ``fputs``, ``frexp``, ``fscanf``,
``isalnum``, ``isalpha``, ``iscntrl``, ``isdigit``,
``isgraph``, ``islower``, ``isprint``, ``ispunct``,
``isspace``, ``isupper``, ``isxdigit``, ``tolower``,
``toupper``, ``labs``, ``ldexp``, ``log10``, ``log``,
``malloc``, ``memchr``, ``memcmp``, ``memcpy``,
``memset``, ``modf``, ``pow``, ``printf``, ``putchar``,
``puts``, ``scanf``, ``sinh``, ``sin``, ``snprintf``,
``sprintf``, ``sqrt``, ``sscanf``, ``strcat``,
``strchr``, ``strcmp``, ``strcpy``, ``strcspn``,
``strlen``, ``strncat``, ``strncmp``, ``strncpy``,
``strpbrk``, ``strrchr``, ``strspn``, ``strstr``,
``tanh``, ``tan``, ``vfprintf``, ``vprintf`` and ``vsprintf``
are all recognized as built-in functions unless
:option:`-fno-builtin` is specified (or :option:`-fno-builtin-``function```
is specified for an individual function).  All of these functions have
corresponding versions prefixed with ``__builtin_``.

GCC provides built-in versions of the ISO C99 floating-point comparison
macros that avoid raising exceptions for unordered operands.  They have
the same names as the standard macros ( ``isgreater``,
``isgreaterequal``, ``isless``, ``islessequal``,
``islessgreater``, and ``isunordered``) , with ``__builtin_``
prefixed.  We intend for a library implementor to be able to simply
``#define`` each standard macro to its built-in equivalent.
In the same fashion, GCC provides ``fpclassify``, ``isfinite``,
``isinf_sign`` and ``isnormal`` built-ins used with
``__builtin_`` prefixed.  The ``isinf`` and ``isnan``
built-in functions appear both with and without the ``__builtin_`` prefix.

.. index:: __builtin_types_compatible_p

Built-in Functionint__builtin_types_compatible_p(``type1``,``type2``)You can use the built-in function ``__builtin_types_compatible_p`` to
determine whether two types are the same.

This built-in function returns 1 if the unqualified versions of the
types ``type1`` and ``type2`` (which are types, not expressions) are
compatible, 0 otherwise.  The result of this built-in function can be
used in integer constant expressions.

This built-in function ignores top level qualifiers (e.g., ``const``,
``volatile``).  For example, ``int`` is equivalent to ``const
int``.

The type ``int[]`` and ``int[5]`` are compatible.  On the other
hand, ``int`` and ``char *`` are not compatible, even if the size
of their types, on the particular architecture are the same.  Also, the
amount of pointer indirection is taken into account when determining
similarity.  Consequently, ``short *`` is not similar to
``short **``.  Furthermore, two types that are typedefed are
considered compatible if their underlying types are compatible.

An ``enum`` type is not considered to be compatible with another
``enum`` type even if both are compatible with the same integer
type; this is what the C standard specifies.
For example, ``enum {foo, bar}`` is not similar to
``enum {hot, dog}``.

You typically use this function in code whose execution varies
depending on the arguments' types.  For example:

.. code-block:: c++

  #define foo(x)                                                  \
    ({                                                           \
      typeof (x) tmp = (x);                                       \
      if (__builtin_types_compatible_p (typeof (x), long double)) \
        tmp = foo_long_double (tmp);                              \
      else if (__builtin_types_compatible_p (typeof (x), double)) \
        tmp = foo_double (tmp);                                   \
      else if (__builtin_types_compatible_p (typeof (x), float))  \
        tmp = foo_float (tmp);                                    \
      else                                                        \
        abort ();                                                 \
      tmp;                                                        \
    })

Note: This construct is only available for C.

.. index:: __builtin_call_with_static_chain

Built-in Function``type``__builtin_call_with_static_chain(``call_exp``,``pointer_exp``)The ``call_exp`` expression must be a function call, and the
``pointer_exp`` expression must be a pointer.  The ``pointer_exp``
is passed to the function call in the target's static chain location.
The result of builtin is the result of the function call.

Note: This builtin is only available for C.
This builtin can be used to call Go closures from C.

.. index:: __builtin_choose_expr

Built-in Function``type``__builtin_choose_expr(``const_exp``,``exp1``,``exp2``)You can use the built-in function ``__builtin_choose_expr`` to
evaluate code depending on the value of a constant expression.  This
built-in function returns ``exp1`` if ``const_exp``, which is an
integer constant expression, is nonzero.  Otherwise it returns ``exp2``.

This built-in function is analogous to the ? : operator in C,
except that the expression returned has its type unaltered by promotion
rules.  Also, the built-in function does not evaluate the expression
that is not chosen.  For example, if ``const_exp`` evaluates to true,
``exp2`` is not evaluated even if it has side-effects.

This built-in function can return an lvalue if the chosen argument is an
lvalue.

If ``exp1`` is returned, the return type is the same as ``exp1``'s
type.  Similarly, if ``exp2`` is returned, its return type is the same
as ``exp2``.

Example:

.. code-block:: c++

  #define foo(x)                                                    \
    __builtin_choose_expr (                                         \
      __builtin_types_compatible_p (typeof (x), double),            \
      foo_double (x),                                               \
      __builtin_choose_expr (                                       \
        __builtin_types_compatible_p (typeof (x), float),           \
        foo_float (x),                                              \
        /* The void expression results in a compile-time error  \
           when assigning the result to something.  */          \
        (void)0))

Note: This construct is only available for C.  Furthermore, the
unused expression (``exp1`` or ``exp2`` depending on the value of
``const_exp``) may still generate syntax errors.  This may change in
future revisions.

.. index:: __builtin_complex

Built-in Function``type``__builtin_complex(``real``,``imag``)The built-in function ``__builtin_complex`` is provided for use in
implementing the ISO C11 macros ``CMPLXF``, ``CMPLX`` and
``CMPLXL``.  ``real`` and ``imag`` must have the same type, a
real binary floating-point type, and the result has the corresponding
complex type with real and imaginary parts ``real`` and ``imag``.
Unlike ``real`` + I * ``imag``, this works even when
infinities, NaNs and negative zeros are involved.

.. index:: __builtin_constant_p

Built-in Functionint__builtin_constant_p(``exp``)You can use the built-in function ``__builtin_constant_p`` to
determine if a value is known to be constant at compile time and hence
that GCC can perform constant-folding on expressions involving that
value.  The argument of the function is the value to test.  The function
returns the integer 1 if the argument is known to be a compile-time
constant and 0 if it is not known to be a compile-time constant.  A
return of 0 does not indicate that the value is not a constant,
but merely that GCC cannot prove it is a constant with the specified
value of the :option:`-O` option.

You typically use this function in an embedded application where
memory is a critical resource.  If you have some complex calculation,
you may want it to be folded if it involves constants, but need to call
a function if it does not.  For example:

.. code-block:: c++

  #define Scale_Value(X)      \
    (__builtin_constant_p (X) \
    ? ((X) * SCALE + OFFSET) : Scale (X))

You may use this built-in function in either a macro or an inline
function.  However, if you use it in an inlined function and pass an
argument of the function as the argument to the built-in, GCC 
never returns 1 when you call the inline function with a string constant
or compound literal (see :ref:`compound-literals`) and does not return 1
when you pass a constant numeric value to the inline function unless you
specify the :option:`-O` option.

You may also use ``__builtin_constant_p`` in initializers for static
data.  For instance, you can write

.. code-block:: c++

  static const int table[] = {
     __builtin_constant_p (EXPRESSION) ? (EXPRESSION) : -1,
     /* ... */
  };

This is an acceptable initializer even if ``EXPRESSION`` is not a
constant expression, including the case where
``__builtin_constant_p`` returns 1 because ``EXPRESSION`` can be
folded to a constant but ``EXPRESSION`` contains operands that are
not otherwise permitted in a static initializer (for example,
``0 && foo ()``).  GCC must be more conservative about evaluating the
built-in in this case, because it has no opportunity to perform
optimization.

.. index:: __builtin_expect

Built-in Functionlong__builtin_expect(long``exp``,long``c``)
.. index:: fprofile-arcs

You may use ``__builtin_expect`` to provide the compiler with
branch prediction information.  In general, you should prefer to
use actual profile feedback for this (:option:`-fprofile-arcs`), as
programmers are notoriously bad at predicting how their programs
actually perform.  However, there are applications in which this
data is hard to collect.

The return value is the value of ``exp``, which should be an integral
expression.  The semantics of the built-in are that it is expected that
``exp`` == ``c``.  For example:

.. code-block:: c++

  if (__builtin_expect (x, 0))
    foo ();

indicates that we do not expect to call ``foo``, since
we expect ``x`` to be zero.  Since you are limited to integral
expressions for ``exp``, you should use constructions such as

.. code-block:: c++

  if (__builtin_expect (ptr != NULL, 1))
    foo (*ptr);

when testing pointer or floating-point values.

.. index:: __builtin_trap

Built-in Functionvoid__builtin_trap(void)This function causes the program to exit abnormally.  GCC implements
this function by using a target-dependent mechanism (such as
intentionally executing an illegal instruction) or by calling
``abort``.  The mechanism used may vary from release to release so
you should not rely on any particular implementation.

.. index:: __builtin_unreachable

Built-in Functionvoid__builtin_unreachable(void)If control flow reaches the point of the ``__builtin_unreachable``,
the program is undefined.  It is useful in situations where the
compiler cannot deduce the unreachability of the code.

One such case is immediately following an ``asm`` statement that
either never terminates, or one that transfers control elsewhere
and never returns.  In this example, without the
``__builtin_unreachable``, GCC issues a warning that control
reaches the end of a non-void function.  It also generates code
to return after the ``asm``.

.. code-block:: c++

  int f (int c, int v)
  {
    if (c)
      {
        return v;
      }
    else
      {
        asm("jmp error_handler");
        __builtin_unreachable ();
      }
  }

Because the ``asm`` statement unconditionally transfers control out
of the function, control never reaches the end of the function
body.  The ``__builtin_unreachable`` is in fact unreachable and
communicates this fact to the compiler.

Another use for ``__builtin_unreachable`` is following a call a
function that never returns but that is not declared
``__attribute__((noreturn))``, as in this example:

.. code-block:: c++

  void function_that_never_returns (void);

  int g (int c)
  {
    if (c)
      {
        return 1;
      }
    else
      {
        function_that_never_returns ();
        __builtin_unreachable ();
      }
  }

.. index:: *__builtin_assume_aligned

Built-in Functionvoid*__builtin_assume_aligned(constvoid*``exp``,size_t``align``,...)This function returns its first argument, and allows the compiler
to assume that the returned pointer is at least ``align`` bytes
aligned.  This built-in can have either two or three arguments,
if it has three, the third argument should have integer type, and
if it is nonzero means misalignment offset.  For example:

.. code-block:: c++

  void *x = __builtin_assume_aligned (arg, 16);

means that the compiler can assume ``x``, set to ``arg``, is at least
16-byte aligned, while:

.. code-block:: c++

  void *x = __builtin_assume_aligned (arg, 32, 8);

means that the compiler can assume for ``x``, set to ``arg``, that
``(char *) x - 8`` is 32-byte aligned.

.. index:: __builtin_LINE

Built-in Functionint__builtin_LINE()This function is the equivalent to the preprocessor ``__LINE__``
macro and returns the line number of the invocation of the built-in.
In a C++ default argument for a function ``F``, it gets the line number of
the call to ``F``.

.. index:: __builtin_FUNCTION

Built-in Functionconst char *__builtin_FUNCTION()This function is the equivalent to the preprocessor ``__FUNCTION__``
macro and returns the function name the invocation of the built-in is in.

.. index:: __builtin_FILE

Built-in Functionconst char *__builtin_FILE()This function is the equivalent to the preprocessor ``__FILE__``
macro and returns the file name the invocation of the built-in is in.
In a C++ default argument for a function ``F``, it gets the file name of
the call to ``F``.

.. index:: __builtin___clear_cache

Built-in Functionvoid__builtin___clear_cache(char*``begin``,char*``end``)This function is used to flush the processor's instruction cache for
the region of memory between ``begin`` inclusive and ``end``
exclusive.  Some targets require that the instruction cache be
flushed, after modifying memory containing code, in order to obtain
deterministic behavior.

If the target does not require instruction cache flushes,
``__builtin___clear_cache`` has no effect.  Otherwise either
instructions are emitted in-line to clear the instruction cache or a
call to the ``__clear_cache`` function in libgcc is made.

.. index:: __builtin_prefetch

Built-in Functionvoid__builtin_prefetch(constvoid*``addr``,...)This function is used to minimize cache-miss latency by moving data into
a cache before it is accessed.
You can insert calls to ``__builtin_prefetch`` into code for which
you know addresses of data in memory that is likely to be accessed soon.
If the target supports them, data prefetch instructions are generated.
If the prefetch is done early enough before the access then the data will
be in the cache by the time it is accessed.

The value of ``addr`` is the address of the memory to prefetch.
There are two optional arguments, ``rw`` and ``locality``.
The value of ``rw`` is a compile-time constant one or zero; one
means that the prefetch is preparing for a write to the memory address
and zero, the default, means that the prefetch is preparing for a read.
The value ``locality`` must be a compile-time constant integer between
zero and three.  A value of zero means that the data has no temporal
locality, so it need not be left in the cache after the access.  A value
of three means that the data has a high degree of temporal locality and
should be left in all levels of cache possible.  Values of one and two
mean, respectively, a low or moderate degree of temporal locality.  The
default is three.

.. code-block:: c++

  for (i = 0; i < n; i++)
    {
      a[i] = a[i] + b[i];
      __builtin_prefetch (&a[i+j], 1, 1);
      __builtin_prefetch (&b[i+j], 0, 1);
      /* ... */
    }

Data prefetch does not generate faults if ``addr`` is invalid, but
the address expression itself must be valid.  For example, a prefetch
of ``p->next`` does not fault if ``p->next`` is not a valid
address, but evaluation faults if ``p`` is not a valid address.

If the target does not support data prefetch, the address expression
is evaluated if it includes side effects but no other code is generated
and GCC does not issue a warning.

.. index:: __builtin_huge_val

Built-in Functiondouble__builtin_huge_val(void)Returns a positive infinity, if supported by the floating-point format,
else ``DBL_MAX``.  This function is suitable for implementing the
ISO C macro ``HUGE_VAL``.

.. index:: __builtin_huge_valf

Built-in Functionfloat__builtin_huge_valf(void)Similar to ``__builtin_huge_val``, except the return type is ``float``.

.. index:: __builtin_huge_vall

Built-in Functionlong double__builtin_huge_vall(void)Similar to ``__builtin_huge_val``, except the return
type is ``long double``.

.. index:: __builtin_fpclassify

Built-in Functionint__builtin_fpclassify(int,int,int,int,int,...)This built-in implements the C99 fpclassify functionality.  The first
five int arguments should be the target library's notion of the
possible FP classes and are used for return values.  They must be
constant values and they must appear in this order: ``FP_NAN``,
``FP_INFINITE``, ``FP_NORMAL``, ``FP_SUBNORMAL`` and
``FP_ZERO``.  The ellipsis is for exactly one floating-point value
to classify.  GCC treats the last argument as type-generic, which
means it does not do default promotion from float to double.

.. index:: __builtin_inf

Built-in Functiondouble__builtin_inf(void)Similar to ``__builtin_huge_val``, except a warning is generated
if the target floating-point format does not support infinities.

.. index:: __builtin_infd32

Built-in Function_Decimal32__builtin_infd32(void)Similar to ``__builtin_inf``, except the return type is ``_Decimal32``.

.. index:: __builtin_infd64

Built-in Function_Decimal64__builtin_infd64(void)Similar to ``__builtin_inf``, except the return type is ``_Decimal64``.

.. index:: __builtin_infd128

Built-in Function_Decimal128__builtin_infd128(void)Similar to ``__builtin_inf``, except the return type is ``_Decimal128``.

.. index:: __builtin_inff

Built-in Functionfloat__builtin_inff(void)Similar to ``__builtin_inf``, except the return type is ``float``.
This function is suitable for implementing the ISO C99 macro ``INFINITY``.

.. index:: __builtin_infl

Built-in Functionlong double__builtin_infl(void)Similar to ``__builtin_inf``, except the return
type is ``long double``.

.. index:: __builtin_isinf_sign

Built-in Functionint__builtin_isinf_sign(...)Similar to ``isinf``, except the return value is -1 for
an argument of ``-Inf`` and 1 for an argument of ``+Inf``.
Note while the parameter list is an
ellipsis, this function only accepts exactly one floating-point
argument.  GCC treats this parameter as type-generic, which means it
does not do default promotion from float to double.

.. index:: __builtin_nan

Built-in Functiondouble__builtin_nan(constchar*str)This is an implementation of the ISO C99 function ``nan``.

Since ISO C99 defines this function in terms of ``strtod``, which we
do not implement, a description of the parsing is in order.  The string
is parsed as by ``strtol``; that is, the base is recognized by
leading 0 or 0x prefixes.  The number parsed is placed
in the significand such that the least significant bit of the number
is at the least significant bit of the significand.  The number is
truncated to fit the significand field provided.  The significand is
forced to be a quiet NaN.

This function, if given a string literal all of which would have been
consumed by ``strtol``, is evaluated early enough that it is considered a
compile-time constant.

.. index:: __builtin_nand32

Built-in Function_Decimal32__builtin_nand32(constchar*str)Similar to ``__builtin_nan``, except the return type is ``_Decimal32``.

.. index:: __builtin_nand64

Built-in Function_Decimal64__builtin_nand64(constchar*str)Similar to ``__builtin_nan``, except the return type is ``_Decimal64``.

.. index:: __builtin_nand128

Built-in Function_Decimal128__builtin_nand128(constchar*str)Similar to ``__builtin_nan``, except the return type is ``_Decimal128``.

.. index:: __builtin_nanf

Built-in Functionfloat__builtin_nanf(constchar*str)Similar to ``__builtin_nan``, except the return type is ``float``.

.. index:: __builtin_nanl

Built-in Functionlong double__builtin_nanl(constchar*str)Similar to ``__builtin_nan``, except the return type is ``long double``.

.. index:: __builtin_nans

Built-in Functiondouble__builtin_nans(constchar*str)Similar to ``__builtin_nan``, except the significand is forced
to be a signaling NaN.  The ``nans`` function is proposed by
http://www.open-std.org/jtc1/sc22/wg14/www/docs/n965.htmWG14 N965.

.. index:: __builtin_nansf

Built-in Functionfloat__builtin_nansf(constchar*str)Similar to ``__builtin_nans``, except the return type is ``float``.

.. index:: __builtin_nansl

Built-in Functionlong double__builtin_nansl(constchar*str)Similar to ``__builtin_nans``, except the return type is ``long double``.

.. index:: __builtin_ffs

Built-in Functionint__builtin_ffs(intx)Returns one plus the index of the least significant 1-bit of ``x``, or
if ``x`` is zero, returns zero.

.. index:: __builtin_clz

Built-in Functionint__builtin_clz(unsignedintx)Returns the number of leading 0-bits in ``x``, starting at the most
significant bit position.  If ``x`` is 0, the result is undefined.

.. index:: __builtin_ctz

Built-in Functionint__builtin_ctz(unsignedintx)Returns the number of trailing 0-bits in ``x``, starting at the least
significant bit position.  If ``x`` is 0, the result is undefined.

.. index:: __builtin_clrsb

Built-in Functionint__builtin_clrsb(intx)Returns the number of leading redundant sign bits in ``x``, i.e. the
number of bits following the most significant bit that are identical
to it.  There are no special cases for 0 or other values. 

.. index:: __builtin_popcount

Built-in Functionint__builtin_popcount(unsignedintx)Returns the number of 1-bits in ``x``.

.. index:: __builtin_parity

Built-in Functionint__builtin_parity(unsignedintx)Returns the parity of ``x``, i.e. the number of 1-bits in ``x``
modulo 2.

.. index:: __builtin_ffsl

Built-in Functionint__builtin_ffsl(long)Similar to ``__builtin_ffs``, except the argument type is
``long``.

.. index:: __builtin_clzl

Built-in Functionint__builtin_clzl(unsignedlong)Similar to ``__builtin_clz``, except the argument type is
``unsigned long``.

.. index:: __builtin_ctzl

Built-in Functionint__builtin_ctzl(unsignedlong)Similar to ``__builtin_ctz``, except the argument type is
``unsigned long``.

.. index:: __builtin_clrsbl

Built-in Functionint__builtin_clrsbl(long)Similar to ``__builtin_clrsb``, except the argument type is
``long``.

.. index:: __builtin_popcountl

Built-in Functionint__builtin_popcountl(unsignedlong)Similar to ``__builtin_popcount``, except the argument type is
``unsigned long``.

.. index:: __builtin_parityl

Built-in Functionint__builtin_parityl(unsignedlong)Similar to ``__builtin_parity``, except the argument type is
``unsigned long``.

.. index:: __builtin_ffsll

Built-in Functionint__builtin_ffsll(longlong)Similar to ``__builtin_ffs``, except the argument type is
``long long``.

.. index:: __builtin_clzll

Built-in Functionint__builtin_clzll(unsignedlonglong)Similar to ``__builtin_clz``, except the argument type is
``unsigned long long``.

.. index:: __builtin_ctzll

Built-in Functionint__builtin_ctzll(unsignedlonglong)Similar to ``__builtin_ctz``, except the argument type is
``unsigned long long``.

.. index:: __builtin_clrsbll

Built-in Functionint__builtin_clrsbll(longlong)Similar to ``__builtin_clrsb``, except the argument type is
``long long``.

.. index:: __builtin_popcountll

Built-in Functionint__builtin_popcountll(unsignedlonglong)Similar to ``__builtin_popcount``, except the argument type is
``unsigned long long``.

.. index:: __builtin_parityll

Built-in Functionint__builtin_parityll(unsignedlonglong)Similar to ``__builtin_parity``, except the argument type is
``unsigned long long``.

.. index:: __builtin_powi

Built-in Functiondouble__builtin_powi(double,int)Returns the first argument raised to the power of the second.  Unlike the
``pow`` function no guarantees about precision and rounding are made.

.. index:: __builtin_powif

Built-in Functionfloat__builtin_powif(float,int)Similar to ``__builtin_powi``, except the argument and return types
are ``float``.

.. index:: __builtin_powil

Built-in Functionlong double__builtin_powil(longdouble,int)Similar to ``__builtin_powi``, except the argument and return types
are ``long double``.

.. index:: __builtin_bswap16

Built-in Functionuint16_t__builtin_bswap16(uint16_tx)Returns ``x`` with the order of the bytes reversed; for example,
``0xaabb`` becomes ``0xbbaa``.  Byte here always means
exactly 8 bits.

.. index:: __builtin_bswap32

Built-in Functionuint32_t__builtin_bswap32(uint32_tx)Similar to ``__builtin_bswap16``, except the argument and return types
are 32 bit.

.. index:: __builtin_bswap64

Built-in Functionuint64_t__builtin_bswap64(uint64_tx)Similar to ``__builtin_bswap32``, except the argument and return types
are 64 bit.

