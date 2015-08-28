.. _integer-overflow-builtins:

Built-in Functions to Perform Arithmetic with Overflow Checking
***************************************************************

The following built-in functions allow performing simple arithmetic operations
together with checking whether the operations overflowed.

.. index:: __builtin_add_overflow

Built-in Functionbool__builtin_add_overflow(``type1``a,``type2``b,``type3``*res)
.. index:: __builtin_sadd_overflow

Built-in Functionbool__builtin_sadd_overflow(inta,intb,int*res)
.. index:: __builtin_saddl_overflow

Built-in Functionbool__builtin_saddl_overflow(longinta,longintb,longint*res)
.. index:: __builtin_saddll_overflow

Built-in Functionbool__builtin_saddll_overflow(longlonginta,longlongintb,longint*res)
.. index:: __builtin_uadd_overflow

Built-in Functionbool__builtin_uadd_overflow(unsignedinta,unsignedintb,unsignedint*res)
.. index:: __builtin_uaddl_overflow

Built-in Functionbool__builtin_uaddl_overflow(unsignedlonginta,unsignedlongintb,unsignedlongint*res)
.. index:: __builtin_uaddll_overflow

Built-in Functionbool__builtin_uaddll_overflow(unsignedlonglonginta,unsignedlonglongintb,unsignedlongint*res)These built-in functions promote the first two operands into infinite precision signed
type and perform addition on those promoted operands.  The result is then
cast to the type the third pointer argument points to and stored there.
If the stored result is equal to the infinite precision result, the built-in
functions return false, otherwise they return true.  As the addition is
performed in infinite signed precision, these built-in functions have fully defined
behavior for all argument values.

The first built-in function allows arbitrary integral types for operands and
the result type must be pointer to some integer type, the rest of the built-in
functions have explicit integer types.

The compiler will attempt to use hardware instructions to implement
these built-in functions where possible, like conditional jump on overflow
after addition, conditional jump on carry etc.

.. index:: __builtin_sub_overflow

Built-in Functionbool__builtin_sub_overflow(``type1``a,``type2``b,``type3``*res)
.. index:: __builtin_ssub_overflow

Built-in Functionbool__builtin_ssub_overflow(inta,intb,int*res)
.. index:: __builtin_ssubl_overflow

Built-in Functionbool__builtin_ssubl_overflow(longinta,longintb,longint*res)
.. index:: __builtin_ssubll_overflow

Built-in Functionbool__builtin_ssubll_overflow(longlonginta,longlongintb,longint*res)
.. index:: __builtin_usub_overflow

Built-in Functionbool__builtin_usub_overflow(unsignedinta,unsignedintb,unsignedint*res)
.. index:: __builtin_usubl_overflow

Built-in Functionbool__builtin_usubl_overflow(unsignedlonginta,unsignedlongintb,unsignedlongint*res)
.. index:: __builtin_usubll_overflow

Built-in Functionbool__builtin_usubll_overflow(unsignedlonglonginta,unsignedlonglongintb,unsignedlongint*res)These built-in functions are similar to the add overflow checking built-in
functions above, except they perform subtraction, subtract the second argument
from the first one, instead of addition.

.. index:: __builtin_mul_overflow

Built-in Functionbool__builtin_mul_overflow(``type1``a,``type2``b,``type3``*res)
.. index:: __builtin_smul_overflow

Built-in Functionbool__builtin_smul_overflow(inta,intb,int*res)
.. index:: __builtin_smull_overflow

Built-in Functionbool__builtin_smull_overflow(longinta,longintb,longint*res)
.. index:: __builtin_smulll_overflow

Built-in Functionbool__builtin_smulll_overflow(longlonginta,longlongintb,longint*res)
.. index:: __builtin_umul_overflow

Built-in Functionbool__builtin_umul_overflow(unsignedinta,unsignedintb,unsignedint*res)
.. index:: __builtin_umull_overflow

Built-in Functionbool__builtin_umull_overflow(unsignedlonginta,unsignedlongintb,unsignedlongint*res)
.. index:: __builtin_umulll_overflow

Built-in Functionbool__builtin_umulll_overflow(unsignedlonglonginta,unsignedlonglongintb,unsignedlongint*res)These built-in functions are similar to the add overflow checking built-in
functions above, except they perform multiplication, instead of addition.

