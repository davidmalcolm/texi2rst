
Backwards Compatibility
***********************

.. index:: Backwards Compatibility

.. index:: ARM [Annotated C++ Reference Manual]

Now that there is a definitive ISO standard C++, G++ has a specification
to adhere to.  The C++ language evolved over time, and features that
used to be acceptable in previous drafts of the standard, such as the ARM
[Annotated C++ Reference Manual], are no longer accepted.  In order to allow
compilation of C++ written to such drafts, G++ contains some backwards
compatibilities.  All such backwards compatibility features are
liable to disappear in future versions of G++. They should be considered
deprecated.   See :ref:`deprecated-features`.

For scope
  If a variable is declared at for scope, it used to remain in scope until
  the end of the scope that contained the for statement (rather than just
  within the for scope).  G++ retains this, but issues a warning, if such a
  variable is accessed outside the for scope.

Implicit C language
  Old C system header files did not contain an ``extern "C" {...}``
  scope to set the language.  On such systems, all header files are
  implicitly scoped inside a C language scope.  Also, an empty prototype
  ``()`` is treated as an unspecified number of arguments, rather
  than no arguments, as C++ demands.

..  LocalWords:  emph deftypefn builtin ARCv2EM SIMD builtins msimd
    LocalWords:  typedef v4si v8hi DMA dma vdiwr vdowr
   Copyright (C) 1988-2015 Free Software Foundation, Inc.
   This is part of the GCC manual.
   For copying conditions, see the file gcc.texi.

