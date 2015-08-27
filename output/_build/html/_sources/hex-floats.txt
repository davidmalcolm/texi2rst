Hex Floats
**********

.. index:: hex floats

ISO C99 supports floating-point numbers written not only in the usual
decimal notation, such as ``1.55e1``, but also numbers such as
``0x1.fp3`` written in hexadecimal format.  As a GNU extension, GCC
supports this in C90 mode (except in some cases when strictly
conforming) and in C++.  In that format the
0x hex introducer and the p or P exponent field are
mandatory.  The exponent is a decimal number that indicates the power of
2 by which the significant part is multiplied.  Thus 0x1.f is

$1 {15\over16}$,

1 15/16,
p3 multiplies it by 8, and the value of ``0x1.fp3``
is the same as ``1.55e1``.

Unlike for floating-point numbers in the decimal notation the exponent
is always required in the hexadecimal notation.  Otherwise the compiler
would not be able to resolve the ambiguity of, e.g., ``0x1.f``.  This
could mean ``1.0f`` or ``1.9375`` since f is also the
extension for floating-point constants of type ``float``.

