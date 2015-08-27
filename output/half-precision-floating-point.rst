
Half-Precision Floating Point
*****************************

.. index:: half-precision floating point

``__fp16`` data typeOn ARM targets, GCC supports half-precision (16-bit) floating point via
the ``__fp16`` type.  You must enable this type explicitly
with the :option:`-mfp16-format` command-line option in order to use it.

ARM supports two incompatible representations for half-precision
floating-point values.  You must choose one of the representations and
use it consistently in your program.

Specifying :option:`-mfp16-format=ieee` selects the IEEE 754-2008 format.
This format can represent normalized values in the range of 2^{-14} to 65504.
There are 11 bits of significand precision, approximately 3
decimal digits.

Specifying :option:`-mfp16-format=alternative` selects the ARM
alternative format.  This representation is similar to the IEEE
format, but does not support infinities or NaNs.  Instead, the range
of exponents is extended, so that this format can represent normalized
values in the range of 2^{-14} to 131008.

The ``__fp16`` type is a storage format only.  For purposes
of arithmetic and other operations, ``__fp16`` values in C or C++
expressions are automatically promoted to ``float``.  In addition,
you cannot declare a function with a return value or parameters
of type ``__fp16``.

Note that conversions from ``double`` to ``__fp16``
involve an intermediate conversion to ``float``.  Because
of rounding, this can sometimes produce a different result than a
direct conversion.

ARM provides hardware support for conversions between
``__fp16`` and ``float`` values
as an extension to VFP and NEON (Advanced SIMD).  GCC generates
code using these hardware instructions if you compile with
options to select an FPU that provides them;
for example, :option:`-mfpu=neon-fp16 -mfloat-abi=softfp`,
in addition to the :option:`-mfp16-format` option to select
a half-precision format.

Language-level support for the ``__fp16`` data type is
independent of whether GCC generates code using hardware floating-point
instructions.  In cases where hardware support is not specified, GCC
implements conversions between ``__fp16`` and ``float`` values
as library calls.

