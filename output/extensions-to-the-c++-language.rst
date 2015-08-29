.. _c++-extensions:

Extensions to the C++ Language
------------------------------

.. index:: extensions, C++ language

.. index:: C++ language extensions

The GNU compiler provides these extensions to the C++ language (and you
can also use most of the C language extensions in your C++ programs).  If you
want to write code that checks whether these features are available, you can
test for the GNU compiler the same way as for C programs: check for a
predefined macro ``__GNUC__``.  You can also use ``__GNUG__`` to
test specifically for GNU C++ (see :ref:`Predefined Macros <common-predefined-macros>`).

.. toctree::

  What constitutes an access to a volatile object. <c++-volatiles>
  C99 restricted pointers and references. <restricted-pointers>
  Where G++ puts inlines, vtables and such. <vague-linkage>
  You can use a single C++ header file for both
                          declarations and definitions. <c++-interface>
  Methods for ensuring that exactly one copy of
                          each needed template instantiation is emitted. <template-instantiation>
  You can extract a function pointer to the
                          method denoted by a ->* or .* expression. <bound-member-functions>
  Variable, function, and type attributes for C++ only. <c++-attributes>
  Declaring multiple function versions. <function-multiversioning>
  Strong using-directives for namespace association. <namespace-association>
  Compiler support for type traits <type-traits>
  Tweaking exception handling to work with Java. <java-exceptions>
  Things will disappear from G++. <deprecated-features>
  Compatibilities with earlier definitions of C++. <backwards-compatibility>

.. toctree::

  when-is-a-volatile-c++-object-accessed?
  restricting-pointer-aliasing
  vague-linkage
  c++-interface-and-implementation-pragmas
  where's-the-template?
  extracting-the-function-pointer-from-a-bound-pointer-to-member-function
  c++-specific-variable,-function,-and-type-attributes
  function-multiversioning
  namespace-association
  type-traits
  java-exceptions
  deprecated-features
  backwards-compatibility

