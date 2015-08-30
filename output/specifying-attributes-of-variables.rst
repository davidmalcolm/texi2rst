  .. _variable-attributes:

Specifying Attributes of Variables
**********************************

.. index:: attribute of variables

.. index:: variable attributes

The keyword ``__attribute__`` allows you to specify special
attributes of variables or structure fields.  This keyword is followed
by an attribute specification inside double parentheses.  Some
attributes are currently defined generically for variables.
Other attributes are defined for variables on particular target
systems.  Other attributes are available for functions
(see :ref:`function-attributes`), labels (see :ref:`label-attributes`) and for 
types (see :ref:`type-attributes`).
Other front ends might define more attributes
(see :ref:`Extensions to the C++ Language <c++-extensions>`).

See :ref:`attribute-syntax`, for details of the exact syntax for using
attributes.

.. toctree::

   <common-variable-attributes>
   <avr-variable-attributes>
   <blackfin-variable-attributes>
   <h8-300-variable-attributes>
   <ia-64-variable-attributes>
   <m32r-d-variable-attributes>
   <mep-variable-attributes>
   <microsoft-windows-variable-attributes>
   <powerpc-variable-attributes>
   <spu-variable-attributes>
   <x86-variable-attributes>
   <xstormy16-variable-attributes>

.. _common-variable-attributes:

Common Variable Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^

The following attributes are supported on most targets.

.. index:: aligned variable attribute

aligned (``alignment``)
  This attribute specifies a minimum alignment for the variable or
  structure field, measured in bytes.  For example, the declaration:

  .. code-block:: c++

    int x __attribute__ ((aligned (16))) = 0;

  causes the compiler to allocate the global variable ``x`` on a
  16-byte boundary.  On a 68040, this could be used in conjunction with
  an ``asm`` expression to access the ``move16`` instruction which
  requires 16-byte aligned operands.

  You can also specify the alignment of structure fields.  For example, to
  create a double-word aligned ``int`` pair, you could write:

  .. code-block:: c++

    struct foo { int x[2] __attribute__ ((aligned (8))); };

  This is an alternative to creating a union with a ``double`` member,
  which forces the union to be double-word aligned.

  As in the preceding examples, you can explicitly specify the alignment
  (in bytes) that you wish the compiler to use for a given variable or
  structure field.  Alternatively, you can leave out the alignment factor
  and just ask the compiler to align a variable or field to the
  default alignment for the target architecture you are compiling for.
  The default alignment is sufficient for all scalar types, but may not be
  enough for all vector types on a target that supports vector operations.
  The default alignment is fixed for a particular target ABI.

  GCC also provides a target specific macro ``__BIGGEST_ALIGNMENT__``,
  which is the largest alignment ever used for any data type on the
  target machine you are compiling for.  For example, you could write:

  .. code-block:: c++

    short array[3] __attribute__ ((aligned (__BIGGEST_ALIGNMENT__)));

  The compiler automatically sets the alignment for the declared
  variable or field to ``__BIGGEST_ALIGNMENT__``.  Doing this can
  often make copy operations more efficient, because the compiler can
  use whatever instructions copy the biggest chunks of memory when
  performing copies to or from the variables or fields that you have
  aligned this way.  Note that the value of ``__BIGGEST_ALIGNMENT__``
  may change depending on command-line options.

  When used on a struct, or struct member, the ``aligned`` attribute can
  only increase the alignment; in order to decrease it, the ``packed``
  attribute must be specified as well.  When used as part of a typedef, the
  ``aligned`` attribute can both increase and decrease alignment, and
  specifying the ``packed`` attribute generates a warning.

  Note that the effectiveness of ``aligned`` attributes may be limited
  by inherent limitations in your linker.  On many systems, the linker is
  only able to arrange for variables to be aligned up to a certain maximum
  alignment.  (For some linkers, the maximum supported alignment may
  be very very small.)  If your linker is only able to align variables
  up to a maximum of 8-byte alignment, then specifying ``aligned(16)``
  in an ``__attribute__`` still only provides you with 8-byte
  alignment.  See your linker documentation for further information.

  The ``aligned`` attribute can also be used for functions
  (see :ref:`common-function-attributes`.)

