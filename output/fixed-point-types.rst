.. _fixed-point:

Fixed-Point Types
*****************

.. index:: fixed-point types

.. index:: _Fract data type

.. index:: _Accum data type

.. index:: _Sat data type

.. index:: hr fixed-suffix

.. index:: r fixed-suffix

.. index:: lr fixed-suffix

.. index:: llr fixed-suffix

.. index:: uhr fixed-suffix

.. index:: ur fixed-suffix

.. index:: ulr fixed-suffix

.. index:: ullr fixed-suffix

.. index:: hk fixed-suffix

.. index:: k fixed-suffix

.. index:: lk fixed-suffix

.. index:: llk fixed-suffix

.. index:: uhk fixed-suffix

.. index:: uk fixed-suffix

.. index:: ulk fixed-suffix

.. index:: ullk fixed-suffix

.. index:: HR fixed-suffix

.. index:: R fixed-suffix

.. index:: LR fixed-suffix

.. index:: LLR fixed-suffix

.. index:: UHR fixed-suffix

.. index:: UR fixed-suffix

.. index:: ULR fixed-suffix

.. index:: ULLR fixed-suffix

.. index:: HK fixed-suffix

.. index:: K fixed-suffix

.. index:: LK fixed-suffix

.. index:: LLK fixed-suffix

.. index:: UHK fixed-suffix

.. index:: UK fixed-suffix

.. index:: ULK fixed-suffix

.. index:: ULLK fixed-suffix

As an extension, GNU C supports fixed-point types as
defined in the N1169 draft of ISO/IEC DTR 18037.  Support for fixed-point
types in GCC will evolve as the draft technical report changes.
Calling conventions for any target might also change.  Not all targets
support fixed-point types.

The fixed-point types are
``short _Fract``,
``_Fract``,
``long _Fract``,
``long long _Fract``,
``unsigned short _Fract``,
``unsigned _Fract``,
``unsigned long _Fract``,
``unsigned long long _Fract``,
``_Sat short _Fract``,
``_Sat _Fract``,
``_Sat long _Fract``,
``_Sat long long _Fract``,
``_Sat unsigned short _Fract``,
``_Sat unsigned _Fract``,
``_Sat unsigned long _Fract``,
``_Sat unsigned long long _Fract``,
``short _Accum``,
``_Accum``,
``long _Accum``,
``long long _Accum``,
``unsigned short _Accum``,
``unsigned _Accum``,
``unsigned long _Accum``,
``unsigned long long _Accum``,
``_Sat short _Accum``,
``_Sat _Accum``,
``_Sat long _Accum``,
``_Sat long long _Accum``,
``_Sat unsigned short _Accum``,
``_Sat unsigned _Accum``,
``_Sat unsigned long _Accum``,
``_Sat unsigned long long _Accum``.

Fixed-point data values contain fractional and optional integral parts.
The format of fixed-point data varies and depends on the target machine.

Support for fixed-point types includes:

* prefix and postfix increment and decrement operators (``++``, ``--``)

* unary arithmetic operators (``+``, ``-``, ``!``)

* binary arithmetic operators (``+``, ``-``, ``*``, ``/``)

* binary shift operators (``<<``, ``>>``)

* relational operators (``<``, ``<=``, ``>=``, ``>``)

* equality operators (``==``, ``!=``)

* assignment operators (``+=``, ``-=``, ``*=``, ``/=``,
  ``<<=``, ``>>=``)

* conversions to and from integer, floating-point, or fixed-point types

Use a suffix in a fixed-point literal constant:

* :samp:`hr` or :samp:`HR` for ``short _Fract`` and
  ``_Sat short _Fract``

* :samp:`r` or :samp:`R` for ``_Fract`` and ``_Sat _Fract``

* :samp:`lr` or :samp:`LR` for ``long _Fract`` and
  ``_Sat long _Fract``

* :samp:`llr` or :samp:`LLR` for ``long long _Fract`` and
  ``_Sat long long _Fract``

* :samp:`uhr` or :samp:`UHR` for ``unsigned short _Fract`` and
  ``_Sat unsigned short _Fract``

* :samp:`ur` or :samp:`UR` for ``unsigned _Fract`` and
  ``_Sat unsigned _Fract``

* :samp:`ulr` or :samp:`ULR` for ``unsigned long _Fract`` and
  ``_Sat unsigned long _Fract``

* :samp:`ullr` or :samp:`ULLR` for ``unsigned long long _Fract``
  and ``_Sat unsigned long long _Fract``

* :samp:`hk` or :samp:`HK` for ``short _Accum`` and
  ``_Sat short _Accum``

* :samp:`k` or :samp:`K` for ``_Accum`` and ``_Sat _Accum``

* :samp:`lk` or :samp:`LK` for ``long _Accum`` and
  ``_Sat long _Accum``

* :samp:`llk` or :samp:`LLK` for ``long long _Accum`` and
  ``_Sat long long _Accum``

* :samp:`uhk` or :samp:`UHK` for ``unsigned short _Accum`` and
  ``_Sat unsigned short _Accum``

* :samp:`uk` or :samp:`UK` for ``unsigned _Accum`` and
  ``_Sat unsigned _Accum``

* :samp:`ulk` or :samp:`ULK` for ``unsigned long _Accum`` and
  ``_Sat unsigned long _Accum``

* :samp:`ullk` or :samp:`ULLK` for ``unsigned long long _Accum``
  and ``_Sat unsigned long long _Accum``

GCC support of fixed-point types as specified by the draft technical report
is incomplete:

* Pragmas to control overflow and rounding behaviors are not implemented.

Fixed-point types are supported by the DWARF 2 debug information format.

