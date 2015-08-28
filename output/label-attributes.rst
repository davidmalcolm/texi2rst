  .. _label-attributes:

Label Attributes
****************

.. index:: Label Attributes

GCC allows attributes to be set on C labels.  See :ref:`attribute-syntax`, for 
details of the exact syntax for using attributes.  Other attributes are 
available for functions (Function Attributes), variables 
(Variable Attributes) and for types (Type Attributes).

This example uses the ``cold`` label attribute to indicate the 
``ErrorHandling`` branch is unlikely to be taken and that the
``ErrorHandling`` label is unused:

.. code-block:: c++

     asm goto ("some asm" : : : : NoError);

  /* This branch (the fall-through from the asm) is less commonly used */
  ErrorHandling: 
     __attribute__((cold, unused)); /* Semi-colon is required here */
     printf("error\n");
     return 0;

  NoError:
     printf("no error\n");
     return 1;

unused

  .. index:: unused label attribute

  This feature is intended for program-generated code that may contain 
  unused labels, but which is compiled with :option:`-Wall`.  It is
  not normally appropriate to use in it human-written code, though it
  could be useful in cases where the code that jumps to the label is
  contained within an ``#ifdef`` conditional.

hot

  .. index:: hot label attribute

  The ``hot`` attribute on a label is used to inform the compiler that
  the path following the label is more likely than paths that are not so
  annotated.  This attribute is used in cases where ``__builtin_expect``
  cannot be used, for instance with computed goto or ``asm goto``.

cold

  .. index:: cold label attribute

  The ``cold`` attribute on labels is used to inform the compiler that
  the path following the label is unlikely to be executed.  This attribute
  is used in cases where ``__builtin_expect`` cannot be used, for instance
  with computed goto or ``asm goto``.

