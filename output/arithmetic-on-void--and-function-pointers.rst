
Arithmetic on ``void``- and Function-Pointers
.. index:: void pointers, arithmetic

.. index:: void, size of pointer to

.. index:: function pointers, arithmetic

.. index:: function, size of pointer to

In GNU C, addition and subtraction operations are supported on pointers to
``void`` and on pointers to functions.  This is done by treating the
size of a ``void`` or of a function as 1.

A consequence of this is that ``sizeof`` is also allowed on ``void``
and on function types, and returns 1.

.. index:: Wpointer-arith

The option :option:`-Wpointer-arith` requests a warning if these extensions
are used.

