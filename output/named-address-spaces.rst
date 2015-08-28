.. _named-address-spaces:

Named Address Spaces
********************

.. index:: Named Address Spaces

As an extension, GNU C supports named address spaces as
defined in the N1275 draft of ISO/IEC DTR 18037.  Support for named
address spaces in GCC will evolve as the draft technical report
changes.  Calling conventions for any target might also change.  At
present, only the AVR, SPU, M32C, and RL78 targets support address
spaces other than the generic address space.

Address space identifiers may be used exactly like any other C type
qualifier (e.g., ``const`` or ``volatile``).  See the N1275
document for more details.

AVR Named Address Spaces
AVR Named Address Spaces
^^^^^^^^^^^^^^^^^^^^^^^^

On the AVR target, there are several address spaces that can be used
in order to put read-only data into the flash memory and access that
data by means of the special instructions ``LPM`` or ``ELPM``
needed to read from flash.

Per default, any data including read-only data is located in RAM
(the generic address space) so that non-generic address spaces are
needed to locate read-only data in flash memory
and to generate the right instructions to access this data
without using (inline) assembler code.

__flash
  ``__flash`` AVR Named Address SpacesThe ``__flash`` qualifier locates data in the
  ``.progmem.data`` section. Data is read using the ``LPM``
  instruction. Pointers to this address space are 16 bits wide.

__flash1 __flash2 __flash3 __flash4 __flash5
  ``__flash1`` AVR Named Address Spaces``__flash2`` AVR Named Address Spaces``__flash3`` AVR Named Address Spaces``__flash4`` AVR Named Address Spaces``__flash5`` AVR Named Address SpacesThese are 16-bit address spaces locating data in section
  ``.progmem``N``.data`` where ``N`` refers to
  address space ``__flash``N````.
  The compiler sets the ``RAMPZ`` segment register appropriately 
  before reading data by means of the ``ELPM`` instruction.

__memx
  ``__memx`` AVR Named Address SpacesThis is a 24-bit address space that linearizes flash and RAM:
  If the high bit of the address is set, data is read from
  RAM using the lower two bytes as RAM address.
  If the high bit of the address is clear, data is read from flash
  with ``RAMPZ`` set according to the high byte of the address.
  See :ref:`avr-built-in-functions`.

  Objects in this address space are located in ``.progmemx.data``.

  Example

.. code-block:: c++

  char my_read (const __flash char ** p)
  {
      /* p is a pointer to RAM that points to a pointer to flash.
         The first indirection of p reads that flash pointer
         from RAM and the second indirection reads a char from this
         flash address.  */

      return **p;
  }

  /* Locate array[] in flash memory */
  const __flash int array[] = { 3, 5, 7, 11, 13, 17, 19 };

  int i = 1;

  int main (void)
  {
     /* Return 17 by reading from flash memory */
     return array[array[i]];
  }

For each named address space supported by avr-gcc there is an equally
named but uppercase built-in macro defined. 
The purpose is to facilitate testing if respective address space
support is available or not:

.. code-block:: c++

  #ifdef __FLASH
  const __flash int var = 1;

  int read_var (void)
  {
      return var;
  }
  #else
  #include <avr/pgmspace.h> /* From AVR-LibC */

  const int var PROGMEM = 1;

  int read_var (void)
  {
      return (int) pgm_read_word (&var);
  }
  #endif /* __FLASH */

Notice that attribute AVR Variable Attributes``progmem``
locates data in flash but
accesses to these data read from generic address space, i.e.
from RAM,
so that you need special accessors like ``pgm_read_byte``
from http://nongnu.org/avr-libc/user-manual/AVR-LibC
together with attribute ``progmem``.

Limitations and caveats

* Reading across the 64 KiB section boundary of
  the ``__flash`` or ``__flash``N```` address spaces
  shows undefined behavior. The only address space that
  supports reading across the 64 KiB flash segment boundaries is
  ``__memx``.

* If you use one of the ``__flash``N```` address spaces
  you must arrange your linker script to locate the
  ``.progmem``N``.data`` sections according to your needs.

* Any data or pointers to the non-generic address spaces must
  be qualified as ``const``, i.e. as read-only data.
  This still applies if the data in one of these address
  spaces like software version number or calibration lookup table are intended to
  be changed after load time by, say, a boot loader. In this case
  the right qualification is ``const`` ``volatile`` so that the compiler
  must not optimize away known values or insert them
  as immediates into operands of instructions.

* The following code initializes a variable ``pfoo``
  located in static storage with a 24-bit address:

  .. code-block:: c++

    extern const __memx char foo;
    const __memx void *pfoo = &foo;

  Such code requires at least binutils 2.23, see
  http://sourceware.org/PR13503PR13503.

M32C Named Address Spaces
^^^^^^^^^^^^^^^^^^^^^^^^^

``__far`` M32C Named Address SpacesOn the M32C target, with the R8C and M16C CPU variants, variables
qualified with ``__far`` are accessed using 32-bit addresses in
order to access memory beyond the first 64 Ki bytes.  If
``__far`` is used with the M32CM or M32C CPU variants, it has no
effect.

RL78 Named Address Spaces
^^^^^^^^^^^^^^^^^^^^^^^^^

``__far`` RL78 Named Address SpacesOn the RL78 target, variables qualified with ``__far`` are accessed
with 32-bit pointers (20-bit addresses) rather than the default 16-bit
addresses.  Non-far variables are assumed to appear in the topmost
64 KiB of the address space.

SPU Named Address Spaces
^^^^^^^^^^^^^^^^^^^^^^^^

``__ea`` SPU Named Address SpacesOn the SPU target variables may be declared as
belonging to another address space by qualifying the type with the
``__ea`` address space identifier:

.. code-block:: c++

  extern int __ea i;

The compiler generates special code to access the variable ``i``.
It may use runtime library
support, or generate special machine instructions to access that address
space.