cleanup (``cleanup_function``)

  .. index:: cleanup variable attribute

  The ``cleanup`` attribute runs a function when the variable goes
  out of scope.  This attribute can only be applied to auto function
  scope variables; it may not be applied to parameters or variables
  with static storage duration.  The function must take one parameter,
  a pointer to a type compatible with the variable.  The return value
  of the function (if any) is ignored.

  If :option:`-fexceptions` is enabled, then ``cleanup_function``
  is run during the stack unwinding that happens during the
  processing of the exception.  Note that the ``cleanup`` attribute
  does not allow the exception to be caught, only to perform an action.
  It is undefined what happens if ``cleanup_function`` does not
  return normally.

.. option:: common, -fcommon, -fno-common

  .. index:: common variable attribute

  .. index:: nocommon variable attribute

  The ``common`` attribute requests GCC to place a variable in
  'common' storage.  The ``nocommon`` attribute requests the
  opposite-to allocate space for it directly.

  These attributes override the default chosen by the
  :option:`-fno-common` and :option:`-fcommon` flags respectively.

deprecated deprecated (``msg``)

  .. index:: deprecated variable attribute

  The ``deprecated`` attribute results in a warning if the variable
  is used anywhere in the source file.  This is useful when identifying
  variables that are expected to be removed in a future version of a
  program.  The warning also includes the location of the declaration
  of the deprecated variable, to enable users to easily find further
  information about why the variable is deprecated, or what they should
  do instead.  Note that the warning only occurs for uses:

  .. code-block:: c++

    extern int old_var __attribute__ ((deprecated));
    extern int old_var;
    int new_fn () { return old_var; }

  results in a warning on line 3 but not line 2.  The optional ``msg``
  argument, which must be a string, is printed in the warning if
  present.

  The ``deprecated`` attribute can also be used for functions and
  types (see :ref:`common-function-attributes`,
  see :ref:`common-type-attributes`).

mode (``mode``)

  .. index:: mode variable attribute

  This attribute specifies the data type for the declaration-whichever
  type corresponds to the mode ``mode``.  This in effect lets you
  request an integer or floating-point type according to its width.

  You may also specify a mode of ``byte`` or ``__byte__`` to
  indicate the mode corresponding to a one-byte integer, ``word`` or
  ``__word__`` for the mode of a one-word integer, and ``pointer``
  or ``__pointer__`` for the mode used to represent pointers.

packed

  .. index:: packed variable attribute

  The ``packed`` attribute specifies that a variable or structure field
  should have the smallest possible alignment-one byte for a variable,
  and one bit for a field, unless you specify a larger value with the
  ``aligned`` attribute.

  Here is a structure in which the field ``x`` is packed, so that it
  immediately follows ``a``:

  .. code-block:: c++

    struct foo
    {
      char a;
      int x[2] __attribute__ ((packed));
    };

  *Note:* The 4.1, 4.2 and 4.3 series of GCC ignore the
  ``packed`` attribute on bit-fields of type ``char``.  This has
  been fixed in GCC 4.4 but the change can lead to differences in the
  structure layout.  See the documentation of
  :option:`-Wpacked-bitfield-compat` for more information.

section ("``section-name``")

  .. index:: section variable attribute

  Normally, the compiler places the objects it generates in sections like
  ``data`` and ``bss``.  Sometimes, however, you need additional sections,
  or you need certain particular variables to appear in special sections,
  for example to map to special hardware.  The ``section``
  attribute specifies that a variable (or function) lives in a particular
  section.  For example, this small program uses several specific section names:

  .. code-block:: c++

    struct duart a __attribute__ ((section ("DUART_A"))) = { 0 };
    struct duart b __attribute__ ((section ("DUART_B"))) = { 0 };
    char stack[10000] __attribute__ ((section ("STACK"))) = { 0 };
    int init_data __attribute__ ((section ("INITDATA")));

    main()
    {
      /* Initialize stack pointer */
      init_sp (stack + sizeof (stack));

      /* Initialize initialized data */
      memcpy (&init_data, &data, &edata - &data);

      /* Turn on the serial ports */
      init_duart (&a);
      init_duart (&b);
    }

  Use the ``section`` attribute with
  *global* variables and not *local* variables,
  as shown in the example.

  You may use the ``section`` attribute with initialized or
  uninitialized global variables but the linker requires
  each object be defined once, with the exception that uninitialized
  variables tentatively go in the ``common`` (or ``bss``) section
  and can be multiply 'defined'.  Using the ``section`` attribute
  changes what section the variable goes into and may cause the
  linker to issue an error if an uninitialized variable has multiple
  definitions.  You can force a variable to be initialized with the
  :option:`-fno-common` flag or the ``nocommon`` attribute.

  Some file formats do not support arbitrary sections so the ``section``
  attribute is not available on all platforms.
  If you need to map the entire contents of a module to a particular
  section, consider using the facilities of the linker instead.

