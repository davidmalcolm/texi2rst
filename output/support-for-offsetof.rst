
Support for ``offsetof``
.. index:: __builtin_offsetof

GCC implements for both C and C++ a syntactic extension to implement
the ``offsetof`` macro.

.. code-block:: c++

  primary:
          "__builtin_offsetof" "(" ``typename`` "," offsetof_member_designator ")"

  offsetof_member_designator:
            ``identifier``
          | offsetof_member_designator "." ``identifier``
          | offsetof_member_designator "[" ``expr`` "]"

This extension is sufficient such that

.. code-block:: c++

  #define offsetof(``type``, ``member``)  __builtin_offsetof (``type``, ``member``)

is a suitable definition of the ``offsetof`` macro.  In C++, ``type``
may be dependent.  In either case, ``member`` may consist of a single
identifier, or a sequence of member accesses and array references.

