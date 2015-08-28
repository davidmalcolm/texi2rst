.. _mixed-declarations:

Mixed Declarations and Code
***************************

.. index:: mixed declarations and code

.. index:: declarations, mixed with code

.. index:: code, mixed with declarations

ISO C99 and ISO C++ allow declarations and code to be freely mixed
within compound statements.  As an extension, GNU C also allows this in
C90 mode.  For example, you could do:

.. code-block:: c++

  int i;
  /* ... */
  i++;
  int j = i + 2;

Each identifier is visible from where it is declared until the end of
the enclosing block.