tls_model ("``tls_model``")

  .. index:: tls_model variable attribute

  The ``tls_model`` attribute sets thread-local storage model
  (see :ref:`thread-local`) of a particular ``__thread`` variable,
  overriding :option:`-ftls-model=` command-line switch on a per-variable
  basis.
  The ``tls_model`` argument should be one of ``global-dynamic``,
  ``local-dynamic``, ``initial-exec`` or ``local-exec``.

  Not all targets support this attribute.

unused

  .. index:: unused variable attribute

  This attribute, attached to a variable, means that the variable is meant
  to be possibly unused.  GCC does not produce a warning for this
  variable.

used

  .. index:: used variable attribute

  This attribute, attached to a variable with static storage, means that
  the variable must be emitted even if it appears that the variable is not
  referenced.

  When applied to a static data member of a C++ class template, the
  attribute also means that the member is instantiated if the
  class itself is instantiated.

vector_size (``bytes``)

  .. index:: vector_size variable attribute

  This attribute specifies the vector size for the variable, measured in
  bytes.  For example, the declaration:

  .. code-block:: c++

    int foo __attribute__ ((vector_size (16)));

  causes the compiler to set the mode for ``foo``, to be 16 bytes,
  divided into ``int`` sized units.  Assuming a 32-bit int (a vector of
  4 units of 4 bytes), the corresponding mode of ``foo`` is V4SI.

  This attribute is only applicable to integral and float scalars,
  although arrays, pointers, and function return values are allowed in
  conjunction with this construct.

  Aggregates with this attribute are invalid, even if they are of the same
  size as a corresponding scalar.  For example, the declaration:

  .. code-block:: c++

    struct S { int a; };
    struct S  __attribute__ ((vector_size (16))) foo;

  is invalid even if the size of the structure is the same as the size of
  the ``int``.

weak

  .. index:: weak variable attribute

  The ``weak`` attribute is described in
  Common Function Attributes.

  .. _avr-variable-attributes:

AVR Variable Attributes
^^^^^^^^^^^^^^^^^^^^^^^

progmem

  .. index:: progmem variable attribute, AVR

  The ``progmem`` attribute is used on the AVR to place read-only
  data in the non-volatile program memory (flash). The ``progmem``
  attribute accomplishes this by putting respective variables into a
  section whose name starts with ``.progmem``.

  This attribute works similar to the ``section`` attribute
  but adds additional checking. Notice that just like the
  ``section`` attribute, ``progmem`` affects the location
  of the data but not how this data is accessed.

  In order to read data located with the ``progmem`` attribute
  (inline) assembler must be used.

  .. code-block:: c++

    /* Use custom macros from http://nongnu.org/avr-libc/user-manual/AVR-LibC */
    #include <avr/pgmspace.h> 

    /* Locate var in flash memory */
    const int var[2] PROGMEM = { 1, 2 };

    int read_var (int i)
    {
        /* Access var[] by accessor macro from avr/pgmspace.h */
        return (int) pgm_read_word (& var[i]);
    }

  AVR is a Harvard architecture processor and data and read-only data
  normally resides in the data memory (RAM).

  See also the AVR Named Address Spaces section for
  an alternate way to locate and access data in flash memory.

io io (``addr``)

  .. index:: io variable attribute, AVR

  Variables with the ``io`` attribute are used to address
  memory-mapped peripherals in the io address range.
  If an address is specified, the variable
  is assigned that address, and the value is interpreted as an
  address in the data address space.
  Example:

  .. code-block:: c++

    volatile int porta __attribute__((io (0x22)));

  The address specified in the address in the data address range.

  Otherwise, the variable it is not assigned an address, but the
  compiler will still use in/out instructions where applicable,
  assuming some other module assigns an address in the io address range.
  Example:

  .. code-block:: c++

    extern volatile int porta __attribute__((io));

