Built-in Functions to Perform Arithmetic with Overflow Checking
***************************************************************

The following built-in functions allow performing simple arithmetic operations
together with checking whether the operations overflowed.

.. index:: __builtin_add_overflow

  Built-in Function bool __builtin_add_overflow (``type1`` a, ``type2`` b, ``type3`` *res)

.. index:: __builtin_sadd_overflow

  Built-in Function bool __builtin_sadd_overflow (int a, int b, int *res)

.. index:: __builtin_saddl_overflow

  Built-in Function bool __builtin_saddl_overflow (long int a, long int b, long int *res)

.. index:: __builtin_saddll_overflow

  Built-in Function bool __builtin_saddll_overflow (long long int a, long long int b, long int *res)

.. index:: __builtin_uadd_overflow

  Built-in Function bool __builtin_uadd_overflow (unsigned int a, unsigned int b, unsigned int *res)

.. index:: __builtin_uaddl_overflow

  Built-in Function bool __builtin_uaddl_overflow (unsigned long int a, unsigned long int b, unsigned long int *res)

.. index:: __builtin_uaddll_overflow

  Built-in Function bool __builtin_uaddll_overflow (unsigned long long int a, unsigned long long int b, unsigned long int *res)

These built-in functions promote the first two operands into infinite precision signed
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

  Built-in Function bool __builtin_sub_overflow (``type1`` a, ``type2`` b, ``type3`` *res)

.. index:: __builtin_ssub_overflow

  Built-in Function bool __builtin_ssub_overflow (int a, int b, int *res)

.. index:: __builtin_ssubl_overflow

  Built-in Function bool __builtin_ssubl_overflow (long int a, long int b, long int *res)

.. index:: __builtin_ssubll_overflow

  Built-in Function bool __builtin_ssubll_overflow (long long int a, long long int b, long int *res)

.. index:: __builtin_usub_overflow

  Built-in Function bool __builtin_usub_overflow (unsigned int a, unsigned int b, unsigned int *res)

.. index:: __builtin_usubl_overflow

  Built-in Function bool __builtin_usubl_overflow (unsigned long int a, unsigned long int b, unsigned long int *res)

.. index:: __builtin_usubll_overflow

  Built-in Function bool __builtin_usubll_overflow (unsigned long long int a, unsigned long long int b, unsigned long int *res)

These built-in functions are similar to the add overflow checking built-in
functions above, except they perform subtraction, subtract the second argument
from the first one, instead of addition.

.. index:: __builtin_mul_overflow

  Built-in Function bool __builtin_mul_overflow (``type1`` a, ``type2`` b, ``type3`` *res)

.. index:: __builtin_smul_overflow

  Built-in Function bool __builtin_smul_overflow (int a, int b, int *res)

.. index:: __builtin_smull_overflow

  Built-in Function bool __builtin_smull_overflow (long int a, long int b, long int *res)

.. index:: __builtin_smulll_overflow

  Built-in Function bool __builtin_smulll_overflow (long long int a, long long int b, long int *res)

.. index:: __builtin_umul_overflow

  Built-in Function bool __builtin_umul_overflow (unsigned int a, unsigned int b, unsigned int *res)

.. index:: __builtin_umull_overflow

  Built-in Function bool __builtin_umull_overflow (unsigned long int a, unsigned long int b, unsigned long int *res)

.. index:: __builtin_umulll_overflow

  Built-in Function bool __builtin_umulll_overflow (unsigned long long int a, unsigned long long int b, unsigned long int *res)

These built-in functions are similar to the add overflow checking built-in
functions above, except they perform multiplication, instead of addition.

