.. _deprecated-features:

Deprecated Features
*******************

In the past, the GNU C++ compiler was extended to experiment with new
features, at a time when the C++ language was still evolving.  Now that
the C++ standard is complete, some of those features are superseded by
superior alternatives.  Using the old features might cause a warning in
some cases that the feature will be dropped in the future.  In other
cases, the feature might be gone already.

While the list below is not exhaustive, it documents some of the options
that are now deprecated:

-fexternal-templates -falt-external-templates
  These are two of the many ways for G++ to implement template
  instantiation.  See :ref:`template-instantiation`.  The C++ standard clearly
  defines how template definitions have to be organized across
  implementation units.  G++ has an implicit instantiation mechanism that
  should work just fine for standard-conforming code.

-fstrict-prototype -fno-strict-prototype
  Previously it was possible to use an empty prototype parameter list to
  indicate an unspecified number of parameters (like C), rather than no
  parameters, as C++ demands.  This feature has been removed, except where
  it is required for backwards compatibility.   See :ref:`backwards-compatibility`.

  G++ allows a virtual function returning void * to be overridden
by one returning a different pointer type.  This extension to the
covariant return type rules is now deprecated and will be removed from a
future version.

The G++ minimum and maximum operators (<? and >?) and
their compound forms (<?=) and >?=) have been deprecated
and are now removed from G++.  Code using these operators should be
modified to use ``std::min`` and ``std::max`` instead.

The named return value extension has been deprecated, and is now
removed from G++.

The use of initializer lists with new expressions has been deprecated,
and is now removed from G++.

Floating and complex non-type template parameters have been deprecated,
and are now removed from G++.

The implicit typename extension has been deprecated and is now
removed from G++.

The use of default arguments in function pointers, function typedefs
and other places where they are not permitted by the standard is
deprecated and will be removed from a future version of G++.

G++ allows floating-point literals to appear in integral constant expressions,
e.g.  enum E { e = int(2.2 * 3.7) } 
This extension is deprecated and will be removed from a future version.

G++ allows static data members of const floating-point type to be declared
with an initializer in a class definition. The standard only allows
initializers for static members of const integral types and const
enumeration types so this extension has been deprecated and will be removed
from a future version.

