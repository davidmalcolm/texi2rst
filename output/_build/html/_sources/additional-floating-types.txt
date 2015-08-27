Additional Floating Types
*************************

.. index:: additional floating types

``__float80`` data type
``__float128`` data type
``w`` floating point suffix
``q`` floating point suffix
``W`` floating point suffix
``Q`` floating point suffix

As an extension, GNU C supports additional floating
types, ``__float80`` and ``__float128`` to support 80-bit
(``XFmode``) and 128-bit (``TFmode``) floating types.
Support for additional types includes the arithmetic operators:
add, subtract, multiply, divide; unary arithmetic operators;
relational operators; equality operators; and conversions to and from
integer and other floating types.  Use a suffix w or W
in a literal constant of type ``__float80`` and q or Q
for ``_float128``.  You can declare complex types using the
corresponding internal complex type, ``XCmode`` for ``__float80``
type and ``TCmode`` for ``__float128`` type:

.. code-block:: c++

  typedef _Complex float __attribute__((mode(TC))) _Complex128;
  typedef _Complex float __attribute__((mode(XC))) _Complex80;

Not all targets support additional floating-point types.  ``__float80``
and ``__float128`` types are supported on x86 and IA-64 targets.
The ``__float128`` type is supported on hppa HP-UX targets.

