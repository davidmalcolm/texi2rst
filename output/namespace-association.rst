
Namespace Association
*********************

Caution: The semantics of this extension are equivalent
to C++ 2011 inline namespaces.  Users should use inline namespaces
instead as this extension will be removed in future versions of G++.

A using-directive with ``__attribute ((strong))`` is stronger
than a normal using-directive in two ways:

* Templates from the used namespace can be specialized and explicitly
  instantiated as though they were members of the using namespace.

* The using namespace is considered an associated namespace of all
  templates in the used namespace for purposes of argument-dependent
  name lookup.

The used namespace must be nested within the using namespace so that
normal unqualified lookup works properly.

This is useful for composing a namespace transparently from
implementation namespaces.  For example:

.. code-block:: c++

  namespace std {
    namespace debug {
      template <class T> struct A { };
    }
    using namespace debug __attribute ((__strong__));
    template <> struct A<int> { };   // OK to specialize

    template <class T> void f (A<T>);
  }

  int main()
  {
    f (std::A<float>());             // lookup finds std::f
    f (std::A<int>());
  }

