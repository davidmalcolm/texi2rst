Binary Constants using the 0b Prefix
Binary constants using the 0b prefix

Integer constants can be written as binary constants, consisting of a
sequence of 0 and 1 digits, prefixed by 0b or
0B.  This is particularly useful in environments that operate a
lot on the bit level (like microcontrollers).

The following statements are identical:

.. code-block:: c++

  i =       42;
  i =     0x2a;
  i =      052;
  i = 0b101010;

The type of these constants follows the same rules as for octal or
hexadecimal integer constants, so suffixes like L or UL
can be applied.

