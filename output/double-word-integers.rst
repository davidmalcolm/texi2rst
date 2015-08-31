.. _long-long:

Double-Word Integers
********************

.. index:: long long data types

.. index:: double-word arithmetic

.. index:: multiprecision arithmetic

.. index:: LL integer suffix

.. index:: ULL integer suffix

ISO C99 supports data types for integers that are at least 64 bits wide,
and as an extension GCC supports them in C90 mode and in C++.
Simply write ``long long int`` for a signed integer, or
``unsigned long long int`` for an unsigned integer.  To make an
integer constant of type ``long long int``, add the suffix :samp:`LL`
to the integer.  To make an integer constant of type ``unsigned long
long int``, add the suffix :samp:`ULL` to the integer.

You can use these types in arithmetic like any other integer types.
Addition, subtraction, and bitwise boolean operations on these types
are open-coded on all types of machines.  Multiplication is open-coded
if the machine supports a fullword-to-doubleword widening multiply
instruction.  Division and shifts are open-coded only on machines that
provide special support.  The operations that are not open-coded use
special library routines that come with GCC.

There may be pitfalls when you use ``long long`` types for function
arguments without function prototypes.  If a function
expects type ``int`` for its argument, and you pass a value of type
``long long int``, confusion results because the caller and the
subroutine disagree about the number of bytes for the argument.
Likewise, if the function expects ``long long int`` and you pass
``int``.  The best way to avoid such problems is to use prototypes.

