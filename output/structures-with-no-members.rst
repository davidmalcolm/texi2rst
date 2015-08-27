
Structures with No Members
**************************

.. index:: empty structures

.. index:: zero-size structures

GCC permits a C structure to have no members:

.. code-block:: c++

  struct empty {
  };

The structure has size zero.  In C++, empty structures are part
of the language.  G++ treats empty structures as if they had a single
member of type ``char``.

