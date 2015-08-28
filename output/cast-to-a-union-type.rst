.. _cast-to-union:

Cast to a Union Type
********************

.. index:: cast to a union

.. index:: union, casting to a

A cast to union type is similar to other casts, except that the type
specified is a union type.  You can specify the type either with
``union ``tag```` or with a typedef name.  A cast to union is actually
a constructor, not a cast, and hence does not yield an lvalue like
normal casts.  (See :ref:`compound-literals`.)

The types that may be cast to the union type are those of the members
of the union.  Thus, given the following union and variables:

.. code-block:: c++

  union foo { int i; double d; };
  int x;
  double y;

both ``x`` and ``y`` can be cast to type ``union foo``.

Using the cast as the right-hand side of an assignment to a variable of
union type is equivalent to storing in a member of the union:

.. code-block:: c++

  union foo u;
  /* ... */
  u = (union foo) x  ==  u.i = x
  u = (union foo) y  ==  u.d = y

You can also use the union cast as a function argument:

.. code-block:: c++

  void hack (union foo);
  /* ... */
  hack ((union foo) x);