io_low io_low (``addr``)

  .. index:: io_low variable attribute, AVR

  This is like the ``io`` attribute, but additionally it informs the
  compiler that the object lies in the lower half of the I/O area,
  allowing the use of ``cbi``, ``sbi``, ``sbic`` and ``sbis``
  instructions.

address address (``addr``)

  .. index:: address variable attribute, AVR

  Variables with the ``address`` attribute are used to address
  memory-mapped peripherals that may lie outside the io address range.

  .. code-block:: c++

    volatile int porta __attribute__((address (0x600)));

  .. _blackfin-variable-attributes:

Blackfin Variable Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Three attributes are currently defined for the Blackfin.

l1_data l1_data_A l1_data_B

  .. index:: l1_data variable attribute, Blackfin

  .. index:: l1_data_A variable attribute, Blackfin

  .. index:: l1_data_B variable attribute, Blackfin

  Use these attributes on the Blackfin to place the variable into L1 Data SRAM.
  Variables with ``l1_data`` attribute are put into the specific section
  named ``.l1.data``. Those with ``l1_data_A`` attribute are put into
  the specific section named ``.l1.data.A``. Those with ``l1_data_B``
  attribute are put into the specific section named ``.l1.data.B``.

l2

  .. index:: l2 variable attribute, Blackfin

  Use this attribute on the Blackfin to place the variable into L2 SRAM.
  Variables with ``l2`` attribute are put into the specific section
  named ``.l2.data``.

  .. _h8-300-variable-attributes:

H8/300 Variable Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^

These variable attributes are available for H8/300 targets:

eightbit_data

  .. index:: eightbit_data variable attribute, H8/300

  .. index:: eight-bit data on the H8/300, H8/300H, and H8S

  Use this attribute on the H8/300, H8/300H, and H8S to indicate that the specified
  variable should be placed into the eight-bit data section.
  The compiler generates more efficient code for certain operations
  on data in the eight-bit data area.  Note the eight-bit data area is limited to
  256 bytes of data.

  You must use GAS and GLD from GNU binutils version 2.7 or later for
  this attribute to work correctly.

tiny_data

  .. index:: tiny_data variable attribute, H8/300

  .. index:: tiny data section on the H8/300H and H8S

  Use this attribute on the H8/300H and H8S to indicate that the specified
  variable should be placed into the tiny data section.
  The compiler generates more efficient code for loads and stores
  on data in the tiny data section.  Note the tiny data area is limited to
  slightly under 32KB of data.

  .. _ia-64-variable-attributes:

IA-64 Variable Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^

The IA-64 back end supports the following variable attribute:

model (``model-name``)

  .. index:: model variable attribute, IA-64

  On IA-64, use this attribute to set the addressability of an object.
  At present, the only supported identifier for ``model-name`` is
  ``small``, indicating addressability via 'small' (22-bit)
  addresses (so that their addresses can be loaded with the ``addl``
  instruction).  Caveat: such addressing is by definition not position
  independent and hence this attribute must not be used for objects
  defined by shared libraries.

  .. _m32r-d-variable-attributes:

M32R/D Variable Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^

One attribute is currently defined for the M32R/D.

model (``model-name``)

  .. index:: model-name variable attribute, M32R/D

  .. index:: variable addressability on the M32R/D

  Use this attribute on the M32R/D to set the addressability of an object.
  The identifier ``model-name`` is one of ``small``, ``medium``,
  or ``large``, representing each of the code models.

  Small model objects live in the lower 16MB of memory (so that their
  addresses can be loaded with the ``ld24`` instruction).

  Medium and large model objects may live anywhere in the 32-bit address space
  (the compiler generates ``seth/add3`` instructions to load their
  addresses).

  .. _mep-variable-attributes:

MeP Variable Attributes
^^^^^^^^^^^^^^^^^^^^^^^

The MeP target has a number of addressing modes and busses.  The
``near`` space spans the standard memory space's first 16 megabytes
(24 bits).  The ``far`` space spans the entire 32-bit memory space.
The ``based`` space is a 128-byte region in the memory space that
is addressed relative to the ``$tp`` register.  The ``tiny``
space is a 65536-byte region relative to the ``$gp`` register.  In
addition to these memory regions, the MeP target has a separate 16-bit
control bus which is specified with ``cb`` attributes.

