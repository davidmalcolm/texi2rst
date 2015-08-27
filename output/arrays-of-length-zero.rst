Arrays of Length Zero
*********************

.. index:: arrays of length zero

.. index:: zero-length arrays

.. index:: length-zero arrays

.. index:: flexible array members

Zero-length arrays are allowed in GNU C.  They are very useful as the
last element of a structure that is really a header for a variable-length
object:

.. code-block:: c++

  struct line {
    int length;
    char contents[0];
  };

  struct line *thisline = (struct line *)
    malloc (sizeof (struct line) + this_length);
  thisline->length = this_length;

In ISO C90, you would have to give ``contents`` a length of 1, which
means either you waste space or complicate the argument to ``malloc``.

In ISO C99, you would use a :dfn:`flexible array member`, which is
slightly different in syntax and semantics:

* Flexible array members are written as ``contents[]`` without
  the ``0``.

  * Flexible array members have incomplete type, and so the ``sizeof``
  operator may not be applied.  As a quirk of the original implementation
  of zero-length arrays, ``sizeof`` evaluates to zero.

  * Flexible array members may only appear as the last member of a
  ``struct`` that is otherwise non-empty.

  * A structure containing a flexible array member, or a union containing
  such a structure (possibly recursively), may not be a member of a
  structure or an element of an array.  (However, these uses are
  permitted by GCC as extensions.)

Non-empty initialization of zero-length
arrays is treated like any case where there are more initializer
elements than the array holds, in that a suitable warning about excess
elements in array is given, and the excess elements (all of them, in
this case) are ignored.

GCC allows static initialization of flexible array members.
This is equivalent to defining a new structure containing the original
structure followed by an array of sufficient size to contain the data.
E.g. in the following, ``f1`` is constructed as if it were declared
like ``f2``.

.. code-block:: c++

  struct f1 {
    int x; int y[];
  } f1 = { 1, { 2, 3, 4 } };

  struct f2 {
    struct f1 f1; int data[3];
  } f2 = { { 1 }, { 2, 3, 4 } };

The convenience of this extension is that ``f1`` has the desired
type, eliminating the need to consistently refer to ``f2.f1``.

This has symmetry with normal static arrays, in that an array of
unknown size is also written with ``[]``.

Of course, this extension only makes sense if the extra data comes at
the end of a top-level object, as otherwise we would be overwriting
data at subsequent offsets.  To avoid undue complication and confusion
with initialization of deeply nested arrays, we simply disallow any
non-empty initialization except when the structure is the top-level
object.  For example:

.. code-block:: c++

  struct foo { int x; int y[]; };
  struct bar { struct foo z; };

  struct foo a = { 1, { 2, 3, 4 } };        // Valid.
  struct bar b = { { 1, { 2, 3, 4 } } };    // Invalid.
  struct bar c = { { 1, { } } };            // Valid.
  struct foo d[1] = { { 1, { 2, 3, 4 } } };  // Invalid.

