Passing Options to the Assembler
********************************

.. prevent bad page break with this line 

You can pass options to the assembler.

.. option:: -Wa,option, -Wa

  Pass ``option`` as an option to the assembler.  If ``option``
  contains commas, it is split into multiple options at the commas.

.. option:: -Xassembler option, -Xassembler

  Pass ``option`` as an option to the assembler.  You can use this to
  supply system-specific assembler options that GCC does not
  recognize.

  If you want to pass an option that takes an argument, you must use
  :option:`-Xassembler` twice, once for the option and once for the argument.