based

  .. index:: based variable attribute, MeP

  Any variable with the ``based`` attribute is assigned to the
  ``.based`` section, and is accessed with relative to the
  ``$tp`` register.

tiny

  .. index:: tiny variable attribute, MeP

  Likewise, the ``tiny`` attribute assigned variables to the
  ``.tiny`` section, relative to the ``$gp`` register.

near

  .. index:: near variable attribute, MeP

  Variables with the ``near`` attribute are assumed to have addresses
  that fit in a 24-bit addressing mode.  This is the default for large
  variables (``-mtiny=4`` is the default) but this attribute can
  override ``-mtiny=`` for small variables, or override ``-ml``.

far

  .. index:: far variable attribute, MeP

  Variables with the ``far`` attribute are addressed using a full
  32-bit address.  Since this covers the entire memory space, this
  allows modules to make no assumptions about where variables might be
  stored.

io
.. index:: io variable attribute, MeP

 io (``addr``)
  Variables with the ``io`` attribute are used to address
  memory-mapped peripherals.  If an address is specified, the variable
  is assigned that address, else it is not assigned an address (it is
  assumed some other module assigns an address).  Example:

  .. code-block:: c++

    int timer_count __attribute__((io(0x123)));

cb cb (``addr``)

  .. index:: cb variable attribute, MeP

  Variables with the ``cb`` attribute are used to access the control
  bus, using special instructions.  ``addr`` indicates the control bus
  address.  Example:

  .. code-block:: c++

    int cpu_clock __attribute__((cb(0x123)));

  .. _microsoft-windows-variable-attributes:

Microsoft Windows Variable Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use these attributes on Microsoft Windows targets.
x86 Variable Attributes for additional Windows compatibility
attributes available on all x86 targets.

dllimport dllexport

  .. index:: dllimport variable attribute

  .. index:: dllexport variable attribute

  The ``dllimport`` and ``dllexport`` attributes are described in
  Microsoft Windows Function Attributes.

selectany

  .. index:: selectany variable attribute

  The ``selectany`` attribute causes an initialized global variable to
  have link-once semantics.  When multiple definitions of the variable are
  encountered by the linker, the first is selected and the remainder are
  discarded.  Following usage by the Microsoft compiler, the linker is told
  *not* to warn about size or content differences of the multiple
  definitions.

  Although the primary usage of this attribute is for POD types, the
  attribute can also be applied to global C++ objects that are initialized
  by a constructor.  In this case, the static initialization and destruction
  code for the object is emitted in each translation defining the object,
  but the calls to the constructor and destructor are protected by a
  link-once guard variable.

  The ``selectany`` attribute is only available on Microsoft Windows
  targets.  You can use ``__declspec (selectany)`` as a synonym for
  ``__attribute__ ((selectany))`` for compatibility with other
  compilers.

shared

  .. index:: shared variable attribute

  On Microsoft Windows, in addition to putting variable definitions in a named
  section, the section can also be shared among all running copies of an
  executable or DLL.  For example, this small program defines shared data
  by putting it in a named section ``shared`` and marking the section
  shareable:

  .. code-block:: c++

    int foo __attribute__((section ("shared"), shared)) = 0;

    int
    main()
    {
      /* Read and write foo.  All running
         copies see the same value.  */
      return 0;
    }

  You may only use the ``shared`` attribute along with ``section``
  attribute with a fully-initialized global definition because of the way
  linkers work.  See ``section`` attribute for more information.

  The ``shared`` attribute is only available on Microsoft Windows.

  .. _powerpc-variable-attributes:

PowerPC Variable Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Three attributes currently are defined for PowerPC configurations:
``altivec``, ``ms_struct`` and ``gcc_struct``.

.. index:: ms_struct variable attribute, PowerPC

.. index:: gcc_struct variable attribute, PowerPC

For full documentation of the struct attributes please see the
documentation in x86 Variable Attributes.

.. index:: altivec variable attribute, PowerPC

For documentation of ``altivec`` attribute please see the
documentation in PowerPC Type Attributes.

.. _spu-variable-attributes:

SPU Variable Attributes
^^^^^^^^^^^^^^^^^^^^^^^

.. index:: spu_vector variable attribute, SPU

The SPU supports the ``spu_vector`` attribute for variables.  For
documentation of this attribute please see the documentation in
SPU Type Attributes.

