.. _compound-literals:

Compound Literals
*****************

.. index:: constructor expressions

.. index:: initializations in expressions

.. index:: structures, constructor expression

.. index:: expressions, constructor

.. index:: compound literals

.. The GNU C name for what C99 calls compound literals was "constructor expressions".

ISO C99 supports compound literals.  A compound literal looks like
a cast containing an initializer.  Its value is an object of the
type specified in the cast, containing the elements specified in
the initializer; it is an lvalue.  As an extension, GCC supports
compound literals in C90 mode and in C++, though the semantics are
somewhat different in C++.

Usually, the specified type is a structure.  Assume that
``struct foo`` and ``structure`` are declared as shown:

.. code-block:: c++

  struct foo {int a; char b[2];} structure;

Here is an example of constructing a ``struct foo`` with a compound literal:

.. code-block:: c++

  structure = ((struct foo) {x + y, 'a', 0});

This is equivalent to writing the following:

.. code-block:: c++

  {
    struct foo temp = {x + y, 'a', 0};
    structure = temp;
  }

You can also construct an array, though this is dangerous in C++, as
explained below.  If all the elements of the compound literal are
(made up of) simple constant expressions, suitable for use in
initializers of objects of static storage duration, then the compound
literal can be coerced to a pointer to its first element and used in
such an initializer, as shown here:

.. code-block:: c++

  char **foo = (char *[]) { "x", "y", "z" };

Compound literals for scalar types and union types are
also allowed, but then the compound literal is equivalent
to a cast.

As a GNU extension, GCC allows initialization of objects with static storage
duration by compound literals (which is not possible in ISO C99, because
the initializer is not a constant).
It is handled as if the object is initialized only with the bracket
enclosed list if the types of the compound literal and the object match.
The initializer list of the compound literal must be constant.
If the object being initialized has array type of unknown size, the size is
determined by compound literal size.

.. code-block:: c++

  static struct foo x = (struct foo) {1, 'a', 'b'};
  static int y[] = (int []) {1, 2, 3};
  static int z[] = (int [3]) {1};

The above lines are equivalent to the following:

.. code-block:: c++

  static struct foo x = {1, 'a', 'b'};
  static int y[] = {1, 2, 3};
  static int z[] = {1, 0, 0};

In C, a compound literal designates an unnamed object with static or
automatic storage duration.  In C++, a compound literal designates a
temporary object, which only lives until the end of its
full-expression.  As a result, well-defined C code that takes the
address of a subobject of a compound literal can be undefined in C++,
so the C++ compiler rejects the conversion of a temporary array to a pointer.
For instance, if the array compound literal example above appeared
inside a function, any subsequent use of foo in C++ has
undefined behavior because the lifetime of the array ends after the
declaration of foo.  

As an optimization, the C++ compiler sometimes gives array compound
literals longer lifetimes: when the array either appears outside a
function or has const-qualified type.  If foo and its
initializer had elements of char *const type rather than
char *, or if foo were a global variable, the array
would have static storage duration.  But it is probably safest just to
avoid the use of array compound literals in code compiled as C++.

