Using Vector Instructions through Built-in Functions
****************************************************

On some targets, the instruction set contains SIMD vector instructions which
operate on multiple values contained in one large register at the same time.
For example, on the x86 the MMX, 3DNow! and SSE extensions can be used
this way.

The first step in using these extensions is to provide the necessary data
types.  This should be done using an appropriate ``typedef``:

.. code-block:: c++

  typedef int v4si __attribute__ ((vector_size (16)));

The ``int`` type specifies the base type, while the attribute specifies
the vector size for the variable, measured in bytes.  For example, the
declaration above causes the compiler to set the mode for the ``v4si``
type to be 16 bytes wide and divided into ``int`` sized units.  For
a 32-bit ``int`` this means a vector of 4 units of 4 bytes, and the
corresponding mode of ``foo`` is V4SI.

The ``vector_size`` attribute is only applicable to integral and
float scalars, although arrays, pointers, and function return values
are allowed in conjunction with this construct. Only sizes that are
a power of two are currently allowed.

All the basic integer types can be used as base types, both as signed
and as unsigned: ``char``, ``short``, ``int``, ``long``,
``long long``.  In addition, ``float`` and ``double`` can be
used to build floating-point vector types.

Specifying a combination that is not valid for the current architecture
causes GCC to synthesize the instructions using a narrower mode.
For example, if you specify a variable of type ``V4SI`` and your
architecture does not allow for this specific SIMD type, GCC
produces code that uses 4 ``SIs``.

The types defined in this manner can be used with a subset of normal C
operations.  Currently, GCC allows using the following operators
on these types: ``+, -, *, /, unary minus, ^, |, &, ~, %``.

The operations behave like C++ ``valarrays``.  Addition is defined as
the addition of the corresponding elements of the operands.  For
example, in the code below, each of the 4 elements in ``a`` is
added to the corresponding 4 elements in ``b`` and the resulting
vector is stored in ``c``.

.. code-block:: c++

  typedef int v4si __attribute__ ((vector_size (16)));

  v4si a, b, c;

  c = a + b;

Subtraction, multiplication, division, and the logical operations
operate in a similar manner.  Likewise, the result of using the unary
minus or complement operators on a vector type is a vector whose
elements are the negative or complemented values of the corresponding
elements in the operand.

It is possible to use shifting operators ``<<``, ``>>`` on
integer-type vectors. The operation is defined as following: ``{a0,
a1, ..., an} >> {b0, b1, ..., bn} == {a0 >> b0, a1 >> b1,
..., an >> bn}``. Vector operands must have the same number of
elements. 

For convenience, it is allowed to use a binary vector operation
where one operand is a scalar. In that case the compiler transforms
the scalar operand into a vector where each element is the scalar from
the operation. The transformation happens only if the scalar could be
safely converted to the vector-element type.
Consider the following code.

.. code-block:: c++

  typedef int v4si __attribute__ ((vector_size (16)));

  v4si a, b, c;
  long l;

  a = b + 1;    /* a = b + {1,1,1,1}; */
  a = 2 * b;    /* a = {2,2,2,2} * b; */

  a = l + a;    /* Error, cannot convert long to int. */

Vectors can be subscripted as if the vector were an array with
the same number of elements and base type.  Out of bound accesses
invoke undefined behavior at run time.  Warnings for out of bound
accesses for vector subscription can be enabled with
:option:`-Warray-bounds`.

Vector comparison is supported with standard comparison
operators: ``==, !=, <, <=, >, >=``. Comparison operands can be
vector expressions of integer-type or real-type. Comparison between
integer-type vectors and real-type vectors are not supported.  The
result of the comparison is a vector of the same width and number of
elements as the comparison operands with a signed integral element
type.

Vectors are compared element-wise producing 0 when comparison is false
and -1 (constant of the appropriate type where all bits are set)
otherwise. Consider the following example.

.. code-block:: c++

  typedef int v4si __attribute__ ((vector_size (16)));

  v4si a = {1,2,3,4};
  v4si b = {3,2,1,4};
  v4si c;

  c = a >  b;     /* The result would be {0, 0,-1, 0}  */
  c = a == b;     /* The result would be {0,-1, 0,-1}  */

In C++, the ternary operator ``?:`` is available. ``a?b:c``, where
``b`` and ``c`` are vectors of the same type and ``a`` is an
integer vector with the same number of elements of the same size as ``b``
and ``c``, computes all three arguments and creates a vector
``{a[0]?b[0]:c[0], a[1]?b[1]:c[1], ...}``.  Note that unlike in
OpenCL, ``a`` is thus interpreted as ``a != 0`` and not ``a < 0``.
As in the case of binary operations, this syntax is also accepted when
one of ``b`` or ``c`` is a scalar that is then transformed into a
vector. If both ``b`` and ``c`` are scalars and the type of
``true?b:c`` has the same size as the element type of ``a``, then
``b`` and ``c`` are converted to a vector type whose elements have
this type and with the same number of elements as ``a``.

In C++, the logic operators ``!, &&, ||`` are available for vectors.
``!v`` is equivalent to ``v == 0``, ``a && b`` is equivalent to
``a!=0 & b!=0`` and ``a || b`` is equivalent to ``a!=0 | b!=0``.
For mixed operations between a scalar ``s`` and a vector ``v``,
``s && v`` is equivalent to ``s?v!=0:0`` (the evaluation is
short-circuit) and ``v && s`` is equivalent to ``v!=0 & (s?-1:0)``.

Vector shuffling is available using functions
``__builtin_shuffle (vec, mask)`` and
``__builtin_shuffle (vec0, vec1, mask)``.
Both functions construct a permutation of elements from one or two
vectors and return a vector of the same type as the input vector(s).
The ``mask`` is an integral vector with the same width (``W``)
and element count (``N``) as the output vector.

The elements of the input vectors are numbered in memory ordering of
``vec0`` beginning at 0 and ``vec1`` beginning at ``N``.  The
elements of ``mask`` are considered modulo ``N`` in the single-operand
case and modulo 2*``N`` in the two-operand case.

Consider the following example,

.. code-block:: c++

  typedef int v4si __attribute__ ((vector_size (16)));

  v4si a = {1,2,3,4};
  v4si b = {5,6,7,8};
  v4si mask1 = {0,1,1,3};
  v4si mask2 = {0,4,2,5};
  v4si res;

  res = __builtin_shuffle (a, mask1);       /* res is {1,2,2,4}  */
  res = __builtin_shuffle (a, b, mask2);    /* res is {1,5,3,6}  */

Note that ``__builtin_shuffle`` is intentionally semantically
compatible with the OpenCL ``shuffle`` and ``shuffle2`` functions.

You can declare variables and use them in function calls and returns, as
well as in assignments and some casts.  You can specify a vector type as
a return type for a function.  Vector types can also be used as function
arguments.  It is possible to cast from one vector type to another,
provided they are of the same size (in fact, you can also cast vectors
to and from other datatypes of the same size).

You cannot operate between vectors of different lengths or different
signedness without a cast.

