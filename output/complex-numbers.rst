.. _complex:

Complex Numbers
***************

.. index:: complex numbers

.. index:: _Complex keyword

.. index:: __complex__ keyword

ISO C99 supports complex floating data types, and as an extension GCC
supports them in C90 mode and in C++.  GCC also supports complex integer data
types which are not part of ISO C99.  You can declare complex types
using the keyword ``_Complex``.  As an extension, the older GNU
keyword ``__complex__`` is also supported.

For example, :samp:`_Complex double x;` declares ``x`` as a
variable whose real part and imaginary part are both of type
``double``.  :samp:`_Complex short int y;` declares ``y`` to
have real and imaginary parts of type ``short int``; this is not
likely to be useful, but it shows that the set of complex types is
complete.

To write a constant with a complex data type, use the suffix :samp:`i` or
:samp:`j` (either one; they are equivalent).  For example, ``2.5fi``
has type ``_Complex float`` and ``3i`` has type
``_Complex int``.  Such a constant always has a pure imaginary
value, but you can form any complex value you like by adding one to a
real constant.  This is a GNU extension; if you have an ISO C99
conforming C library (such as the GNU C Library), and want to construct complex
constants of floating type, you should include ``<complex.h>`` and
use the macros ``I`` or ``_Complex_I`` instead.

.. index:: __real__ keyword

.. index:: __imag__ keyword

To extract the real part of a complex-valued expression ``exp``, write
``__real__ ``exp````.  Likewise, use ``__imag__`` to
extract the imaginary part.  This is a GNU extension; for values of
floating type, you should use the ISO C99 functions ``crealf``,
``creal``, ``creall``, ``cimagf``, ``cimag`` and
``cimagl``, declared in ``<complex.h>`` and also provided as
built-in functions by GCC.

.. index:: complex conjugation

The operator :samp:`~` performs complex conjugation when used on a value
with a complex type.  This is a GNU extension; for values of
floating type, you should use the ISO C99 functions ``conjf``,
``conj`` and ``conjl``, declared in ``<complex.h>`` and also
provided as built-in functions by GCC.

GCC can allocate complex automatic variables in a noncontiguous
fashion; it's even possible for the real part to be in a register while
the imaginary part is on the stack (or vice versa).  Only the DWARF 2
debug info format can represent this, so use of DWARF 2 is recommended.
If you are using the stabs debug info format, GCC describes a noncontiguous
complex variable as if it were two separate variables of noncomplex type.
If the variable's actual name is ``foo``, the two fictitious
variables are named ``foo$real`` and ``foo$imag``.  You can
examine and set these two fictitious variables with your debugger.