.. _x86-variable-attributes:

x86 Variable Attributes
^^^^^^^^^^^^^^^^^^^^^^^

Two attributes are currently defined for x86 configurations:
``ms_struct`` and ``gcc_struct``.

ms_struct gcc_struct

  .. index:: ms_struct variable attribute, x86

  .. index:: gcc_struct variable attribute, x86

  If ``packed`` is used on a structure, or if bit-fields are used,
  it may be that the Microsoft ABI lays out the structure differently
  than the way GCC normally does.  Particularly when moving packed
  data between functions compiled with GCC and the native Microsoft compiler
  (either via function call or as data in a file), it may be necessary to access
  either format.

  Currently :option:`-m[no-]ms-bitfields` is provided for the Microsoft Windows x86
  compilers to match the native Microsoft compiler.

  The Microsoft structure layout algorithm is fairly simple with the exception
  of the bit-field packing.  
  The padding and alignment of members of structures and whether a bit-field 
  can straddle a storage-unit boundary are determine by these rules:

  * Structure members are stored sequentially in the order in which they are
    declared: the first member has the lowest memory address and the last member
    the highest.

  * Every data object has an alignment requirement.  The alignment requirement
    for all data except structures, unions, and arrays is either the size of the
    object or the current packing size (specified with either the
    ``aligned`` attribute or the ``pack`` pragma),
    whichever is less.  For structures, unions, and arrays,
    the alignment requirement is the largest alignment requirement of its members.
    Every object is allocated an offset so that:

    .. code-block:: c++

      offset % alignment_requirement == 0

  * Adjacent bit-fields are packed into the same 1-, 2-, or 4-byte allocation
    unit if the integral types are the same size and if the next bit-field fits
    into the current allocation unit without crossing the boundary imposed by the
    common alignment requirements of the bit-fields.

  MSVC interprets zero-length bit-fields in the following ways:

  * If a zero-length bit-field is inserted between two bit-fields that
    are normally coalesced, the bit-fields are not coalesced.

    For example:

    .. code-block:: c++

      struct
       {
         unsigned long bf_1 : 12;
         unsigned long : 0;
         unsigned long bf_2 : 12;
       } t1;

    The size of ``t1`` is 8 bytes with the zero-length bit-field.  If the
    zero-length bit-field were removed, ``t1``'s size would be 4 bytes.

  * If a zero-length bit-field is inserted after a bit-field, ``foo``, and the
    alignment of the zero-length bit-field is greater than the member that follows it,
    ``bar``, ``bar`` is aligned as the type of the zero-length bit-field.

    For example:

    .. code-block:: c++

      struct
       {
         char foo : 4;
         short : 0;
         char bar;
       } t2;

      struct
       {
         char foo : 4;
         short : 0;
         double bar;
       } t3;

    For ``t2``, ``bar`` is placed at offset 2, rather than offset 1.
    Accordingly, the size of ``t2`` is 4.  For ``t3``, the zero-length
    bit-field does not affect the alignment of ``bar`` or, as a result, the size
    of the structure.

    Taking this into account, it is important to note the following:

    * If a zero-length bit-field follows a normal bit-field, the type of the
      zero-length bit-field may affect the alignment of the structure as whole. For
      example, ``t2`` has a size of 4 bytes, since the zero-length bit-field follows a
      normal bit-field, and is of type short.

    * Even if a zero-length bit-field is not followed by a normal bit-field, it may
      still affect the alignment of the structure:

      .. code-block:: c++

        struct
         {
           char foo : 6;
           long : 0;
         } t4;

      Here, ``t4`` takes up 4 bytes.

  * Zero-length bit-fields following non-bit-field members are ignored:

    .. code-block:: c++

      struct
       {
         char foo;
         long : 0;
         char bar;
       } t5;

    Here, ``t5`` takes up 2 bytes.

  .. _xstormy16-variable-attributes:

Xstormy16 Variable Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One attribute is currently defined for xstormy16 configurations:
``below100``.

below100

  .. index:: below100 variable attribute, Xstormy16

  If a variable has the ``below100`` attribute (``BELOW100`` is
  allowed also), GCC places the variable in the first 0x100 bytes of
  memory and use special opcodes to access it.  Such variables are
  placed in either the ``.bss_below100`` section or the
  ``.data_below100`` section.

