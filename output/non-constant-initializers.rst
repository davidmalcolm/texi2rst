
Non-Constant Initializers
*************************

.. index:: initializers, non-constant

.. index:: non-constant initializers

As in standard C++ and ISO C99, the elements of an aggregate initializer for an
automatic variable are not required to be constant expressions in GNU C.
Here is an example of an initializer with run-time varying elements:

.. code-block:: c++

  foo (float f, float g)
  {
    float beat_freqs[2] = { f-g, f+g };
    /* ... */
  }

