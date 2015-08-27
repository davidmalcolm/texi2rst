Built-in Functions Specific to Particular Target Machines
*********************************************************

On some target machines, GCC supports many built-in functions specific
to those machines.  Generally these generate calls to specific machine
instructions, but allow the compiler to schedule those calls.

.. toctree::

   <aarch64-built-in-functions>
   <alpha-built-in-functions>
   <altera-nios-ii-built-in-functions>
   <arc-built-in-functions>
   <arc-simd-built-in-functions>
   <arm-iwmmxt-built-in-functions>
   <arm-c-language-extensions-(acle)>
   <arm-floating-point-status-and-control-intrinsics>
   <avr-built-in-functions>
   <blackfin-built-in-functions>
   <fr-v-built-in-functions>
   <mips-dsp-built-in-functions>
   <mips-paired-single-support>
   <mips-loongson-built-in-functions>
   <other-mips-built-in-functions>
   <msp430-built-in-functions>
   <nds32-built-in-functions>
   <picochip-built-in-functions>
   <powerpc-built-in-functions>
   <powerpc-altivec/vsx-built-in-functions>
   <powerpc-hardware-transactional-memory-built-in-functions>
   <rx-built-in-functions>
   <s/390-system-z-built-in-functions>
   <sh-built-in-functions>
   <sparc-vis-built-in-functions>
   <spu-built-in-functions>
   <ti-c6x-built-in-functions>
   <tile-gx-built-in-functions>
   <tilepro-built-in-functions>
   <x86-built-in-functions>
   <x86-transactional-memory-intrinsics>

:: _aarch64-built-in-functions:

AArch64 Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^

These built-in functions are available for the AArch64 family of
processors.

.. code-block:: c++

  unsigned int __builtin_aarch64_get_fpcr ()
  void __builtin_aarch64_set_fpcr (unsigned int)
  unsigned int __builtin_aarch64_get_fpsr ()
  void __builtin_aarch64_set_fpsr (unsigned int)

:: _alpha-built-in-functions:

Alpha Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^

These built-in functions are available for the Alpha family of
processors, depending on the command-line switches used.

The following built-in functions are always available.  They
all generate the machine instruction that is part of the name.

.. code-block:: c++

  long __builtin_alpha_implver (void)
  long __builtin_alpha_rpcc (void)
  long __builtin_alpha_amask (long)
  long __builtin_alpha_cmpbge (long, long)
  long __builtin_alpha_extbl (long, long)
  long __builtin_alpha_extwl (long, long)
  long __builtin_alpha_extll (long, long)
  long __builtin_alpha_extql (long, long)
  long __builtin_alpha_extwh (long, long)
  long __builtin_alpha_extlh (long, long)
  long __builtin_alpha_extqh (long, long)
  long __builtin_alpha_insbl (long, long)
  long __builtin_alpha_inswl (long, long)
  long __builtin_alpha_insll (long, long)
  long __builtin_alpha_insql (long, long)
  long __builtin_alpha_inswh (long, long)
  long __builtin_alpha_inslh (long, long)
  long __builtin_alpha_insqh (long, long)
  long __builtin_alpha_mskbl (long, long)
  long __builtin_alpha_mskwl (long, long)
  long __builtin_alpha_mskll (long, long)
  long __builtin_alpha_mskql (long, long)
  long __builtin_alpha_mskwh (long, long)
  long __builtin_alpha_msklh (long, long)
  long __builtin_alpha_mskqh (long, long)
  long __builtin_alpha_umulh (long, long)
  long __builtin_alpha_zap (long, long)
  long __builtin_alpha_zapnot (long, long)

The following built-in functions are always with :option:`-mmax`
or :option:`-mcpu=``cpu``` where ``cpu`` is ``pca56`` or
later.  They all generate the machine instruction that is part
of the name.

.. code-block:: c++

  long __builtin_alpha_pklb (long)
  long __builtin_alpha_pkwb (long)
  long __builtin_alpha_unpkbl (long)
  long __builtin_alpha_unpkbw (long)
  long __builtin_alpha_minub8 (long, long)
  long __builtin_alpha_minsb8 (long, long)
  long __builtin_alpha_minuw4 (long, long)
  long __builtin_alpha_minsw4 (long, long)
  long __builtin_alpha_maxub8 (long, long)
  long __builtin_alpha_maxsb8 (long, long)
  long __builtin_alpha_maxuw4 (long, long)
  long __builtin_alpha_maxsw4 (long, long)
  long __builtin_alpha_perr (long, long)

The following built-in functions are always with :option:`-mcix`
or :option:`-mcpu=``cpu``` where ``cpu`` is ``ev67`` or
later.  They all generate the machine instruction that is part
of the name.

.. code-block:: c++

  long __builtin_alpha_cttz (long)
  long __builtin_alpha_ctlz (long)
  long __builtin_alpha_ctpop (long)

The following built-in functions are available on systems that use the OSF/1
PALcode.  Normally they invoke the ``rduniq`` and ``wruniq``
PAL calls, but when invoked with :option:`-mtls-kernel`, they invoke
``rdval`` and ``wrval``.

.. code-block:: c++

  void *__builtin_thread_pointer (void)
  void __builtin_set_thread_pointer (void *)

:: _altera-nios-ii-built-in-functions:

Altera Nios II Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These built-in functions are available for the Altera Nios II
family of processors.

The following built-in functions are always available.  They
all generate the machine instruction that is part of the name.

.. code-block:: c++

  int __builtin_ldbio (volatile const void *)
  int __builtin_ldbuio (volatile const void *)
  int __builtin_ldhio (volatile const void *)
  int __builtin_ldhuio (volatile const void *)
  int __builtin_ldwio (volatile const void *)
  void __builtin_stbio (volatile void *, int)
  void __builtin_sthio (volatile void *, int)
  void __builtin_stwio (volatile void *, int)
  void __builtin_sync (void)
  int __builtin_rdctl (int) 
  void __builtin_wrctl (int, int)

The following built-in functions are always available.  They
all generate a Nios II Custom Instruction. The name of the
function represents the types that the function takes and
returns. The letter before the ``n`` is the return type
or void if absent. The ``n`` represents the first parameter
to all the custom instructions, the custom instruction number.
The two letters after the ``n`` represent the up to two
parameters to the function.

The letters represent the following data types:

<no letter>
  ``void`` for return type and no parameter for parameter types.

i
  ``int`` for return type and parameter type

f
  ``float`` for return type and parameter type

p
  ``void *`` for return type and parameter type

And the function names are:

.. code-block:: c++

  void __builtin_custom_n (void)
  void __builtin_custom_ni (int)
  void __builtin_custom_nf (float)
  void __builtin_custom_np (void *)
  void __builtin_custom_nii (int, int)
  void __builtin_custom_nif (int, float)
  void __builtin_custom_nip (int, void *)
  void __builtin_custom_nfi (float, int)
  void __builtin_custom_nff (float, float)
  void __builtin_custom_nfp (float, void *)
  void __builtin_custom_npi (void *, int)
  void __builtin_custom_npf (void *, float)
  void __builtin_custom_npp (void *, void *)
  int __builtin_custom_in (void)
  int __builtin_custom_ini (int)
  int __builtin_custom_inf (float)
  int __builtin_custom_inp (void *)
  int __builtin_custom_inii (int, int)
  int __builtin_custom_inif (int, float)
  int __builtin_custom_inip (int, void *)
  int __builtin_custom_infi (float, int)
  int __builtin_custom_inff (float, float)
  int __builtin_custom_infp (float, void *)
  int __builtin_custom_inpi (void *, int)
  int __builtin_custom_inpf (void *, float)
  int __builtin_custom_inpp (void *, void *)
  float __builtin_custom_fn (void)
  float __builtin_custom_fni (int)
  float __builtin_custom_fnf (float)
  float __builtin_custom_fnp (void *)
  float __builtin_custom_fnii (int, int)
  float __builtin_custom_fnif (int, float)
  float __builtin_custom_fnip (int, void *)
  float __builtin_custom_fnfi (float, int)
  float __builtin_custom_fnff (float, float)
  float __builtin_custom_fnfp (float, void *)
  float __builtin_custom_fnpi (void *, int)
  float __builtin_custom_fnpf (void *, float)
  float __builtin_custom_fnpp (void *, void *)
  void * __builtin_custom_pn (void)
  void * __builtin_custom_pni (int)
  void * __builtin_custom_pnf (float)
  void * __builtin_custom_pnp (void *)
  void * __builtin_custom_pnii (int, int)
  void * __builtin_custom_pnif (int, float)
  void * __builtin_custom_pnip (int, void *)
  void * __builtin_custom_pnfi (float, int)
  void * __builtin_custom_pnff (float, float)
  void * __builtin_custom_pnfp (float, void *)
  void * __builtin_custom_pnpi (void *, int)
  void * __builtin_custom_pnpf (void *, float)
  void * __builtin_custom_pnpp (void *, void *)

:: _arc-built-in-functions:

ARC Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^

The following built-in functions are provided for ARC targets.  The
built-ins generate the corresponding assembly instructions.  In the
examples given below, the generated code often requires an operand or
result to be in a register.  Where necessary further code will be
generated to ensure this is true, but for brevity this is not
described in each case.

Note: Using a built-in to generate an instruction not supported
by a target may cause problems. At present the compiler is not
guaranteed to detect such misuse, and as a result an internal compiler
error may be generated.

.. index:: __builtin_arc_aligned

  Built-in Function int __builtin_arc_aligned (void *``val``, int ``alignval``)
Return 1 if ``val`` is known to have the byte alignment given
by ``alignval``, otherwise return 0.
Note that this is different from

.. code-block:: c++

  __alignof__(*(char *)``val``) >= alignval

because __alignof__ sees only the type of the dereference, whereas
__builtin_arc_align uses alignment information from the pointer
as well as from the pointed-to type.
The information available will depend on optimization level.

.. index:: __builtin_arc_brk

  Built-in Function void __builtin_arc_brk (void)
Generates

.. code-block:: c++

  brk

.. index:: __builtin_arc_core_read

  Built-in Function unsigned int __builtin_arc_core_read (unsigned int ``regno``)
The operand is the number of a register to be read.  Generates:

.. code-block:: c++

  mov  ``dest``, r``regno``

where the value in ``dest`` will be the result returned from the
built-in.

.. index:: __builtin_arc_core_write

  Built-in Function void __builtin_arc_core_write (unsigned int ``regno``, unsigned int ``val``)
The first operand is the number of a register to be written, the
second operand is a compile time constant to write into that
register.  Generates:

.. code-block:: c++

  mov  r``regno``, ``val``

.. index:: __builtin_arc_divaw

  Built-in Function int __builtin_arc_divaw (int ``a``, int ``b``)
Only available if either :option:`-mcpu=ARC700` or :option:`-meA` is set.
Generates:

.. code-block:: c++

  divaw  ``dest``, ``a``, ``b``

where the value in ``dest`` will be the result returned from the
built-in.

.. index:: __builtin_arc_flag

  Built-in Function void __builtin_arc_flag (unsigned int ``a``)
Generates

.. code-block:: c++

  flag  ``a``

.. index:: __builtin_arc_lr

  Built-in Function unsigned int __builtin_arc_lr (unsigned int ``auxr``)
The operand, ``auxv``, is the address of an auxiliary register and
must be a compile time constant.  Generates:

.. code-block:: c++

  lr  ``dest``, [``auxr``]

Where the value in ``dest`` will be the result returned from the
built-in.

.. index:: __builtin_arc_mul64

  Built-in Function void __builtin_arc_mul64 (int ``a``, int ``b``)
Only available with :option:`-mmul64`.  Generates:

.. code-block:: c++

  mul64  ``a``, ``b``

.. index:: __builtin_arc_mulu64

  Built-in Function void __builtin_arc_mulu64 (unsigned int ``a``, unsigned int ``b``)
Only available with :option:`-mmul64`.  Generates:

.. code-block:: c++

  mulu64  ``a``, ``b``

.. index:: __builtin_arc_nop

  Built-in Function void __builtin_arc_nop (void)
Generates:

.. code-block:: c++

  nop

.. index:: __builtin_arc_norm

  Built-in Function int __builtin_arc_norm (int ``src``)
Only valid if the norm instruction is available through the
:option:`-mnorm` option or by default with :option:`-mcpu=ARC700`.
Generates:

.. code-block:: c++

  norm  ``dest``, ``src``

Where the value in ``dest`` will be the result returned from the
built-in.

.. index:: __builtin_arc_normw

  Built-in Function  short int __builtin_arc_normw (short int ``src``)
Only valid if the normw instruction is available through the
:option:`-mnorm` option or by default with :option:`-mcpu=ARC700`.
Generates:

.. code-block:: c++

  normw  ``dest``, ``src``

Where the value in ``dest`` will be the result returned from the
built-in.

.. index:: __builtin_arc_rtie

  Built-in Function  void __builtin_arc_rtie (void)
Generates:

.. code-block:: c++

  rtie

.. index:: __builtin_arc_sleep

  Built-in Function  void __builtin_arc_sleep (int ``a``
Generates:

.. code-block:: c++

  sleep  ``a``

.. index:: __builtin_arc_sr

  Built-in Function  void __builtin_arc_sr (unsigned int ``auxr``, unsigned int ``val``)
The first argument, ``auxv``, is the address of an auxiliary
register, the second argument, ``val``, is a compile time constant
to be written to the register.  Generates:

.. code-block:: c++

  sr  ``auxr``, [``val``]

.. index:: __builtin_arc_swap

  Built-in Function  int __builtin_arc_swap (int ``src``)
Only valid with :option:`-mswap`.  Generates:

.. code-block:: c++

  swap  ``dest``, ``src``

Where the value in ``dest`` will be the result returned from the
built-in.

.. index:: __builtin_arc_swi

  Built-in Function  void __builtin_arc_swi (void)
Generates:

.. code-block:: c++

  swi

.. index:: __builtin_arc_sync

  Built-in Function  void __builtin_arc_sync (void)
Only available with :option:`-mcpu=ARC700`.  Generates:

.. code-block:: c++

  sync

.. index:: __builtin_arc_trap_s

  Built-in Function  void __builtin_arc_trap_s (unsigned int ``c``)
Only available with :option:`-mcpu=ARC700`.  Generates:

.. code-block:: c++

  trap_s  ``c``

.. index:: __builtin_arc_unimp_s

  Built-in Function  void __builtin_arc_unimp_s (void)
Only available with :option:`-mcpu=ARC700`.  Generates:

.. code-block:: c++

  unimp_s

The instructions generated by the following builtins are not
considered as candidates for scheduling.  They are not moved around by
the compiler during scheduling, and thus can be expected to appear
where they are put in the C code:

.. code-block:: c++

  __builtin_arc_brk()
  __builtin_arc_core_read()
  __builtin_arc_core_write()
  __builtin_arc_flag()
  __builtin_arc_lr()
  __builtin_arc_sleep()
  __builtin_arc_sr()
  __builtin_arc_swi()

:: _arc-simd-built-in-functions:

ARC SIMD Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

SIMD builtins provided by the compiler can be used to generate the
vector instructions.  This section describes the available builtins
and their usage in programs.  With the :option:`-msimd` option, the
compiler provides 128-bit vector types, which can be specified using
the ``vector_size`` attribute.  The header file arc-simd.h
can be included to use the following predefined types:

.. code-block:: c++

  typedef int __v4si   __attribute__((vector_size(16)));
  typedef short __v8hi __attribute__((vector_size(16)));

These types can be used to define 128-bit variables.  The built-in
functions listed in the following section can be used on these
variables to generate the vector operations.

For all builtins, ``__builtin_arc_``someinsn````, the header file
arc-simd.h also provides equivalent macros called
``_``someinsn```` that can be used for programming ease and
improved readability.  The following macros for DMA control are also
provided:

.. code-block:: c++

  #define _setup_dma_in_channel_reg _vdiwr
  #define _setup_dma_out_channel_reg _vdowr

The following is a complete list of all the SIMD built-ins provided
for ARC, grouped by calling signature.

The following take two ``__v8hi`` arguments and return a
``__v8hi`` result:

.. code-block:: c++

  __v8hi __builtin_arc_vaddaw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vaddw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vand (__v8hi, __v8hi)
  __v8hi __builtin_arc_vandaw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vavb (__v8hi, __v8hi)
  __v8hi __builtin_arc_vavrb (__v8hi, __v8hi)
  __v8hi __builtin_arc_vbic (__v8hi, __v8hi)
  __v8hi __builtin_arc_vbicaw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vdifaw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vdifw (__v8hi, __v8hi)
  __v8hi __builtin_arc_veqw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vh264f (__v8hi, __v8hi)
  __v8hi __builtin_arc_vh264ft (__v8hi, __v8hi)
  __v8hi __builtin_arc_vh264fw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vlew (__v8hi, __v8hi)
  __v8hi __builtin_arc_vltw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmaxaw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmaxw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vminaw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vminw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmr1aw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmr1w (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmr2aw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmr2w (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmr3aw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmr3w (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmr4aw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmr4w (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmr5aw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmr5w (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmr6aw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmr6w (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmr7aw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmr7w (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmrb (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmulaw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmulfaw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmulfw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vmulw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vnew (__v8hi, __v8hi)
  __v8hi __builtin_arc_vor (__v8hi, __v8hi)
  __v8hi __builtin_arc_vsubaw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vsubw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vsummw (__v8hi, __v8hi)
  __v8hi __builtin_arc_vvc1f (__v8hi, __v8hi)
  __v8hi __builtin_arc_vvc1ft (__v8hi, __v8hi)
  __v8hi __builtin_arc_vxor (__v8hi, __v8hi)
  __v8hi __builtin_arc_vxoraw (__v8hi, __v8hi)

The following take one ``__v8hi`` and one ``int`` argument and return a
``__v8hi`` result:

.. code-block:: c++

  __v8hi __builtin_arc_vbaddw (__v8hi, int)
  __v8hi __builtin_arc_vbmaxw (__v8hi, int)
  __v8hi __builtin_arc_vbminw (__v8hi, int)
  __v8hi __builtin_arc_vbmulaw (__v8hi, int)
  __v8hi __builtin_arc_vbmulfw (__v8hi, int)
  __v8hi __builtin_arc_vbmulw (__v8hi, int)
  __v8hi __builtin_arc_vbrsubw (__v8hi, int)
  __v8hi __builtin_arc_vbsubw (__v8hi, int)

The following take one ``__v8hi`` argument and one ``int`` argument which
must be a 3-bit compile time constant indicating a register number
I0-I7.  They return a ``__v8hi`` result.

.. code-block:: c++

  __v8hi __builtin_arc_vasrw (__v8hi, const int)
  __v8hi __builtin_arc_vsr8 (__v8hi, const int)
  __v8hi __builtin_arc_vsr8aw (__v8hi, const int)

The following take one ``__v8hi`` argument and one ``int``
argument which must be a 6-bit compile time constant.  They return a
``__v8hi`` result.

.. code-block:: c++

  __v8hi __builtin_arc_vasrpwbi (__v8hi, const int)
  __v8hi __builtin_arc_vasrrpwbi (__v8hi, const int)
  __v8hi __builtin_arc_vasrrwi (__v8hi, const int)
  __v8hi __builtin_arc_vasrsrwi (__v8hi, const int)
  __v8hi __builtin_arc_vasrwi (__v8hi, const int)
  __v8hi __builtin_arc_vsr8awi (__v8hi, const int)
  __v8hi __builtin_arc_vsr8i (__v8hi, const int)

The following take one ``__v8hi`` argument and one ``int`` argument which
must be a 8-bit compile time constant.  They return a ``__v8hi``
result.

.. code-block:: c++

  __v8hi __builtin_arc_vd6tapf (__v8hi, const int)
  __v8hi __builtin_arc_vmvaw (__v8hi, const int)
  __v8hi __builtin_arc_vmvw (__v8hi, const int)
  __v8hi __builtin_arc_vmvzw (__v8hi, const int)

The following take two ``int`` arguments, the second of which which
must be a 8-bit compile time constant.  They return a ``__v8hi``
result:

.. code-block:: c++

  __v8hi __builtin_arc_vmovaw (int, const int)
  __v8hi __builtin_arc_vmovw (int, const int)
  __v8hi __builtin_arc_vmovzw (int, const int)

The following take a single ``__v8hi`` argument and return a
``__v8hi`` result:

.. code-block:: c++

  __v8hi __builtin_arc_vabsaw (__v8hi)
  __v8hi __builtin_arc_vabsw (__v8hi)
  __v8hi __builtin_arc_vaddsuw (__v8hi)
  __v8hi __builtin_arc_vexch1 (__v8hi)
  __v8hi __builtin_arc_vexch2 (__v8hi)
  __v8hi __builtin_arc_vexch4 (__v8hi)
  __v8hi __builtin_arc_vsignw (__v8hi)
  __v8hi __builtin_arc_vupbaw (__v8hi)
  __v8hi __builtin_arc_vupbw (__v8hi)
  __v8hi __builtin_arc_vupsbaw (__v8hi)
  __v8hi __builtin_arc_vupsbw (__v8hi)

The following take two ``int`` arguments and return no result:

.. code-block:: c++

  void __builtin_arc_vdirun (int, int)
  void __builtin_arc_vdorun (int, int)

The following take two ``int`` arguments and return no result.  The
first argument must a 3-bit compile time constant indicating one of
the DR0-DR7 DMA setup channels:

.. code-block:: c++

  void __builtin_arc_vdiwr (const int, int)
  void __builtin_arc_vdowr (const int, int)

The following take an ``int`` argument and return no result:

.. code-block:: c++

  void __builtin_arc_vendrec (int)
  void __builtin_arc_vrec (int)
  void __builtin_arc_vrecrun (int)
  void __builtin_arc_vrun (int)

The following take a ``__v8hi`` argument and two ``int``
arguments and return a ``__v8hi`` result.  The second argument must
be a 3-bit compile time constants, indicating one the registers I0-I7,
and the third argument must be an 8-bit compile time constant.

Note: Although the equivalent hardware instructions do not take
an SIMD register as an operand, these builtins overwrite the relevant
bits of the ``__v8hi`` register provided as the first argument with
the value loaded from the ``[Ib, u8]`` location in the SDM.

.. code-block:: c++

  __v8hi __builtin_arc_vld32 (__v8hi, const int, const int)
  __v8hi __builtin_arc_vld32wh (__v8hi, const int, const int)
  __v8hi __builtin_arc_vld32wl (__v8hi, const int, const int)
  __v8hi __builtin_arc_vld64 (__v8hi, const int, const int)

The following take two ``int`` arguments and return a ``__v8hi``
result.  The first argument must be a 3-bit compile time constants,
indicating one the registers I0-I7, and the second argument must be an
8-bit compile time constant.

.. code-block:: c++

  __v8hi __builtin_arc_vld128 (const int, const int)
  __v8hi __builtin_arc_vld64w (const int, const int)

The following take a ``__v8hi`` argument and two ``int``
arguments and return no result.  The second argument must be a 3-bit
compile time constants, indicating one the registers I0-I7, and the
third argument must be an 8-bit compile time constant.

.. code-block:: c++

  void __builtin_arc_vst128 (__v8hi, const int, const int)
  void __builtin_arc_vst64 (__v8hi, const int, const int)

The following take a ``__v8hi`` argument and three ``int``
arguments and return no result.  The second argument must be a 3-bit
compile-time constant, identifying the 16-bit sub-register to be
stored, the third argument must be a 3-bit compile time constants,
indicating one the registers I0-I7, and the fourth argument must be an
8-bit compile time constant.

.. code-block:: c++

  void __builtin_arc_vst16_n (__v8hi, const int, const int, const int)
  void __builtin_arc_vst32_n (__v8hi, const int, const int, const int)

:: _arm-iwmmxt-built-in-functions:

ARM iWMMXt Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These built-in functions are available for the ARM family of
processors when the :option:`-mcpu=iwmmxt` switch is used:

.. code-block:: c++

  typedef int v2si __attribute__ ((vector_size (8)));
  typedef short v4hi __attribute__ ((vector_size (8)));
  typedef char v8qi __attribute__ ((vector_size (8)));

  int __builtin_arm_getwcgr0 (void)
  void __builtin_arm_setwcgr0 (int)
  int __builtin_arm_getwcgr1 (void)
  void __builtin_arm_setwcgr1 (int)
  int __builtin_arm_getwcgr2 (void)
  void __builtin_arm_setwcgr2 (int)
  int __builtin_arm_getwcgr3 (void)
  void __builtin_arm_setwcgr3 (int)
  int __builtin_arm_textrmsb (v8qi, int)
  int __builtin_arm_textrmsh (v4hi, int)
  int __builtin_arm_textrmsw (v2si, int)
  int __builtin_arm_textrmub (v8qi, int)
  int __builtin_arm_textrmuh (v4hi, int)
  int __builtin_arm_textrmuw (v2si, int)
  v8qi __builtin_arm_tinsrb (v8qi, int, int)
  v4hi __builtin_arm_tinsrh (v4hi, int, int)
  v2si __builtin_arm_tinsrw (v2si, int, int)
  long long __builtin_arm_tmia (long long, int, int)
  long long __builtin_arm_tmiabb (long long, int, int)
  long long __builtin_arm_tmiabt (long long, int, int)
  long long __builtin_arm_tmiaph (long long, int, int)
  long long __builtin_arm_tmiatb (long long, int, int)
  long long __builtin_arm_tmiatt (long long, int, int)
  int __builtin_arm_tmovmskb (v8qi)
  int __builtin_arm_tmovmskh (v4hi)
  int __builtin_arm_tmovmskw (v2si)
  long long __builtin_arm_waccb (v8qi)
  long long __builtin_arm_wacch (v4hi)
  long long __builtin_arm_waccw (v2si)
  v8qi __builtin_arm_waddb (v8qi, v8qi)
  v8qi __builtin_arm_waddbss (v8qi, v8qi)
  v8qi __builtin_arm_waddbus (v8qi, v8qi)
  v4hi __builtin_arm_waddh (v4hi, v4hi)
  v4hi __builtin_arm_waddhss (v4hi, v4hi)
  v4hi __builtin_arm_waddhus (v4hi, v4hi)
  v2si __builtin_arm_waddw (v2si, v2si)
  v2si __builtin_arm_waddwss (v2si, v2si)
  v2si __builtin_arm_waddwus (v2si, v2si)
  v8qi __builtin_arm_walign (v8qi, v8qi, int)
  long long __builtin_arm_wand(long long, long long)
  long long __builtin_arm_wandn (long long, long long)
  v8qi __builtin_arm_wavg2b (v8qi, v8qi)
  v8qi __builtin_arm_wavg2br (v8qi, v8qi)
  v4hi __builtin_arm_wavg2h (v4hi, v4hi)
  v4hi __builtin_arm_wavg2hr (v4hi, v4hi)
  v8qi __builtin_arm_wcmpeqb (v8qi, v8qi)
  v4hi __builtin_arm_wcmpeqh (v4hi, v4hi)
  v2si __builtin_arm_wcmpeqw (v2si, v2si)
  v8qi __builtin_arm_wcmpgtsb (v8qi, v8qi)
  v4hi __builtin_arm_wcmpgtsh (v4hi, v4hi)
  v2si __builtin_arm_wcmpgtsw (v2si, v2si)
  v8qi __builtin_arm_wcmpgtub (v8qi, v8qi)
  v4hi __builtin_arm_wcmpgtuh (v4hi, v4hi)
  v2si __builtin_arm_wcmpgtuw (v2si, v2si)
  long long __builtin_arm_wmacs (long long, v4hi, v4hi)
  long long __builtin_arm_wmacsz (v4hi, v4hi)
  long long __builtin_arm_wmacu (long long, v4hi, v4hi)
  long long __builtin_arm_wmacuz (v4hi, v4hi)
  v4hi __builtin_arm_wmadds (v4hi, v4hi)
  v4hi __builtin_arm_wmaddu (v4hi, v4hi)
  v8qi __builtin_arm_wmaxsb (v8qi, v8qi)
  v4hi __builtin_arm_wmaxsh (v4hi, v4hi)
  v2si __builtin_arm_wmaxsw (v2si, v2si)
  v8qi __builtin_arm_wmaxub (v8qi, v8qi)
  v4hi __builtin_arm_wmaxuh (v4hi, v4hi)
  v2si __builtin_arm_wmaxuw (v2si, v2si)
  v8qi __builtin_arm_wminsb (v8qi, v8qi)
  v4hi __builtin_arm_wminsh (v4hi, v4hi)
  v2si __builtin_arm_wminsw (v2si, v2si)
  v8qi __builtin_arm_wminub (v8qi, v8qi)
  v4hi __builtin_arm_wminuh (v4hi, v4hi)
  v2si __builtin_arm_wminuw (v2si, v2si)
  v4hi __builtin_arm_wmulsm (v4hi, v4hi)
  v4hi __builtin_arm_wmulul (v4hi, v4hi)
  v4hi __builtin_arm_wmulum (v4hi, v4hi)
  long long __builtin_arm_wor (long long, long long)
  v2si __builtin_arm_wpackdss (long long, long long)
  v2si __builtin_arm_wpackdus (long long, long long)
  v8qi __builtin_arm_wpackhss (v4hi, v4hi)
  v8qi __builtin_arm_wpackhus (v4hi, v4hi)
  v4hi __builtin_arm_wpackwss (v2si, v2si)
  v4hi __builtin_arm_wpackwus (v2si, v2si)
  long long __builtin_arm_wrord (long long, long long)
  long long __builtin_arm_wrordi (long long, int)
  v4hi __builtin_arm_wrorh (v4hi, long long)
  v4hi __builtin_arm_wrorhi (v4hi, int)
  v2si __builtin_arm_wrorw (v2si, long long)
  v2si __builtin_arm_wrorwi (v2si, int)
  v2si __builtin_arm_wsadb (v2si, v8qi, v8qi)
  v2si __builtin_arm_wsadbz (v8qi, v8qi)
  v2si __builtin_arm_wsadh (v2si, v4hi, v4hi)
  v2si __builtin_arm_wsadhz (v4hi, v4hi)
  v4hi __builtin_arm_wshufh (v4hi, int)
  long long __builtin_arm_wslld (long long, long long)
  long long __builtin_arm_wslldi (long long, int)
  v4hi __builtin_arm_wsllh (v4hi, long long)
  v4hi __builtin_arm_wsllhi (v4hi, int)
  v2si __builtin_arm_wsllw (v2si, long long)
  v2si __builtin_arm_wsllwi (v2si, int)
  long long __builtin_arm_wsrad (long long, long long)
  long long __builtin_arm_wsradi (long long, int)
  v4hi __builtin_arm_wsrah (v4hi, long long)
  v4hi __builtin_arm_wsrahi (v4hi, int)
  v2si __builtin_arm_wsraw (v2si, long long)
  v2si __builtin_arm_wsrawi (v2si, int)
  long long __builtin_arm_wsrld (long long, long long)
  long long __builtin_arm_wsrldi (long long, int)
  v4hi __builtin_arm_wsrlh (v4hi, long long)
  v4hi __builtin_arm_wsrlhi (v4hi, int)
  v2si __builtin_arm_wsrlw (v2si, long long)
  v2si __builtin_arm_wsrlwi (v2si, int)
  v8qi __builtin_arm_wsubb (v8qi, v8qi)
  v8qi __builtin_arm_wsubbss (v8qi, v8qi)
  v8qi __builtin_arm_wsubbus (v8qi, v8qi)
  v4hi __builtin_arm_wsubh (v4hi, v4hi)
  v4hi __builtin_arm_wsubhss (v4hi, v4hi)
  v4hi __builtin_arm_wsubhus (v4hi, v4hi)
  v2si __builtin_arm_wsubw (v2si, v2si)
  v2si __builtin_arm_wsubwss (v2si, v2si)
  v2si __builtin_arm_wsubwus (v2si, v2si)
  v4hi __builtin_arm_wunpckehsb (v8qi)
  v2si __builtin_arm_wunpckehsh (v4hi)
  long long __builtin_arm_wunpckehsw (v2si)
  v4hi __builtin_arm_wunpckehub (v8qi)
  v2si __builtin_arm_wunpckehuh (v4hi)
  long long __builtin_arm_wunpckehuw (v2si)
  v4hi __builtin_arm_wunpckelsb (v8qi)
  v2si __builtin_arm_wunpckelsh (v4hi)
  long long __builtin_arm_wunpckelsw (v2si)
  v4hi __builtin_arm_wunpckelub (v8qi)
  v2si __builtin_arm_wunpckeluh (v4hi)
  long long __builtin_arm_wunpckeluw (v2si)
  v8qi __builtin_arm_wunpckihb (v8qi, v8qi)
  v4hi __builtin_arm_wunpckihh (v4hi, v4hi)
  v2si __builtin_arm_wunpckihw (v2si, v2si)
  v8qi __builtin_arm_wunpckilb (v8qi, v8qi)
  v4hi __builtin_arm_wunpckilh (v4hi, v4hi)
  v2si __builtin_arm_wunpckilw (v2si, v2si)
  long long __builtin_arm_wxor (long long, long long)
  long long __builtin_arm_wzero ()

:: _arm-c-language-extensions-(acle):

ARM C Language Extensions (ACLE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GCC implements extensions for C as described in the ARM C Language
Extensions (ACLE) specification, which can be found at
http://infocenter.arm.com/help/topic/com.arm.doc.ihi0053c/IHI0053C_acle_2_0.pdf.

As a part of ACLE, GCC implements extensions for Advanced SIMD as described in
the ARM C Language Extensions Specification.  The complete list of Advanced SIMD
intrinsics can be found at
http://infocenter.arm.com/help/topic/com.arm.doc.ihi0073a/IHI0073A_arm_neon_intrinsics_ref.pdf.
The built-in intrinsics for the Advanced SIMD extension are available when
NEON is enabled.

Currently, ARM and AArch64 back ends do not support ACLE 2.0 fully.  Both
back ends support CRC32 intrinsics from arm_acle.h.  The ARM back end's
16-bit floating-point Advanced SIMD intrinsics currently comply to ACLE v1.1.
AArch64's back end does not have support for 16-bit floating point Advanced SIMD
intrinsics yet.

See ARM Options and AArch64 Options for more information on the
availability of extensions.

:: _arm-floating-point-status-and-control-intrinsics:

ARM Floating Point Status and Control Intrinsics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These built-in functions are available for the ARM family of
processors with floating-point unit.

.. code-block:: c++

  unsigned int __builtin_arm_get_fpscr ()
  void __builtin_arm_set_fpscr (unsigned int)

:: _avr-built-in-functions:

AVR Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^

For each built-in function for AVR, there is an equally named,
uppercase built-in macro defined. That way users can easily query if
or if not a specific built-in is implemented or not. For example, if
``__builtin_avr_nop`` is available the macro
``__BUILTIN_AVR_NOP`` is defined to ``1`` and undefined otherwise.

The following built-in functions map to the respective machine
instruction, i.e. ``nop``, ``sei``, ``cli``, ``sleep``,
``wdr``, ``swap``, ``fmul``, ``fmuls``
resp. ``fmulsu``. The three ``fmul*`` built-ins are implemented
as library call if no hardware multiplier is available.

.. code-block:: c++

  void __builtin_avr_nop (void)
  void __builtin_avr_sei (void)
  void __builtin_avr_cli (void)
  void __builtin_avr_sleep (void)
  void __builtin_avr_wdr (void)
  unsigned char __builtin_avr_swap (unsigned char)
  unsigned int __builtin_avr_fmul (unsigned char, unsigned char)
  int __builtin_avr_fmuls (char, char)
  int __builtin_avr_fmulsu (char, unsigned char)

In order to delay execution for a specific number of cycles, GCC
implements

.. code-block:: c++

  void __builtin_avr_delay_cycles (unsigned long ticks)

``ticks`` is the number of ticks to delay execution. Note that this
built-in does not take into account the effect of interrupts that
might increase delay time. ``ticks`` must be a compile-time
integer constant; delays with a variable number of cycles are not supported.

.. code-block:: c++

  char __builtin_avr_flash_segment (const __memx void*)

This built-in takes a byte address to the 24-bit
AVR Named Address Spacesaddress space ``__memx`` and returns
the number of the flash segment (the 64 KiB chunk) where the address
points to.  Counting starts at ``0``.
If the address does not point to flash memory, return ``-1``.

.. code-block:: c++

  unsigned char __builtin_avr_insert_bits (unsigned long map, unsigned char bits, unsigned char val)

Insert bits from ``bits`` into ``val`` and return the resulting
value. The nibbles of ``map`` determine how the insertion is
performed: Let ``X`` be the ``n``-th nibble of ``map``

* If ``X`` is ``0xf``,
  then the ``n``-th bit of ``val`` is returned unaltered.

  * If X is in the range 0...7,
  then the ``n``-th result bit is set to the ``X``-th bit of ``bits``

  * If X is in the range 8...``0xe``,
  then the ``n``-th result bit is undefined.

One typical use case for this built-in is adjusting input and
output values to non-contiguous port layouts. Some examples:

.. code-block:: c++

  // same as val, bits is unused
  __builtin_avr_insert_bits (0xffffffff, bits, val)

.. code-block:: c++

  // same as bits, val is unused
  __builtin_avr_insert_bits (0x76543210, bits, val)

.. code-block:: c++

  // same as rotating bits by 4
  __builtin_avr_insert_bits (0x32107654, bits, 0)

.. code-block:: c++

  // high nibble of result is the high nibble of val
  // low nibble of result is the low nibble of bits
  __builtin_avr_insert_bits (0xffff3210, bits, val)

.. code-block:: c++

  // reverse the bit order of bits
  __builtin_avr_insert_bits (0x01234567, bits, 0)

:: _blackfin-built-in-functions:

Blackfin Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently, there are two Blackfin-specific built-in functions.  These are
used for generating ``CSYNC`` and ``SSYNC`` machine insns without
using inline assembly; by using these built-in functions the compiler can
automatically add workarounds for hardware errata involving these
instructions.  These functions are named as follows:

.. code-block:: c++

  void __builtin_bfin_csync (void)
  void __builtin_bfin_ssync (void)

:: _fr-v-built-in-functions:

FR-V Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^

GCC provides many FR-V-specific built-in functions.  In general,
these functions are intended to be compatible with those described
by FR-V Family, Softune C/C++ Compiler Manual (V6), Fujitsu
Semiconductor.  The two exceptions are ``__MDUNPACKH`` and
``__MBTOHE``, the GCC forms of which pass 128-bit values by
pointer rather than by value.

Most of the functions are named after specific FR-V instructions.
Such functions are said to be 'directly mapped' and are summarized
here in tabular form.

.. toctree::

   <argument-types>
   <directly-mapped-integer-functions>
   <directly-mapped-media-functions>
   <raw-read/write-functions>
   <other-built-in-functions>

:: _argument-types:

Argument Types
~~~~~~~~~~~~~~

The arguments to the built-in functions can be divided into three groups:
register numbers, compile-time constants and run-time values.  In order
to make this classification clear at a glance, the arguments and return
values are given the following pseudo types:

Pseudo type Real C type Constant? Description
``uh`` ``unsigned short`` No an unsigned halfword
``uw1`` ``unsigned int`` No an unsigned word
``sw1`` ``int`` No a signed word
``uw2`` ``unsigned long long`` No
an unsigned doubleword
``sw2`` ``long long`` No a signed doubleword
``const`` ``int`` Yes an integer constant
``acc`` ``int`` Yes an ACC register number
``iacc`` ``int`` Yes an IACC register number

These pseudo types are not defined by GCC, they are simply a notational
convenience used in this manual.

Arguments of type ``uh``, ``uw1``, ``sw1``, ``uw2``
and ``sw2`` are evaluated at run time.  They correspond to
register operands in the underlying FR-V instructions.

``const`` arguments represent immediate operands in the underlying
FR-V instructions.  They must be compile-time constants.

``acc`` arguments are evaluated at compile time and specify the number
of an accumulator register.  For example, an ``acc`` argument of 2
selects the ACC2 register.

``iacc`` arguments are similar to ``acc`` arguments but specify the
number of an IACC register.  See Other Built-in Functions
for more details.

:: _directly-mapped-integer-functions:

Directly-Mapped Integer Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The functions listed below map directly to FR-V I-type instructions.

Function prototype Example usage Assembly output
``sw1 __ADDSS (sw1, sw1)``
````c`` = __ADDSS (``a``, ``b``)``
``ADDSS ``a``,``b``,``c````
``sw1 __SCAN (sw1, sw1)``
````c`` = __SCAN (``a``, ``b``)``
``SCAN ``a``,``b``,``c````
``sw1 __SCUTSS (sw1)``
````b`` = __SCUTSS (``a``)``
``SCUTSS ``a``,``b````
``sw1 __SLASS (sw1, sw1)``
````c`` = __SLASS (``a``, ``b``)``
``SLASS ``a``,``b``,``c````
``void __SMASS (sw1, sw1)``
``__SMASS (``a``, ``b``)``
``SMASS ``a``,``b````
``void __SMSSS (sw1, sw1)``
``__SMSSS (``a``, ``b``)``
``SMSSS ``a``,``b````
``void __SMU (sw1, sw1)``
``__SMU (``a``, ``b``)``
``SMU ``a``,``b````
``sw2 __SMUL (sw1, sw1)``
````c`` = __SMUL (``a``, ``b``)``
``SMUL ``a``,``b``,``c````
``sw1 __SUBSS (sw1, sw1)``
````c`` = __SUBSS (``a``, ``b``)``
``SUBSS ``a``,``b``,``c````
``uw2 __UMUL (uw1, uw1)``
````c`` = __UMUL (``a``, ``b``)``
``UMUL ``a``,``b``,``c````

:: _directly-mapped-media-functions:

Directly-Mapped Media Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The functions listed below map directly to FR-V M-type instructions.

Function prototype Example usage Assembly output
``uw1 __MABSHS (sw1)``
````b`` = __MABSHS (``a``)``
``MABSHS ``a``,``b````
``void __MADDACCS (acc, acc)``
``__MADDACCS (``b``, ``a``)``
``MADDACCS ``a``,``b````
``sw1 __MADDHSS (sw1, sw1)``
````c`` = __MADDHSS (``a``, ``b``)``
``MADDHSS ``a``,``b``,``c````
``uw1 __MADDHUS (uw1, uw1)``
````c`` = __MADDHUS (``a``, ``b``)``
``MADDHUS ``a``,``b``,``c````
``uw1 __MAND (uw1, uw1)``
````c`` = __MAND (``a``, ``b``)``
``MAND ``a``,``b``,``c````
``void __MASACCS (acc, acc)``
``__MASACCS (``b``, ``a``)``
``MASACCS ``a``,``b````
``uw1 __MAVEH (uw1, uw1)``
````c`` = __MAVEH (``a``, ``b``)``
``MAVEH ``a``,``b``,``c````
``uw2 __MBTOH (uw1)``
````b`` = __MBTOH (``a``)``
``MBTOH ``a``,``b````
``void __MBTOHE (uw1 *, uw1)``
``__MBTOHE (&``b``, ``a``)``
``MBTOHE ``a``,``b````
``void __MCLRACC (acc)``
``__MCLRACC (``a``)``
``MCLRACC ``a````
``void __MCLRACCA (void)``
``__MCLRACCA ()``
``MCLRACCA``
``uw1 __Mcop1 (uw1, uw1)``
````c`` = __Mcop1 (``a``, ``b``)``
``Mcop1 ``a``,``b``,``c````
``uw1 __Mcop2 (uw1, uw1)``
````c`` = __Mcop2 (``a``, ``b``)``
``Mcop2 ``a``,``b``,``c````
``uw1 __MCPLHI (uw2, const)``
````c`` = __MCPLHI (``a``, ``b``)``
``MCPLHI ``a``,#``b``,``c````
``uw1 __MCPLI (uw2, const)``
````c`` = __MCPLI (``a``, ``b``)``
``MCPLI ``a``,#``b``,``c````
``void __MCPXIS (acc, sw1, sw1)``
``__MCPXIS (``c``, ``a``, ``b``)``
``MCPXIS ``a``,``b``,``c````
``void __MCPXIU (acc, uw1, uw1)``
``__MCPXIU (``c``, ``a``, ``b``)``
``MCPXIU ``a``,``b``,``c````
``void __MCPXRS (acc, sw1, sw1)``
``__MCPXRS (``c``, ``a``, ``b``)``
``MCPXRS ``a``,``b``,``c````
``void __MCPXRU (acc, uw1, uw1)``
``__MCPXRU (``c``, ``a``, ``b``)``
``MCPXRU ``a``,``b``,``c````
``uw1 __MCUT (acc, uw1)``
````c`` = __MCUT (``a``, ``b``)``
``MCUT ``a``,``b``,``c````
``uw1 __MCUTSS (acc, sw1)``
````c`` = __MCUTSS (``a``, ``b``)``
``MCUTSS ``a``,``b``,``c````
``void __MDADDACCS (acc, acc)``
``__MDADDACCS (``b``, ``a``)``
``MDADDACCS ``a``,``b````
``void __MDASACCS (acc, acc)``
``__MDASACCS (``b``, ``a``)``
``MDASACCS ``a``,``b````
``uw2 __MDCUTSSI (acc, const)``
````c`` = __MDCUTSSI (``a``, ``b``)``
``MDCUTSSI ``a``,#``b``,``c````
``uw2 __MDPACKH (uw2, uw2)``
````c`` = __MDPACKH (``a``, ``b``)``
``MDPACKH ``a``,``b``,``c````
``uw2 __MDROTLI (uw2, const)``
````c`` = __MDROTLI (``a``, ``b``)``
``MDROTLI ``a``,#``b``,``c````
``void __MDSUBACCS (acc, acc)``
``__MDSUBACCS (``b``, ``a``)``
``MDSUBACCS ``a``,``b````
``void __MDUNPACKH (uw1 *, uw2)``
``__MDUNPACKH (&``b``, ``a``)``
``MDUNPACKH ``a``,``b````
``uw2 __MEXPDHD (uw1, const)``
````c`` = __MEXPDHD (``a``, ``b``)``
``MEXPDHD ``a``,#``b``,``c````
``uw1 __MEXPDHW (uw1, const)``
````c`` = __MEXPDHW (``a``, ``b``)``
``MEXPDHW ``a``,#``b``,``c````
``uw1 __MHDSETH (uw1, const)``
````c`` = __MHDSETH (``a``, ``b``)``
``MHDSETH ``a``,#``b``,``c````
``sw1 __MHDSETS (const)``
````b`` = __MHDSETS (``a``)``
``MHDSETS #``a``,``b````
``uw1 __MHSETHIH (uw1, const)``
````b`` = __MHSETHIH (``b``, ``a``)``
``MHSETHIH #``a``,``b````
``sw1 __MHSETHIS (sw1, const)``
````b`` = __MHSETHIS (``b``, ``a``)``
``MHSETHIS #``a``,``b````
``uw1 __MHSETLOH (uw1, const)``
````b`` = __MHSETLOH (``b``, ``a``)``
``MHSETLOH #``a``,``b````
``sw1 __MHSETLOS (sw1, const)``
````b`` = __MHSETLOS (``b``, ``a``)``
``MHSETLOS #``a``,``b````
``uw1 __MHTOB (uw2)``
````b`` = __MHTOB (``a``)``
``MHTOB ``a``,``b````
``void __MMACHS (acc, sw1, sw1)``
``__MMACHS (``c``, ``a``, ``b``)``
``MMACHS ``a``,``b``,``c````
``void __MMACHU (acc, uw1, uw1)``
``__MMACHU (``c``, ``a``, ``b``)``
``MMACHU ``a``,``b``,``c````
``void __MMRDHS (acc, sw1, sw1)``
``__MMRDHS (``c``, ``a``, ``b``)``
``MMRDHS ``a``,``b``,``c````
``void __MMRDHU (acc, uw1, uw1)``
``__MMRDHU (``c``, ``a``, ``b``)``
``MMRDHU ``a``,``b``,``c````
``void __MMULHS (acc, sw1, sw1)``
``__MMULHS (``c``, ``a``, ``b``)``
``MMULHS ``a``,``b``,``c````
``void __MMULHU (acc, uw1, uw1)``
``__MMULHU (``c``, ``a``, ``b``)``
``MMULHU ``a``,``b``,``c````
``void __MMULXHS (acc, sw1, sw1)``
``__MMULXHS (``c``, ``a``, ``b``)``
``MMULXHS ``a``,``b``,``c````
``void __MMULXHU (acc, uw1, uw1)``
``__MMULXHU (``c``, ``a``, ``b``)``
``MMULXHU ``a``,``b``,``c````
``uw1 __MNOT (uw1)``
````b`` = __MNOT (``a``)``
``MNOT ``a``,``b````
``uw1 __MOR (uw1, uw1)``
````c`` = __MOR (``a``, ``b``)``
``MOR ``a``,``b``,``c````
``uw1 __MPACKH (uh, uh)``
````c`` = __MPACKH (``a``, ``b``)``
``MPACKH ``a``,``b``,``c````
``sw2 __MQADDHSS (sw2, sw2)``
````c`` = __MQADDHSS (``a``, ``b``)``
``MQADDHSS ``a``,``b``,``c````
``uw2 __MQADDHUS (uw2, uw2)``
````c`` = __MQADDHUS (``a``, ``b``)``
``MQADDHUS ``a``,``b``,``c````
``void __MQCPXIS (acc, sw2, sw2)``
``__MQCPXIS (``c``, ``a``, ``b``)``
``MQCPXIS ``a``,``b``,``c````
``void __MQCPXIU (acc, uw2, uw2)``
``__MQCPXIU (``c``, ``a``, ``b``)``
``MQCPXIU ``a``,``b``,``c````
``void __MQCPXRS (acc, sw2, sw2)``
``__MQCPXRS (``c``, ``a``, ``b``)``
``MQCPXRS ``a``,``b``,``c````
``void __MQCPXRU (acc, uw2, uw2)``
``__MQCPXRU (``c``, ``a``, ``b``)``
``MQCPXRU ``a``,``b``,``c````
``sw2 __MQLCLRHS (sw2, sw2)``
````c`` = __MQLCLRHS (``a``, ``b``)``
``MQLCLRHS ``a``,``b``,``c````
``sw2 __MQLMTHS (sw2, sw2)``
````c`` = __MQLMTHS (``a``, ``b``)``
``MQLMTHS ``a``,``b``,``c````
``void __MQMACHS (acc, sw2, sw2)``
``__MQMACHS (``c``, ``a``, ``b``)``
``MQMACHS ``a``,``b``,``c````
``void __MQMACHU (acc, uw2, uw2)``
``__MQMACHU (``c``, ``a``, ``b``)``
``MQMACHU ``a``,``b``,``c````
``void __MQMACXHS (acc, sw2, sw2)``
``__MQMACXHS (``c``, ``a``, ``b``)``
``MQMACXHS ``a``,``b``,``c````
``void __MQMULHS (acc, sw2, sw2)``
``__MQMULHS (``c``, ``a``, ``b``)``
``MQMULHS ``a``,``b``,``c````
``void __MQMULHU (acc, uw2, uw2)``
``__MQMULHU (``c``, ``a``, ``b``)``
``MQMULHU ``a``,``b``,``c````
``void __MQMULXHS (acc, sw2, sw2)``
``__MQMULXHS (``c``, ``a``, ``b``)``
``MQMULXHS ``a``,``b``,``c````
``void __MQMULXHU (acc, uw2, uw2)``
``__MQMULXHU (``c``, ``a``, ``b``)``
``MQMULXHU ``a``,``b``,``c````
``sw2 __MQSATHS (sw2, sw2)``
````c`` = __MQSATHS (``a``, ``b``)``
``MQSATHS ``a``,``b``,``c````
``uw2 __MQSLLHI (uw2, int)``
````c`` = __MQSLLHI (``a``, ``b``)``
``MQSLLHI ``a``,``b``,``c````
``sw2 __MQSRAHI (sw2, int)``
````c`` = __MQSRAHI (``a``, ``b``)``
``MQSRAHI ``a``,``b``,``c````
``sw2 __MQSUBHSS (sw2, sw2)``
````c`` = __MQSUBHSS (``a``, ``b``)``
``MQSUBHSS ``a``,``b``,``c````
``uw2 __MQSUBHUS (uw2, uw2)``
````c`` = __MQSUBHUS (``a``, ``b``)``
``MQSUBHUS ``a``,``b``,``c````
``void __MQXMACHS (acc, sw2, sw2)``
``__MQXMACHS (``c``, ``a``, ``b``)``
``MQXMACHS ``a``,``b``,``c````
``void __MQXMACXHS (acc, sw2, sw2)``
``__MQXMACXHS (``c``, ``a``, ``b``)``
``MQXMACXHS ``a``,``b``,``c````
``uw1 __MRDACC (acc)``
````b`` = __MRDACC (``a``)``
``MRDACC ``a``,``b````
``uw1 __MRDACCG (acc)``
````b`` = __MRDACCG (``a``)``
``MRDACCG ``a``,``b````
``uw1 __MROTLI (uw1, const)``
````c`` = __MROTLI (``a``, ``b``)``
``MROTLI ``a``,#``b``,``c````
``uw1 __MROTRI (uw1, const)``
````c`` = __MROTRI (``a``, ``b``)``
``MROTRI ``a``,#``b``,``c````
``sw1 __MSATHS (sw1, sw1)``
````c`` = __MSATHS (``a``, ``b``)``
``MSATHS ``a``,``b``,``c````
``uw1 __MSATHU (uw1, uw1)``
````c`` = __MSATHU (``a``, ``b``)``
``MSATHU ``a``,``b``,``c````
``uw1 __MSLLHI (uw1, const)``
````c`` = __MSLLHI (``a``, ``b``)``
``MSLLHI ``a``,#``b``,``c````
``sw1 __MSRAHI (sw1, const)``
````c`` = __MSRAHI (``a``, ``b``)``
``MSRAHI ``a``,#``b``,``c````
``uw1 __MSRLHI (uw1, const)``
````c`` = __MSRLHI (``a``, ``b``)``
``MSRLHI ``a``,#``b``,``c````
``void __MSUBACCS (acc, acc)``
``__MSUBACCS (``b``, ``a``)``
``MSUBACCS ``a``,``b````
``sw1 __MSUBHSS (sw1, sw1)``
````c`` = __MSUBHSS (``a``, ``b``)``
``MSUBHSS ``a``,``b``,``c````
``uw1 __MSUBHUS (uw1, uw1)``
````c`` = __MSUBHUS (``a``, ``b``)``
``MSUBHUS ``a``,``b``,``c````
``void __MTRAP (void)``
``__MTRAP ()``
``MTRAP``
``uw2 __MUNPACKH (uw1)``
````b`` = __MUNPACKH (``a``)``
``MUNPACKH ``a``,``b````
``uw1 __MWCUT (uw2, uw1)``
````c`` = __MWCUT (``a``, ``b``)``
``MWCUT ``a``,``b``,``c````
``void __MWTACC (acc, uw1)``
``__MWTACC (``b``, ``a``)``
``MWTACC ``a``,``b````
``void __MWTACCG (acc, uw1)``
``__MWTACCG (``b``, ``a``)``
``MWTACCG ``a``,``b````
``uw1 __MXOR (uw1, uw1)``
````c`` = __MXOR (``a``, ``b``)``
``MXOR ``a``,``b``,``c````

:: _raw-read/write-functions:

Raw Read/Write Functions
~~~~~~~~~~~~~~~~~~~~~~~~

This sections describes built-in functions related to read and write
instructions to access memory.  These functions generate
``membar`` instructions to flush the I/O load and stores where
appropriate, as described in Fujitsu's manual described above.

unsigned char __builtin_read8 (void *``data``)
unsigned short __builtin_read16 (void *``data``)
unsigned long __builtin_read32 (void *``data``)

unsigned long long __builtin_read64 (void *``data``)

  void __builtin_write8 (void *``data``, unsigned char ``datum``)
void __builtin_write16 (void *``data``, unsigned short ``datum``)
void __builtin_write32 (void *``data``, unsigned long ``datum``)
void __builtin_write64 (void *``data``, unsigned long long ``datum``)

:: _other-built-in-functions:

Other Built-in Functions
~~~~~~~~~~~~~~~~~~~~~~~~

This section describes built-in functions that are not named after
a specific FR-V instruction.

sw2 __IACCreadll (iacc ``reg``)
  Return the full 64-bit value of IACC0.  The ``reg`` argument is reserved
  for future expansion and must be 0.

sw1 __IACCreadl (iacc ``reg``)
  Return the value of IACC0H if ``reg`` is 0 and IACC0L if ``reg`` is 1.
  Other values of ``reg`` are rejected as invalid.

void __IACCsetll (iacc ``reg``, sw2 ``x``)
  Set the full 64-bit value of IACC0 to ``x``.  The ``reg`` argument
  is reserved for future expansion and must be 0.

void __IACCsetl (iacc ``reg``, sw1 ``x``)
  Set IACC0H to ``x`` if ``reg`` is 0 and IACC0L to ``x`` if ``reg``
  is 1.  Other values of ``reg`` are rejected as invalid.

void __data_prefetch0 (const void *``x``)
  Use the ``dcpl`` instruction to load the contents of address ``x``
  into the data cache.

void __data_prefetch (const void *``x``)
  Use the ``nldub`` instruction to load the contents of address ``x``
  into the data cache.  The instruction is issued in slot I1.

:: _mips-dsp-built-in-functions:

MIPS DSP Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The MIPS DSP Application-Specific Extension (ASE) includes new
instructions that are designed to improve the performance of DSP and
media applications.  It provides instructions that operate on packed
8-bit/16-bit integer data, Q7, Q15 and Q31 fractional data.

GCC supports MIPS DSP operations using both the generic
vector extensions (Vector Extensions) and a collection of
MIPS-specific built-in functions.  Both kinds of support are
enabled by the :option:`-mdsp` command-line option.

Revision 2 of the ASE was introduced in the second half of 2006.
This revision adds extra instructions to the original ASE, but is
otherwise backwards-compatible with it.  You can select revision 2
using the command-line option :option:`-mdspr2`; this option implies
:option:`-mdsp`.

The SCOUNT and POS bits of the DSP control register are global.  The
WRDSP, EXTPDP, EXTPDPV and MTHLIP instructions modify the SCOUNT and
POS bits.  During optimization, the compiler does not delete these
instructions and it does not delete calls to functions containing
these instructions.

At present, GCC only provides support for operations on 32-bit
vectors.  The vector type associated with 8-bit integer data is
usually called ``v4i8``, the vector type associated with Q7
is usually called ``v4q7``, the vector type associated with 16-bit
integer data is usually called ``v2i16``, and the vector type
associated with Q15 is usually called ``v2q15``.  They can be
defined in C as follows:

.. code-block:: c++

  typedef signed char v4i8 __attribute__ ((vector_size(4)));
  typedef signed char v4q7 __attribute__ ((vector_size(4)));
  typedef short v2i16 __attribute__ ((vector_size(4)));
  typedef short v2q15 __attribute__ ((vector_size(4)));

``v4i8``, ``v4q7``, ``v2i16`` and ``v2q15`` values are
initialized in the same way as aggregates.  For example:

.. code-block:: c++

  v4i8 a = {1, 2, 3, 4};
  v4i8 b;
  b = (v4i8) {5, 6, 7, 8};

  v2q15 c = {0x0fcb, 0x3a75};
  v2q15 d;
  d = (v2q15) {0.1234 * 0x1.0p15, 0.4567 * 0x1.0p15};

Note: The CPU's endianness determines the order in which values
are packed.  On little-endian targets, the first value is the least
significant and the last value is the most significant.  The opposite
order applies to big-endian targets.  For example, the code above
sets the lowest byte of ``a`` to ``1`` on little-endian targets
and ``4`` on big-endian targets.

Note: Q7, Q15 and Q31 values must be initialized with their integer
representation.  As shown in this example, the integer representation
of a Q7 value can be obtained by multiplying the fractional value by
``0x1.0p7``.  The equivalent for Q15 values is to multiply by
``0x1.0p15``.  The equivalent for Q31 values is to multiply by
``0x1.0p31``.

The table below lists the ``v4i8`` and ``v2q15`` operations for which
hardware support exists.  ``a`` and ``b`` are ``v4i8`` values,
and ``c`` and ``d`` are ``v2q15`` values.

C code MIPS instruction
``a + b`` ``addu.qb``
``c + d`` ``addq.ph``
``a - b`` ``subu.qb``
``c - d`` ``subq.ph``

The table below lists the ``v2i16`` operation for which
hardware support exists for the DSP ASE REV 2.  ``e`` and ``f`` are
``v2i16`` values.

C code MIPS instruction
``e * f`` ``mul.ph``

It is easier to describe the DSP built-in functions if we first define
the following types:

.. code-block:: c++

  typedef int q31;
  typedef int i32;
  typedef unsigned int ui32;
  typedef long long a64;

``q31`` and ``i32`` are actually the same as ``int``, but we
use ``q31`` to indicate a Q31 fractional value and ``i32`` to
indicate a 32-bit integer value.  Similarly, ``a64`` is the same as
``long long``, but we use ``a64`` to indicate values that are
placed in one of the four DSP accumulators (``$ac0``,
``$ac1``, ``$ac2`` or ``$ac3``).

Also, some built-in functions prefer or require immediate numbers as
parameters, because the corresponding DSP instructions accept both immediate
numbers and register operands, or accept immediate numbers only.  The
immediate parameters are listed as follows.

.. code-block:: c++

  imm0_3: 0 to 3.
  imm0_7: 0 to 7.
  imm0_15: 0 to 15.
  imm0_31: 0 to 31.
  imm0_63: 0 to 63.
  imm0_255: 0 to 255.
  imm_n32_31: -32 to 31.
  imm_n512_511: -512 to 511.

The following built-in functions map directly to a particular MIPS DSP
instruction.  Please refer to the architecture specification
for details on what each instruction does.

.. code-block:: c++

  v2q15 __builtin_mips_addq_ph (v2q15, v2q15)
  v2q15 __builtin_mips_addq_s_ph (v2q15, v2q15)
  q31 __builtin_mips_addq_s_w (q31, q31)
  v4i8 __builtin_mips_addu_qb (v4i8, v4i8)
  v4i8 __builtin_mips_addu_s_qb (v4i8, v4i8)
  v2q15 __builtin_mips_subq_ph (v2q15, v2q15)
  v2q15 __builtin_mips_subq_s_ph (v2q15, v2q15)
  q31 __builtin_mips_subq_s_w (q31, q31)
  v4i8 __builtin_mips_subu_qb (v4i8, v4i8)
  v4i8 __builtin_mips_subu_s_qb (v4i8, v4i8)
  i32 __builtin_mips_addsc (i32, i32)
  i32 __builtin_mips_addwc (i32, i32)
  i32 __builtin_mips_modsub (i32, i32)
  i32 __builtin_mips_raddu_w_qb (v4i8)
  v2q15 __builtin_mips_absq_s_ph (v2q15)
  q31 __builtin_mips_absq_s_w (q31)
  v4i8 __builtin_mips_precrq_qb_ph (v2q15, v2q15)
  v2q15 __builtin_mips_precrq_ph_w (q31, q31)
  v2q15 __builtin_mips_precrq_rs_ph_w (q31, q31)
  v4i8 __builtin_mips_precrqu_s_qb_ph (v2q15, v2q15)
  q31 __builtin_mips_preceq_w_phl (v2q15)
  q31 __builtin_mips_preceq_w_phr (v2q15)
  v2q15 __builtin_mips_precequ_ph_qbl (v4i8)
  v2q15 __builtin_mips_precequ_ph_qbr (v4i8)
  v2q15 __builtin_mips_precequ_ph_qbla (v4i8)
  v2q15 __builtin_mips_precequ_ph_qbra (v4i8)
  v2q15 __builtin_mips_preceu_ph_qbl (v4i8)
  v2q15 __builtin_mips_preceu_ph_qbr (v4i8)
  v2q15 __builtin_mips_preceu_ph_qbla (v4i8)
  v2q15 __builtin_mips_preceu_ph_qbra (v4i8)
  v4i8 __builtin_mips_shll_qb (v4i8, imm0_7)
  v4i8 __builtin_mips_shll_qb (v4i8, i32)
  v2q15 __builtin_mips_shll_ph (v2q15, imm0_15)
  v2q15 __builtin_mips_shll_ph (v2q15, i32)
  v2q15 __builtin_mips_shll_s_ph (v2q15, imm0_15)
  v2q15 __builtin_mips_shll_s_ph (v2q15, i32)
  q31 __builtin_mips_shll_s_w (q31, imm0_31)
  q31 __builtin_mips_shll_s_w (q31, i32)
  v4i8 __builtin_mips_shrl_qb (v4i8, imm0_7)
  v4i8 __builtin_mips_shrl_qb (v4i8, i32)
  v2q15 __builtin_mips_shra_ph (v2q15, imm0_15)
  v2q15 __builtin_mips_shra_ph (v2q15, i32)
  v2q15 __builtin_mips_shra_r_ph (v2q15, imm0_15)
  v2q15 __builtin_mips_shra_r_ph (v2q15, i32)
  q31 __builtin_mips_shra_r_w (q31, imm0_31)
  q31 __builtin_mips_shra_r_w (q31, i32)
  v2q15 __builtin_mips_muleu_s_ph_qbl (v4i8, v2q15)
  v2q15 __builtin_mips_muleu_s_ph_qbr (v4i8, v2q15)
  v2q15 __builtin_mips_mulq_rs_ph (v2q15, v2q15)
  q31 __builtin_mips_muleq_s_w_phl (v2q15, v2q15)
  q31 __builtin_mips_muleq_s_w_phr (v2q15, v2q15)
  a64 __builtin_mips_dpau_h_qbl (a64, v4i8, v4i8)
  a64 __builtin_mips_dpau_h_qbr (a64, v4i8, v4i8)
  a64 __builtin_mips_dpsu_h_qbl (a64, v4i8, v4i8)
  a64 __builtin_mips_dpsu_h_qbr (a64, v4i8, v4i8)
  a64 __builtin_mips_dpaq_s_w_ph (a64, v2q15, v2q15)
  a64 __builtin_mips_dpaq_sa_l_w (a64, q31, q31)
  a64 __builtin_mips_dpsq_s_w_ph (a64, v2q15, v2q15)
  a64 __builtin_mips_dpsq_sa_l_w (a64, q31, q31)
  a64 __builtin_mips_mulsaq_s_w_ph (a64, v2q15, v2q15)
  a64 __builtin_mips_maq_s_w_phl (a64, v2q15, v2q15)
  a64 __builtin_mips_maq_s_w_phr (a64, v2q15, v2q15)
  a64 __builtin_mips_maq_sa_w_phl (a64, v2q15, v2q15)
  a64 __builtin_mips_maq_sa_w_phr (a64, v2q15, v2q15)
  i32 __builtin_mips_bitrev (i32)
  i32 __builtin_mips_insv (i32, i32)
  v4i8 __builtin_mips_repl_qb (imm0_255)
  v4i8 __builtin_mips_repl_qb (i32)
  v2q15 __builtin_mips_repl_ph (imm_n512_511)
  v2q15 __builtin_mips_repl_ph (i32)
  void __builtin_mips_cmpu_eq_qb (v4i8, v4i8)
  void __builtin_mips_cmpu_lt_qb (v4i8, v4i8)
  void __builtin_mips_cmpu_le_qb (v4i8, v4i8)
  i32 __builtin_mips_cmpgu_eq_qb (v4i8, v4i8)
  i32 __builtin_mips_cmpgu_lt_qb (v4i8, v4i8)
  i32 __builtin_mips_cmpgu_le_qb (v4i8, v4i8)
  void __builtin_mips_cmp_eq_ph (v2q15, v2q15)
  void __builtin_mips_cmp_lt_ph (v2q15, v2q15)
  void __builtin_mips_cmp_le_ph (v2q15, v2q15)
  v4i8 __builtin_mips_pick_qb (v4i8, v4i8)
  v2q15 __builtin_mips_pick_ph (v2q15, v2q15)
  v2q15 __builtin_mips_packrl_ph (v2q15, v2q15)
  i32 __builtin_mips_extr_w (a64, imm0_31)
  i32 __builtin_mips_extr_w (a64, i32)
  i32 __builtin_mips_extr_r_w (a64, imm0_31)
  i32 __builtin_mips_extr_s_h (a64, i32)
  i32 __builtin_mips_extr_rs_w (a64, imm0_31)
  i32 __builtin_mips_extr_rs_w (a64, i32)
  i32 __builtin_mips_extr_s_h (a64, imm0_31)
  i32 __builtin_mips_extr_r_w (a64, i32)
  i32 __builtin_mips_extp (a64, imm0_31)
  i32 __builtin_mips_extp (a64, i32)
  i32 __builtin_mips_extpdp (a64, imm0_31)
  i32 __builtin_mips_extpdp (a64, i32)
  a64 __builtin_mips_shilo (a64, imm_n32_31)
  a64 __builtin_mips_shilo (a64, i32)
  a64 __builtin_mips_mthlip (a64, i32)
  void __builtin_mips_wrdsp (i32, imm0_63)
  i32 __builtin_mips_rddsp (imm0_63)
  i32 __builtin_mips_lbux (void *, i32)
  i32 __builtin_mips_lhx (void *, i32)
  i32 __builtin_mips_lwx (void *, i32)
  a64 __builtin_mips_ldx (void *, i32) [MIPS64 only]
  i32 __builtin_mips_bposge32 (void)
  a64 __builtin_mips_madd (a64, i32, i32);
  a64 __builtin_mips_maddu (a64, ui32, ui32);
  a64 __builtin_mips_msub (a64, i32, i32);
  a64 __builtin_mips_msubu (a64, ui32, ui32);
  a64 __builtin_mips_mult (i32, i32);
  a64 __builtin_mips_multu (ui32, ui32);

The following built-in functions map directly to a particular MIPS DSP REV 2
instruction.  Please refer to the architecture specification
for details on what each instruction does.

.. code-block:: c++

  v4q7 __builtin_mips_absq_s_qb (v4q7);
  v2i16 __builtin_mips_addu_ph (v2i16, v2i16);
  v2i16 __builtin_mips_addu_s_ph (v2i16, v2i16);
  v4i8 __builtin_mips_adduh_qb (v4i8, v4i8);
  v4i8 __builtin_mips_adduh_r_qb (v4i8, v4i8);
  i32 __builtin_mips_append (i32, i32, imm0_31);
  i32 __builtin_mips_balign (i32, i32, imm0_3);
  i32 __builtin_mips_cmpgdu_eq_qb (v4i8, v4i8);
  i32 __builtin_mips_cmpgdu_lt_qb (v4i8, v4i8);
  i32 __builtin_mips_cmpgdu_le_qb (v4i8, v4i8);
  a64 __builtin_mips_dpa_w_ph (a64, v2i16, v2i16);
  a64 __builtin_mips_dps_w_ph (a64, v2i16, v2i16);
  v2i16 __builtin_mips_mul_ph (v2i16, v2i16);
  v2i16 __builtin_mips_mul_s_ph (v2i16, v2i16);
  q31 __builtin_mips_mulq_rs_w (q31, q31);
  v2q15 __builtin_mips_mulq_s_ph (v2q15, v2q15);
  q31 __builtin_mips_mulq_s_w (q31, q31);
  a64 __builtin_mips_mulsa_w_ph (a64, v2i16, v2i16);
  v4i8 __builtin_mips_precr_qb_ph (v2i16, v2i16);
  v2i16 __builtin_mips_precr_sra_ph_w (i32, i32, imm0_31);
  v2i16 __builtin_mips_precr_sra_r_ph_w (i32, i32, imm0_31);
  i32 __builtin_mips_prepend (i32, i32, imm0_31);
  v4i8 __builtin_mips_shra_qb (v4i8, imm0_7);
  v4i8 __builtin_mips_shra_r_qb (v4i8, imm0_7);
  v4i8 __builtin_mips_shra_qb (v4i8, i32);
  v4i8 __builtin_mips_shra_r_qb (v4i8, i32);
  v2i16 __builtin_mips_shrl_ph (v2i16, imm0_15);
  v2i16 __builtin_mips_shrl_ph (v2i16, i32);
  v2i16 __builtin_mips_subu_ph (v2i16, v2i16);
  v2i16 __builtin_mips_subu_s_ph (v2i16, v2i16);
  v4i8 __builtin_mips_subuh_qb (v4i8, v4i8);
  v4i8 __builtin_mips_subuh_r_qb (v4i8, v4i8);
  v2q15 __builtin_mips_addqh_ph (v2q15, v2q15);
  v2q15 __builtin_mips_addqh_r_ph (v2q15, v2q15);
  q31 __builtin_mips_addqh_w (q31, q31);
  q31 __builtin_mips_addqh_r_w (q31, q31);
  v2q15 __builtin_mips_subqh_ph (v2q15, v2q15);
  v2q15 __builtin_mips_subqh_r_ph (v2q15, v2q15);
  q31 __builtin_mips_subqh_w (q31, q31);
  q31 __builtin_mips_subqh_r_w (q31, q31);
  a64 __builtin_mips_dpax_w_ph (a64, v2i16, v2i16);
  a64 __builtin_mips_dpsx_w_ph (a64, v2i16, v2i16);
  a64 __builtin_mips_dpaqx_s_w_ph (a64, v2q15, v2q15);
  a64 __builtin_mips_dpaqx_sa_w_ph (a64, v2q15, v2q15);
  a64 __builtin_mips_dpsqx_s_w_ph (a64, v2q15, v2q15);
  a64 __builtin_mips_dpsqx_sa_w_ph (a64, v2q15, v2q15);

:: _mips-paired-single-support:

MIPS Paired-Single Support
^^^^^^^^^^^^^^^^^^^^^^^^^^

The MIPS64 architecture includes a number of instructions that
operate on pairs of single-precision floating-point values.
Each pair is packed into a 64-bit floating-point register,
with one element being designated the 'upper half' and
the other being designated the 'lower half'.

GCC supports paired-single operations using both the generic
vector extensions (Vector Extensions) and a collection of
MIPS-specific built-in functions.  Both kinds of support are
enabled by the :option:`-mpaired-single` command-line option.

The vector type associated with paired-single values is usually
called ``v2sf``.  It can be defined in C as follows:

.. code-block:: c++

  typedef float v2sf __attribute__ ((vector_size (8)));

``v2sf`` values are initialized in the same way as aggregates.
For example:

.. code-block:: c++

  v2sf a = {1.5, 9.1};
  v2sf b;
  float e, f;
  b = (v2sf) {e, f};

Note: The CPU's endianness determines which value is stored in
the upper half of a register and which value is stored in the lower half.
On little-endian targets, the first value is the lower one and the second
value is the upper one.  The opposite order applies to big-endian targets.
For example, the code above sets the lower half of ``a`` to
``1.5`` on little-endian targets and ``9.1`` on big-endian targets.

:: _mips-loongson-built-in-functions:

MIPS Loongson Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GCC provides intrinsics to access the SIMD instructions provided by the
ST Microelectronics Loongson-2E and -2F processors.  These intrinsics,
available after inclusion of the ``loongson.h`` header file,
operate on the following 64-bit vector types:

* ``uint8x8_t``, a vector of eight unsigned 8-bit integers;
  * ``uint16x4_t``, a vector of four unsigned 16-bit integers;
  * ``uint32x2_t``, a vector of two unsigned 32-bit integers;
  * ``int8x8_t``, a vector of eight signed 8-bit integers;
  * ``int16x4_t``, a vector of four signed 16-bit integers;
  * ``int32x2_t``, a vector of two signed 32-bit integers.

The intrinsics provided are listed below; each is named after the
machine instruction to which it corresponds, with suffixes added as
appropriate to distinguish intrinsics that expand to the same machine
instruction yet have different argument types.  Refer to the architecture
documentation for a description of the functionality of each
instruction.

.. code-block:: c++

  int16x4_t packsswh (int32x2_t s, int32x2_t t);
  int8x8_t packsshb (int16x4_t s, int16x4_t t);
  uint8x8_t packushb (uint16x4_t s, uint16x4_t t);
  uint32x2_t paddw_u (uint32x2_t s, uint32x2_t t);
  uint16x4_t paddh_u (uint16x4_t s, uint16x4_t t);
  uint8x8_t paddb_u (uint8x8_t s, uint8x8_t t);
  int32x2_t paddw_s (int32x2_t s, int32x2_t t);
  int16x4_t paddh_s (int16x4_t s, int16x4_t t);
  int8x8_t paddb_s (int8x8_t s, int8x8_t t);
  uint64_t paddd_u (uint64_t s, uint64_t t);
  int64_t paddd_s (int64_t s, int64_t t);
  int16x4_t paddsh (int16x4_t s, int16x4_t t);
  int8x8_t paddsb (int8x8_t s, int8x8_t t);
  uint16x4_t paddush (uint16x4_t s, uint16x4_t t);
  uint8x8_t paddusb (uint8x8_t s, uint8x8_t t);
  uint64_t pandn_ud (uint64_t s, uint64_t t);
  uint32x2_t pandn_uw (uint32x2_t s, uint32x2_t t);
  uint16x4_t pandn_uh (uint16x4_t s, uint16x4_t t);
  uint8x8_t pandn_ub (uint8x8_t s, uint8x8_t t);
  int64_t pandn_sd (int64_t s, int64_t t);
  int32x2_t pandn_sw (int32x2_t s, int32x2_t t);
  int16x4_t pandn_sh (int16x4_t s, int16x4_t t);
  int8x8_t pandn_sb (int8x8_t s, int8x8_t t);
  uint16x4_t pavgh (uint16x4_t s, uint16x4_t t);
  uint8x8_t pavgb (uint8x8_t s, uint8x8_t t);
  uint32x2_t pcmpeqw_u (uint32x2_t s, uint32x2_t t);
  uint16x4_t pcmpeqh_u (uint16x4_t s, uint16x4_t t);
  uint8x8_t pcmpeqb_u (uint8x8_t s, uint8x8_t t);
  int32x2_t pcmpeqw_s (int32x2_t s, int32x2_t t);
  int16x4_t pcmpeqh_s (int16x4_t s, int16x4_t t);
  int8x8_t pcmpeqb_s (int8x8_t s, int8x8_t t);
  uint32x2_t pcmpgtw_u (uint32x2_t s, uint32x2_t t);
  uint16x4_t pcmpgth_u (uint16x4_t s, uint16x4_t t);
  uint8x8_t pcmpgtb_u (uint8x8_t s, uint8x8_t t);
  int32x2_t pcmpgtw_s (int32x2_t s, int32x2_t t);
  int16x4_t pcmpgth_s (int16x4_t s, int16x4_t t);
  int8x8_t pcmpgtb_s (int8x8_t s, int8x8_t t);
  uint16x4_t pextrh_u (uint16x4_t s, int field);
  int16x4_t pextrh_s (int16x4_t s, int field);
  uint16x4_t pinsrh_0_u (uint16x4_t s, uint16x4_t t);
  uint16x4_t pinsrh_1_u (uint16x4_t s, uint16x4_t t);
  uint16x4_t pinsrh_2_u (uint16x4_t s, uint16x4_t t);
  uint16x4_t pinsrh_3_u (uint16x4_t s, uint16x4_t t);
  int16x4_t pinsrh_0_s (int16x4_t s, int16x4_t t);
  int16x4_t pinsrh_1_s (int16x4_t s, int16x4_t t);
  int16x4_t pinsrh_2_s (int16x4_t s, int16x4_t t);
  int16x4_t pinsrh_3_s (int16x4_t s, int16x4_t t);
  int32x2_t pmaddhw (int16x4_t s, int16x4_t t);
  int16x4_t pmaxsh (int16x4_t s, int16x4_t t);
  uint8x8_t pmaxub (uint8x8_t s, uint8x8_t t);
  int16x4_t pminsh (int16x4_t s, int16x4_t t);
  uint8x8_t pminub (uint8x8_t s, uint8x8_t t);
  uint8x8_t pmovmskb_u (uint8x8_t s);
  int8x8_t pmovmskb_s (int8x8_t s);
  uint16x4_t pmulhuh (uint16x4_t s, uint16x4_t t);
  int16x4_t pmulhh (int16x4_t s, int16x4_t t);
  int16x4_t pmullh (int16x4_t s, int16x4_t t);
  int64_t pmuluw (uint32x2_t s, uint32x2_t t);
  uint8x8_t pasubub (uint8x8_t s, uint8x8_t t);
  uint16x4_t biadd (uint8x8_t s);
  uint16x4_t psadbh (uint8x8_t s, uint8x8_t t);
  uint16x4_t pshufh_u (uint16x4_t dest, uint16x4_t s, uint8_t order);
  int16x4_t pshufh_s (int16x4_t dest, int16x4_t s, uint8_t order);
  uint16x4_t psllh_u (uint16x4_t s, uint8_t amount);
  int16x4_t psllh_s (int16x4_t s, uint8_t amount);
  uint32x2_t psllw_u (uint32x2_t s, uint8_t amount);
  int32x2_t psllw_s (int32x2_t s, uint8_t amount);
  uint16x4_t psrlh_u (uint16x4_t s, uint8_t amount);
  int16x4_t psrlh_s (int16x4_t s, uint8_t amount);
  uint32x2_t psrlw_u (uint32x2_t s, uint8_t amount);
  int32x2_t psrlw_s (int32x2_t s, uint8_t amount);
  uint16x4_t psrah_u (uint16x4_t s, uint8_t amount);
  int16x4_t psrah_s (int16x4_t s, uint8_t amount);
  uint32x2_t psraw_u (uint32x2_t s, uint8_t amount);
  int32x2_t psraw_s (int32x2_t s, uint8_t amount);
  uint32x2_t psubw_u (uint32x2_t s, uint32x2_t t);
  uint16x4_t psubh_u (uint16x4_t s, uint16x4_t t);
  uint8x8_t psubb_u (uint8x8_t s, uint8x8_t t);
  int32x2_t psubw_s (int32x2_t s, int32x2_t t);
  int16x4_t psubh_s (int16x4_t s, int16x4_t t);
  int8x8_t psubb_s (int8x8_t s, int8x8_t t);
  uint64_t psubd_u (uint64_t s, uint64_t t);
  int64_t psubd_s (int64_t s, int64_t t);
  int16x4_t psubsh (int16x4_t s, int16x4_t t);
  int8x8_t psubsb (int8x8_t s, int8x8_t t);
  uint16x4_t psubush (uint16x4_t s, uint16x4_t t);
  uint8x8_t psubusb (uint8x8_t s, uint8x8_t t);
  uint32x2_t punpckhwd_u (uint32x2_t s, uint32x2_t t);
  uint16x4_t punpckhhw_u (uint16x4_t s, uint16x4_t t);
  uint8x8_t punpckhbh_u (uint8x8_t s, uint8x8_t t);
  int32x2_t punpckhwd_s (int32x2_t s, int32x2_t t);
  int16x4_t punpckhhw_s (int16x4_t s, int16x4_t t);
  int8x8_t punpckhbh_s (int8x8_t s, int8x8_t t);
  uint32x2_t punpcklwd_u (uint32x2_t s, uint32x2_t t);
  uint16x4_t punpcklhw_u (uint16x4_t s, uint16x4_t t);
  uint8x8_t punpcklbh_u (uint8x8_t s, uint8x8_t t);
  int32x2_t punpcklwd_s (int32x2_t s, int32x2_t t);
  int16x4_t punpcklhw_s (int16x4_t s, int16x4_t t);
  int8x8_t punpcklbh_s (int8x8_t s, int8x8_t t);

.. toctree::

   <paired-single-arithmetic>
   <paired-single-built-in-functions>
   <mips-3d-built-in-functions>

:: _paired-single-arithmetic:

Paired-Single Arithmetic
~~~~~~~~~~~~~~~~~~~~~~~~

The table below lists the ``v2sf`` operations for which hardware
support exists.  ``a``, ``b`` and ``c`` are ``v2sf``
values and ``x`` is an integral value.

C code MIPS instruction
``a + b`` ``add.ps``
``a - b`` ``sub.ps``
``-a`` ``neg.ps``
``a * b`` ``mul.ps``
``a * b + c`` ``madd.ps``
``a * b - c`` ``msub.ps``
``-(a * b + c)`` ``nmadd.ps``
``-(a * b - c)`` ``nmsub.ps``
``x ? a : b`` ``movn.ps``/``movz.ps``

Note that the multiply-accumulate instructions can be disabled
using the command-line option ``-mno-fused-madd``.

:: _paired-single-built-in-functions:

Paired-Single Built-in Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following paired-single functions map directly to a particular
MIPS instruction.  Please refer to the architecture specification
for details on what each instruction does.

v2sf __builtin_mips_pll_ps (v2sf, v2sf)
  Pair lower lower (``pll.ps``).

v2sf __builtin_mips_pul_ps (v2sf, v2sf)
  Pair upper lower (``pul.ps``).

v2sf __builtin_mips_plu_ps (v2sf, v2sf)
  Pair lower upper (``plu.ps``).

v2sf __builtin_mips_puu_ps (v2sf, v2sf)
  Pair upper upper (``puu.ps``).

v2sf __builtin_mips_cvt_ps_s (float, float)
  Convert pair to paired single (``cvt.ps.s``).

float __builtin_mips_cvt_s_pl (v2sf)
  Convert pair lower to single (``cvt.s.pl``).

float __builtin_mips_cvt_s_pu (v2sf)
  Convert pair upper to single (``cvt.s.pu``).

v2sf __builtin_mips_abs_ps (v2sf)
  Absolute value (``abs.ps``).

v2sf __builtin_mips_alnv_ps (v2sf, v2sf, int)
  Align variable (``alnv.ps``).

  Note: The value of the third parameter must be 0 or 4
  modulo 8, otherwise the result is unpredictable.  Please read the
  instruction description for details.

The following multi-instruction functions are also available.
In each case, ``cond`` can be any of the 16 floating-point conditions:
``f``, ``un``, ``eq``, ``ueq``, ``olt``, ``ult``,
``ole``, ``ule``, ``sf``, ``ngle``, ``seq``, ``ngl``,
``lt``, ``nge``, ``le`` or ``ngt``.

v2sf __builtin_mips_movt_c_``cond``_ps (v2sf ``a``, v2sf ``b``, v2sf ``c``, v2sf ``d``)v2sf __builtin_mips_movf_c_``cond``_ps (v2sf ``a``, v2sf ``b``, v2sf ``c``, v2sf ``d``)
  Conditional move based on floating-point comparison (``c.``cond``.ps``,
  ``movt.ps``/``movf.ps``).

  The ``movt`` functions return the value ``x`` computed by:

  .. code-block:: c++

    c.``cond``.ps ``cc``,``a``,``b``
    mov.ps ``x``,``c``
    movt.ps ``x``,``d``,``cc``

  The ``movf`` functions are similar but use ``movf.ps`` instead
  of ``movt.ps``.

int __builtin_mips_upper_c_``cond``_ps (v2sf ``a``, v2sf ``b``)int __builtin_mips_lower_c_``cond``_ps (v2sf ``a``, v2sf ``b``)
  Comparison of two paired-single values (``c.``cond``.ps``,
  ``bc1t``/``bc1f``).

  These functions compare ``a`` and ``b`` using ``c.``cond``.ps``
  and return either the upper or lower half of the result.  For example:

  .. code-block:: c++

    v2sf a, b;
    if (__builtin_mips_upper_c_eq_ps (a, b))
      upper_halves_are_equal ();
    else
      upper_halves_are_unequal ();

    if (__builtin_mips_lower_c_eq_ps (a, b))
      lower_halves_are_equal ();
    else
      lower_halves_are_unequal ();

:: _mips-3d-built-in-functions:

MIPS-3D Built-in Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~

The MIPS-3D Application-Specific Extension (ASE) includes additional
paired-single instructions that are designed to improve the performance
of 3D graphics operations.  Support for these instructions is controlled
by the :option:`-mips3d` command-line option.

The functions listed below map directly to a particular MIPS-3D
instruction.  Please refer to the architecture specification for
more details on what each instruction does.

v2sf __builtin_mips_addr_ps (v2sf, v2sf)
  Reduction add (``addr.ps``).

v2sf __builtin_mips_mulr_ps (v2sf, v2sf)
  Reduction multiply (``mulr.ps``).

v2sf __builtin_mips_cvt_pw_ps (v2sf)
  Convert paired single to paired word (``cvt.pw.ps``).

v2sf __builtin_mips_cvt_ps_pw (v2sf)
  Convert paired word to paired single (``cvt.ps.pw``).

float __builtin_mips_recip1_s (float)double __builtin_mips_recip1_d (double)v2sf __builtin_mips_recip1_ps (v2sf)
  Reduced-precision reciprocal (sequence step 1) (``recip1.``fmt````).

float __builtin_mips_recip2_s (float, float)double __builtin_mips_recip2_d (double, double)v2sf __builtin_mips_recip2_ps (v2sf, v2sf)
  Reduced-precision reciprocal (sequence step 2) (``recip2.``fmt````).

float __builtin_mips_rsqrt1_s (float)double __builtin_mips_rsqrt1_d (double)v2sf __builtin_mips_rsqrt1_ps (v2sf)
  Reduced-precision reciprocal square root (sequence step 1)
  (``rsqrt1.``fmt````).

float __builtin_mips_rsqrt2_s (float, float)double __builtin_mips_rsqrt2_d (double, double)v2sf __builtin_mips_rsqrt2_ps (v2sf, v2sf)
  Reduced-precision reciprocal square root (sequence step 2)
  (``rsqrt2.``fmt````).

The following multi-instruction functions are also available.
In each case, ``cond`` can be any of the 16 floating-point conditions:
``f``, ``un``, ``eq``, ``ueq``, ``olt``, ``ult``,
``ole``, ``ule``, ``sf``, ``ngle``, ``seq``,
``ngl``, ``lt``, ``nge``, ``le`` or ``ngt``.

int __builtin_mips_cabs_``cond``_s (float ``a``, float ``b``)int __builtin_mips_cabs_``cond``_d (double ``a``, double ``b``)
  Absolute comparison of two scalar values (``cabs.``cond``.``fmt````,
  ``bc1t``/``bc1f``).

  These functions compare ``a`` and ``b`` using ``cabs.``cond``.s``
  or ``cabs.``cond``.d`` and return the result as a boolean value.
  For example:

  .. code-block:: c++

    float a, b;
    if (__builtin_mips_cabs_eq_s (a, b))
      true ();
    else
      false ();

int __builtin_mips_upper_cabs_``cond``_ps (v2sf ``a``, v2sf ``b``)int __builtin_mips_lower_cabs_``cond``_ps (v2sf ``a``, v2sf ``b``)
  Absolute comparison of two paired-single values (``cabs.``cond``.ps``,
  ``bc1t``/``bc1f``).

  These functions compare ``a`` and ``b`` using ``cabs.``cond``.ps``
  and return either the upper or lower half of the result.  For example:

  .. code-block:: c++

    v2sf a, b;
    if (__builtin_mips_upper_cabs_eq_ps (a, b))
      upper_halves_are_equal ();
    else
      upper_halves_are_unequal ();

    if (__builtin_mips_lower_cabs_eq_ps (a, b))
      lower_halves_are_equal ();
    else
      lower_halves_are_unequal ();

v2sf __builtin_mips_movt_cabs_``cond``_ps (v2sf ``a``, v2sf ``b``, v2sf ``c``, v2sf ``d``)v2sf __builtin_mips_movf_cabs_``cond``_ps (v2sf ``a``, v2sf ``b``, v2sf ``c``, v2sf ``d``)
  Conditional move based on absolute comparison (``cabs.``cond``.ps``,
  ``movt.ps``/``movf.ps``).

  The ``movt`` functions return the value ``x`` computed by:

  .. code-block:: c++

    cabs.``cond``.ps ``cc``,``a``,``b``
    mov.ps ``x``,``c``
    movt.ps ``x``,``d``,``cc``

  The ``movf`` functions are similar but use ``movf.ps`` instead
  of ``movt.ps``.

int __builtin_mips_any_c_``cond``_ps (v2sf ``a``, v2sf ``b``)int __builtin_mips_all_c_``cond``_ps (v2sf ``a``, v2sf ``b``)int __builtin_mips_any_cabs_``cond``_ps (v2sf ``a``, v2sf ``b``)int __builtin_mips_all_cabs_``cond``_ps (v2sf ``a``, v2sf ``b``)
  Comparison of two paired-single values
  (``c.``cond``.ps``/``cabs.``cond``.ps``,
  ``bc1any2t``/``bc1any2f``).

  These functions compare ``a`` and ``b`` using ``c.``cond``.ps``
  or ``cabs.``cond``.ps``.  The ``any`` forms return true if either
  result is true and the ``all`` forms return true if both results are true.
  For example:

  .. code-block:: c++

    v2sf a, b;
    if (__builtin_mips_any_c_eq_ps (a, b))
      one_is_true ();
    else
      both_are_false ();

    if (__builtin_mips_all_c_eq_ps (a, b))
      both_are_true ();
    else
      one_is_false ();

int __builtin_mips_any_c_``cond``_4s (v2sf ``a``, v2sf ``b``, v2sf ``c``, v2sf ``d``)int __builtin_mips_all_c_``cond``_4s (v2sf ``a``, v2sf ``b``, v2sf ``c``, v2sf ``d``)int __builtin_mips_any_cabs_``cond``_4s (v2sf ``a``, v2sf ``b``, v2sf ``c``, v2sf ``d``)int __builtin_mips_all_cabs_``cond``_4s (v2sf ``a``, v2sf ``b``, v2sf ``c``, v2sf ``d``)
  Comparison of four paired-single values
  (``c.``cond``.ps``/``cabs.``cond``.ps``,
  ``bc1any4t``/``bc1any4f``).

  These functions use ``c.``cond``.ps`` or ``cabs.``cond``.ps``
  to compare ``a`` with ``b`` and to compare ``c`` with ``d``.
  The ``any`` forms return true if any of the four results are true
  and the ``all`` forms return true if all four results are true.
  For example:

  .. code-block:: c++

    v2sf a, b, c, d;
    if (__builtin_mips_any_c_eq_4s (a, b, c, d))
      some_are_true ();
    else
      all_are_false ();

    if (__builtin_mips_all_c_eq_4s (a, b, c, d))
      all_are_true ();
    else
      some_are_false ();

:: _other-mips-built-in-functions:

Other MIPS Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GCC provides other MIPS-specific built-in functions:

void __builtin_mips_cache (int ``op``, const volatile void *``addr``)
  Insert a cache instruction with operands ``op`` and ``addr``.
  GCC defines the preprocessor macro ``___GCC_HAVE_BUILTIN_MIPS_CACHE``
  when this function is available.

unsigned int __builtin_mips_get_fcsr (void)void __builtin_mips_set_fcsr (unsigned int ``value``)
  Get and set the contents of the floating-point control and status register
  (FPU control register 31).  These functions are only available in hard-float
  code but can be called in both MIPS16 and non-MIPS16 contexts.

  ``__builtin_mips_set_fcsr`` can be used to change any bit of the
  register except the condition codes, which GCC assumes are preserved.

:: _msp430-built-in-functions:

MSP430 Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^

GCC provides a couple of special builtin functions to aid in the
writing of interrupt handlers in C.

__bic_SR_register_on_exit (int ``mask``)
  This clears the indicated bits in the saved copy of the status register
  currently residing on the stack.  This only works inside interrupt
  handlers and the changes to the status register will only take affect
  once the handler returns.

__bis_SR_register_on_exit (int ``mask``)
  This sets the indicated bits in the saved copy of the status register
  currently residing on the stack.  This only works inside interrupt
  handlers and the changes to the status register will only take affect
  once the handler returns.

__delay_cycles (long long ``cycles``)
  This inserts an instruction sequence that takes exactly ``cycles``
  cycles (between 0 and about 17E9) to complete.  The inserted sequence
  may use jumps, loops, or no-ops, and does not interfere with any other
  instructions.  Note that ``cycles`` must be a compile-time constant
  integer - that is, you must pass a number, not a variable that may be
  optimized to a constant later.  The number of cycles delayed by this
  builtin is exact.

:: _nds32-built-in-functions:

NDS32 Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^

These built-in functions are available for the NDS32 target:

.. index:: __builtin_nds32_isync

  Built-in Function void __builtin_nds32_isync (int *``addr``)
Insert an ISYNC instruction into the instruction stream where
``addr`` is an instruction address for serialization.

.. index:: __builtin_nds32_isb

  Built-in Function void __builtin_nds32_isb (void)
Insert an ISB instruction into the instruction stream.

.. index:: __builtin_nds32_mfsr

  Built-in Function int __builtin_nds32_mfsr (int ``sr``)
Return the content of a system register which is mapped by ``sr``.

.. index:: __builtin_nds32_mfusr

  Built-in Function int __builtin_nds32_mfusr (int ``usr``)
Return the content of a user space register which is mapped by ``usr``.

.. index:: __builtin_nds32_mtsr

  Built-in Function void __builtin_nds32_mtsr (int ``value``, int ``sr``)
Move the ``value`` to a system register which is mapped by ``sr``.

.. index:: __builtin_nds32_mtusr

  Built-in Function void __builtin_nds32_mtusr (int ``value``, int ``usr``)
Move the ``value`` to a user space register which is mapped by ``usr``.

.. index:: __builtin_nds32_setgie_en

  Built-in Function void __builtin_nds32_setgie_en (void)
Enable global interrupt.

.. index:: __builtin_nds32_setgie_dis

  Built-in Function void __builtin_nds32_setgie_dis (void)
Disable global interrupt.

:: _picochip-built-in-functions:

picoChip Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

GCC provides an interface to selected machine instructions from the
picoChip instruction set.

int __builtin_sbc (int ``value``)
  Sign bit count.  Return the number of consecutive bits in ``value``
  that have the same value as the sign bit.  The result is the number of
  leading sign bits minus one, giving the number of redundant sign bits in
  ``value``.

int __builtin_byteswap (int ``value``)
  Byte swap.  Return the result of swapping the upper and lower bytes of
  ``value``.

int __builtin_brev (int ``value``)
  Bit reversal.  Return the result of reversing the bits in
  ``value``.  Bit 15 is swapped with bit 0, bit 14 is swapped with bit 1,
  and so on.

int __builtin_adds (int ``x``, int ``y``)
  Saturating addition.  Return the result of adding ``x`` and ``y``,
  storing the value 32767 if the result overflows.

int __builtin_subs (int ``x``, int ``y``)
  Saturating subtraction.  Return the result of subtracting ``y`` from
  ``x``, storing the value -32768 if the result overflows.

void __builtin_halt (void)
  Halt.  The processor stops execution.  This built-in is useful for
  implementing assertions.

:: _powerpc-built-in-functions:

PowerPC Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^

These built-in functions are available for the PowerPC family of
processors:

.. code-block:: c++

  float __builtin_recipdivf (float, float);
  float __builtin_rsqrtf (float);
  double __builtin_recipdiv (double, double);
  double __builtin_rsqrt (double);
  uint64_t __builtin_ppc_get_timebase ();
  unsigned long __builtin_ppc_mftb ();
  double __builtin_unpack_longdouble (long double, int);
  long double __builtin_pack_longdouble (double, double);

The ``vec_rsqrt``, ``__builtin_rsqrt``, and
``__builtin_rsqrtf`` functions generate multiple instructions to
implement the reciprocal sqrt functionality using reciprocal sqrt
estimate instructions.

The ``__builtin_recipdiv``, and ``__builtin_recipdivf``
functions generate multiple instructions to implement division using
the reciprocal estimate instructions.

The ``__builtin_ppc_get_timebase`` and ``__builtin_ppc_mftb``
functions generate instructions to read the Time Base Register.  The
``__builtin_ppc_get_timebase`` function may generate multiple
instructions and always returns the 64 bits of the Time Base Register.
The ``__builtin_ppc_mftb`` function always generates one instruction and
returns the Time Base Register value as an unsigned long, throwing away
the most significant word on 32-bit environments.

The following built-in functions are available for the PowerPC family
of processors, starting with ISA 2.06 or later (:option:`-mcpu=power7`
or :option:`-mpopcntd`):

.. code-block:: c++

  long __builtin_bpermd (long, long);
  int __builtin_divwe (int, int);
  int __builtin_divweo (int, int);
  unsigned int __builtin_divweu (unsigned int, unsigned int);
  unsigned int __builtin_divweuo (unsigned int, unsigned int);
  long __builtin_divde (long, long);
  long __builtin_divdeo (long, long);
  unsigned long __builtin_divdeu (unsigned long, unsigned long);
  unsigned long __builtin_divdeuo (unsigned long, unsigned long);
  unsigned int cdtbcd (unsigned int);
  unsigned int cbcdtd (unsigned int);
  unsigned int addg6s (unsigned int, unsigned int);

The ``__builtin_divde``, ``__builtin_divdeo``,
``__builtin_divdeu``, ``__builtin_divdeou`` functions require a
64-bit environment support ISA 2.06 or later.

The following built-in functions are available for the PowerPC family
of processors when hardware decimal floating point
(:option:`-mhard-dfp`) is available:

.. code-block:: c++

  _Decimal64 __builtin_dxex (_Decimal64);
  _Decimal128 __builtin_dxexq (_Decimal128);
  _Decimal64 __builtin_ddedpd (int, _Decimal64);
  _Decimal128 __builtin_ddedpdq (int, _Decimal128);
  _Decimal64 __builtin_denbcd (int, _Decimal64);
  _Decimal128 __builtin_denbcdq (int, _Decimal128);
  _Decimal64 __builtin_diex (_Decimal64, _Decimal64);
  _Decimal128 _builtin_diexq (_Decimal128, _Decimal128);
  _Decimal64 __builtin_dscli (_Decimal64, int);
  _Decimal128 __builtin_dscliq (_Decimal128, int);
  _Decimal64 __builtin_dscri (_Decimal64, int);
  _Decimal128 __builtin_dscriq (_Decimal128, int);
  unsigned long long __builtin_unpack_dec128 (_Decimal128, int);
  _Decimal128 __builtin_pack_dec128 (unsigned long long, unsigned long long);

The following built-in functions are available for the PowerPC family
of processors when the Vector Scalar (vsx) instruction set is
available:

.. code-block:: c++

  unsigned long long __builtin_unpack_vector_int128 (vector __int128_t, int);
  vector __int128_t __builtin_pack_vector_int128 (unsigned long long,
                                                  unsigned long long);

:: _powerpc-altivec/vsx-built-in-functions:

PowerPC AltiVec Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GCC provides an interface for the PowerPC family of processors to access
the AltiVec operations described in Motorola's AltiVec Programming
Interface Manual.  The interface is made available by including
``<altivec.h>`` and using :option:`-maltivec` and
:option:`-mabi=altivec`.  The interface supports the following vector
types.

.. code-block:: c++

  vector unsigned char
  vector signed char
  vector bool char

  vector unsigned short
  vector signed short
  vector bool short
  vector pixel

  vector unsigned int
  vector signed int
  vector bool int
  vector float

If :option:`-mvsx` is used the following additional vector types are
implemented.

.. code-block:: c++

  vector unsigned long
  vector signed long
  vector double

The long types are only implemented for 64-bit code generation, and
the long type is only used in the floating point/integer conversion
instructions.

GCC's implementation of the high-level language interface available from
C and C++ code differs from Motorola's documentation in several ways.

* A vector constant is a list of constant expressions within curly braces.

  * A vector initializer requires no cast if the vector constant is of the
  same type as the variable it is initializing.

  * If ``signed`` or ``unsigned`` is omitted, the signedness of the
  vector type is the default signedness of the base type.  The default
  varies depending on the operating system, so a portable program should
  always specify the signedness.

  * Compiling with :option:`-maltivec` adds keywords ``__vector``,
  ``vector``, ``__pixel``, ``pixel``, ``__bool`` and
  ``bool``.  When compiling ISO C, the context-sensitive substitution
  of the keywords ``vector``, ``pixel`` and ``bool`` is
  disabled.  To use them, you must include ``<altivec.h>`` instead.

  * GCC allows using a ``typedef`` name as the type specifier for a
  vector type.

  * For C, overloaded functions are implemented with macros so the following
  does not work:

  .. code-block:: c++

      vec_add ((vector signed int){1, 2, 3, 4}, foo);

  Since ``vec_add`` is a macro, the vector constant in the example
  is treated as four separate arguments.  Wrap the entire argument in
  parentheses for this to work.

Note: Only the ``<altivec.h>`` interface is supported.
Internally, GCC uses built-in functions to achieve the functionality in
the aforementioned header file, but they are not supported and are
subject to change without notice.

The following interfaces are supported for the generic and specific
AltiVec operations and the AltiVec predicates.  In cases where there
is a direct mapping between generic and specific operations, only the
generic names are shown here, although the specific operations can also
be used.

Arguments that are documented as ``const int`` require literal
integral values within the range required for that operation.

.. code-block:: c++

  vector signed char vec_abs (vector signed char);
  vector signed short vec_abs (vector signed short);
  vector signed int vec_abs (vector signed int);
  vector float vec_abs (vector float);

  vector signed char vec_abss (vector signed char);
  vector signed short vec_abss (vector signed short);
  vector signed int vec_abss (vector signed int);

  vector signed char vec_add (vector bool char, vector signed char);
  vector signed char vec_add (vector signed char, vector bool char);
  vector signed char vec_add (vector signed char, vector signed char);
  vector unsigned char vec_add (vector bool char, vector unsigned char);
  vector unsigned char vec_add (vector unsigned char, vector bool char);
  vector unsigned char vec_add (vector unsigned char,
                                vector unsigned char);
  vector signed short vec_add (vector bool short, vector signed short);
  vector signed short vec_add (vector signed short, vector bool short);
  vector signed short vec_add (vector signed short, vector signed short);
  vector unsigned short vec_add (vector bool short,
                                 vector unsigned short);
  vector unsigned short vec_add (vector unsigned short,
                                 vector bool short);
  vector unsigned short vec_add (vector unsigned short,
                                 vector unsigned short);
  vector signed int vec_add (vector bool int, vector signed int);
  vector signed int vec_add (vector signed int, vector bool int);
  vector signed int vec_add (vector signed int, vector signed int);
  vector unsigned int vec_add (vector bool int, vector unsigned int);
  vector unsigned int vec_add (vector unsigned int, vector bool int);
  vector unsigned int vec_add (vector unsigned int, vector unsigned int);
  vector float vec_add (vector float, vector float);

  vector float vec_vaddfp (vector float, vector float);

  vector signed int vec_vadduwm (vector bool int, vector signed int);
  vector signed int vec_vadduwm (vector signed int, vector bool int);
  vector signed int vec_vadduwm (vector signed int, vector signed int);
  vector unsigned int vec_vadduwm (vector bool int, vector unsigned int);
  vector unsigned int vec_vadduwm (vector unsigned int, vector bool int);
  vector unsigned int vec_vadduwm (vector unsigned int,
                                   vector unsigned int);

  vector signed short vec_vadduhm (vector bool short,
                                   vector signed short);
  vector signed short vec_vadduhm (vector signed short,
                                   vector bool short);
  vector signed short vec_vadduhm (vector signed short,
                                   vector signed short);
  vector unsigned short vec_vadduhm (vector bool short,
                                     vector unsigned short);
  vector unsigned short vec_vadduhm (vector unsigned short,
                                     vector bool short);
  vector unsigned short vec_vadduhm (vector unsigned short,
                                     vector unsigned short);

  vector signed char vec_vaddubm (vector bool char, vector signed char);
  vector signed char vec_vaddubm (vector signed char, vector bool char);
  vector signed char vec_vaddubm (vector signed char, vector signed char);
  vector unsigned char vec_vaddubm (vector bool char,
                                    vector unsigned char);
  vector unsigned char vec_vaddubm (vector unsigned char,
                                    vector bool char);
  vector unsigned char vec_vaddubm (vector unsigned char,
                                    vector unsigned char);

  vector unsigned int vec_addc (vector unsigned int, vector unsigned int);

  vector unsigned char vec_adds (vector bool char, vector unsigned char);
  vector unsigned char vec_adds (vector unsigned char, vector bool char);
  vector unsigned char vec_adds (vector unsigned char,
                                 vector unsigned char);
  vector signed char vec_adds (vector bool char, vector signed char);
  vector signed char vec_adds (vector signed char, vector bool char);
  vector signed char vec_adds (vector signed char, vector signed char);
  vector unsigned short vec_adds (vector bool short,
                                  vector unsigned short);
  vector unsigned short vec_adds (vector unsigned short,
                                  vector bool short);
  vector unsigned short vec_adds (vector unsigned short,
                                  vector unsigned short);
  vector signed short vec_adds (vector bool short, vector signed short);
  vector signed short vec_adds (vector signed short, vector bool short);
  vector signed short vec_adds (vector signed short, vector signed short);
  vector unsigned int vec_adds (vector bool int, vector unsigned int);
  vector unsigned int vec_adds (vector unsigned int, vector bool int);
  vector unsigned int vec_adds (vector unsigned int, vector unsigned int);
  vector signed int vec_adds (vector bool int, vector signed int);
  vector signed int vec_adds (vector signed int, vector bool int);
  vector signed int vec_adds (vector signed int, vector signed int);

  vector signed int vec_vaddsws (vector bool int, vector signed int);
  vector signed int vec_vaddsws (vector signed int, vector bool int);
  vector signed int vec_vaddsws (vector signed int, vector signed int);

  vector unsigned int vec_vadduws (vector bool int, vector unsigned int);
  vector unsigned int vec_vadduws (vector unsigned int, vector bool int);
  vector unsigned int vec_vadduws (vector unsigned int,
                                   vector unsigned int);

  vector signed short vec_vaddshs (vector bool short,
                                   vector signed short);
  vector signed short vec_vaddshs (vector signed short,
                                   vector bool short);
  vector signed short vec_vaddshs (vector signed short,
                                   vector signed short);

  vector unsigned short vec_vadduhs (vector bool short,
                                     vector unsigned short);
  vector unsigned short vec_vadduhs (vector unsigned short,
                                     vector bool short);
  vector unsigned short vec_vadduhs (vector unsigned short,
                                     vector unsigned short);

  vector signed char vec_vaddsbs (vector bool char, vector signed char);
  vector signed char vec_vaddsbs (vector signed char, vector bool char);
  vector signed char vec_vaddsbs (vector signed char, vector signed char);

  vector unsigned char vec_vaddubs (vector bool char,
                                    vector unsigned char);
  vector unsigned char vec_vaddubs (vector unsigned char,
                                    vector bool char);
  vector unsigned char vec_vaddubs (vector unsigned char,
                                    vector unsigned char);

  vector float vec_and (vector float, vector float);
  vector float vec_and (vector float, vector bool int);
  vector float vec_and (vector bool int, vector float);
  vector bool int vec_and (vector bool int, vector bool int);
  vector signed int vec_and (vector bool int, vector signed int);
  vector signed int vec_and (vector signed int, vector bool int);
  vector signed int vec_and (vector signed int, vector signed int);
  vector unsigned int vec_and (vector bool int, vector unsigned int);
  vector unsigned int vec_and (vector unsigned int, vector bool int);
  vector unsigned int vec_and (vector unsigned int, vector unsigned int);
  vector bool short vec_and (vector bool short, vector bool short);
  vector signed short vec_and (vector bool short, vector signed short);
  vector signed short vec_and (vector signed short, vector bool short);
  vector signed short vec_and (vector signed short, vector signed short);
  vector unsigned short vec_and (vector bool short,
                                 vector unsigned short);
  vector unsigned short vec_and (vector unsigned short,
                                 vector bool short);
  vector unsigned short vec_and (vector unsigned short,
                                 vector unsigned short);
  vector signed char vec_and (vector bool char, vector signed char);
  vector bool char vec_and (vector bool char, vector bool char);
  vector signed char vec_and (vector signed char, vector bool char);
  vector signed char vec_and (vector signed char, vector signed char);
  vector unsigned char vec_and (vector bool char, vector unsigned char);
  vector unsigned char vec_and (vector unsigned char, vector bool char);
  vector unsigned char vec_and (vector unsigned char,
                                vector unsigned char);

  vector float vec_andc (vector float, vector float);
  vector float vec_andc (vector float, vector bool int);
  vector float vec_andc (vector bool int, vector float);
  vector bool int vec_andc (vector bool int, vector bool int);
  vector signed int vec_andc (vector bool int, vector signed int);
  vector signed int vec_andc (vector signed int, vector bool int);
  vector signed int vec_andc (vector signed int, vector signed int);
  vector unsigned int vec_andc (vector bool int, vector unsigned int);
  vector unsigned int vec_andc (vector unsigned int, vector bool int);
  vector unsigned int vec_andc (vector unsigned int, vector unsigned int);
  vector bool short vec_andc (vector bool short, vector bool short);
  vector signed short vec_andc (vector bool short, vector signed short);
  vector signed short vec_andc (vector signed short, vector bool short);
  vector signed short vec_andc (vector signed short, vector signed short);
  vector unsigned short vec_andc (vector bool short,
                                  vector unsigned short);
  vector unsigned short vec_andc (vector unsigned short,
                                  vector bool short);
  vector unsigned short vec_andc (vector unsigned short,
                                  vector unsigned short);
  vector signed char vec_andc (vector bool char, vector signed char);
  vector bool char vec_andc (vector bool char, vector bool char);
  vector signed char vec_andc (vector signed char, vector bool char);
  vector signed char vec_andc (vector signed char, vector signed char);
  vector unsigned char vec_andc (vector bool char, vector unsigned char);
  vector unsigned char vec_andc (vector unsigned char, vector bool char);
  vector unsigned char vec_andc (vector unsigned char,
                                 vector unsigned char);

  vector unsigned char vec_avg (vector unsigned char,
                                vector unsigned char);
  vector signed char vec_avg (vector signed char, vector signed char);
  vector unsigned short vec_avg (vector unsigned short,
                                 vector unsigned short);
  vector signed short vec_avg (vector signed short, vector signed short);
  vector unsigned int vec_avg (vector unsigned int, vector unsigned int);
  vector signed int vec_avg (vector signed int, vector signed int);

  vector signed int vec_vavgsw (vector signed int, vector signed int);

  vector unsigned int vec_vavguw (vector unsigned int,
                                  vector unsigned int);

  vector signed short vec_vavgsh (vector signed short,
                                  vector signed short);

  vector unsigned short vec_vavguh (vector unsigned short,
                                    vector unsigned short);

  vector signed char vec_vavgsb (vector signed char, vector signed char);

  vector unsigned char vec_vavgub (vector unsigned char,
                                   vector unsigned char);

  vector float vec_copysign (vector float);

  vector float vec_ceil (vector float);

  vector signed int vec_cmpb (vector float, vector float);

  vector bool char vec_cmpeq (vector signed char, vector signed char);
  vector bool char vec_cmpeq (vector unsigned char, vector unsigned char);
  vector bool short vec_cmpeq (vector signed short, vector signed short);
  vector bool short vec_cmpeq (vector unsigned short,
                               vector unsigned short);
  vector bool int vec_cmpeq (vector signed int, vector signed int);
  vector bool int vec_cmpeq (vector unsigned int, vector unsigned int);
  vector bool int vec_cmpeq (vector float, vector float);

  vector bool int vec_vcmpeqfp (vector float, vector float);

  vector bool int vec_vcmpequw (vector signed int, vector signed int);
  vector bool int vec_vcmpequw (vector unsigned int, vector unsigned int);

  vector bool short vec_vcmpequh (vector signed short,
                                  vector signed short);
  vector bool short vec_vcmpequh (vector unsigned short,
                                  vector unsigned short);

  vector bool char vec_vcmpequb (vector signed char, vector signed char);
  vector bool char vec_vcmpequb (vector unsigned char,
                                 vector unsigned char);

  vector bool int vec_cmpge (vector float, vector float);

  vector bool char vec_cmpgt (vector unsigned char, vector unsigned char);
  vector bool char vec_cmpgt (vector signed char, vector signed char);
  vector bool short vec_cmpgt (vector unsigned short,
                               vector unsigned short);
  vector bool short vec_cmpgt (vector signed short, vector signed short);
  vector bool int vec_cmpgt (vector unsigned int, vector unsigned int);
  vector bool int vec_cmpgt (vector signed int, vector signed int);
  vector bool int vec_cmpgt (vector float, vector float);

  vector bool int vec_vcmpgtfp (vector float, vector float);

  vector bool int vec_vcmpgtsw (vector signed int, vector signed int);

  vector bool int vec_vcmpgtuw (vector unsigned int, vector unsigned int);

  vector bool short vec_vcmpgtsh (vector signed short,
                                  vector signed short);

  vector bool short vec_vcmpgtuh (vector unsigned short,
                                  vector unsigned short);

  vector bool char vec_vcmpgtsb (vector signed char, vector signed char);

  vector bool char vec_vcmpgtub (vector unsigned char,
                                 vector unsigned char);

  vector bool int vec_cmple (vector float, vector float);

  vector bool char vec_cmplt (vector unsigned char, vector unsigned char);
  vector bool char vec_cmplt (vector signed char, vector signed char);
  vector bool short vec_cmplt (vector unsigned short,
                               vector unsigned short);
  vector bool short vec_cmplt (vector signed short, vector signed short);
  vector bool int vec_cmplt (vector unsigned int, vector unsigned int);
  vector bool int vec_cmplt (vector signed int, vector signed int);
  vector bool int vec_cmplt (vector float, vector float);

  vector float vec_cpsgn (vector float, vector float);

  vector float vec_ctf (vector unsigned int, const int);
  vector float vec_ctf (vector signed int, const int);
  vector double vec_ctf (vector unsigned long, const int);
  vector double vec_ctf (vector signed long, const int);

  vector float vec_vcfsx (vector signed int, const int);

  vector float vec_vcfux (vector unsigned int, const int);

  vector signed int vec_cts (vector float, const int);
  vector signed long vec_cts (vector double, const int);

  vector unsigned int vec_ctu (vector float, const int);
  vector unsigned long vec_ctu (vector double, const int);

  void vec_dss (const int);

  void vec_dssall (void);

  void vec_dst (const vector unsigned char *, int, const int);
  void vec_dst (const vector signed char *, int, const int);
  void vec_dst (const vector bool char *, int, const int);
  void vec_dst (const vector unsigned short *, int, const int);
  void vec_dst (const vector signed short *, int, const int);
  void vec_dst (const vector bool short *, int, const int);
  void vec_dst (const vector pixel *, int, const int);
  void vec_dst (const vector unsigned int *, int, const int);
  void vec_dst (const vector signed int *, int, const int);
  void vec_dst (const vector bool int *, int, const int);
  void vec_dst (const vector float *, int, const int);
  void vec_dst (const unsigned char *, int, const int);
  void vec_dst (const signed char *, int, const int);
  void vec_dst (const unsigned short *, int, const int);
  void vec_dst (const short *, int, const int);
  void vec_dst (const unsigned int *, int, const int);
  void vec_dst (const int *, int, const int);
  void vec_dst (const unsigned long *, int, const int);
  void vec_dst (const long *, int, const int);
  void vec_dst (const float *, int, const int);

  void vec_dstst (const vector unsigned char *, int, const int);
  void vec_dstst (const vector signed char *, int, const int);
  void vec_dstst (const vector bool char *, int, const int);
  void vec_dstst (const vector unsigned short *, int, const int);
  void vec_dstst (const vector signed short *, int, const int);
  void vec_dstst (const vector bool short *, int, const int);
  void vec_dstst (const vector pixel *, int, const int);
  void vec_dstst (const vector unsigned int *, int, const int);
  void vec_dstst (const vector signed int *, int, const int);
  void vec_dstst (const vector bool int *, int, const int);
  void vec_dstst (const vector float *, int, const int);
  void vec_dstst (const unsigned char *, int, const int);
  void vec_dstst (const signed char *, int, const int);
  void vec_dstst (const unsigned short *, int, const int);
  void vec_dstst (const short *, int, const int);
  void vec_dstst (const unsigned int *, int, const int);
  void vec_dstst (const int *, int, const int);
  void vec_dstst (const unsigned long *, int, const int);
  void vec_dstst (const long *, int, const int);
  void vec_dstst (const float *, int, const int);

  void vec_dststt (const vector unsigned char *, int, const int);
  void vec_dststt (const vector signed char *, int, const int);
  void vec_dststt (const vector bool char *, int, const int);
  void vec_dststt (const vector unsigned short *, int, const int);
  void vec_dststt (const vector signed short *, int, const int);
  void vec_dststt (const vector bool short *, int, const int);
  void vec_dststt (const vector pixel *, int, const int);
  void vec_dststt (const vector unsigned int *, int, const int);
  void vec_dststt (const vector signed int *, int, const int);
  void vec_dststt (const vector bool int *, int, const int);
  void vec_dststt (const vector float *, int, const int);
  void vec_dststt (const unsigned char *, int, const int);
  void vec_dststt (const signed char *, int, const int);
  void vec_dststt (const unsigned short *, int, const int);
  void vec_dststt (const short *, int, const int);
  void vec_dststt (const unsigned int *, int, const int);
  void vec_dststt (const int *, int, const int);
  void vec_dststt (const unsigned long *, int, const int);
  void vec_dststt (const long *, int, const int);
  void vec_dststt (const float *, int, const int);

  void vec_dstt (const vector unsigned char *, int, const int);
  void vec_dstt (const vector signed char *, int, const int);
  void vec_dstt (const vector bool char *, int, const int);
  void vec_dstt (const vector unsigned short *, int, const int);
  void vec_dstt (const vector signed short *, int, const int);
  void vec_dstt (const vector bool short *, int, const int);
  void vec_dstt (const vector pixel *, int, const int);
  void vec_dstt (const vector unsigned int *, int, const int);
  void vec_dstt (const vector signed int *, int, const int);
  void vec_dstt (const vector bool int *, int, const int);
  void vec_dstt (const vector float *, int, const int);
  void vec_dstt (const unsigned char *, int, const int);
  void vec_dstt (const signed char *, int, const int);
  void vec_dstt (const unsigned short *, int, const int);
  void vec_dstt (const short *, int, const int);
  void vec_dstt (const unsigned int *, int, const int);
  void vec_dstt (const int *, int, const int);
  void vec_dstt (const unsigned long *, int, const int);
  void vec_dstt (const long *, int, const int);
  void vec_dstt (const float *, int, const int);

  vector float vec_expte (vector float);

  vector float vec_floor (vector float);

  vector float vec_ld (int, const vector float *);
  vector float vec_ld (int, const float *);
  vector bool int vec_ld (int, const vector bool int *);
  vector signed int vec_ld (int, const vector signed int *);
  vector signed int vec_ld (int, const int *);
  vector signed int vec_ld (int, const long *);
  vector unsigned int vec_ld (int, const vector unsigned int *);
  vector unsigned int vec_ld (int, const unsigned int *);
  vector unsigned int vec_ld (int, const unsigned long *);
  vector bool short vec_ld (int, const vector bool short *);
  vector pixel vec_ld (int, const vector pixel *);
  vector signed short vec_ld (int, const vector signed short *);
  vector signed short vec_ld (int, const short *);
  vector unsigned short vec_ld (int, const vector unsigned short *);
  vector unsigned short vec_ld (int, const unsigned short *);
  vector bool char vec_ld (int, const vector bool char *);
  vector signed char vec_ld (int, const vector signed char *);
  vector signed char vec_ld (int, const signed char *);
  vector unsigned char vec_ld (int, const vector unsigned char *);
  vector unsigned char vec_ld (int, const unsigned char *);

  vector signed char vec_lde (int, const signed char *);
  vector unsigned char vec_lde (int, const unsigned char *);
  vector signed short vec_lde (int, const short *);
  vector unsigned short vec_lde (int, const unsigned short *);
  vector float vec_lde (int, const float *);
  vector signed int vec_lde (int, const int *);
  vector unsigned int vec_lde (int, const unsigned int *);
  vector signed int vec_lde (int, const long *);
  vector unsigned int vec_lde (int, const unsigned long *);

  vector float vec_lvewx (int, float *);
  vector signed int vec_lvewx (int, int *);
  vector unsigned int vec_lvewx (int, unsigned int *);
  vector signed int vec_lvewx (int, long *);
  vector unsigned int vec_lvewx (int, unsigned long *);

  vector signed short vec_lvehx (int, short *);
  vector unsigned short vec_lvehx (int, unsigned short *);

  vector signed char vec_lvebx (int, char *);
  vector unsigned char vec_lvebx (int, unsigned char *);

  vector float vec_ldl (int, const vector float *);
  vector float vec_ldl (int, const float *);
  vector bool int vec_ldl (int, const vector bool int *);
  vector signed int vec_ldl (int, const vector signed int *);
  vector signed int vec_ldl (int, const int *);
  vector signed int vec_ldl (int, const long *);
  vector unsigned int vec_ldl (int, const vector unsigned int *);
  vector unsigned int vec_ldl (int, const unsigned int *);
  vector unsigned int vec_ldl (int, const unsigned long *);
  vector bool short vec_ldl (int, const vector bool short *);
  vector pixel vec_ldl (int, const vector pixel *);
  vector signed short vec_ldl (int, const vector signed short *);
  vector signed short vec_ldl (int, const short *);
  vector unsigned short vec_ldl (int, const vector unsigned short *);
  vector unsigned short vec_ldl (int, const unsigned short *);
  vector bool char vec_ldl (int, const vector bool char *);
  vector signed char vec_ldl (int, const vector signed char *);
  vector signed char vec_ldl (int, const signed char *);
  vector unsigned char vec_ldl (int, const vector unsigned char *);
  vector unsigned char vec_ldl (int, const unsigned char *);

  vector float vec_loge (vector float);

  vector unsigned char vec_lvsl (int, const volatile unsigned char *);
  vector unsigned char vec_lvsl (int, const volatile signed char *);
  vector unsigned char vec_lvsl (int, const volatile unsigned short *);
  vector unsigned char vec_lvsl (int, const volatile short *);
  vector unsigned char vec_lvsl (int, const volatile unsigned int *);
  vector unsigned char vec_lvsl (int, const volatile int *);
  vector unsigned char vec_lvsl (int, const volatile unsigned long *);
  vector unsigned char vec_lvsl (int, const volatile long *);
  vector unsigned char vec_lvsl (int, const volatile float *);

  vector unsigned char vec_lvsr (int, const volatile unsigned char *);
  vector unsigned char vec_lvsr (int, const volatile signed char *);
  vector unsigned char vec_lvsr (int, const volatile unsigned short *);
  vector unsigned char vec_lvsr (int, const volatile short *);
  vector unsigned char vec_lvsr (int, const volatile unsigned int *);
  vector unsigned char vec_lvsr (int, const volatile int *);
  vector unsigned char vec_lvsr (int, const volatile unsigned long *);
  vector unsigned char vec_lvsr (int, const volatile long *);
  vector unsigned char vec_lvsr (int, const volatile float *);

  vector float vec_madd (vector float, vector float, vector float);

  vector signed short vec_madds (vector signed short,
                                 vector signed short,
                                 vector signed short);

  vector unsigned char vec_max (vector bool char, vector unsigned char);
  vector unsigned char vec_max (vector unsigned char, vector bool char);
  vector unsigned char vec_max (vector unsigned char,
                                vector unsigned char);
  vector signed char vec_max (vector bool char, vector signed char);
  vector signed char vec_max (vector signed char, vector bool char);
  vector signed char vec_max (vector signed char, vector signed char);
  vector unsigned short vec_max (vector bool short,
                                 vector unsigned short);
  vector unsigned short vec_max (vector unsigned short,
                                 vector bool short);
  vector unsigned short vec_max (vector unsigned short,
                                 vector unsigned short);
  vector signed short vec_max (vector bool short, vector signed short);
  vector signed short vec_max (vector signed short, vector bool short);
  vector signed short vec_max (vector signed short, vector signed short);
  vector unsigned int vec_max (vector bool int, vector unsigned int);
  vector unsigned int vec_max (vector unsigned int, vector bool int);
  vector unsigned int vec_max (vector unsigned int, vector unsigned int);
  vector signed int vec_max (vector bool int, vector signed int);
  vector signed int vec_max (vector signed int, vector bool int);
  vector signed int vec_max (vector signed int, vector signed int);
  vector float vec_max (vector float, vector float);

  vector float vec_vmaxfp (vector float, vector float);

  vector signed int vec_vmaxsw (vector bool int, vector signed int);
  vector signed int vec_vmaxsw (vector signed int, vector bool int);
  vector signed int vec_vmaxsw (vector signed int, vector signed int);

  vector unsigned int vec_vmaxuw (vector bool int, vector unsigned int);
  vector unsigned int vec_vmaxuw (vector unsigned int, vector bool int);
  vector unsigned int vec_vmaxuw (vector unsigned int,
                                  vector unsigned int);

  vector signed short vec_vmaxsh (vector bool short, vector signed short);
  vector signed short vec_vmaxsh (vector signed short, vector bool short);
  vector signed short vec_vmaxsh (vector signed short,
                                  vector signed short);

  vector unsigned short vec_vmaxuh (vector bool short,
                                    vector unsigned short);
  vector unsigned short vec_vmaxuh (vector unsigned short,
                                    vector bool short);
  vector unsigned short vec_vmaxuh (vector unsigned short,
                                    vector unsigned short);

  vector signed char vec_vmaxsb (vector bool char, vector signed char);
  vector signed char vec_vmaxsb (vector signed char, vector bool char);
  vector signed char vec_vmaxsb (vector signed char, vector signed char);

  vector unsigned char vec_vmaxub (vector bool char,
                                   vector unsigned char);
  vector unsigned char vec_vmaxub (vector unsigned char,
                                   vector bool char);
  vector unsigned char vec_vmaxub (vector unsigned char,
                                   vector unsigned char);

  vector bool char vec_mergeh (vector bool char, vector bool char);
  vector signed char vec_mergeh (vector signed char, vector signed char);
  vector unsigned char vec_mergeh (vector unsigned char,
                                   vector unsigned char);
  vector bool short vec_mergeh (vector bool short, vector bool short);
  vector pixel vec_mergeh (vector pixel, vector pixel);
  vector signed short vec_mergeh (vector signed short,
                                  vector signed short);
  vector unsigned short vec_mergeh (vector unsigned short,
                                    vector unsigned short);
  vector float vec_mergeh (vector float, vector float);
  vector bool int vec_mergeh (vector bool int, vector bool int);
  vector signed int vec_mergeh (vector signed int, vector signed int);
  vector unsigned int vec_mergeh (vector unsigned int,
                                  vector unsigned int);

  vector float vec_vmrghw (vector float, vector float);
  vector bool int vec_vmrghw (vector bool int, vector bool int);
  vector signed int vec_vmrghw (vector signed int, vector signed int);
  vector unsigned int vec_vmrghw (vector unsigned int,
                                  vector unsigned int);

  vector bool short vec_vmrghh (vector bool short, vector bool short);
  vector signed short vec_vmrghh (vector signed short,
                                  vector signed short);
  vector unsigned short vec_vmrghh (vector unsigned short,
                                    vector unsigned short);
  vector pixel vec_vmrghh (vector pixel, vector pixel);

  vector bool char vec_vmrghb (vector bool char, vector bool char);
  vector signed char vec_vmrghb (vector signed char, vector signed char);
  vector unsigned char vec_vmrghb (vector unsigned char,
                                   vector unsigned char);

  vector bool char vec_mergel (vector bool char, vector bool char);
  vector signed char vec_mergel (vector signed char, vector signed char);
  vector unsigned char vec_mergel (vector unsigned char,
                                   vector unsigned char);
  vector bool short vec_mergel (vector bool short, vector bool short);
  vector pixel vec_mergel (vector pixel, vector pixel);
  vector signed short vec_mergel (vector signed short,
                                  vector signed short);
  vector unsigned short vec_mergel (vector unsigned short,
                                    vector unsigned short);
  vector float vec_mergel (vector float, vector float);
  vector bool int vec_mergel (vector bool int, vector bool int);
  vector signed int vec_mergel (vector signed int, vector signed int);
  vector unsigned int vec_mergel (vector unsigned int,
                                  vector unsigned int);

  vector float vec_vmrglw (vector float, vector float);
  vector signed int vec_vmrglw (vector signed int, vector signed int);
  vector unsigned int vec_vmrglw (vector unsigned int,
                                  vector unsigned int);
  vector bool int vec_vmrglw (vector bool int, vector bool int);

  vector bool short vec_vmrglh (vector bool short, vector bool short);
  vector signed short vec_vmrglh (vector signed short,
                                  vector signed short);
  vector unsigned short vec_vmrglh (vector unsigned short,
                                    vector unsigned short);
  vector pixel vec_vmrglh (vector pixel, vector pixel);

  vector bool char vec_vmrglb (vector bool char, vector bool char);
  vector signed char vec_vmrglb (vector signed char, vector signed char);
  vector unsigned char vec_vmrglb (vector unsigned char,
                                   vector unsigned char);

  vector unsigned short vec_mfvscr (void);

  vector unsigned char vec_min (vector bool char, vector unsigned char);
  vector unsigned char vec_min (vector unsigned char, vector bool char);
  vector unsigned char vec_min (vector unsigned char,
                                vector unsigned char);
  vector signed char vec_min (vector bool char, vector signed char);
  vector signed char vec_min (vector signed char, vector bool char);
  vector signed char vec_min (vector signed char, vector signed char);
  vector unsigned short vec_min (vector bool short,
                                 vector unsigned short);
  vector unsigned short vec_min (vector unsigned short,
                                 vector bool short);
  vector unsigned short vec_min (vector unsigned short,
                                 vector unsigned short);
  vector signed short vec_min (vector bool short, vector signed short);
  vector signed short vec_min (vector signed short, vector bool short);
  vector signed short vec_min (vector signed short, vector signed short);
  vector unsigned int vec_min (vector bool int, vector unsigned int);
  vector unsigned int vec_min (vector unsigned int, vector bool int);
  vector unsigned int vec_min (vector unsigned int, vector unsigned int);
  vector signed int vec_min (vector bool int, vector signed int);
  vector signed int vec_min (vector signed int, vector bool int);
  vector signed int vec_min (vector signed int, vector signed int);
  vector float vec_min (vector float, vector float);

  vector float vec_vminfp (vector float, vector float);

  vector signed int vec_vminsw (vector bool int, vector signed int);
  vector signed int vec_vminsw (vector signed int, vector bool int);
  vector signed int vec_vminsw (vector signed int, vector signed int);

  vector unsigned int vec_vminuw (vector bool int, vector unsigned int);
  vector unsigned int vec_vminuw (vector unsigned int, vector bool int);
  vector unsigned int vec_vminuw (vector unsigned int,
                                  vector unsigned int);

  vector signed short vec_vminsh (vector bool short, vector signed short);
  vector signed short vec_vminsh (vector signed short, vector bool short);
  vector signed short vec_vminsh (vector signed short,
                                  vector signed short);

  vector unsigned short vec_vminuh (vector bool short,
                                    vector unsigned short);
  vector unsigned short vec_vminuh (vector unsigned short,
                                    vector bool short);
  vector unsigned short vec_vminuh (vector unsigned short,
                                    vector unsigned short);

  vector signed char vec_vminsb (vector bool char, vector signed char);
  vector signed char vec_vminsb (vector signed char, vector bool char);
  vector signed char vec_vminsb (vector signed char, vector signed char);

  vector unsigned char vec_vminub (vector bool char,
                                   vector unsigned char);
  vector unsigned char vec_vminub (vector unsigned char,
                                   vector bool char);
  vector unsigned char vec_vminub (vector unsigned char,
                                   vector unsigned char);

  vector signed short vec_mladd (vector signed short,
                                 vector signed short,
                                 vector signed short);
  vector signed short vec_mladd (vector signed short,
                                 vector unsigned short,
                                 vector unsigned short);
  vector signed short vec_mladd (vector unsigned short,
                                 vector signed short,
                                 vector signed short);
  vector unsigned short vec_mladd (vector unsigned short,
                                   vector unsigned short,
                                   vector unsigned short);

  vector signed short vec_mradds (vector signed short,
                                  vector signed short,
                                  vector signed short);

  vector unsigned int vec_msum (vector unsigned char,
                                vector unsigned char,
                                vector unsigned int);
  vector signed int vec_msum (vector signed char,
                              vector unsigned char,
                              vector signed int);
  vector unsigned int vec_msum (vector unsigned short,
                                vector unsigned short,
                                vector unsigned int);
  vector signed int vec_msum (vector signed short,
                              vector signed short,
                              vector signed int);

  vector signed int vec_vmsumshm (vector signed short,
                                  vector signed short,
                                  vector signed int);

  vector unsigned int vec_vmsumuhm (vector unsigned short,
                                    vector unsigned short,
                                    vector unsigned int);

  vector signed int vec_vmsummbm (vector signed char,
                                  vector unsigned char,
                                  vector signed int);

  vector unsigned int vec_vmsumubm (vector unsigned char,
                                    vector unsigned char,
                                    vector unsigned int);

  vector unsigned int vec_msums (vector unsigned short,
                                 vector unsigned short,
                                 vector unsigned int);
  vector signed int vec_msums (vector signed short,
                               vector signed short,
                               vector signed int);

  vector signed int vec_vmsumshs (vector signed short,
                                  vector signed short,
                                  vector signed int);

  vector unsigned int vec_vmsumuhs (vector unsigned short,
                                    vector unsigned short,
                                    vector unsigned int);

  void vec_mtvscr (vector signed int);
  void vec_mtvscr (vector unsigned int);
  void vec_mtvscr (vector bool int);
  void vec_mtvscr (vector signed short);
  void vec_mtvscr (vector unsigned short);
  void vec_mtvscr (vector bool short);
  void vec_mtvscr (vector pixel);
  void vec_mtvscr (vector signed char);
  void vec_mtvscr (vector unsigned char);
  void vec_mtvscr (vector bool char);

  vector unsigned short vec_mule (vector unsigned char,
                                  vector unsigned char);
  vector signed short vec_mule (vector signed char,
                                vector signed char);
  vector unsigned int vec_mule (vector unsigned short,
                                vector unsigned short);
  vector signed int vec_mule (vector signed short, vector signed short);

  vector signed int vec_vmulesh (vector signed short,
                                 vector signed short);

  vector unsigned int vec_vmuleuh (vector unsigned short,
                                   vector unsigned short);

  vector signed short vec_vmulesb (vector signed char,
                                   vector signed char);

  vector unsigned short vec_vmuleub (vector unsigned char,
                                    vector unsigned char);

  vector unsigned short vec_mulo (vector unsigned char,
                                  vector unsigned char);
  vector signed short vec_mulo (vector signed char, vector signed char);
  vector unsigned int vec_mulo (vector unsigned short,
                                vector unsigned short);
  vector signed int vec_mulo (vector signed short, vector signed short);

  vector signed int vec_vmulosh (vector signed short,
                                 vector signed short);

  vector unsigned int vec_vmulouh (vector unsigned short,
                                   vector unsigned short);

  vector signed short vec_vmulosb (vector signed char,
                                   vector signed char);

  vector unsigned short vec_vmuloub (vector unsigned char,
                                     vector unsigned char);

  vector float vec_nmsub (vector float, vector float, vector float);

  vector float vec_nor (vector float, vector float);
  vector signed int vec_nor (vector signed int, vector signed int);
  vector unsigned int vec_nor (vector unsigned int, vector unsigned int);
  vector bool int vec_nor (vector bool int, vector bool int);
  vector signed short vec_nor (vector signed short, vector signed short);
  vector unsigned short vec_nor (vector unsigned short,
                                 vector unsigned short);
  vector bool short vec_nor (vector bool short, vector bool short);
  vector signed char vec_nor (vector signed char, vector signed char);
  vector unsigned char vec_nor (vector unsigned char,
                                vector unsigned char);
  vector bool char vec_nor (vector bool char, vector bool char);

  vector float vec_or (vector float, vector float);
  vector float vec_or (vector float, vector bool int);
  vector float vec_or (vector bool int, vector float);
  vector bool int vec_or (vector bool int, vector bool int);
  vector signed int vec_or (vector bool int, vector signed int);
  vector signed int vec_or (vector signed int, vector bool int);
  vector signed int vec_or (vector signed int, vector signed int);
  vector unsigned int vec_or (vector bool int, vector unsigned int);
  vector unsigned int vec_or (vector unsigned int, vector bool int);
  vector unsigned int vec_or (vector unsigned int, vector unsigned int);
  vector bool short vec_or (vector bool short, vector bool short);
  vector signed short vec_or (vector bool short, vector signed short);
  vector signed short vec_or (vector signed short, vector bool short);
  vector signed short vec_or (vector signed short, vector signed short);
  vector unsigned short vec_or (vector bool short, vector unsigned short);
  vector unsigned short vec_or (vector unsigned short, vector bool short);
  vector unsigned short vec_or (vector unsigned short,
                                vector unsigned short);
  vector signed char vec_or (vector bool char, vector signed char);
  vector bool char vec_or (vector bool char, vector bool char);
  vector signed char vec_or (vector signed char, vector bool char);
  vector signed char vec_or (vector signed char, vector signed char);
  vector unsigned char vec_or (vector bool char, vector unsigned char);
  vector unsigned char vec_or (vector unsigned char, vector bool char);
  vector unsigned char vec_or (vector unsigned char,
                               vector unsigned char);

  vector signed char vec_pack (vector signed short, vector signed short);
  vector unsigned char vec_pack (vector unsigned short,
                                 vector unsigned short);
  vector bool char vec_pack (vector bool short, vector bool short);
  vector signed short vec_pack (vector signed int, vector signed int);
  vector unsigned short vec_pack (vector unsigned int,
                                  vector unsigned int);
  vector bool short vec_pack (vector bool int, vector bool int);

  vector bool short vec_vpkuwum (vector bool int, vector bool int);
  vector signed short vec_vpkuwum (vector signed int, vector signed int);
  vector unsigned short vec_vpkuwum (vector unsigned int,
                                     vector unsigned int);

  vector bool char vec_vpkuhum (vector bool short, vector bool short);
  vector signed char vec_vpkuhum (vector signed short,
                                  vector signed short);
  vector unsigned char vec_vpkuhum (vector unsigned short,
                                    vector unsigned short);

  vector pixel vec_packpx (vector unsigned int, vector unsigned int);

  vector unsigned char vec_packs (vector unsigned short,
                                  vector unsigned short);
  vector signed char vec_packs (vector signed short, vector signed short);
  vector unsigned short vec_packs (vector unsigned int,
                                   vector unsigned int);
  vector signed short vec_packs (vector signed int, vector signed int);

  vector signed short vec_vpkswss (vector signed int, vector signed int);

  vector unsigned short vec_vpkuwus (vector unsigned int,
                                     vector unsigned int);

  vector signed char vec_vpkshss (vector signed short,
                                  vector signed short);

  vector unsigned char vec_vpkuhus (vector unsigned short,
                                    vector unsigned short);

  vector unsigned char vec_packsu (vector unsigned short,
                                   vector unsigned short);
  vector unsigned char vec_packsu (vector signed short,
                                   vector signed short);
  vector unsigned short vec_packsu (vector unsigned int,
                                    vector unsigned int);
  vector unsigned short vec_packsu (vector signed int, vector signed int);

  vector unsigned short vec_vpkswus (vector signed int,
                                     vector signed int);

  vector unsigned char vec_vpkshus (vector signed short,
                                    vector signed short);

  vector float vec_perm (vector float,
                         vector float,
                         vector unsigned char);
  vector signed int vec_perm (vector signed int,
                              vector signed int,
                              vector unsigned char);
  vector unsigned int vec_perm (vector unsigned int,
                                vector unsigned int,
                                vector unsigned char);
  vector bool int vec_perm (vector bool int,
                            vector bool int,
                            vector unsigned char);
  vector signed short vec_perm (vector signed short,
                                vector signed short,
                                vector unsigned char);
  vector unsigned short vec_perm (vector unsigned short,
                                  vector unsigned short,
                                  vector unsigned char);
  vector bool short vec_perm (vector bool short,
                              vector bool short,
                              vector unsigned char);
  vector pixel vec_perm (vector pixel,
                         vector pixel,
                         vector unsigned char);
  vector signed char vec_perm (vector signed char,
                               vector signed char,
                               vector unsigned char);
  vector unsigned char vec_perm (vector unsigned char,
                                 vector unsigned char,
                                 vector unsigned char);
  vector bool char vec_perm (vector bool char,
                             vector bool char,
                             vector unsigned char);

  vector float vec_re (vector float);

  vector signed char vec_rl (vector signed char,
                             vector unsigned char);
  vector unsigned char vec_rl (vector unsigned char,
                               vector unsigned char);
  vector signed short vec_rl (vector signed short, vector unsigned short);
  vector unsigned short vec_rl (vector unsigned short,
                                vector unsigned short);
  vector signed int vec_rl (vector signed int, vector unsigned int);
  vector unsigned int vec_rl (vector unsigned int, vector unsigned int);

  vector signed int vec_vrlw (vector signed int, vector unsigned int);
  vector unsigned int vec_vrlw (vector unsigned int, vector unsigned int);

  vector signed short vec_vrlh (vector signed short,
                                vector unsigned short);
  vector unsigned short vec_vrlh (vector unsigned short,
                                  vector unsigned short);

  vector signed char vec_vrlb (vector signed char, vector unsigned char);
  vector unsigned char vec_vrlb (vector unsigned char,
                                 vector unsigned char);

  vector float vec_round (vector float);

  vector float vec_recip (vector float, vector float);

  vector float vec_rsqrt (vector float);

  vector float vec_rsqrte (vector float);

  vector float vec_sel (vector float, vector float, vector bool int);
  vector float vec_sel (vector float, vector float, vector unsigned int);
  vector signed int vec_sel (vector signed int,
                             vector signed int,
                             vector bool int);
  vector signed int vec_sel (vector signed int,
                             vector signed int,
                             vector unsigned int);
  vector unsigned int vec_sel (vector unsigned int,
                               vector unsigned int,
                               vector bool int);
  vector unsigned int vec_sel (vector unsigned int,
                               vector unsigned int,
                               vector unsigned int);
  vector bool int vec_sel (vector bool int,
                           vector bool int,
                           vector bool int);
  vector bool int vec_sel (vector bool int,
                           vector bool int,
                           vector unsigned int);
  vector signed short vec_sel (vector signed short,
                               vector signed short,
                               vector bool short);
  vector signed short vec_sel (vector signed short,
                               vector signed short,
                               vector unsigned short);
  vector unsigned short vec_sel (vector unsigned short,
                                 vector unsigned short,
                                 vector bool short);
  vector unsigned short vec_sel (vector unsigned short,
                                 vector unsigned short,
                                 vector unsigned short);
  vector bool short vec_sel (vector bool short,
                             vector bool short,
                             vector bool short);
  vector bool short vec_sel (vector bool short,
                             vector bool short,
                             vector unsigned short);
  vector signed char vec_sel (vector signed char,
                              vector signed char,
                              vector bool char);
  vector signed char vec_sel (vector signed char,
                              vector signed char,
                              vector unsigned char);
  vector unsigned char vec_sel (vector unsigned char,
                                vector unsigned char,
                                vector bool char);
  vector unsigned char vec_sel (vector unsigned char,
                                vector unsigned char,
                                vector unsigned char);
  vector bool char vec_sel (vector bool char,
                            vector bool char,
                            vector bool char);
  vector bool char vec_sel (vector bool char,
                            vector bool char,
                            vector unsigned char);

  vector signed char vec_sl (vector signed char,
                             vector unsigned char);
  vector unsigned char vec_sl (vector unsigned char,
                               vector unsigned char);
  vector signed short vec_sl (vector signed short, vector unsigned short);
  vector unsigned short vec_sl (vector unsigned short,
                                vector unsigned short);
  vector signed int vec_sl (vector signed int, vector unsigned int);
  vector unsigned int vec_sl (vector unsigned int, vector unsigned int);

  vector signed int vec_vslw (vector signed int, vector unsigned int);
  vector unsigned int vec_vslw (vector unsigned int, vector unsigned int);

  vector signed short vec_vslh (vector signed short,
                                vector unsigned short);
  vector unsigned short vec_vslh (vector unsigned short,
                                  vector unsigned short);

  vector signed char vec_vslb (vector signed char, vector unsigned char);
  vector unsigned char vec_vslb (vector unsigned char,
                                 vector unsigned char);

  vector float vec_sld (vector float, vector float, const int);
  vector signed int vec_sld (vector signed int,
                             vector signed int,
                             const int);
  vector unsigned int vec_sld (vector unsigned int,
                               vector unsigned int,
                               const int);
  vector bool int vec_sld (vector bool int,
                           vector bool int,
                           const int);
  vector signed short vec_sld (vector signed short,
                               vector signed short,
                               const int);
  vector unsigned short vec_sld (vector unsigned short,
                                 vector unsigned short,
                                 const int);
  vector bool short vec_sld (vector bool short,
                             vector bool short,
                             const int);
  vector pixel vec_sld (vector pixel,
                        vector pixel,
                        const int);
  vector signed char vec_sld (vector signed char,
                              vector signed char,
                              const int);
  vector unsigned char vec_sld (vector unsigned char,
                                vector unsigned char,
                                const int);
  vector bool char vec_sld (vector bool char,
                            vector bool char,
                            const int);

  vector signed int vec_sll (vector signed int,
                             vector unsigned int);
  vector signed int vec_sll (vector signed int,
                             vector unsigned short);
  vector signed int vec_sll (vector signed int,
                             vector unsigned char);
  vector unsigned int vec_sll (vector unsigned int,
                               vector unsigned int);
  vector unsigned int vec_sll (vector unsigned int,
                               vector unsigned short);
  vector unsigned int vec_sll (vector unsigned int,
                               vector unsigned char);
  vector bool int vec_sll (vector bool int,
                           vector unsigned int);
  vector bool int vec_sll (vector bool int,
                           vector unsigned short);
  vector bool int vec_sll (vector bool int,
                           vector unsigned char);
  vector signed short vec_sll (vector signed short,
                               vector unsigned int);
  vector signed short vec_sll (vector signed short,
                               vector unsigned short);
  vector signed short vec_sll (vector signed short,
                               vector unsigned char);
  vector unsigned short vec_sll (vector unsigned short,
                                 vector unsigned int);
  vector unsigned short vec_sll (vector unsigned short,
                                 vector unsigned short);
  vector unsigned short vec_sll (vector unsigned short,
                                 vector unsigned char);
  vector bool short vec_sll (vector bool short, vector unsigned int);
  vector bool short vec_sll (vector bool short, vector unsigned short);
  vector bool short vec_sll (vector bool short, vector unsigned char);
  vector pixel vec_sll (vector pixel, vector unsigned int);
  vector pixel vec_sll (vector pixel, vector unsigned short);
  vector pixel vec_sll (vector pixel, vector unsigned char);
  vector signed char vec_sll (vector signed char, vector unsigned int);
  vector signed char vec_sll (vector signed char, vector unsigned short);
  vector signed char vec_sll (vector signed char, vector unsigned char);
  vector unsigned char vec_sll (vector unsigned char,
                                vector unsigned int);
  vector unsigned char vec_sll (vector unsigned char,
                                vector unsigned short);
  vector unsigned char vec_sll (vector unsigned char,
                                vector unsigned char);
  vector bool char vec_sll (vector bool char, vector unsigned int);
  vector bool char vec_sll (vector bool char, vector unsigned short);
  vector bool char vec_sll (vector bool char, vector unsigned char);

  vector float vec_slo (vector float, vector signed char);
  vector float vec_slo (vector float, vector unsigned char);
  vector signed int vec_slo (vector signed int, vector signed char);
  vector signed int vec_slo (vector signed int, vector unsigned char);
  vector unsigned int vec_slo (vector unsigned int, vector signed char);
  vector unsigned int vec_slo (vector unsigned int, vector unsigned char);
  vector signed short vec_slo (vector signed short, vector signed char);
  vector signed short vec_slo (vector signed short, vector unsigned char);
  vector unsigned short vec_slo (vector unsigned short,
                                 vector signed char);
  vector unsigned short vec_slo (vector unsigned short,
                                 vector unsigned char);
  vector pixel vec_slo (vector pixel, vector signed char);
  vector pixel vec_slo (vector pixel, vector unsigned char);
  vector signed char vec_slo (vector signed char, vector signed char);
  vector signed char vec_slo (vector signed char, vector unsigned char);
  vector unsigned char vec_slo (vector unsigned char, vector signed char);
  vector unsigned char vec_slo (vector unsigned char,
                                vector unsigned char);

  vector signed char vec_splat (vector signed char, const int);
  vector unsigned char vec_splat (vector unsigned char, const int);
  vector bool char vec_splat (vector bool char, const int);
  vector signed short vec_splat (vector signed short, const int);
  vector unsigned short vec_splat (vector unsigned short, const int);
  vector bool short vec_splat (vector bool short, const int);
  vector pixel vec_splat (vector pixel, const int);
  vector float vec_splat (vector float, const int);
  vector signed int vec_splat (vector signed int, const int);
  vector unsigned int vec_splat (vector unsigned int, const int);
  vector bool int vec_splat (vector bool int, const int);
  vector signed long vec_splat (vector signed long, const int);
  vector unsigned long vec_splat (vector unsigned long, const int);

  vector signed char vec_splats (signed char);
  vector unsigned char vec_splats (unsigned char);
  vector signed short vec_splats (signed short);
  vector unsigned short vec_splats (unsigned short);
  vector signed int vec_splats (signed int);
  vector unsigned int vec_splats (unsigned int);
  vector float vec_splats (float);

  vector float vec_vspltw (vector float, const int);
  vector signed int vec_vspltw (vector signed int, const int);
  vector unsigned int vec_vspltw (vector unsigned int, const int);
  vector bool int vec_vspltw (vector bool int, const int);

  vector bool short vec_vsplth (vector bool short, const int);
  vector signed short vec_vsplth (vector signed short, const int);
  vector unsigned short vec_vsplth (vector unsigned short, const int);
  vector pixel vec_vsplth (vector pixel, const int);

  vector signed char vec_vspltb (vector signed char, const int);
  vector unsigned char vec_vspltb (vector unsigned char, const int);
  vector bool char vec_vspltb (vector bool char, const int);

  vector signed char vec_splat_s8 (const int);

  vector signed short vec_splat_s16 (const int);

  vector signed int vec_splat_s32 (const int);

  vector unsigned char vec_splat_u8 (const int);

  vector unsigned short vec_splat_u16 (const int);

  vector unsigned int vec_splat_u32 (const int);

  vector signed char vec_sr (vector signed char, vector unsigned char);
  vector unsigned char vec_sr (vector unsigned char,
                               vector unsigned char);
  vector signed short vec_sr (vector signed short,
                              vector unsigned short);
  vector unsigned short vec_sr (vector unsigned short,
                                vector unsigned short);
  vector signed int vec_sr (vector signed int, vector unsigned int);
  vector unsigned int vec_sr (vector unsigned int, vector unsigned int);

  vector signed int vec_vsrw (vector signed int, vector unsigned int);
  vector unsigned int vec_vsrw (vector unsigned int, vector unsigned int);

  vector signed short vec_vsrh (vector signed short,
                                vector unsigned short);
  vector unsigned short vec_vsrh (vector unsigned short,
                                  vector unsigned short);

  vector signed char vec_vsrb (vector signed char, vector unsigned char);
  vector unsigned char vec_vsrb (vector unsigned char,
                                 vector unsigned char);

  vector signed char vec_sra (vector signed char, vector unsigned char);
  vector unsigned char vec_sra (vector unsigned char,
                                vector unsigned char);
  vector signed short vec_sra (vector signed short,
                               vector unsigned short);
  vector unsigned short vec_sra (vector unsigned short,
                                 vector unsigned short);
  vector signed int vec_sra (vector signed int, vector unsigned int);
  vector unsigned int vec_sra (vector unsigned int, vector unsigned int);

  vector signed int vec_vsraw (vector signed int, vector unsigned int);
  vector unsigned int vec_vsraw (vector unsigned int,
                                 vector unsigned int);

  vector signed short vec_vsrah (vector signed short,
                                 vector unsigned short);
  vector unsigned short vec_vsrah (vector unsigned short,
                                   vector unsigned short);

  vector signed char vec_vsrab (vector signed char, vector unsigned char);
  vector unsigned char vec_vsrab (vector unsigned char,
                                  vector unsigned char);

  vector signed int vec_srl (vector signed int, vector unsigned int);
  vector signed int vec_srl (vector signed int, vector unsigned short);
  vector signed int vec_srl (vector signed int, vector unsigned char);
  vector unsigned int vec_srl (vector unsigned int, vector unsigned int);
  vector unsigned int vec_srl (vector unsigned int,
                               vector unsigned short);
  vector unsigned int vec_srl (vector unsigned int, vector unsigned char);
  vector bool int vec_srl (vector bool int, vector unsigned int);
  vector bool int vec_srl (vector bool int, vector unsigned short);
  vector bool int vec_srl (vector bool int, vector unsigned char);
  vector signed short vec_srl (vector signed short, vector unsigned int);
  vector signed short vec_srl (vector signed short,
                               vector unsigned short);
  vector signed short vec_srl (vector signed short, vector unsigned char);
  vector unsigned short vec_srl (vector unsigned short,
                                 vector unsigned int);
  vector unsigned short vec_srl (vector unsigned short,
                                 vector unsigned short);
  vector unsigned short vec_srl (vector unsigned short,
                                 vector unsigned char);
  vector bool short vec_srl (vector bool short, vector unsigned int);
  vector bool short vec_srl (vector bool short, vector unsigned short);
  vector bool short vec_srl (vector bool short, vector unsigned char);
  vector pixel vec_srl (vector pixel, vector unsigned int);
  vector pixel vec_srl (vector pixel, vector unsigned short);
  vector pixel vec_srl (vector pixel, vector unsigned char);
  vector signed char vec_srl (vector signed char, vector unsigned int);
  vector signed char vec_srl (vector signed char, vector unsigned short);
  vector signed char vec_srl (vector signed char, vector unsigned char);
  vector unsigned char vec_srl (vector unsigned char,
                                vector unsigned int);
  vector unsigned char vec_srl (vector unsigned char,
                                vector unsigned short);
  vector unsigned char vec_srl (vector unsigned char,
                                vector unsigned char);
  vector bool char vec_srl (vector bool char, vector unsigned int);
  vector bool char vec_srl (vector bool char, vector unsigned short);
  vector bool char vec_srl (vector bool char, vector unsigned char);

  vector float vec_sro (vector float, vector signed char);
  vector float vec_sro (vector float, vector unsigned char);
  vector signed int vec_sro (vector signed int, vector signed char);
  vector signed int vec_sro (vector signed int, vector unsigned char);
  vector unsigned int vec_sro (vector unsigned int, vector signed char);
  vector unsigned int vec_sro (vector unsigned int, vector unsigned char);
  vector signed short vec_sro (vector signed short, vector signed char);
  vector signed short vec_sro (vector signed short, vector unsigned char);
  vector unsigned short vec_sro (vector unsigned short,
                                 vector signed char);
  vector unsigned short vec_sro (vector unsigned short,
                                 vector unsigned char);
  vector pixel vec_sro (vector pixel, vector signed char);
  vector pixel vec_sro (vector pixel, vector unsigned char);
  vector signed char vec_sro (vector signed char, vector signed char);
  vector signed char vec_sro (vector signed char, vector unsigned char);
  vector unsigned char vec_sro (vector unsigned char, vector signed char);
  vector unsigned char vec_sro (vector unsigned char,
                                vector unsigned char);

  void vec_st (vector float, int, vector float *);
  void vec_st (vector float, int, float *);
  void vec_st (vector signed int, int, vector signed int *);
  void vec_st (vector signed int, int, int *);
  void vec_st (vector unsigned int, int, vector unsigned int *);
  void vec_st (vector unsigned int, int, unsigned int *);
  void vec_st (vector bool int, int, vector bool int *);
  void vec_st (vector bool int, int, unsigned int *);
  void vec_st (vector bool int, int, int *);
  void vec_st (vector signed short, int, vector signed short *);
  void vec_st (vector signed short, int, short *);
  void vec_st (vector unsigned short, int, vector unsigned short *);
  void vec_st (vector unsigned short, int, unsigned short *);
  void vec_st (vector bool short, int, vector bool short *);
  void vec_st (vector bool short, int, unsigned short *);
  void vec_st (vector pixel, int, vector pixel *);
  void vec_st (vector pixel, int, unsigned short *);
  void vec_st (vector pixel, int, short *);
  void vec_st (vector bool short, int, short *);
  void vec_st (vector signed char, int, vector signed char *);
  void vec_st (vector signed char, int, signed char *);
  void vec_st (vector unsigned char, int, vector unsigned char *);
  void vec_st (vector unsigned char, int, unsigned char *);
  void vec_st (vector bool char, int, vector bool char *);
  void vec_st (vector bool char, int, unsigned char *);
  void vec_st (vector bool char, int, signed char *);

  void vec_ste (vector signed char, int, signed char *);
  void vec_ste (vector unsigned char, int, unsigned char *);
  void vec_ste (vector bool char, int, signed char *);
  void vec_ste (vector bool char, int, unsigned char *);
  void vec_ste (vector signed short, int, short *);
  void vec_ste (vector unsigned short, int, unsigned short *);
  void vec_ste (vector bool short, int, short *);
  void vec_ste (vector bool short, int, unsigned short *);
  void vec_ste (vector pixel, int, short *);
  void vec_ste (vector pixel, int, unsigned short *);
  void vec_ste (vector float, int, float *);
  void vec_ste (vector signed int, int, int *);
  void vec_ste (vector unsigned int, int, unsigned int *);
  void vec_ste (vector bool int, int, int *);
  void vec_ste (vector bool int, int, unsigned int *);

  void vec_stvewx (vector float, int, float *);
  void vec_stvewx (vector signed int, int, int *);
  void vec_stvewx (vector unsigned int, int, unsigned int *);
  void vec_stvewx (vector bool int, int, int *);
  void vec_stvewx (vector bool int, int, unsigned int *);

  void vec_stvehx (vector signed short, int, short *);
  void vec_stvehx (vector unsigned short, int, unsigned short *);
  void vec_stvehx (vector bool short, int, short *);
  void vec_stvehx (vector bool short, int, unsigned short *);
  void vec_stvehx (vector pixel, int, short *);
  void vec_stvehx (vector pixel, int, unsigned short *);

  void vec_stvebx (vector signed char, int, signed char *);
  void vec_stvebx (vector unsigned char, int, unsigned char *);
  void vec_stvebx (vector bool char, int, signed char *);
  void vec_stvebx (vector bool char, int, unsigned char *);

  void vec_stl (vector float, int, vector float *);
  void vec_stl (vector float, int, float *);
  void vec_stl (vector signed int, int, vector signed int *);
  void vec_stl (vector signed int, int, int *);
  void vec_stl (vector unsigned int, int, vector unsigned int *);
  void vec_stl (vector unsigned int, int, unsigned int *);
  void vec_stl (vector bool int, int, vector bool int *);
  void vec_stl (vector bool int, int, unsigned int *);
  void vec_stl (vector bool int, int, int *);
  void vec_stl (vector signed short, int, vector signed short *);
  void vec_stl (vector signed short, int, short *);
  void vec_stl (vector unsigned short, int, vector unsigned short *);
  void vec_stl (vector unsigned short, int, unsigned short *);
  void vec_stl (vector bool short, int, vector bool short *);
  void vec_stl (vector bool short, int, unsigned short *);
  void vec_stl (vector bool short, int, short *);
  void vec_stl (vector pixel, int, vector pixel *);
  void vec_stl (vector pixel, int, unsigned short *);
  void vec_stl (vector pixel, int, short *);
  void vec_stl (vector signed char, int, vector signed char *);
  void vec_stl (vector signed char, int, signed char *);
  void vec_stl (vector unsigned char, int, vector unsigned char *);
  void vec_stl (vector unsigned char, int, unsigned char *);
  void vec_stl (vector bool char, int, vector bool char *);
  void vec_stl (vector bool char, int, unsigned char *);
  void vec_stl (vector bool char, int, signed char *);

  vector signed char vec_sub (vector bool char, vector signed char);
  vector signed char vec_sub (vector signed char, vector bool char);
  vector signed char vec_sub (vector signed char, vector signed char);
  vector unsigned char vec_sub (vector bool char, vector unsigned char);
  vector unsigned char vec_sub (vector unsigned char, vector bool char);
  vector unsigned char vec_sub (vector unsigned char,
                                vector unsigned char);
  vector signed short vec_sub (vector bool short, vector signed short);
  vector signed short vec_sub (vector signed short, vector bool short);
  vector signed short vec_sub (vector signed short, vector signed short);
  vector unsigned short vec_sub (vector bool short,
                                 vector unsigned short);
  vector unsigned short vec_sub (vector unsigned short,
                                 vector bool short);
  vector unsigned short vec_sub (vector unsigned short,
                                 vector unsigned short);
  vector signed int vec_sub (vector bool int, vector signed int);
  vector signed int vec_sub (vector signed int, vector bool int);
  vector signed int vec_sub (vector signed int, vector signed int);
  vector unsigned int vec_sub (vector bool int, vector unsigned int);
  vector unsigned int vec_sub (vector unsigned int, vector bool int);
  vector unsigned int vec_sub (vector unsigned int, vector unsigned int);
  vector float vec_sub (vector float, vector float);

  vector float vec_vsubfp (vector float, vector float);

  vector signed int vec_vsubuwm (vector bool int, vector signed int);
  vector signed int vec_vsubuwm (vector signed int, vector bool int);
  vector signed int vec_vsubuwm (vector signed int, vector signed int);
  vector unsigned int vec_vsubuwm (vector bool int, vector unsigned int);
  vector unsigned int vec_vsubuwm (vector unsigned int, vector bool int);
  vector unsigned int vec_vsubuwm (vector unsigned int,
                                   vector unsigned int);

  vector signed short vec_vsubuhm (vector bool short,
                                   vector signed short);
  vector signed short vec_vsubuhm (vector signed short,
                                   vector bool short);
  vector signed short vec_vsubuhm (vector signed short,
                                   vector signed short);
  vector unsigned short vec_vsubuhm (vector bool short,
                                     vector unsigned short);
  vector unsigned short vec_vsubuhm (vector unsigned short,
                                     vector bool short);
  vector unsigned short vec_vsubuhm (vector unsigned short,
                                     vector unsigned short);

  vector signed char vec_vsububm (vector bool char, vector signed char);
  vector signed char vec_vsububm (vector signed char, vector bool char);
  vector signed char vec_vsububm (vector signed char, vector signed char);
  vector unsigned char vec_vsububm (vector bool char,
                                    vector unsigned char);
  vector unsigned char vec_vsububm (vector unsigned char,
                                    vector bool char);
  vector unsigned char vec_vsububm (vector unsigned char,
                                    vector unsigned char);

  vector unsigned int vec_subc (vector unsigned int, vector unsigned int);

  vector unsigned char vec_subs (vector bool char, vector unsigned char);
  vector unsigned char vec_subs (vector unsigned char, vector bool char);
  vector unsigned char vec_subs (vector unsigned char,
                                 vector unsigned char);
  vector signed char vec_subs (vector bool char, vector signed char);
  vector signed char vec_subs (vector signed char, vector bool char);
  vector signed char vec_subs (vector signed char, vector signed char);
  vector unsigned short vec_subs (vector bool short,
                                  vector unsigned short);
  vector unsigned short vec_subs (vector unsigned short,
                                  vector bool short);
  vector unsigned short vec_subs (vector unsigned short,
                                  vector unsigned short);
  vector signed short vec_subs (vector bool short, vector signed short);
  vector signed short vec_subs (vector signed short, vector bool short);
  vector signed short vec_subs (vector signed short, vector signed short);
  vector unsigned int vec_subs (vector bool int, vector unsigned int);
  vector unsigned int vec_subs (vector unsigned int, vector bool int);
  vector unsigned int vec_subs (vector unsigned int, vector unsigned int);
  vector signed int vec_subs (vector bool int, vector signed int);
  vector signed int vec_subs (vector signed int, vector bool int);
  vector signed int vec_subs (vector signed int, vector signed int);

  vector signed int vec_vsubsws (vector bool int, vector signed int);
  vector signed int vec_vsubsws (vector signed int, vector bool int);
  vector signed int vec_vsubsws (vector signed int, vector signed int);

  vector unsigned int vec_vsubuws (vector bool int, vector unsigned int);
  vector unsigned int vec_vsubuws (vector unsigned int, vector bool int);
  vector unsigned int vec_vsubuws (vector unsigned int,
                                   vector unsigned int);

  vector signed short vec_vsubshs (vector bool short,
                                   vector signed short);
  vector signed short vec_vsubshs (vector signed short,
                                   vector bool short);
  vector signed short vec_vsubshs (vector signed short,
                                   vector signed short);

  vector unsigned short vec_vsubuhs (vector bool short,
                                     vector unsigned short);
  vector unsigned short vec_vsubuhs (vector unsigned short,
                                     vector bool short);
  vector unsigned short vec_vsubuhs (vector unsigned short,
                                     vector unsigned short);

  vector signed char vec_vsubsbs (vector bool char, vector signed char);
  vector signed char vec_vsubsbs (vector signed char, vector bool char);
  vector signed char vec_vsubsbs (vector signed char, vector signed char);

  vector unsigned char vec_vsububs (vector bool char,
                                    vector unsigned char);
  vector unsigned char vec_vsububs (vector unsigned char,
                                    vector bool char);
  vector unsigned char vec_vsububs (vector unsigned char,
                                    vector unsigned char);

  vector unsigned int vec_sum4s (vector unsigned char,
                                 vector unsigned int);
  vector signed int vec_sum4s (vector signed char, vector signed int);
  vector signed int vec_sum4s (vector signed short, vector signed int);

  vector signed int vec_vsum4shs (vector signed short, vector signed int);

  vector signed int vec_vsum4sbs (vector signed char, vector signed int);

  vector unsigned int vec_vsum4ubs (vector unsigned char,
                                    vector unsigned int);

  vector signed int vec_sum2s (vector signed int, vector signed int);

  vector signed int vec_sums (vector signed int, vector signed int);

  vector float vec_trunc (vector float);

  vector signed short vec_unpackh (vector signed char);
  vector bool short vec_unpackh (vector bool char);
  vector signed int vec_unpackh (vector signed short);
  vector bool int vec_unpackh (vector bool short);
  vector unsigned int vec_unpackh (vector pixel);

  vector bool int vec_vupkhsh (vector bool short);
  vector signed int vec_vupkhsh (vector signed short);

  vector unsigned int vec_vupkhpx (vector pixel);

  vector bool short vec_vupkhsb (vector bool char);
  vector signed short vec_vupkhsb (vector signed char);

  vector signed short vec_unpackl (vector signed char);
  vector bool short vec_unpackl (vector bool char);
  vector unsigned int vec_unpackl (vector pixel);
  vector signed int vec_unpackl (vector signed short);
  vector bool int vec_unpackl (vector bool short);

  vector unsigned int vec_vupklpx (vector pixel);

  vector bool int vec_vupklsh (vector bool short);
  vector signed int vec_vupklsh (vector signed short);

  vector bool short vec_vupklsb (vector bool char);
  vector signed short vec_vupklsb (vector signed char);

  vector float vec_xor (vector float, vector float);
  vector float vec_xor (vector float, vector bool int);
  vector float vec_xor (vector bool int, vector float);
  vector bool int vec_xor (vector bool int, vector bool int);
  vector signed int vec_xor (vector bool int, vector signed int);
  vector signed int vec_xor (vector signed int, vector bool int);
  vector signed int vec_xor (vector signed int, vector signed int);
  vector unsigned int vec_xor (vector bool int, vector unsigned int);
  vector unsigned int vec_xor (vector unsigned int, vector bool int);
  vector unsigned int vec_xor (vector unsigned int, vector unsigned int);
  vector bool short vec_xor (vector bool short, vector bool short);
  vector signed short vec_xor (vector bool short, vector signed short);
  vector signed short vec_xor (vector signed short, vector bool short);
  vector signed short vec_xor (vector signed short, vector signed short);
  vector unsigned short vec_xor (vector bool short,
                                 vector unsigned short);
  vector unsigned short vec_xor (vector unsigned short,
                                 vector bool short);
  vector unsigned short vec_xor (vector unsigned short,
                                 vector unsigned short);
  vector signed char vec_xor (vector bool char, vector signed char);
  vector bool char vec_xor (vector bool char, vector bool char);
  vector signed char vec_xor (vector signed char, vector bool char);
  vector signed char vec_xor (vector signed char, vector signed char);
  vector unsigned char vec_xor (vector bool char, vector unsigned char);
  vector unsigned char vec_xor (vector unsigned char, vector bool char);
  vector unsigned char vec_xor (vector unsigned char,
                                vector unsigned char);

  int vec_all_eq (vector signed char, vector bool char);
  int vec_all_eq (vector signed char, vector signed char);
  int vec_all_eq (vector unsigned char, vector bool char);
  int vec_all_eq (vector unsigned char, vector unsigned char);
  int vec_all_eq (vector bool char, vector bool char);
  int vec_all_eq (vector bool char, vector unsigned char);
  int vec_all_eq (vector bool char, vector signed char);
  int vec_all_eq (vector signed short, vector bool short);
  int vec_all_eq (vector signed short, vector signed short);
  int vec_all_eq (vector unsigned short, vector bool short);
  int vec_all_eq (vector unsigned short, vector unsigned short);
  int vec_all_eq (vector bool short, vector bool short);
  int vec_all_eq (vector bool short, vector unsigned short);
  int vec_all_eq (vector bool short, vector signed short);
  int vec_all_eq (vector pixel, vector pixel);
  int vec_all_eq (vector signed int, vector bool int);
  int vec_all_eq (vector signed int, vector signed int);
  int vec_all_eq (vector unsigned int, vector bool int);
  int vec_all_eq (vector unsigned int, vector unsigned int);
  int vec_all_eq (vector bool int, vector bool int);
  int vec_all_eq (vector bool int, vector unsigned int);
  int vec_all_eq (vector bool int, vector signed int);
  int vec_all_eq (vector float, vector float);

  int vec_all_ge (vector bool char, vector unsigned char);
  int vec_all_ge (vector unsigned char, vector bool char);
  int vec_all_ge (vector unsigned char, vector unsigned char);
  int vec_all_ge (vector bool char, vector signed char);
  int vec_all_ge (vector signed char, vector bool char);
  int vec_all_ge (vector signed char, vector signed char);
  int vec_all_ge (vector bool short, vector unsigned short);
  int vec_all_ge (vector unsigned short, vector bool short);
  int vec_all_ge (vector unsigned short, vector unsigned short);
  int vec_all_ge (vector signed short, vector signed short);
  int vec_all_ge (vector bool short, vector signed short);
  int vec_all_ge (vector signed short, vector bool short);
  int vec_all_ge (vector bool int, vector unsigned int);
  int vec_all_ge (vector unsigned int, vector bool int);
  int vec_all_ge (vector unsigned int, vector unsigned int);
  int vec_all_ge (vector bool int, vector signed int);
  int vec_all_ge (vector signed int, vector bool int);
  int vec_all_ge (vector signed int, vector signed int);
  int vec_all_ge (vector float, vector float);

  int vec_all_gt (vector bool char, vector unsigned char);
  int vec_all_gt (vector unsigned char, vector bool char);
  int vec_all_gt (vector unsigned char, vector unsigned char);
  int vec_all_gt (vector bool char, vector signed char);
  int vec_all_gt (vector signed char, vector bool char);
  int vec_all_gt (vector signed char, vector signed char);
  int vec_all_gt (vector bool short, vector unsigned short);
  int vec_all_gt (vector unsigned short, vector bool short);
  int vec_all_gt (vector unsigned short, vector unsigned short);
  int vec_all_gt (vector bool short, vector signed short);
  int vec_all_gt (vector signed short, vector bool short);
  int vec_all_gt (vector signed short, vector signed short);
  int vec_all_gt (vector bool int, vector unsigned int);
  int vec_all_gt (vector unsigned int, vector bool int);
  int vec_all_gt (vector unsigned int, vector unsigned int);
  int vec_all_gt (vector bool int, vector signed int);
  int vec_all_gt (vector signed int, vector bool int);
  int vec_all_gt (vector signed int, vector signed int);
  int vec_all_gt (vector float, vector float);

  int vec_all_in (vector float, vector float);

  int vec_all_le (vector bool char, vector unsigned char);
  int vec_all_le (vector unsigned char, vector bool char);
  int vec_all_le (vector unsigned char, vector unsigned char);
  int vec_all_le (vector bool char, vector signed char);
  int vec_all_le (vector signed char, vector bool char);
  int vec_all_le (vector signed char, vector signed char);
  int vec_all_le (vector bool short, vector unsigned short);
  int vec_all_le (vector unsigned short, vector bool short);
  int vec_all_le (vector unsigned short, vector unsigned short);
  int vec_all_le (vector bool short, vector signed short);
  int vec_all_le (vector signed short, vector bool short);
  int vec_all_le (vector signed short, vector signed short);
  int vec_all_le (vector bool int, vector unsigned int);
  int vec_all_le (vector unsigned int, vector bool int);
  int vec_all_le (vector unsigned int, vector unsigned int);
  int vec_all_le (vector bool int, vector signed int);
  int vec_all_le (vector signed int, vector bool int);
  int vec_all_le (vector signed int, vector signed int);
  int vec_all_le (vector float, vector float);

  int vec_all_lt (vector bool char, vector unsigned char);
  int vec_all_lt (vector unsigned char, vector bool char);
  int vec_all_lt (vector unsigned char, vector unsigned char);
  int vec_all_lt (vector bool char, vector signed char);
  int vec_all_lt (vector signed char, vector bool char);
  int vec_all_lt (vector signed char, vector signed char);
  int vec_all_lt (vector bool short, vector unsigned short);
  int vec_all_lt (vector unsigned short, vector bool short);
  int vec_all_lt (vector unsigned short, vector unsigned short);
  int vec_all_lt (vector bool short, vector signed short);
  int vec_all_lt (vector signed short, vector bool short);
  int vec_all_lt (vector signed short, vector signed short);
  int vec_all_lt (vector bool int, vector unsigned int);
  int vec_all_lt (vector unsigned int, vector bool int);
  int vec_all_lt (vector unsigned int, vector unsigned int);
  int vec_all_lt (vector bool int, vector signed int);
  int vec_all_lt (vector signed int, vector bool int);
  int vec_all_lt (vector signed int, vector signed int);
  int vec_all_lt (vector float, vector float);

  int vec_all_nan (vector float);

  int vec_all_ne (vector signed char, vector bool char);
  int vec_all_ne (vector signed char, vector signed char);
  int vec_all_ne (vector unsigned char, vector bool char);
  int vec_all_ne (vector unsigned char, vector unsigned char);
  int vec_all_ne (vector bool char, vector bool char);
  int vec_all_ne (vector bool char, vector unsigned char);
  int vec_all_ne (vector bool char, vector signed char);
  int vec_all_ne (vector signed short, vector bool short);
  int vec_all_ne (vector signed short, vector signed short);
  int vec_all_ne (vector unsigned short, vector bool short);
  int vec_all_ne (vector unsigned short, vector unsigned short);
  int vec_all_ne (vector bool short, vector bool short);
  int vec_all_ne (vector bool short, vector unsigned short);
  int vec_all_ne (vector bool short, vector signed short);
  int vec_all_ne (vector pixel, vector pixel);
  int vec_all_ne (vector signed int, vector bool int);
  int vec_all_ne (vector signed int, vector signed int);
  int vec_all_ne (vector unsigned int, vector bool int);
  int vec_all_ne (vector unsigned int, vector unsigned int);
  int vec_all_ne (vector bool int, vector bool int);
  int vec_all_ne (vector bool int, vector unsigned int);
  int vec_all_ne (vector bool int, vector signed int);
  int vec_all_ne (vector float, vector float);

  int vec_all_nge (vector float, vector float);

  int vec_all_ngt (vector float, vector float);

  int vec_all_nle (vector float, vector float);

  int vec_all_nlt (vector float, vector float);

  int vec_all_numeric (vector float);

  int vec_any_eq (vector signed char, vector bool char);
  int vec_any_eq (vector signed char, vector signed char);
  int vec_any_eq (vector unsigned char, vector bool char);
  int vec_any_eq (vector unsigned char, vector unsigned char);
  int vec_any_eq (vector bool char, vector bool char);
  int vec_any_eq (vector bool char, vector unsigned char);
  int vec_any_eq (vector bool char, vector signed char);
  int vec_any_eq (vector signed short, vector bool short);
  int vec_any_eq (vector signed short, vector signed short);
  int vec_any_eq (vector unsigned short, vector bool short);
  int vec_any_eq (vector unsigned short, vector unsigned short);
  int vec_any_eq (vector bool short, vector bool short);
  int vec_any_eq (vector bool short, vector unsigned short);
  int vec_any_eq (vector bool short, vector signed short);
  int vec_any_eq (vector pixel, vector pixel);
  int vec_any_eq (vector signed int, vector bool int);
  int vec_any_eq (vector signed int, vector signed int);
  int vec_any_eq (vector unsigned int, vector bool int);
  int vec_any_eq (vector unsigned int, vector unsigned int);
  int vec_any_eq (vector bool int, vector bool int);
  int vec_any_eq (vector bool int, vector unsigned int);
  int vec_any_eq (vector bool int, vector signed int);
  int vec_any_eq (vector float, vector float);

  int vec_any_ge (vector signed char, vector bool char);
  int vec_any_ge (vector unsigned char, vector bool char);
  int vec_any_ge (vector unsigned char, vector unsigned char);
  int vec_any_ge (vector signed char, vector signed char);
  int vec_any_ge (vector bool char, vector unsigned char);
  int vec_any_ge (vector bool char, vector signed char);
  int vec_any_ge (vector unsigned short, vector bool short);
  int vec_any_ge (vector unsigned short, vector unsigned short);
  int vec_any_ge (vector signed short, vector signed short);
  int vec_any_ge (vector signed short, vector bool short);
  int vec_any_ge (vector bool short, vector unsigned short);
  int vec_any_ge (vector bool short, vector signed short);
  int vec_any_ge (vector signed int, vector bool int);
  int vec_any_ge (vector unsigned int, vector bool int);
  int vec_any_ge (vector unsigned int, vector unsigned int);
  int vec_any_ge (vector signed int, vector signed int);
  int vec_any_ge (vector bool int, vector unsigned int);
  int vec_any_ge (vector bool int, vector signed int);
  int vec_any_ge (vector float, vector float);

  int vec_any_gt (vector bool char, vector unsigned char);
  int vec_any_gt (vector unsigned char, vector bool char);
  int vec_any_gt (vector unsigned char, vector unsigned char);
  int vec_any_gt (vector bool char, vector signed char);
  int vec_any_gt (vector signed char, vector bool char);
  int vec_any_gt (vector signed char, vector signed char);
  int vec_any_gt (vector bool short, vector unsigned short);
  int vec_any_gt (vector unsigned short, vector bool short);
  int vec_any_gt (vector unsigned short, vector unsigned short);
  int vec_any_gt (vector bool short, vector signed short);
  int vec_any_gt (vector signed short, vector bool short);
  int vec_any_gt (vector signed short, vector signed short);
  int vec_any_gt (vector bool int, vector unsigned int);
  int vec_any_gt (vector unsigned int, vector bool int);
  int vec_any_gt (vector unsigned int, vector unsigned int);
  int vec_any_gt (vector bool int, vector signed int);
  int vec_any_gt (vector signed int, vector bool int);
  int vec_any_gt (vector signed int, vector signed int);
  int vec_any_gt (vector float, vector float);

  int vec_any_le (vector bool char, vector unsigned char);
  int vec_any_le (vector unsigned char, vector bool char);
  int vec_any_le (vector unsigned char, vector unsigned char);
  int vec_any_le (vector bool char, vector signed char);
  int vec_any_le (vector signed char, vector bool char);
  int vec_any_le (vector signed char, vector signed char);
  int vec_any_le (vector bool short, vector unsigned short);
  int vec_any_le (vector unsigned short, vector bool short);
  int vec_any_le (vector unsigned short, vector unsigned short);
  int vec_any_le (vector bool short, vector signed short);
  int vec_any_le (vector signed short, vector bool short);
  int vec_any_le (vector signed short, vector signed short);
  int vec_any_le (vector bool int, vector unsigned int);
  int vec_any_le (vector unsigned int, vector bool int);
  int vec_any_le (vector unsigned int, vector unsigned int);
  int vec_any_le (vector bool int, vector signed int);
  int vec_any_le (vector signed int, vector bool int);
  int vec_any_le (vector signed int, vector signed int);
  int vec_any_le (vector float, vector float);

  int vec_any_lt (vector bool char, vector unsigned char);
  int vec_any_lt (vector unsigned char, vector bool char);
  int vec_any_lt (vector unsigned char, vector unsigned char);
  int vec_any_lt (vector bool char, vector signed char);
  int vec_any_lt (vector signed char, vector bool char);
  int vec_any_lt (vector signed char, vector signed char);
  int vec_any_lt (vector bool short, vector unsigned short);
  int vec_any_lt (vector unsigned short, vector bool short);
  int vec_any_lt (vector unsigned short, vector unsigned short);
  int vec_any_lt (vector bool short, vector signed short);
  int vec_any_lt (vector signed short, vector bool short);
  int vec_any_lt (vector signed short, vector signed short);
  int vec_any_lt (vector bool int, vector unsigned int);
  int vec_any_lt (vector unsigned int, vector bool int);
  int vec_any_lt (vector unsigned int, vector unsigned int);
  int vec_any_lt (vector bool int, vector signed int);
  int vec_any_lt (vector signed int, vector bool int);
  int vec_any_lt (vector signed int, vector signed int);
  int vec_any_lt (vector float, vector float);

  int vec_any_nan (vector float);

  int vec_any_ne (vector signed char, vector bool char);
  int vec_any_ne (vector signed char, vector signed char);
  int vec_any_ne (vector unsigned char, vector bool char);
  int vec_any_ne (vector unsigned char, vector unsigned char);
  int vec_any_ne (vector bool char, vector bool char);
  int vec_any_ne (vector bool char, vector unsigned char);
  int vec_any_ne (vector bool char, vector signed char);
  int vec_any_ne (vector signed short, vector bool short);
  int vec_any_ne (vector signed short, vector signed short);
  int vec_any_ne (vector unsigned short, vector bool short);
  int vec_any_ne (vector unsigned short, vector unsigned short);
  int vec_any_ne (vector bool short, vector bool short);
  int vec_any_ne (vector bool short, vector unsigned short);
  int vec_any_ne (vector bool short, vector signed short);
  int vec_any_ne (vector pixel, vector pixel);
  int vec_any_ne (vector signed int, vector bool int);
  int vec_any_ne (vector signed int, vector signed int);
  int vec_any_ne (vector unsigned int, vector bool int);
  int vec_any_ne (vector unsigned int, vector unsigned int);
  int vec_any_ne (vector bool int, vector bool int);
  int vec_any_ne (vector bool int, vector unsigned int);
  int vec_any_ne (vector bool int, vector signed int);
  int vec_any_ne (vector float, vector float);

  int vec_any_nge (vector float, vector float);

  int vec_any_ngt (vector float, vector float);

  int vec_any_nle (vector float, vector float);

  int vec_any_nlt (vector float, vector float);

  int vec_any_numeric (vector float);

  int vec_any_out (vector float, vector float);

If the vector/scalar (VSX) instruction set is available, the following
additional functions are available:

.. code-block:: c++

  vector double vec_abs (vector double);
  vector double vec_add (vector double, vector double);
  vector double vec_and (vector double, vector double);
  vector double vec_and (vector double, vector bool long);
  vector double vec_and (vector bool long, vector double);
  vector long vec_and (vector long, vector long);
  vector long vec_and (vector long, vector bool long);
  vector long vec_and (vector bool long, vector long);
  vector unsigned long vec_and (vector unsigned long, vector unsigned long);
  vector unsigned long vec_and (vector unsigned long, vector bool long);
  vector unsigned long vec_and (vector bool long, vector unsigned long);
  vector double vec_andc (vector double, vector double);
  vector double vec_andc (vector double, vector bool long);
  vector double vec_andc (vector bool long, vector double);
  vector long vec_andc (vector long, vector long);
  vector long vec_andc (vector long, vector bool long);
  vector long vec_andc (vector bool long, vector long);
  vector unsigned long vec_andc (vector unsigned long, vector unsigned long);
  vector unsigned long vec_andc (vector unsigned long, vector bool long);
  vector unsigned long vec_andc (vector bool long, vector unsigned long);
  vector double vec_ceil (vector double);
  vector bool long vec_cmpeq (vector double, vector double);
  vector bool long vec_cmpge (vector double, vector double);
  vector bool long vec_cmpgt (vector double, vector double);
  vector bool long vec_cmple (vector double, vector double);
  vector bool long vec_cmplt (vector double, vector double);
  vector double vec_cpsgn (vector double, vector double);
  vector float vec_div (vector float, vector float);
  vector double vec_div (vector double, vector double);
  vector long vec_div (vector long, vector long);
  vector unsigned long vec_div (vector unsigned long, vector unsigned long);
  vector double vec_floor (vector double);
  vector double vec_ld (int, const vector double *);
  vector double vec_ld (int, const double *);
  vector double vec_ldl (int, const vector double *);
  vector double vec_ldl (int, const double *);
  vector unsigned char vec_lvsl (int, const volatile double *);
  vector unsigned char vec_lvsr (int, const volatile double *);
  vector double vec_madd (vector double, vector double, vector double);
  vector double vec_max (vector double, vector double);
  vector signed long vec_mergeh (vector signed long, vector signed long);
  vector signed long vec_mergeh (vector signed long, vector bool long);
  vector signed long vec_mergeh (vector bool long, vector signed long);
  vector unsigned long vec_mergeh (vector unsigned long, vector unsigned long);
  vector unsigned long vec_mergeh (vector unsigned long, vector bool long);
  vector unsigned long vec_mergeh (vector bool long, vector unsigned long);
  vector signed long vec_mergel (vector signed long, vector signed long);
  vector signed long vec_mergel (vector signed long, vector bool long);
  vector signed long vec_mergel (vector bool long, vector signed long);
  vector unsigned long vec_mergel (vector unsigned long, vector unsigned long);
  vector unsigned long vec_mergel (vector unsigned long, vector bool long);
  vector unsigned long vec_mergel (vector bool long, vector unsigned long);
  vector double vec_min (vector double, vector double);
  vector float vec_msub (vector float, vector float, vector float);
  vector double vec_msub (vector double, vector double, vector double);
  vector float vec_mul (vector float, vector float);
  vector double vec_mul (vector double, vector double);
  vector long vec_mul (vector long, vector long);
  vector unsigned long vec_mul (vector unsigned long, vector unsigned long);
  vector float vec_nearbyint (vector float);
  vector double vec_nearbyint (vector double);
  vector float vec_nmadd (vector float, vector float, vector float);
  vector double vec_nmadd (vector double, vector double, vector double);
  vector double vec_nmsub (vector double, vector double, vector double);
  vector double vec_nor (vector double, vector double);
  vector long vec_nor (vector long, vector long);
  vector long vec_nor (vector long, vector bool long);
  vector long vec_nor (vector bool long, vector long);
  vector unsigned long vec_nor (vector unsigned long, vector unsigned long);
  vector unsigned long vec_nor (vector unsigned long, vector bool long);
  vector unsigned long vec_nor (vector bool long, vector unsigned long);
  vector double vec_or (vector double, vector double);
  vector double vec_or (vector double, vector bool long);
  vector double vec_or (vector bool long, vector double);
  vector long vec_or (vector long, vector long);
  vector long vec_or (vector long, vector bool long);
  vector long vec_or (vector bool long, vector long);
  vector unsigned long vec_or (vector unsigned long, vector unsigned long);
  vector unsigned long vec_or (vector unsigned long, vector bool long);
  vector unsigned long vec_or (vector bool long, vector unsigned long);
  vector double vec_perm (vector double, vector double, vector unsigned char);
  vector long vec_perm (vector long, vector long, vector unsigned char);
  vector unsigned long vec_perm (vector unsigned long, vector unsigned long,
                                 vector unsigned char);
  vector double vec_rint (vector double);
  vector double vec_recip (vector double, vector double);
  vector double vec_rsqrt (vector double);
  vector double vec_rsqrte (vector double);
  vector double vec_sel (vector double, vector double, vector bool long);
  vector double vec_sel (vector double, vector double, vector unsigned long);
  vector long vec_sel (vector long, vector long, vector long);
  vector long vec_sel (vector long, vector long, vector unsigned long);
  vector long vec_sel (vector long, vector long, vector bool long);
  vector unsigned long vec_sel (vector unsigned long, vector unsigned long,
                                vector long);
  vector unsigned long vec_sel (vector unsigned long, vector unsigned long,
                                vector unsigned long);
  vector unsigned long vec_sel (vector unsigned long, vector unsigned long,
                                vector bool long);
  vector double vec_splats (double);
  vector signed long vec_splats (signed long);
  vector unsigned long vec_splats (unsigned long);
  vector float vec_sqrt (vector float);
  vector double vec_sqrt (vector double);
  void vec_st (vector double, int, vector double *);
  void vec_st (vector double, int, double *);
  vector double vec_sub (vector double, vector double);
  vector double vec_trunc (vector double);
  vector double vec_xor (vector double, vector double);
  vector double vec_xor (vector double, vector bool long);
  vector double vec_xor (vector bool long, vector double);
  vector long vec_xor (vector long, vector long);
  vector long vec_xor (vector long, vector bool long);
  vector long vec_xor (vector bool long, vector long);
  vector unsigned long vec_xor (vector unsigned long, vector unsigned long);
  vector unsigned long vec_xor (vector unsigned long, vector bool long);
  vector unsigned long vec_xor (vector bool long, vector unsigned long);
  int vec_all_eq (vector double, vector double);
  int vec_all_ge (vector double, vector double);
  int vec_all_gt (vector double, vector double);
  int vec_all_le (vector double, vector double);
  int vec_all_lt (vector double, vector double);
  int vec_all_nan (vector double);
  int vec_all_ne (vector double, vector double);
  int vec_all_nge (vector double, vector double);
  int vec_all_ngt (vector double, vector double);
  int vec_all_nle (vector double, vector double);
  int vec_all_nlt (vector double, vector double);
  int vec_all_numeric (vector double);
  int vec_any_eq (vector double, vector double);
  int vec_any_ge (vector double, vector double);
  int vec_any_gt (vector double, vector double);
  int vec_any_le (vector double, vector double);
  int vec_any_lt (vector double, vector double);
  int vec_any_nan (vector double);
  int vec_any_ne (vector double, vector double);
  int vec_any_nge (vector double, vector double);
  int vec_any_ngt (vector double, vector double);
  int vec_any_nle (vector double, vector double);
  int vec_any_nlt (vector double, vector double);
  int vec_any_numeric (vector double);

  vector double vec_vsx_ld (int, const vector double *);
  vector double vec_vsx_ld (int, const double *);
  vector float vec_vsx_ld (int, const vector float *);
  vector float vec_vsx_ld (int, const float *);
  vector bool int vec_vsx_ld (int, const vector bool int *);
  vector signed int vec_vsx_ld (int, const vector signed int *);
  vector signed int vec_vsx_ld (int, const int *);
  vector signed int vec_vsx_ld (int, const long *);
  vector unsigned int vec_vsx_ld (int, const vector unsigned int *);
  vector unsigned int vec_vsx_ld (int, const unsigned int *);
  vector unsigned int vec_vsx_ld (int, const unsigned long *);
  vector bool short vec_vsx_ld (int, const vector bool short *);
  vector pixel vec_vsx_ld (int, const vector pixel *);
  vector signed short vec_vsx_ld (int, const vector signed short *);
  vector signed short vec_vsx_ld (int, const short *);
  vector unsigned short vec_vsx_ld (int, const vector unsigned short *);
  vector unsigned short vec_vsx_ld (int, const unsigned short *);
  vector bool char vec_vsx_ld (int, const vector bool char *);
  vector signed char vec_vsx_ld (int, const vector signed char *);
  vector signed char vec_vsx_ld (int, const signed char *);
  vector unsigned char vec_vsx_ld (int, const vector unsigned char *);
  vector unsigned char vec_vsx_ld (int, const unsigned char *);

  void vec_vsx_st (vector double, int, vector double *);
  void vec_vsx_st (vector double, int, double *);
  void vec_vsx_st (vector float, int, vector float *);
  void vec_vsx_st (vector float, int, float *);
  void vec_vsx_st (vector signed int, int, vector signed int *);
  void vec_vsx_st (vector signed int, int, int *);
  void vec_vsx_st (vector unsigned int, int, vector unsigned int *);
  void vec_vsx_st (vector unsigned int, int, unsigned int *);
  void vec_vsx_st (vector bool int, int, vector bool int *);
  void vec_vsx_st (vector bool int, int, unsigned int *);
  void vec_vsx_st (vector bool int, int, int *);
  void vec_vsx_st (vector signed short, int, vector signed short *);
  void vec_vsx_st (vector signed short, int, short *);
  void vec_vsx_st (vector unsigned short, int, vector unsigned short *);
  void vec_vsx_st (vector unsigned short, int, unsigned short *);
  void vec_vsx_st (vector bool short, int, vector bool short *);
  void vec_vsx_st (vector bool short, int, unsigned short *);
  void vec_vsx_st (vector pixel, int, vector pixel *);
  void vec_vsx_st (vector pixel, int, unsigned short *);
  void vec_vsx_st (vector pixel, int, short *);
  void vec_vsx_st (vector bool short, int, short *);
  void vec_vsx_st (vector signed char, int, vector signed char *);
  void vec_vsx_st (vector signed char, int, signed char *);
  void vec_vsx_st (vector unsigned char, int, vector unsigned char *);
  void vec_vsx_st (vector unsigned char, int, unsigned char *);
  void vec_vsx_st (vector bool char, int, vector bool char *);
  void vec_vsx_st (vector bool char, int, unsigned char *);
  void vec_vsx_st (vector bool char, int, signed char *);

  vector double vec_xxpermdi (vector double, vector double, int);
  vector float vec_xxpermdi (vector float, vector float, int);
  vector long long vec_xxpermdi (vector long long, vector long long, int);
  vector unsigned long long vec_xxpermdi (vector unsigned long long,
                                          vector unsigned long long, int);
  vector int vec_xxpermdi (vector int, vector int, int);
  vector unsigned int vec_xxpermdi (vector unsigned int,
                                    vector unsigned int, int);
  vector short vec_xxpermdi (vector short, vector short, int);
  vector unsigned short vec_xxpermdi (vector unsigned short,
                                      vector unsigned short, int);
  vector signed char vec_xxpermdi (vector signed char, vector signed char, int);
  vector unsigned char vec_xxpermdi (vector unsigned char,
                                     vector unsigned char, int);

  vector double vec_xxsldi (vector double, vector double, int);
  vector float vec_xxsldi (vector float, vector float, int);
  vector long long vec_xxsldi (vector long long, vector long long, int);
  vector unsigned long long vec_xxsldi (vector unsigned long long,
                                        vector unsigned long long, int);
  vector int vec_xxsldi (vector int, vector int, int);
  vector unsigned int vec_xxsldi (vector unsigned int, vector unsigned int, int);
  vector short vec_xxsldi (vector short, vector short, int);
  vector unsigned short vec_xxsldi (vector unsigned short,
                                    vector unsigned short, int);
  vector signed char vec_xxsldi (vector signed char, vector signed char, int);
  vector unsigned char vec_xxsldi (vector unsigned char,
                                   vector unsigned char, int);

Note that the vec_ld and vec_st built-in functions always
generate the AltiVec LVX and STVX instructions even
if the VSX instruction set is available.  The vec_vsx_ld and
vec_vsx_st built-in functions always generate the VSX LXVD2X,
LXVW4X, STXVD2X, and STXVW4X instructions.

If the ISA 2.07 additions to the vector/scalar (power8-vector)
instruction set is available, the following additional functions are
available for both 32-bit and 64-bit targets.  For 64-bit targets, you
can use ``vector long`` instead of ``vector long long``,
``vector bool long`` instead of ``vector bool long long``, and
``vector unsigned long`` instead of ``vector unsigned long long``.

.. code-block:: c++

  vector long long vec_abs (vector long long);

  vector long long vec_add (vector long long, vector long long);
  vector unsigned long long vec_add (vector unsigned long long,
                                     vector unsigned long long);

  int vec_all_eq (vector long long, vector long long);
  int vec_all_eq (vector unsigned long long, vector unsigned long long);
  int vec_all_ge (vector long long, vector long long);
  int vec_all_ge (vector unsigned long long, vector unsigned long long);
  int vec_all_gt (vector long long, vector long long);
  int vec_all_gt (vector unsigned long long, vector unsigned long long);
  int vec_all_le (vector long long, vector long long);
  int vec_all_le (vector unsigned long long, vector unsigned long long);
  int vec_all_lt (vector long long, vector long long);
  int vec_all_lt (vector unsigned long long, vector unsigned long long);
  int vec_all_ne (vector long long, vector long long);
  int vec_all_ne (vector unsigned long long, vector unsigned long long);

  int vec_any_eq (vector long long, vector long long);
  int vec_any_eq (vector unsigned long long, vector unsigned long long);
  int vec_any_ge (vector long long, vector long long);
  int vec_any_ge (vector unsigned long long, vector unsigned long long);
  int vec_any_gt (vector long long, vector long long);
  int vec_any_gt (vector unsigned long long, vector unsigned long long);
  int vec_any_le (vector long long, vector long long);
  int vec_any_le (vector unsigned long long, vector unsigned long long);
  int vec_any_lt (vector long long, vector long long);
  int vec_any_lt (vector unsigned long long, vector unsigned long long);
  int vec_any_ne (vector long long, vector long long);
  int vec_any_ne (vector unsigned long long, vector unsigned long long);

  vector long long vec_eqv (vector long long, vector long long);
  vector long long vec_eqv (vector bool long long, vector long long);
  vector long long vec_eqv (vector long long, vector bool long long);
  vector unsigned long long vec_eqv (vector unsigned long long,
                                     vector unsigned long long);
  vector unsigned long long vec_eqv (vector bool long long,
                                     vector unsigned long long);
  vector unsigned long long vec_eqv (vector unsigned long long,
                                     vector bool long long);
  vector int vec_eqv (vector int, vector int);
  vector int vec_eqv (vector bool int, vector int);
  vector int vec_eqv (vector int, vector bool int);
  vector unsigned int vec_eqv (vector unsigned int, vector unsigned int);
  vector unsigned int vec_eqv (vector bool unsigned int,
                               vector unsigned int);
  vector unsigned int vec_eqv (vector unsigned int,
                               vector bool unsigned int);
  vector short vec_eqv (vector short, vector short);
  vector short vec_eqv (vector bool short, vector short);
  vector short vec_eqv (vector short, vector bool short);
  vector unsigned short vec_eqv (vector unsigned short, vector unsigned short);
  vector unsigned short vec_eqv (vector bool unsigned short,
                                 vector unsigned short);
  vector unsigned short vec_eqv (vector unsigned short,
                                 vector bool unsigned short);
  vector signed char vec_eqv (vector signed char, vector signed char);
  vector signed char vec_eqv (vector bool signed char, vector signed char);
  vector signed char vec_eqv (vector signed char, vector bool signed char);
  vector unsigned char vec_eqv (vector unsigned char, vector unsigned char);
  vector unsigned char vec_eqv (vector bool unsigned char, vector unsigned char);
  vector unsigned char vec_eqv (vector unsigned char, vector bool unsigned char);

  vector long long vec_max (vector long long, vector long long);
  vector unsigned long long vec_max (vector unsigned long long,
                                     vector unsigned long long);

  vector signed int vec_mergee (vector signed int, vector signed int);
  vector unsigned int vec_mergee (vector unsigned int, vector unsigned int);
  vector bool int vec_mergee (vector bool int, vector bool int);

  vector signed int vec_mergeo (vector signed int, vector signed int);
  vector unsigned int vec_mergeo (vector unsigned int, vector unsigned int);
  vector bool int vec_mergeo (vector bool int, vector bool int);

  vector long long vec_min (vector long long, vector long long);
  vector unsigned long long vec_min (vector unsigned long long,
                                     vector unsigned long long);

  vector long long vec_nand (vector long long, vector long long);
  vector long long vec_nand (vector bool long long, vector long long);
  vector long long vec_nand (vector long long, vector bool long long);
  vector unsigned long long vec_nand (vector unsigned long long,
                                      vector unsigned long long);
  vector unsigned long long vec_nand (vector bool long long,
                                     vector unsigned long long);
  vector unsigned long long vec_nand (vector unsigned long long,
                                      vector bool long long);
  vector int vec_nand (vector int, vector int);
  vector int vec_nand (vector bool int, vector int);
  vector int vec_nand (vector int, vector bool int);
  vector unsigned int vec_nand (vector unsigned int, vector unsigned int);
  vector unsigned int vec_nand (vector bool unsigned int,
                                vector unsigned int);
  vector unsigned int vec_nand (vector unsigned int,
                                vector bool unsigned int);
  vector short vec_nand (vector short, vector short);
  vector short vec_nand (vector bool short, vector short);
  vector short vec_nand (vector short, vector bool short);
  vector unsigned short vec_nand (vector unsigned short, vector unsigned short);
  vector unsigned short vec_nand (vector bool unsigned short,
                                  vector unsigned short);
  vector unsigned short vec_nand (vector unsigned short,
                                  vector bool unsigned short);
  vector signed char vec_nand (vector signed char, vector signed char);
  vector signed char vec_nand (vector bool signed char, vector signed char);
  vector signed char vec_nand (vector signed char, vector bool signed char);
  vector unsigned char vec_nand (vector unsigned char, vector unsigned char);
  vector unsigned char vec_nand (vector bool unsigned char, vector unsigned char);
  vector unsigned char vec_nand (vector unsigned char, vector bool unsigned char);

  vector long long vec_orc (vector long long, vector long long);
  vector long long vec_orc (vector bool long long, vector long long);
  vector long long vec_orc (vector long long, vector bool long long);
  vector unsigned long long vec_orc (vector unsigned long long,
                                     vector unsigned long long);
  vector unsigned long long vec_orc (vector bool long long,
                                     vector unsigned long long);
  vector unsigned long long vec_orc (vector unsigned long long,
                                     vector bool long long);
  vector int vec_orc (vector int, vector int);
  vector int vec_orc (vector bool int, vector int);
  vector int vec_orc (vector int, vector bool int);
  vector unsigned int vec_orc (vector unsigned int, vector unsigned int);
  vector unsigned int vec_orc (vector bool unsigned int,
                               vector unsigned int);
  vector unsigned int vec_orc (vector unsigned int,
                               vector bool unsigned int);
  vector short vec_orc (vector short, vector short);
  vector short vec_orc (vector bool short, vector short);
  vector short vec_orc (vector short, vector bool short);
  vector unsigned short vec_orc (vector unsigned short, vector unsigned short);
  vector unsigned short vec_orc (vector bool unsigned short,
                                 vector unsigned short);
  vector unsigned short vec_orc (vector unsigned short,
                                 vector bool unsigned short);
  vector signed char vec_orc (vector signed char, vector signed char);
  vector signed char vec_orc (vector bool signed char, vector signed char);
  vector signed char vec_orc (vector signed char, vector bool signed char);
  vector unsigned char vec_orc (vector unsigned char, vector unsigned char);
  vector unsigned char vec_orc (vector bool unsigned char, vector unsigned char);
  vector unsigned char vec_orc (vector unsigned char, vector bool unsigned char);

  vector int vec_pack (vector long long, vector long long);
  vector unsigned int vec_pack (vector unsigned long long,
                                vector unsigned long long);
  vector bool int vec_pack (vector bool long long, vector bool long long);

  vector int vec_packs (vector long long, vector long long);
  vector unsigned int vec_packs (vector unsigned long long,
                                 vector unsigned long long);

  vector unsigned int vec_packsu (vector long long, vector long long);
  vector unsigned int vec_packsu (vector unsigned long long,
                                  vector unsigned long long);

  vector long long vec_rl (vector long long,
                           vector unsigned long long);
  vector long long vec_rl (vector unsigned long long,
                           vector unsigned long long);

  vector long long vec_sl (vector long long, vector unsigned long long);
  vector long long vec_sl (vector unsigned long long,
                           vector unsigned long long);

  vector long long vec_sr (vector long long, vector unsigned long long);
  vector unsigned long long char vec_sr (vector unsigned long long,
                                         vector unsigned long long);

  vector long long vec_sra (vector long long, vector unsigned long long);
  vector unsigned long long vec_sra (vector unsigned long long,
                                     vector unsigned long long);

  vector long long vec_sub (vector long long, vector long long);
  vector unsigned long long vec_sub (vector unsigned long long,
                                     vector unsigned long long);

  vector long long vec_unpackh (vector int);
  vector unsigned long long vec_unpackh (vector unsigned int);

  vector long long vec_unpackl (vector int);
  vector unsigned long long vec_unpackl (vector unsigned int);

  vector long long vec_vaddudm (vector long long, vector long long);
  vector long long vec_vaddudm (vector bool long long, vector long long);
  vector long long vec_vaddudm (vector long long, vector bool long long);
  vector unsigned long long vec_vaddudm (vector unsigned long long,
                                         vector unsigned long long);
  vector unsigned long long vec_vaddudm (vector bool unsigned long long,
                                         vector unsigned long long);
  vector unsigned long long vec_vaddudm (vector unsigned long long,
                                         vector bool unsigned long long);

  vector long long vec_vbpermq (vector signed char, vector signed char);
  vector long long vec_vbpermq (vector unsigned char, vector unsigned char);

  vector long long vec_cntlz (vector long long);
  vector unsigned long long vec_cntlz (vector unsigned long long);
  vector int vec_cntlz (vector int);
  vector unsigned int vec_cntlz (vector int);
  vector short vec_cntlz (vector short);
  vector unsigned short vec_cntlz (vector unsigned short);
  vector signed char vec_cntlz (vector signed char);
  vector unsigned char vec_cntlz (vector unsigned char);

  vector long long vec_vclz (vector long long);
  vector unsigned long long vec_vclz (vector unsigned long long);
  vector int vec_vclz (vector int);
  vector unsigned int vec_vclz (vector int);
  vector short vec_vclz (vector short);
  vector unsigned short vec_vclz (vector unsigned short);
  vector signed char vec_vclz (vector signed char);
  vector unsigned char vec_vclz (vector unsigned char);

  vector signed char vec_vclzb (vector signed char);
  vector unsigned char vec_vclzb (vector unsigned char);

  vector long long vec_vclzd (vector long long);
  vector unsigned long long vec_vclzd (vector unsigned long long);

  vector short vec_vclzh (vector short);
  vector unsigned short vec_vclzh (vector unsigned short);

  vector int vec_vclzw (vector int);
  vector unsigned int vec_vclzw (vector int);

  vector signed char vec_vgbbd (vector signed char);
  vector unsigned char vec_vgbbd (vector unsigned char);

  vector long long vec_vmaxsd (vector long long, vector long long);

  vector unsigned long long vec_vmaxud (vector unsigned long long,
                                        unsigned vector long long);

  vector long long vec_vminsd (vector long long, vector long long);

  vector unsigned long long vec_vminud (vector long long,
                                        vector long long);

  vector int vec_vpksdss (vector long long, vector long long);
  vector unsigned int vec_vpksdss (vector long long, vector long long);

  vector unsigned int vec_vpkudus (vector unsigned long long,
                                   vector unsigned long long);

  vector int vec_vpkudum (vector long long, vector long long);
  vector unsigned int vec_vpkudum (vector unsigned long long,
                                   vector unsigned long long);
  vector bool int vec_vpkudum (vector bool long long, vector bool long long);

  vector long long vec_vpopcnt (vector long long);
  vector unsigned long long vec_vpopcnt (vector unsigned long long);
  vector int vec_vpopcnt (vector int);
  vector unsigned int vec_vpopcnt (vector int);
  vector short vec_vpopcnt (vector short);
  vector unsigned short vec_vpopcnt (vector unsigned short);
  vector signed char vec_vpopcnt (vector signed char);
  vector unsigned char vec_vpopcnt (vector unsigned char);

  vector signed char vec_vpopcntb (vector signed char);
  vector unsigned char vec_vpopcntb (vector unsigned char);

  vector long long vec_vpopcntd (vector long long);
  vector unsigned long long vec_vpopcntd (vector unsigned long long);

  vector short vec_vpopcnth (vector short);
  vector unsigned short vec_vpopcnth (vector unsigned short);

  vector int vec_vpopcntw (vector int);
  vector unsigned int vec_vpopcntw (vector int);

  vector long long vec_vrld (vector long long, vector unsigned long long);
  vector unsigned long long vec_vrld (vector unsigned long long,
                                      vector unsigned long long);

  vector long long vec_vsld (vector long long, vector unsigned long long);
  vector long long vec_vsld (vector unsigned long long,
                             vector unsigned long long);

  vector long long vec_vsrad (vector long long, vector unsigned long long);
  vector unsigned long long vec_vsrad (vector unsigned long long,
                                       vector unsigned long long);

  vector long long vec_vsrd (vector long long, vector unsigned long long);
  vector unsigned long long char vec_vsrd (vector unsigned long long,
                                           vector unsigned long long);

  vector long long vec_vsubudm (vector long long, vector long long);
  vector long long vec_vsubudm (vector bool long long, vector long long);
  vector long long vec_vsubudm (vector long long, vector bool long long);
  vector unsigned long long vec_vsubudm (vector unsigned long long,
                                         vector unsigned long long);
  vector unsigned long long vec_vsubudm (vector bool long long,
                                         vector unsigned long long);
  vector unsigned long long vec_vsubudm (vector unsigned long long,
                                         vector bool long long);

  vector long long vec_vupkhsw (vector int);
  vector unsigned long long vec_vupkhsw (vector unsigned int);

  vector long long vec_vupklsw (vector int);
  vector unsigned long long vec_vupklsw (vector int);

If the ISA 2.07 additions to the vector/scalar (power8-vector)
instruction set is available, the following additional functions are
available for 64-bit targets.  New vector types
(``vector __int128_t`` and ``vector __uint128_t``) are available
to hold the ``__int128_t`` and ``__uint128_t`` types to use these
builtins.

The normal vector extract, and set operations work on
``vector __int128_t`` and ``vector __uint128_t`` types,
but the index value must be 0.

.. code-block:: c++

  vector __int128_t vec_vaddcuq (vector __int128_t, vector __int128_t);
  vector __uint128_t vec_vaddcuq (vector __uint128_t, vector __uint128_t);

  vector __int128_t vec_vadduqm (vector __int128_t, vector __int128_t);
  vector __uint128_t vec_vadduqm (vector __uint128_t, vector __uint128_t);

  vector __int128_t vec_vaddecuq (vector __int128_t, vector __int128_t,
                                  vector __int128_t);
  vector __uint128_t vec_vaddecuq (vector __uint128_t, vector __uint128_t, 
                                   vector __uint128_t);

  vector __int128_t vec_vaddeuqm (vector __int128_t, vector __int128_t,
                                  vector __int128_t);
  vector __uint128_t vec_vaddeuqm (vector __uint128_t, vector __uint128_t, 
                                   vector __uint128_t);

  vector __int128_t vec_vsubecuq (vector __int128_t, vector __int128_t,
                                  vector __int128_t);
  vector __uint128_t vec_vsubecuq (vector __uint128_t, vector __uint128_t, 
                                   vector __uint128_t);

  vector __int128_t vec_vsubeuqm (vector __int128_t, vector __int128_t,
                                  vector __int128_t);
  vector __uint128_t vec_vsubeuqm (vector __uint128_t, vector __uint128_t,
                                   vector __uint128_t);

  vector __int128_t vec_vsubcuq (vector __int128_t, vector __int128_t);
  vector __uint128_t vec_vsubcuq (vector __uint128_t, vector __uint128_t);

  __int128_t vec_vsubuqm (__int128_t, __int128_t);
  __uint128_t vec_vsubuqm (__uint128_t, __uint128_t);

  vector __int128_t __builtin_bcdadd (vector __int128_t, vector__int128_t);
  int __builtin_bcdadd_lt (vector __int128_t, vector__int128_t);
  int __builtin_bcdadd_eq (vector __int128_t, vector__int128_t);
  int __builtin_bcdadd_gt (vector __int128_t, vector__int128_t);
  int __builtin_bcdadd_ov (vector __int128_t, vector__int128_t);
  vector __int128_t bcdsub (vector __int128_t, vector__int128_t);
  int __builtin_bcdsub_lt (vector __int128_t, vector__int128_t);
  int __builtin_bcdsub_eq (vector __int128_t, vector__int128_t);
  int __builtin_bcdsub_gt (vector __int128_t, vector__int128_t);
  int __builtin_bcdsub_ov (vector __int128_t, vector__int128_t);

If the cryptographic instructions are enabled (:option:`-mcrypto` or
:option:`-mcpu=power8`), the following builtins are enabled.

.. code-block:: c++

  vector unsigned long long __builtin_crypto_vsbox (vector unsigned long long);

  vector unsigned long long __builtin_crypto_vcipher (vector unsigned long long,
                                                      vector unsigned long long);

  vector unsigned long long __builtin_crypto_vcipherlast
                                       (vector unsigned long long,
                                        vector unsigned long long);

  vector unsigned long long __builtin_crypto_vncipher (vector unsigned long long,
                                                       vector unsigned long long);

  vector unsigned long long __builtin_crypto_vncipherlast
                                       (vector unsigned long long,
                                        vector unsigned long long);

  vector unsigned char __builtin_crypto_vpermxor (vector unsigned char,
                                                  vector unsigned char,
                                                  vector unsigned char);

  vector unsigned short __builtin_crypto_vpermxor (vector unsigned short,
                                                   vector unsigned short,
                                                   vector unsigned short);

  vector unsigned int __builtin_crypto_vpermxor (vector unsigned int,
                                                 vector unsigned int,
                                                 vector unsigned int);

  vector unsigned long long __builtin_crypto_vpermxor (vector unsigned long long,
                                                       vector unsigned long long,
                                                       vector unsigned long long);

  vector unsigned char __builtin_crypto_vpmsumb (vector unsigned char,
                                                 vector unsigned char);

  vector unsigned short __builtin_crypto_vpmsumb (vector unsigned short,
                                                  vector unsigned short);

  vector unsigned int __builtin_crypto_vpmsumb (vector unsigned int,
                                                vector unsigned int);

  vector unsigned long long __builtin_crypto_vpmsumb (vector unsigned long long,
                                                      vector unsigned long long);

  vector unsigned long long __builtin_crypto_vshasigmad
                                 (vector unsigned long long, int, int);

  vector unsigned int __builtin_crypto_vshasigmaw (vector unsigned int,
                                                   int, int);

The second argument to the ``__builtin_crypto_vshasigmad`` and
``__builtin_crypto_vshasigmaw`` builtin functions must be a constant
integer that is 0 or 1.  The third argument to these builtin functions
must be a constant integer in the range of 0 to 15.

:: _powerpc-hardware-transactional-memory-built-in-functions:

PowerPC Hardware Transactional Memory Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GCC provides two interfaces for accessing the Hardware Transactional
Memory (HTM) instructions available on some of the PowerPC family
of processors (eg, POWER8).  The two interfaces come in a low level
interface, consisting of built-in functions specific to PowerPC and a
higher level interface consisting of inline functions that are common
between PowerPC and S/390.

PowerPC HTM Low Level Built-in Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following low level built-in functions are available with
:option:`-mhtm` or :option:`-mcpu=CPU` where CPU is 'power8' or later.
They all generate the machine instruction that is part of the name.

The HTM builtins (with the exception of ``__builtin_tbegin``) return
the full 4-bit condition register value set by their associated hardware
instruction.  The header file ``htmintrin.h`` defines some macros that can
be used to decipher the return value.  The ``__builtin_tbegin`` builtin
returns a simple true or false value depending on whether a transaction was
successfully started or not.  The arguments of the builtins match exactly the
type and order of the associated hardware instruction's operands, except for
the ``__builtin_tcheck`` builtin, which does not take any input arguments.
Refer to the ISA manual for a description of each instruction's operands.

.. code-block:: c++

  unsigned int __builtin_tbegin (unsigned int)
  unsigned int __builtin_tend (unsigned int)

  unsigned int __builtin_tabort (unsigned int)
  unsigned int __builtin_tabortdc (unsigned int, unsigned int, unsigned int)
  unsigned int __builtin_tabortdci (unsigned int, unsigned int, int)
  unsigned int __builtin_tabortwc (unsigned int, unsigned int, unsigned int)
  unsigned int __builtin_tabortwci (unsigned int, unsigned int, int)

  unsigned int __builtin_tcheck (void)
  unsigned int __builtin_treclaim (unsigned int)
  unsigned int __builtin_trechkpt (void)
  unsigned int __builtin_tsr (unsigned int)

In addition to the above HTM built-ins, we have added built-ins for
some common extended mnemonics of the HTM instructions:

.. code-block:: c++

  unsigned int __builtin_tendall (void)
  unsigned int __builtin_tresume (void)
  unsigned int __builtin_tsuspend (void)

The following set of built-in functions are available to gain access
to the HTM specific special purpose registers.

.. code-block:: c++

  unsigned long __builtin_get_texasr (void)
  unsigned long __builtin_get_texasru (void)
  unsigned long __builtin_get_tfhar (void)
  unsigned long __builtin_get_tfiar (void)

  void __builtin_set_texasr (unsigned long);
  void __builtin_set_texasru (unsigned long);
  void __builtin_set_tfhar (unsigned long);
  void __builtin_set_tfiar (unsigned long);

Example usage of these low level built-in functions may look like:

.. code-block:: c++

  #include <htmintrin.h>

  int num_retries = 10;

  while (1)
    {
      if (__builtin_tbegin (0))
        {
          /* Transaction State Initiated.  */
          if (is_locked (lock))
            __builtin_tabort (0);
          ... transaction code...
          __builtin_tend (0);
          break;
        }
      else
        {
          /* Transaction State Failed.  Use locks if the transaction
             failure is "persistent" or we've tried too many times.  */
          if (num_retries-- <= 0
              || _TEXASRU_FAILURE_PERSISTENT (__builtin_get_texasru ()))
            {
              acquire_lock (lock);
              ... non transactional fallback path...
              release_lock (lock);
              break;
            }
        }
    }

One final built-in function has been added that returns the value of
the 2-bit Transaction State field of the Machine Status Register (MSR)
as stored in ``CR0``.

.. code-block:: c++

  unsigned long __builtin_ttest (void)

This built-in can be used to determine the current transaction state
using the following code example:

.. code-block:: c++

  #include <htmintrin.h>

  unsigned char tx_state = _HTM_STATE (__builtin_ttest ());

  if (tx_state == _HTM_TRANSACTIONAL)
    {
      /* Code to use in transactional state.  */
    }
  else if (tx_state == _HTM_NONTRANSACTIONAL)
    {
      /* Code to use in non-transactional state.  */
    }
  else if (tx_state == _HTM_SUSPENDED)
    {
      /* Code to use in transaction suspended state.  */
    }

PowerPC HTM High Level Inline Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following high level HTM interface is made available by including
``<htmxlintrin.h>`` and using :option:`-mhtm` or :option:`-mcpu=CPU`
where CPU is 'power8' or later.  This interface is common between PowerPC
and S/390, allowing users to write one HTM source implementation that
can be compiled and executed on either system.

.. code-block:: c++

  long __TM_simple_begin (void)
  long __TM_begin (void* const TM_buff)
  long __TM_end (void)
  void __TM_abort (void)
  void __TM_named_abort (unsigned char const code)
  void __TM_resume (void)
  void __TM_suspend (void)

  long __TM_is_user_abort (void* const TM_buff)
  long __TM_is_named_user_abort (void* const TM_buff, unsigned char *code)
  long __TM_is_illegal (void* const TM_buff)
  long __TM_is_footprint_exceeded (void* const TM_buff)
  long __TM_nesting_depth (void* const TM_buff)
  long __TM_is_nested_too_deep(void* const TM_buff)
  long __TM_is_conflict(void* const TM_buff)
  long __TM_is_failure_persistent(void* const TM_buff)
  long __TM_failure_address(void* const TM_buff)
  long long __TM_failure_code(void* const TM_buff)

Using these common set of HTM inline functions, we can create
a more portable version of the HTM example in the previous
section that will work on either PowerPC or S/390:

.. code-block:: c++

  #include <htmxlintrin.h>

  int num_retries = 10;
  TM_buff_type TM_buff;

  while (1)
    {
      if (__TM_begin (TM_buff) == _HTM_TBEGIN_STARTED)
        {
          /* Transaction State Initiated.  */
          if (is_locked (lock))
            __TM_abort ();
          ... transaction code...
          __TM_end ();
          break;
        }
      else
        {
          /* Transaction State Failed.  Use locks if the transaction
             failure is "persistent" or we've tried too many times.  */
          if (num_retries-- <= 0
              || __TM_is_failure_persistent (TM_buff))
            {
              acquire_lock (lock);
              ... non transactional fallback path...
              release_lock (lock);
              break;
            }
        }
    }

:: _rx-built-in-functions:

RX Built-in Functions
^^^^^^^^^^^^^^^^^^^^^

GCC supports some of the RX instructions which cannot be expressed in
the C programming language via the use of built-in functions.  The
following functions are supported:

.. index:: __builtin_rx_brk

  Built-in Function  void __builtin_rx_brk (void)
Generates the ``brk`` machine instruction.

.. index:: __builtin_rx_clrpsw

  Built-in Function  void __builtin_rx_clrpsw (int)
Generates the ``clrpsw`` machine instruction to clear the specified
bit in the processor status word.

.. index:: __builtin_rx_int

  Built-in Function  void __builtin_rx_int (int)
Generates the ``int`` machine instruction to generate an interrupt
with the specified value.

.. index:: __builtin_rx_machi

  Built-in Function  void __builtin_rx_machi (int, int)
Generates the ``machi`` machine instruction to add the result of
multiplying the top 16 bits of the two arguments into the
accumulator.

.. index:: __builtin_rx_maclo

  Built-in Function  void __builtin_rx_maclo (int, int)
Generates the ``maclo`` machine instruction to add the result of
multiplying the bottom 16 bits of the two arguments into the
accumulator.

.. index:: __builtin_rx_mulhi

  Built-in Function  void __builtin_rx_mulhi (int, int)
Generates the ``mulhi`` machine instruction to place the result of
multiplying the top 16 bits of the two arguments into the
accumulator.

.. index:: __builtin_rx_mullo

  Built-in Function  void __builtin_rx_mullo (int, int)
Generates the ``mullo`` machine instruction to place the result of
multiplying the bottom 16 bits of the two arguments into the
accumulator.

.. index:: __builtin_rx_mvfachi

  Built-in Function  int  __builtin_rx_mvfachi (void)
Generates the ``mvfachi`` machine instruction to read the top
32 bits of the accumulator.

.. index:: __builtin_rx_mvfacmi

  Built-in Function  int  __builtin_rx_mvfacmi (void)
Generates the ``mvfacmi`` machine instruction to read the middle
32 bits of the accumulator.

.. index:: __builtin_rx_mvfc

  Built-in Function  int __builtin_rx_mvfc (int)
Generates the ``mvfc`` machine instruction which reads the control
register specified in its argument and returns its value.

.. index:: __builtin_rx_mvtachi

  Built-in Function  void __builtin_rx_mvtachi (int)
Generates the ``mvtachi`` machine instruction to set the top
32 bits of the accumulator.

.. index:: __builtin_rx_mvtaclo

  Built-in Function  void __builtin_rx_mvtaclo (int)
Generates the ``mvtaclo`` machine instruction to set the bottom
32 bits of the accumulator.

.. index:: __builtin_rx_mvtc

  Built-in Function  void __builtin_rx_mvtc (int reg, int val)
Generates the ``mvtc`` machine instruction which sets control
register number ``reg`` to ``val``.

.. index:: __builtin_rx_mvtipl

  Built-in Function  void __builtin_rx_mvtipl (int)
Generates the ``mvtipl`` machine instruction set the interrupt
priority level.

.. index:: __builtin_rx_racw

  Built-in Function  void __builtin_rx_racw (int)
Generates the ``racw`` machine instruction to round the accumulator
according to the specified mode.

.. index:: __builtin_rx_revw

  Built-in Function  int __builtin_rx_revw (int)
Generates the ``revw`` machine instruction which swaps the bytes in
the argument so that bits 0-7 now occupy bits 8-15 and vice versa,
and also bits 16-23 occupy bits 24-31 and vice versa.

.. index:: __builtin_rx_rmpa

  Built-in Function  void __builtin_rx_rmpa (void)
Generates the ``rmpa`` machine instruction which initiates a
repeated multiply and accumulate sequence.

.. index:: __builtin_rx_round

  Built-in Function  void __builtin_rx_round (float)
Generates the ``round`` machine instruction which returns the
floating-point argument rounded according to the current rounding mode
set in the floating-point status word register.

.. index:: __builtin_rx_sat

  Built-in Function  int __builtin_rx_sat (int)
Generates the ``sat`` machine instruction which returns the
saturated value of the argument.

.. index:: __builtin_rx_setpsw

  Built-in Function  void __builtin_rx_setpsw (int)
Generates the ``setpsw`` machine instruction to set the specified
bit in the processor status word.

.. index:: __builtin_rx_wait

  Built-in Function  void __builtin_rx_wait (void)
Generates the ``wait`` machine instruction.

:: _s/390-system-z-built-in-functions:

S/390 System z Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: __builtin_tbegin

  Built-in Function int __builtin_tbegin (void*)
Generates the ``tbegin`` machine instruction starting a
non-constraint hardware transaction.  If the parameter is non-NULL the
memory area is used to store the transaction diagnostic buffer and
will be passed as first operand to ``tbegin``.  This buffer can be
defined using the ``struct __htm_tdb`` C struct defined in
``htmintrin.h`` and must reside on a double-word boundary.  The
second tbegin operand is set to ``0xff0c``. This enables
save/restore of all GPRs and disables aborts for FPR and AR
manipulations inside the transaction body.  The condition code set by
the tbegin instruction is returned as integer value.  The tbegin
instruction by definition overwrites the content of all FPRs.  The
compiler will generate code which saves and restores the FPRs.  For
soft-float code it is recommended to used the ``*_nofloat``
variant.  In order to prevent a TDB from being written it is required
to pass an constant zero value as parameter.  Passing the zero value
through a variable is not sufficient.  Although modifications of
access registers inside the transaction will not trigger an
transaction abort it is not supported to actually modify them.  Access
registers do not get saved when entering a transaction. They will have
undefined state when reaching the abort code.

Macros for the possible return codes of tbegin are defined in the
``htmintrin.h`` header file:

_HTM_TBEGIN_STARTED
  ``tbegin`` has been executed as part of normal processing.  The
  transaction body is supposed to be executed.

_HTM_TBEGIN_INDETERMINATE
  The transaction was aborted due to an indeterminate condition which
  might be persistent.

_HTM_TBEGIN_TRANSIENT
  The transaction aborted due to a transient failure.  The transaction
  should be re-executed in that case.

_HTM_TBEGIN_PERSISTENT
  The transaction aborted due to a persistent failure.  Re-execution
  under same circumstances will not be productive.

.. index:: _HTM_FIRST_USER_ABORT_CODE

  Macro _HTM_FIRST_USER_ABORT_CODE
The ``_HTM_FIRST_USER_ABORT_CODE`` defined in ``htmintrin.h``
specifies the first abort code which can be used for
``__builtin_tabort``.  Values below this threshold are reserved for
machine use.

.. index:: struct __htm_tdb

  Data type struct __htm_tdb
The ``struct __htm_tdb`` defined in ``htmintrin.h`` describes
the structure of the transaction diagnostic block as specified in the
Principles of Operation manual chapter 5-91.

.. index:: __builtin_tbegin_nofloat

  Built-in Function int __builtin_tbegin_nofloat (void*)
Same as ``__builtin_tbegin`` but without FPR saves and restores.
Using this variant in code making use of FPRs will leave the FPRs in
undefined state when entering the transaction abort handler code.

.. index:: __builtin_tbegin_retry

  Built-in Function int __builtin_tbegin_retry (void*, int)
In addition to ``__builtin_tbegin`` a loop for transient failures
is generated.  If tbegin returns a condition code of 2 the transaction
will be retried as often as specified in the second argument.  The
perform processor assist instruction is used to tell the CPU about the
number of fails so far.

.. index:: __builtin_tbegin_retry_nofloat

  Built-in Function int __builtin_tbegin_retry_nofloat (void*, int)
Same as ``__builtin_tbegin_retry`` but without FPR saves and
restores.  Using this variant in code making use of FPRs will leave
the FPRs in undefined state when entering the transaction abort
handler code.

.. index:: __builtin_tbeginc

  Built-in Function void __builtin_tbeginc (void)
Generates the ``tbeginc`` machine instruction starting a constraint
hardware transaction.  The second operand is set to ``0xff08``.

.. index:: __builtin_tend

  Built-in Function int __builtin_tend (void)
Generates the ``tend`` machine instruction finishing a transaction
and making the changes visible to other threads.  The condition code
generated by tend is returned as integer value.

.. index:: __builtin_tabort

  Built-in Function void __builtin_tabort (int)
Generates the ``tabort`` machine instruction with the specified
abort code.  Abort codes from 0 through 255 are reserved and will
result in an error message.

.. index:: __builtin_tx_assist

  Built-in Function void __builtin_tx_assist (int)
Generates the ``ppa rX,rY,1`` machine instruction.  Where the
integer parameter is loaded into rX and a value of zero is loaded into
rY.  The integer parameter specifies the number of times the
transaction repeatedly aborted.

.. index:: __builtin_tx_nesting_depth

  Built-in Function int __builtin_tx_nesting_depth (void)
Generates the ``etnd`` machine instruction.  The current nesting
depth is returned as integer value.  For a nesting depth of 0 the code
is not executed as part of an transaction.

.. index:: __builtin_non_tx_store

  Built-in Function void __builtin_non_tx_store (uint64_t *, uint64_t)

Generates the ``ntstg`` machine instruction.  The second argument
is written to the first arguments location.  The store operation will
not be rolled-back in case of an transaction abort.

:: _sh-built-in-functions:

SH Built-in Functions
^^^^^^^^^^^^^^^^^^^^^

The following built-in functions are supported on the SH1, SH2, SH3 and SH4
families of processors:

.. index:: __builtin_set_thread_pointer

  Built-in Function void __builtin_set_thread_pointer (void *``ptr``)
Sets the GBR register to the specified value ``ptr``.  This is usually
used by system code that manages threads and execution contexts.  The compiler
normally does not generate code that modifies the contents of GBR and
thus the value is preserved across function calls.  Changing the GBR
value in user code must be done with caution, since the compiler might use
GBR in order to access thread local variables.

.. index:: __builtin_thread_pointer

  Built-in Function void * __builtin_thread_pointer (void)
Returns the value that is currently set in the GBR register.
Memory loads and stores that use the thread pointer as a base address are
turned into GBR based displacement loads and stores, if possible.
For example:

.. code-block:: c++

  struct my_tcb
  {
     int a, b, c, d, e;
  };

  int get_tcb_value (void)
  {
    // Generate mov.l @(8,gbr),r0 instruction
    return ((my_tcb*)__builtin_thread_pointer ())->c;
  }

.. index:: __builtin_sh_get_fpscr

  Built-in Function unsigned int __builtin_sh_get_fpscr (void)
Returns the value that is currently set in the FPSCR register.

.. index:: __builtin_sh_set_fpscr

  Built-in Function void __builtin_sh_set_fpscr (unsigned int ``val``)
Sets the FPSCR register to the specified value ``val``, while
preserving the current values of the FR, SZ and PR bits.

:: _sparc-vis-built-in-functions:

SPARC VIS Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GCC supports SIMD operations on the SPARC using both the generic vector
extensions (Vector Extensions) as well as built-in functions for
the SPARC Visual Instruction Set (VIS).  When you use the :option:`-mvis`
switch, the VIS extension is exposed as the following built-in functions:

.. code-block:: c++

  typedef int v1si __attribute__ ((vector_size (4)));
  typedef int v2si __attribute__ ((vector_size (8)));
  typedef short v4hi __attribute__ ((vector_size (8)));
  typedef short v2hi __attribute__ ((vector_size (4)));
  typedef unsigned char v8qi __attribute__ ((vector_size (8)));
  typedef unsigned char v4qi __attribute__ ((vector_size (4)));

  void __builtin_vis_write_gsr (int64_t);
  int64_t __builtin_vis_read_gsr (void);

  void * __builtin_vis_alignaddr (void *, long);
  void * __builtin_vis_alignaddrl (void *, long);
  int64_t __builtin_vis_faligndatadi (int64_t, int64_t);
  v2si __builtin_vis_faligndatav2si (v2si, v2si);
  v4hi __builtin_vis_faligndatav4hi (v4si, v4si);
  v8qi __builtin_vis_faligndatav8qi (v8qi, v8qi);

  v4hi __builtin_vis_fexpand (v4qi);

  v4hi __builtin_vis_fmul8x16 (v4qi, v4hi);
  v4hi __builtin_vis_fmul8x16au (v4qi, v2hi);
  v4hi __builtin_vis_fmul8x16al (v4qi, v2hi);
  v4hi __builtin_vis_fmul8sux16 (v8qi, v4hi);
  v4hi __builtin_vis_fmul8ulx16 (v8qi, v4hi);
  v2si __builtin_vis_fmuld8sux16 (v4qi, v2hi);
  v2si __builtin_vis_fmuld8ulx16 (v4qi, v2hi);

  v4qi __builtin_vis_fpack16 (v4hi);
  v8qi __builtin_vis_fpack32 (v2si, v8qi);
  v2hi __builtin_vis_fpackfix (v2si);
  v8qi __builtin_vis_fpmerge (v4qi, v4qi);

  int64_t __builtin_vis_pdist (v8qi, v8qi, int64_t);

  long __builtin_vis_edge8 (void *, void *);
  long __builtin_vis_edge8l (void *, void *);
  long __builtin_vis_edge16 (void *, void *);
  long __builtin_vis_edge16l (void *, void *);
  long __builtin_vis_edge32 (void *, void *);
  long __builtin_vis_edge32l (void *, void *);

  long __builtin_vis_fcmple16 (v4hi, v4hi);
  long __builtin_vis_fcmple32 (v2si, v2si);
  long __builtin_vis_fcmpne16 (v4hi, v4hi);
  long __builtin_vis_fcmpne32 (v2si, v2si);
  long __builtin_vis_fcmpgt16 (v4hi, v4hi);
  long __builtin_vis_fcmpgt32 (v2si, v2si);
  long __builtin_vis_fcmpeq16 (v4hi, v4hi);
  long __builtin_vis_fcmpeq32 (v2si, v2si);

  v4hi __builtin_vis_fpadd16 (v4hi, v4hi);
  v2hi __builtin_vis_fpadd16s (v2hi, v2hi);
  v2si __builtin_vis_fpadd32 (v2si, v2si);
  v1si __builtin_vis_fpadd32s (v1si, v1si);
  v4hi __builtin_vis_fpsub16 (v4hi, v4hi);
  v2hi __builtin_vis_fpsub16s (v2hi, v2hi);
  v2si __builtin_vis_fpsub32 (v2si, v2si);
  v1si __builtin_vis_fpsub32s (v1si, v1si);

  long __builtin_vis_array8 (long, long);
  long __builtin_vis_array16 (long, long);
  long __builtin_vis_array32 (long, long);

When you use the :option:`-mvis2` switch, the VIS version 2.0 built-in
functions also become available:

.. code-block:: c++

  long __builtin_vis_bmask (long, long);
  int64_t __builtin_vis_bshuffledi (int64_t, int64_t);
  v2si __builtin_vis_bshufflev2si (v2si, v2si);
  v4hi __builtin_vis_bshufflev2si (v4hi, v4hi);
  v8qi __builtin_vis_bshufflev2si (v8qi, v8qi);

  long __builtin_vis_edge8n (void *, void *);
  long __builtin_vis_edge8ln (void *, void *);
  long __builtin_vis_edge16n (void *, void *);
  long __builtin_vis_edge16ln (void *, void *);
  long __builtin_vis_edge32n (void *, void *);
  long __builtin_vis_edge32ln (void *, void *);

When you use the :option:`-mvis3` switch, the VIS version 3.0 built-in
functions also become available:

.. code-block:: c++

  void __builtin_vis_cmask8 (long);
  void __builtin_vis_cmask16 (long);
  void __builtin_vis_cmask32 (long);

  v4hi __builtin_vis_fchksm16 (v4hi, v4hi);

  v4hi __builtin_vis_fsll16 (v4hi, v4hi);
  v4hi __builtin_vis_fslas16 (v4hi, v4hi);
  v4hi __builtin_vis_fsrl16 (v4hi, v4hi);
  v4hi __builtin_vis_fsra16 (v4hi, v4hi);
  v2si __builtin_vis_fsll16 (v2si, v2si);
  v2si __builtin_vis_fslas16 (v2si, v2si);
  v2si __builtin_vis_fsrl16 (v2si, v2si);
  v2si __builtin_vis_fsra16 (v2si, v2si);

  long __builtin_vis_pdistn (v8qi, v8qi);

  v4hi __builtin_vis_fmean16 (v4hi, v4hi);

  int64_t __builtin_vis_fpadd64 (int64_t, int64_t);
  int64_t __builtin_vis_fpsub64 (int64_t, int64_t);

  v4hi __builtin_vis_fpadds16 (v4hi, v4hi);
  v2hi __builtin_vis_fpadds16s (v2hi, v2hi);
  v4hi __builtin_vis_fpsubs16 (v4hi, v4hi);
  v2hi __builtin_vis_fpsubs16s (v2hi, v2hi);
  v2si __builtin_vis_fpadds32 (v2si, v2si);
  v1si __builtin_vis_fpadds32s (v1si, v1si);
  v2si __builtin_vis_fpsubs32 (v2si, v2si);
  v1si __builtin_vis_fpsubs32s (v1si, v1si);

  long __builtin_vis_fucmple8 (v8qi, v8qi);
  long __builtin_vis_fucmpne8 (v8qi, v8qi);
  long __builtin_vis_fucmpgt8 (v8qi, v8qi);
  long __builtin_vis_fucmpeq8 (v8qi, v8qi);

  float __builtin_vis_fhadds (float, float);
  double __builtin_vis_fhaddd (double, double);
  float __builtin_vis_fhsubs (float, float);
  double __builtin_vis_fhsubd (double, double);
  float __builtin_vis_fnhadds (float, float);
  double __builtin_vis_fnhaddd (double, double);

  int64_t __builtin_vis_umulxhi (int64_t, int64_t);
  int64_t __builtin_vis_xmulx (int64_t, int64_t);
  int64_t __builtin_vis_xmulxhi (int64_t, int64_t);

:: _spu-built-in-functions:

SPU Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^

GCC provides extensions for the SPU processor as described in the
Sony/Toshiba/IBM SPU Language Extensions Specification, which can be
found at http://cell.scei.co.jp/ or
http://www.ibm.com/developerworks/power/cell/.  GCC's
implementation differs in several ways.

* The optional extension of specifying vector constants in parentheses is
  not supported.

  * A vector initializer requires no cast if the vector constant is of the
  same type as the variable it is initializing.

  * If ``signed`` or ``unsigned`` is omitted, the signedness of the
  vector type is the default signedness of the base type.  The default
  varies depending on the operating system, so a portable program should
  always specify the signedness.

  * By default, the keyword ``__vector`` is added. The macro
  ``vector`` is defined in ``<spu_intrinsics.h>`` and can be
  undefined.

  * GCC allows using a ``typedef`` name as the type specifier for a
  vector type.

  * For C, overloaded functions are implemented with macros so the following
  does not work:

  .. code-block:: c++

      spu_add ((vector signed int){1, 2, 3, 4}, foo);

  Since ``spu_add`` is a macro, the vector constant in the example
  is treated as four separate arguments.  Wrap the entire argument in
  parentheses for this to work.

  * The extended version of ``__builtin_expect`` is not supported.

Note: Only the interface described in the aforementioned
specification is supported. Internally, GCC uses built-in functions to
implement the required functionality, but these are not supported and
are subject to change without notice.

:: _ti-c6x-built-in-functions:

TI C6X Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^

GCC provides intrinsics to access certain instructions of the TI C6X
processors.  These intrinsics, listed below, are available after
inclusion of the ``c6x_intrinsics.h`` header file.  They map directly
to C6X instructions.

.. code-block:: c++

  int _sadd (int, int)
  int _ssub (int, int)
  int _sadd2 (int, int)
  int _ssub2 (int, int)
  long long _mpy2 (int, int)
  long long _smpy2 (int, int)
  int _add4 (int, int)
  int _sub4 (int, int)
  int _saddu4 (int, int)

  int _smpy (int, int)
  int _smpyh (int, int)
  int _smpyhl (int, int)
  int _smpylh (int, int)

  int _sshl (int, int)
  int _subc (int, int)

  int _avg2 (int, int)
  int _avgu4 (int, int)

  int _clrr (int, int)
  int _extr (int, int)
  int _extru (int, int)
  int _abs (int)
  int _abs2 (int)

:: _tile-gx-built-in-functions:

TILE-Gx Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^

GCC provides intrinsics to access every instruction of the TILE-Gx
processor.  The intrinsics are of the form:

.. code-block:: c++

  unsigned long long __insn_``op`` (...)

Where ``op`` is the name of the instruction.  Refer to the ISA manual
for the complete list of instructions.

GCC also provides intrinsics to directly access the network registers.
The intrinsics are:

.. code-block:: c++

  unsigned long long __tile_idn0_receive (void)
  unsigned long long __tile_idn1_receive (void)
  unsigned long long __tile_udn0_receive (void)
  unsigned long long __tile_udn1_receive (void)
  unsigned long long __tile_udn2_receive (void)
  unsigned long long __tile_udn3_receive (void)
  void __tile_idn_send (unsigned long long)
  void __tile_udn_send (unsigned long long)

The intrinsic ``void __tile_network_barrier (void)`` is used to
guarantee that no network operations before it are reordered with
those after it.

:: _tilepro-built-in-functions:

TILEPro Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^

GCC provides intrinsics to access every instruction of the TILEPro
processor.  The intrinsics are of the form:

.. code-block:: c++

  unsigned __insn_``op`` (...)

where ``op`` is the name of the instruction.  Refer to the ISA manual
for the complete list of instructions.

GCC also provides intrinsics to directly access the network registers.
The intrinsics are:

.. code-block:: c++

  unsigned __tile_idn0_receive (void)
  unsigned __tile_idn1_receive (void)
  unsigned __tile_sn_receive (void)
  unsigned __tile_udn0_receive (void)
  unsigned __tile_udn1_receive (void)
  unsigned __tile_udn2_receive (void)
  unsigned __tile_udn3_receive (void)
  void __tile_idn_send (unsigned)
  void __tile_sn_send (unsigned)
  void __tile_udn_send (unsigned)

The intrinsic ``void __tile_network_barrier (void)`` is used to
guarantee that no network operations before it are reordered with
those after it.

:: _x86-built-in-functions:

x86 Built-in Functions
^^^^^^^^^^^^^^^^^^^^^^

These built-in functions are available for the x86-32 and x86-64 family
of computers, depending on the command-line switches used.

If you specify command-line switches such as :option:`-msse`,
the compiler could use the extended instruction sets even if the built-ins
are not used explicitly in the program.  For this reason, applications
that perform run-time CPU detection must compile separate files for each
supported architecture, using the appropriate flags.  In particular,
the file containing the CPU detection code should be compiled without
these options.

The following machine modes are available for use with MMX built-in functions
(Vector Extensions): ``V2SI`` for a vector of two 32-bit integers,
``V4HI`` for a vector of four 16-bit integers, and ``V8QI`` for a
vector of eight 8-bit integers.  Some of the built-in functions operate on
MMX registers as a whole 64-bit entity, these use ``V1DI`` as their mode.

If 3DNow! extensions are enabled, ``V2SF`` is used as a mode for a vector
of two 32-bit floating-point values.

If SSE extensions are enabled, ``V4SF`` is used for a vector of four 32-bit
floating-point values.  Some instructions use a vector of four 32-bit
integers, these use ``V4SI``.  Finally, some instructions operate on an
entire vector register, interpreting it as a 128-bit integer, these use mode
``TI``.

In 64-bit mode, the x86-64 family of processors uses additional built-in
functions for efficient use of ``TF`` (``__float128``) 128-bit
floating point and ``TC`` 128-bit complex floating-point values.

The following floating-point built-in functions are available in 64-bit
mode.  All of them implement the function that is part of the name.

.. code-block:: c++

  __float128 __builtin_fabsq (__float128)
  __float128 __builtin_copysignq (__float128, __float128)

The following built-in function is always available.

void __builtin_ia32_pause (void)
  Generates the ``pause`` machine instruction with a compiler memory
  barrier.

The following floating-point built-in functions are made available in the
64-bit mode.

__float128 __builtin_infq (void)
  Similar to ``__builtin_inf``, except the return type is ``__float128``.

  .. index:: __builtin_infq

__float128 __builtin_huge_valq (void)
  Similar to ``__builtin_huge_val``, except the return type is ``__float128``.

  .. index:: __builtin_huge_valq

The following built-in functions are always available and can be used to
check the target platform type.

.. index:: __builtin_cpu_init

  Built-in Function void __builtin_cpu_init (void)
This function runs the CPU detection code to check the type of CPU and the
features supported.  This built-in function needs to be invoked along with the built-in functions
to check CPU type and features, ``__builtin_cpu_is`` and
``__builtin_cpu_supports``, only when used in a function that is
executed before any constructors are called.  The CPU detection code is
automatically executed in a very high priority constructor.

For example, this function has to be used in ``ifunc`` resolvers that
check for CPU type using the built-in functions ``__builtin_cpu_is``
and ``__builtin_cpu_supports``, or in constructors on targets that
don't support constructor priority.

.. code-block:: c++

  static void (*resolve_memcpy (void)) (void)
  {
    // ifunc resolvers fire before constructors, explicitly call the init
    // function.
    __builtin_cpu_init ();
    if (__builtin_cpu_supports ("ssse3"))
      return ssse3_memcpy; // super fast memcpy with ssse3 instructions.
    else
      return default_memcpy;
  }

  void *memcpy (void *, const void *, size_t)
       __attribute__ ((ifunc ("resolve_memcpy")));

.. index:: __builtin_cpu_is

  Built-in Function int __builtin_cpu_is (const char *``cpuname``)
This function returns a positive integer if the run-time CPU
is of type ``cpuname``
and returns ``0`` otherwise. The following CPU names can be detected:

intel
  Intel CPU.

atom
  Intel Atom CPU.

core2
  Intel Core 2 CPU.

corei7
  Intel Core i7 CPU.

nehalem
  Intel Core i7 Nehalem CPU.

westmere
  Intel Core i7 Westmere CPU.

sandybridge
  Intel Core i7 Sandy Bridge CPU.

amd
  AMD CPU.

amdfam10h
  AMD Family 10h CPU.

barcelona
  AMD Family 10h Barcelona CPU.

shanghai
  AMD Family 10h Shanghai CPU.

istanbul
  AMD Family 10h Istanbul CPU.

btver1
  AMD Family 14h CPU.

amdfam15h
  AMD Family 15h CPU.

bdver1
  AMD Family 15h Bulldozer version 1.

bdver2
  AMD Family 15h Bulldozer version 2.

bdver3
  AMD Family 15h Bulldozer version 3.

bdver4
  AMD Family 15h Bulldozer version 4.

btver2
  AMD Family 16h CPU.

Here is an example:

.. code-block:: c++

  if (__builtin_cpu_is ("corei7"))
    {
       do_corei7 (); // Core i7 specific implementation.
    }
  else
    {
       do_generic (); // Generic implementation.
    }

.. index:: __builtin_cpu_supports

  Built-in Function int __builtin_cpu_supports (const char *``feature``)
This function returns a positive integer if the run-time CPU
supports ``feature``
and returns ``0`` otherwise. The following features can be detected:

cmov
  CMOV instruction.

mmx
  MMX instructions.

popcnt
  POPCNT instruction.

sse
  SSE instructions.

sse2
  SSE2 instructions.

sse3
  SSE3 instructions.

ssse3
  SSSE3 instructions.

sse4.1
  SSE4.1 instructions.

sse4.2
  SSE4.2 instructions.

avx
  AVX instructions.

avx2
  AVX2 instructions.

avx512f
  AVX512F instructions.

Here is an example:

.. code-block:: c++

  if (__builtin_cpu_supports ("popcnt"))
    {
       asm("popcnt %1,%0" : "=r"(count) : "rm"(n) : "cc");
    }
  else
    {
       count = generic_countbits (n); //generic implementation.
    }

The following built-in functions are made available by :option:`-mmmx`.
All of them generate the machine instruction that is part of the name.

.. code-block:: c++

  v8qi __builtin_ia32_paddb (v8qi, v8qi)
  v4hi __builtin_ia32_paddw (v4hi, v4hi)
  v2si __builtin_ia32_paddd (v2si, v2si)
  v8qi __builtin_ia32_psubb (v8qi, v8qi)
  v4hi __builtin_ia32_psubw (v4hi, v4hi)
  v2si __builtin_ia32_psubd (v2si, v2si)
  v8qi __builtin_ia32_paddsb (v8qi, v8qi)
  v4hi __builtin_ia32_paddsw (v4hi, v4hi)
  v8qi __builtin_ia32_psubsb (v8qi, v8qi)
  v4hi __builtin_ia32_psubsw (v4hi, v4hi)
  v8qi __builtin_ia32_paddusb (v8qi, v8qi)
  v4hi __builtin_ia32_paddusw (v4hi, v4hi)
  v8qi __builtin_ia32_psubusb (v8qi, v8qi)
  v4hi __builtin_ia32_psubusw (v4hi, v4hi)
  v4hi __builtin_ia32_pmullw (v4hi, v4hi)
  v4hi __builtin_ia32_pmulhw (v4hi, v4hi)
  di __builtin_ia32_pand (di, di)
  di __builtin_ia32_pandn (di,di)
  di __builtin_ia32_por (di, di)
  di __builtin_ia32_pxor (di, di)
  v8qi __builtin_ia32_pcmpeqb (v8qi, v8qi)
  v4hi __builtin_ia32_pcmpeqw (v4hi, v4hi)
  v2si __builtin_ia32_pcmpeqd (v2si, v2si)
  v8qi __builtin_ia32_pcmpgtb (v8qi, v8qi)
  v4hi __builtin_ia32_pcmpgtw (v4hi, v4hi)
  v2si __builtin_ia32_pcmpgtd (v2si, v2si)
  v8qi __builtin_ia32_punpckhbw (v8qi, v8qi)
  v4hi __builtin_ia32_punpckhwd (v4hi, v4hi)
  v2si __builtin_ia32_punpckhdq (v2si, v2si)
  v8qi __builtin_ia32_punpcklbw (v8qi, v8qi)
  v4hi __builtin_ia32_punpcklwd (v4hi, v4hi)
  v2si __builtin_ia32_punpckldq (v2si, v2si)
  v8qi __builtin_ia32_packsswb (v4hi, v4hi)
  v4hi __builtin_ia32_packssdw (v2si, v2si)
  v8qi __builtin_ia32_packuswb (v4hi, v4hi)

  v4hi __builtin_ia32_psllw (v4hi, v4hi)
  v2si __builtin_ia32_pslld (v2si, v2si)
  v1di __builtin_ia32_psllq (v1di, v1di)
  v4hi __builtin_ia32_psrlw (v4hi, v4hi)
  v2si __builtin_ia32_psrld (v2si, v2si)
  v1di __builtin_ia32_psrlq (v1di, v1di)
  v4hi __builtin_ia32_psraw (v4hi, v4hi)
  v2si __builtin_ia32_psrad (v2si, v2si)
  v4hi __builtin_ia32_psllwi (v4hi, int)
  v2si __builtin_ia32_pslldi (v2si, int)
  v1di __builtin_ia32_psllqi (v1di, int)
  v4hi __builtin_ia32_psrlwi (v4hi, int)
  v2si __builtin_ia32_psrldi (v2si, int)
  v1di __builtin_ia32_psrlqi (v1di, int)
  v4hi __builtin_ia32_psrawi (v4hi, int)
  v2si __builtin_ia32_psradi (v2si, int)

The following built-in functions are made available either with
:option:`-msse`, or with a combination of :option:`-m3dnow` and
:option:`-march=athlon`.  All of them generate the machine
instruction that is part of the name.

.. code-block:: c++

  v4hi __builtin_ia32_pmulhuw (v4hi, v4hi)
  v8qi __builtin_ia32_pavgb (v8qi, v8qi)
  v4hi __builtin_ia32_pavgw (v4hi, v4hi)
  v1di __builtin_ia32_psadbw (v8qi, v8qi)
  v8qi __builtin_ia32_pmaxub (v8qi, v8qi)
  v4hi __builtin_ia32_pmaxsw (v4hi, v4hi)
  v8qi __builtin_ia32_pminub (v8qi, v8qi)
  v4hi __builtin_ia32_pminsw (v4hi, v4hi)
  int __builtin_ia32_pmovmskb (v8qi)
  void __builtin_ia32_maskmovq (v8qi, v8qi, char *)
  void __builtin_ia32_movntq (di *, di)
  void __builtin_ia32_sfence (void)

The following built-in functions are available when :option:`-msse` is used.
All of them generate the machine instruction that is part of the name.

.. code-block:: c++

  int __builtin_ia32_comieq (v4sf, v4sf)
  int __builtin_ia32_comineq (v4sf, v4sf)
  int __builtin_ia32_comilt (v4sf, v4sf)
  int __builtin_ia32_comile (v4sf, v4sf)
  int __builtin_ia32_comigt (v4sf, v4sf)
  int __builtin_ia32_comige (v4sf, v4sf)
  int __builtin_ia32_ucomieq (v4sf, v4sf)
  int __builtin_ia32_ucomineq (v4sf, v4sf)
  int __builtin_ia32_ucomilt (v4sf, v4sf)
  int __builtin_ia32_ucomile (v4sf, v4sf)
  int __builtin_ia32_ucomigt (v4sf, v4sf)
  int __builtin_ia32_ucomige (v4sf, v4sf)
  v4sf __builtin_ia32_addps (v4sf, v4sf)
  v4sf __builtin_ia32_subps (v4sf, v4sf)
  v4sf __builtin_ia32_mulps (v4sf, v4sf)
  v4sf __builtin_ia32_divps (v4sf, v4sf)
  v4sf __builtin_ia32_addss (v4sf, v4sf)
  v4sf __builtin_ia32_subss (v4sf, v4sf)
  v4sf __builtin_ia32_mulss (v4sf, v4sf)
  v4sf __builtin_ia32_divss (v4sf, v4sf)
  v4sf __builtin_ia32_cmpeqps (v4sf, v4sf)
  v4sf __builtin_ia32_cmpltps (v4sf, v4sf)
  v4sf __builtin_ia32_cmpleps (v4sf, v4sf)
  v4sf __builtin_ia32_cmpgtps (v4sf, v4sf)
  v4sf __builtin_ia32_cmpgeps (v4sf, v4sf)
  v4sf __builtin_ia32_cmpunordps (v4sf, v4sf)
  v4sf __builtin_ia32_cmpneqps (v4sf, v4sf)
  v4sf __builtin_ia32_cmpnltps (v4sf, v4sf)
  v4sf __builtin_ia32_cmpnleps (v4sf, v4sf)
  v4sf __builtin_ia32_cmpngtps (v4sf, v4sf)
  v4sf __builtin_ia32_cmpngeps (v4sf, v4sf)
  v4sf __builtin_ia32_cmpordps (v4sf, v4sf)
  v4sf __builtin_ia32_cmpeqss (v4sf, v4sf)
  v4sf __builtin_ia32_cmpltss (v4sf, v4sf)
  v4sf __builtin_ia32_cmpless (v4sf, v4sf)
  v4sf __builtin_ia32_cmpunordss (v4sf, v4sf)
  v4sf __builtin_ia32_cmpneqss (v4sf, v4sf)
  v4sf __builtin_ia32_cmpnltss (v4sf, v4sf)
  v4sf __builtin_ia32_cmpnless (v4sf, v4sf)
  v4sf __builtin_ia32_cmpordss (v4sf, v4sf)
  v4sf __builtin_ia32_maxps (v4sf, v4sf)
  v4sf __builtin_ia32_maxss (v4sf, v4sf)
  v4sf __builtin_ia32_minps (v4sf, v4sf)
  v4sf __builtin_ia32_minss (v4sf, v4sf)
  v4sf __builtin_ia32_andps (v4sf, v4sf)
  v4sf __builtin_ia32_andnps (v4sf, v4sf)
  v4sf __builtin_ia32_orps (v4sf, v4sf)
  v4sf __builtin_ia32_xorps (v4sf, v4sf)
  v4sf __builtin_ia32_movss (v4sf, v4sf)
  v4sf __builtin_ia32_movhlps (v4sf, v4sf)
  v4sf __builtin_ia32_movlhps (v4sf, v4sf)
  v4sf __builtin_ia32_unpckhps (v4sf, v4sf)
  v4sf __builtin_ia32_unpcklps (v4sf, v4sf)
  v4sf __builtin_ia32_cvtpi2ps (v4sf, v2si)
  v4sf __builtin_ia32_cvtsi2ss (v4sf, int)
  v2si __builtin_ia32_cvtps2pi (v4sf)
  int __builtin_ia32_cvtss2si (v4sf)
  v2si __builtin_ia32_cvttps2pi (v4sf)
  int __builtin_ia32_cvttss2si (v4sf)
  v4sf __builtin_ia32_rcpps (v4sf)
  v4sf __builtin_ia32_rsqrtps (v4sf)
  v4sf __builtin_ia32_sqrtps (v4sf)
  v4sf __builtin_ia32_rcpss (v4sf)
  v4sf __builtin_ia32_rsqrtss (v4sf)
  v4sf __builtin_ia32_sqrtss (v4sf)
  v4sf __builtin_ia32_shufps (v4sf, v4sf, int)
  void __builtin_ia32_movntps (float *, v4sf)
  int __builtin_ia32_movmskps (v4sf)

The following built-in functions are available when :option:`-msse` is used.

v4sf __builtin_ia32_loadups (float *)
  Generates the ``movups`` machine instruction as a load from memory.

void __builtin_ia32_storeups (float *, v4sf)
  Generates the ``movups`` machine instruction as a store to memory.

v4sf __builtin_ia32_loadss (float *)
  Generates the ``movss`` machine instruction as a load from memory.

v4sf __builtin_ia32_loadhps (v4sf, const v2sf *)
  Generates the ``movhps`` machine instruction as a load from memory.

v4sf __builtin_ia32_loadlps (v4sf, const v2sf *)
  Generates the ``movlps`` machine instruction as a load from memory

void __builtin_ia32_storehps (v2sf *, v4sf)
  Generates the ``movhps`` machine instruction as a store to memory.

void __builtin_ia32_storelps (v2sf *, v4sf)
  Generates the ``movlps`` machine instruction as a store to memory.

The following built-in functions are available when :option:`-msse2` is used.
All of them generate the machine instruction that is part of the name.

.. code-block:: c++

  int __builtin_ia32_comisdeq (v2df, v2df)
  int __builtin_ia32_comisdlt (v2df, v2df)
  int __builtin_ia32_comisdle (v2df, v2df)
  int __builtin_ia32_comisdgt (v2df, v2df)
  int __builtin_ia32_comisdge (v2df, v2df)
  int __builtin_ia32_comisdneq (v2df, v2df)
  int __builtin_ia32_ucomisdeq (v2df, v2df)
  int __builtin_ia32_ucomisdlt (v2df, v2df)
  int __builtin_ia32_ucomisdle (v2df, v2df)
  int __builtin_ia32_ucomisdgt (v2df, v2df)
  int __builtin_ia32_ucomisdge (v2df, v2df)
  int __builtin_ia32_ucomisdneq (v2df, v2df)
  v2df __builtin_ia32_cmpeqpd (v2df, v2df)
  v2df __builtin_ia32_cmpltpd (v2df, v2df)
  v2df __builtin_ia32_cmplepd (v2df, v2df)
  v2df __builtin_ia32_cmpgtpd (v2df, v2df)
  v2df __builtin_ia32_cmpgepd (v2df, v2df)
  v2df __builtin_ia32_cmpunordpd (v2df, v2df)
  v2df __builtin_ia32_cmpneqpd (v2df, v2df)
  v2df __builtin_ia32_cmpnltpd (v2df, v2df)
  v2df __builtin_ia32_cmpnlepd (v2df, v2df)
  v2df __builtin_ia32_cmpngtpd (v2df, v2df)
  v2df __builtin_ia32_cmpngepd (v2df, v2df)
  v2df __builtin_ia32_cmpordpd (v2df, v2df)
  v2df __builtin_ia32_cmpeqsd (v2df, v2df)
  v2df __builtin_ia32_cmpltsd (v2df, v2df)
  v2df __builtin_ia32_cmplesd (v2df, v2df)
  v2df __builtin_ia32_cmpunordsd (v2df, v2df)
  v2df __builtin_ia32_cmpneqsd (v2df, v2df)
  v2df __builtin_ia32_cmpnltsd (v2df, v2df)
  v2df __builtin_ia32_cmpnlesd (v2df, v2df)
  v2df __builtin_ia32_cmpordsd (v2df, v2df)
  v2di __builtin_ia32_paddq (v2di, v2di)
  v2di __builtin_ia32_psubq (v2di, v2di)
  v2df __builtin_ia32_addpd (v2df, v2df)
  v2df __builtin_ia32_subpd (v2df, v2df)
  v2df __builtin_ia32_mulpd (v2df, v2df)
  v2df __builtin_ia32_divpd (v2df, v2df)
  v2df __builtin_ia32_addsd (v2df, v2df)
  v2df __builtin_ia32_subsd (v2df, v2df)
  v2df __builtin_ia32_mulsd (v2df, v2df)
  v2df __builtin_ia32_divsd (v2df, v2df)
  v2df __builtin_ia32_minpd (v2df, v2df)
  v2df __builtin_ia32_maxpd (v2df, v2df)
  v2df __builtin_ia32_minsd (v2df, v2df)
  v2df __builtin_ia32_maxsd (v2df, v2df)
  v2df __builtin_ia32_andpd (v2df, v2df)
  v2df __builtin_ia32_andnpd (v2df, v2df)
  v2df __builtin_ia32_orpd (v2df, v2df)
  v2df __builtin_ia32_xorpd (v2df, v2df)
  v2df __builtin_ia32_movsd (v2df, v2df)
  v2df __builtin_ia32_unpckhpd (v2df, v2df)
  v2df __builtin_ia32_unpcklpd (v2df, v2df)
  v16qi __builtin_ia32_paddb128 (v16qi, v16qi)
  v8hi __builtin_ia32_paddw128 (v8hi, v8hi)
  v4si __builtin_ia32_paddd128 (v4si, v4si)
  v2di __builtin_ia32_paddq128 (v2di, v2di)
  v16qi __builtin_ia32_psubb128 (v16qi, v16qi)
  v8hi __builtin_ia32_psubw128 (v8hi, v8hi)
  v4si __builtin_ia32_psubd128 (v4si, v4si)
  v2di __builtin_ia32_psubq128 (v2di, v2di)
  v8hi __builtin_ia32_pmullw128 (v8hi, v8hi)
  v8hi __builtin_ia32_pmulhw128 (v8hi, v8hi)
  v2di __builtin_ia32_pand128 (v2di, v2di)
  v2di __builtin_ia32_pandn128 (v2di, v2di)
  v2di __builtin_ia32_por128 (v2di, v2di)
  v2di __builtin_ia32_pxor128 (v2di, v2di)
  v16qi __builtin_ia32_pavgb128 (v16qi, v16qi)
  v8hi __builtin_ia32_pavgw128 (v8hi, v8hi)
  v16qi __builtin_ia32_pcmpeqb128 (v16qi, v16qi)
  v8hi __builtin_ia32_pcmpeqw128 (v8hi, v8hi)
  v4si __builtin_ia32_pcmpeqd128 (v4si, v4si)
  v16qi __builtin_ia32_pcmpgtb128 (v16qi, v16qi)
  v8hi __builtin_ia32_pcmpgtw128 (v8hi, v8hi)
  v4si __builtin_ia32_pcmpgtd128 (v4si, v4si)
  v16qi __builtin_ia32_pmaxub128 (v16qi, v16qi)
  v8hi __builtin_ia32_pmaxsw128 (v8hi, v8hi)
  v16qi __builtin_ia32_pminub128 (v16qi, v16qi)
  v8hi __builtin_ia32_pminsw128 (v8hi, v8hi)
  v16qi __builtin_ia32_punpckhbw128 (v16qi, v16qi)
  v8hi __builtin_ia32_punpckhwd128 (v8hi, v8hi)
  v4si __builtin_ia32_punpckhdq128 (v4si, v4si)
  v2di __builtin_ia32_punpckhqdq128 (v2di, v2di)
  v16qi __builtin_ia32_punpcklbw128 (v16qi, v16qi)
  v8hi __builtin_ia32_punpcklwd128 (v8hi, v8hi)
  v4si __builtin_ia32_punpckldq128 (v4si, v4si)
  v2di __builtin_ia32_punpcklqdq128 (v2di, v2di)
  v16qi __builtin_ia32_packsswb128 (v8hi, v8hi)
  v8hi __builtin_ia32_packssdw128 (v4si, v4si)
  v16qi __builtin_ia32_packuswb128 (v8hi, v8hi)
  v8hi __builtin_ia32_pmulhuw128 (v8hi, v8hi)
  void __builtin_ia32_maskmovdqu (v16qi, v16qi)
  v2df __builtin_ia32_loadupd (double *)
  void __builtin_ia32_storeupd (double *, v2df)
  v2df __builtin_ia32_loadhpd (v2df, double const *)
  v2df __builtin_ia32_loadlpd (v2df, double const *)
  int __builtin_ia32_movmskpd (v2df)
  int __builtin_ia32_pmovmskb128 (v16qi)
  void __builtin_ia32_movnti (int *, int)
  void __builtin_ia32_movnti64 (long long int *, long long int)
  void __builtin_ia32_movntpd (double *, v2df)
  void __builtin_ia32_movntdq (v2df *, v2df)
  v4si __builtin_ia32_pshufd (v4si, int)
  v8hi __builtin_ia32_pshuflw (v8hi, int)
  v8hi __builtin_ia32_pshufhw (v8hi, int)
  v2di __builtin_ia32_psadbw128 (v16qi, v16qi)
  v2df __builtin_ia32_sqrtpd (v2df)
  v2df __builtin_ia32_sqrtsd (v2df)
  v2df __builtin_ia32_shufpd (v2df, v2df, int)
  v2df __builtin_ia32_cvtdq2pd (v4si)
  v4sf __builtin_ia32_cvtdq2ps (v4si)
  v4si __builtin_ia32_cvtpd2dq (v2df)
  v2si __builtin_ia32_cvtpd2pi (v2df)
  v4sf __builtin_ia32_cvtpd2ps (v2df)
  v4si __builtin_ia32_cvttpd2dq (v2df)
  v2si __builtin_ia32_cvttpd2pi (v2df)
  v2df __builtin_ia32_cvtpi2pd (v2si)
  int __builtin_ia32_cvtsd2si (v2df)
  int __builtin_ia32_cvttsd2si (v2df)
  long long __builtin_ia32_cvtsd2si64 (v2df)
  long long __builtin_ia32_cvttsd2si64 (v2df)
  v4si __builtin_ia32_cvtps2dq (v4sf)
  v2df __builtin_ia32_cvtps2pd (v4sf)
  v4si __builtin_ia32_cvttps2dq (v4sf)
  v2df __builtin_ia32_cvtsi2sd (v2df, int)
  v2df __builtin_ia32_cvtsi642sd (v2df, long long)
  v4sf __builtin_ia32_cvtsd2ss (v4sf, v2df)
  v2df __builtin_ia32_cvtss2sd (v2df, v4sf)
  void __builtin_ia32_clflush (const void *)
  void __builtin_ia32_lfence (void)
  void __builtin_ia32_mfence (void)
  v16qi __builtin_ia32_loaddqu (const char *)
  void __builtin_ia32_storedqu (char *, v16qi)
  v1di __builtin_ia32_pmuludq (v2si, v2si)
  v2di __builtin_ia32_pmuludq128 (v4si, v4si)
  v8hi __builtin_ia32_psllw128 (v8hi, v8hi)
  v4si __builtin_ia32_pslld128 (v4si, v4si)
  v2di __builtin_ia32_psllq128 (v2di, v2di)
  v8hi __builtin_ia32_psrlw128 (v8hi, v8hi)
  v4si __builtin_ia32_psrld128 (v4si, v4si)
  v2di __builtin_ia32_psrlq128 (v2di, v2di)
  v8hi __builtin_ia32_psraw128 (v8hi, v8hi)
  v4si __builtin_ia32_psrad128 (v4si, v4si)
  v2di __builtin_ia32_pslldqi128 (v2di, int)
  v8hi __builtin_ia32_psllwi128 (v8hi, int)
  v4si __builtin_ia32_pslldi128 (v4si, int)
  v2di __builtin_ia32_psllqi128 (v2di, int)
  v2di __builtin_ia32_psrldqi128 (v2di, int)
  v8hi __builtin_ia32_psrlwi128 (v8hi, int)
  v4si __builtin_ia32_psrldi128 (v4si, int)
  v2di __builtin_ia32_psrlqi128 (v2di, int)
  v8hi __builtin_ia32_psrawi128 (v8hi, int)
  v4si __builtin_ia32_psradi128 (v4si, int)
  v4si __builtin_ia32_pmaddwd128 (v8hi, v8hi)
  v2di __builtin_ia32_movq128 (v2di)

The following built-in functions are available when :option:`-msse3` is used.
All of them generate the machine instruction that is part of the name.

.. code-block:: c++

  v2df __builtin_ia32_addsubpd (v2df, v2df)
  v4sf __builtin_ia32_addsubps (v4sf, v4sf)
  v2df __builtin_ia32_haddpd (v2df, v2df)
  v4sf __builtin_ia32_haddps (v4sf, v4sf)
  v2df __builtin_ia32_hsubpd (v2df, v2df)
  v4sf __builtin_ia32_hsubps (v4sf, v4sf)
  v16qi __builtin_ia32_lddqu (char const *)
  void __builtin_ia32_monitor (void *, unsigned int, unsigned int)
  v4sf __builtin_ia32_movshdup (v4sf)
  v4sf __builtin_ia32_movsldup (v4sf)
  void __builtin_ia32_mwait (unsigned int, unsigned int)

The following built-in functions are available when :option:`-mssse3` is used.
All of them generate the machine instruction that is part of the name.

.. code-block:: c++

  v2si __builtin_ia32_phaddd (v2si, v2si)
  v4hi __builtin_ia32_phaddw (v4hi, v4hi)
  v4hi __builtin_ia32_phaddsw (v4hi, v4hi)
  v2si __builtin_ia32_phsubd (v2si, v2si)
  v4hi __builtin_ia32_phsubw (v4hi, v4hi)
  v4hi __builtin_ia32_phsubsw (v4hi, v4hi)
  v4hi __builtin_ia32_pmaddubsw (v8qi, v8qi)
  v4hi __builtin_ia32_pmulhrsw (v4hi, v4hi)
  v8qi __builtin_ia32_pshufb (v8qi, v8qi)
  v8qi __builtin_ia32_psignb (v8qi, v8qi)
  v2si __builtin_ia32_psignd (v2si, v2si)
  v4hi __builtin_ia32_psignw (v4hi, v4hi)
  v1di __builtin_ia32_palignr (v1di, v1di, int)
  v8qi __builtin_ia32_pabsb (v8qi)
  v2si __builtin_ia32_pabsd (v2si)
  v4hi __builtin_ia32_pabsw (v4hi)

The following built-in functions are available when :option:`-mssse3` is used.
All of them generate the machine instruction that is part of the name.

.. code-block:: c++

  v4si __builtin_ia32_phaddd128 (v4si, v4si)
  v8hi __builtin_ia32_phaddw128 (v8hi, v8hi)
  v8hi __builtin_ia32_phaddsw128 (v8hi, v8hi)
  v4si __builtin_ia32_phsubd128 (v4si, v4si)
  v8hi __builtin_ia32_phsubw128 (v8hi, v8hi)
  v8hi __builtin_ia32_phsubsw128 (v8hi, v8hi)
  v8hi __builtin_ia32_pmaddubsw128 (v16qi, v16qi)
  v8hi __builtin_ia32_pmulhrsw128 (v8hi, v8hi)
  v16qi __builtin_ia32_pshufb128 (v16qi, v16qi)
  v16qi __builtin_ia32_psignb128 (v16qi, v16qi)
  v4si __builtin_ia32_psignd128 (v4si, v4si)
  v8hi __builtin_ia32_psignw128 (v8hi, v8hi)
  v2di __builtin_ia32_palignr128 (v2di, v2di, int)
  v16qi __builtin_ia32_pabsb128 (v16qi)
  v4si __builtin_ia32_pabsd128 (v4si)
  v8hi __builtin_ia32_pabsw128 (v8hi)

The following built-in functions are available when :option:`-msse4.1` is
used.  All of them generate the machine instruction that is part of the
name.

.. code-block:: c++

  v2df __builtin_ia32_blendpd (v2df, v2df, const int)
  v4sf __builtin_ia32_blendps (v4sf, v4sf, const int)
  v2df __builtin_ia32_blendvpd (v2df, v2df, v2df)
  v4sf __builtin_ia32_blendvps (v4sf, v4sf, v4sf)
  v2df __builtin_ia32_dppd (v2df, v2df, const int)
  v4sf __builtin_ia32_dpps (v4sf, v4sf, const int)
  v4sf __builtin_ia32_insertps128 (v4sf, v4sf, const int)
  v2di __builtin_ia32_movntdqa (v2di *);
  v16qi __builtin_ia32_mpsadbw128 (v16qi, v16qi, const int)
  v8hi __builtin_ia32_packusdw128 (v4si, v4si)
  v16qi __builtin_ia32_pblendvb128 (v16qi, v16qi, v16qi)
  v8hi __builtin_ia32_pblendw128 (v8hi, v8hi, const int)
  v2di __builtin_ia32_pcmpeqq (v2di, v2di)
  v8hi __builtin_ia32_phminposuw128 (v8hi)
  v16qi __builtin_ia32_pmaxsb128 (v16qi, v16qi)
  v4si __builtin_ia32_pmaxsd128 (v4si, v4si)
  v4si __builtin_ia32_pmaxud128 (v4si, v4si)
  v8hi __builtin_ia32_pmaxuw128 (v8hi, v8hi)
  v16qi __builtin_ia32_pminsb128 (v16qi, v16qi)
  v4si __builtin_ia32_pminsd128 (v4si, v4si)
  v4si __builtin_ia32_pminud128 (v4si, v4si)
  v8hi __builtin_ia32_pminuw128 (v8hi, v8hi)
  v4si __builtin_ia32_pmovsxbd128 (v16qi)
  v2di __builtin_ia32_pmovsxbq128 (v16qi)
  v8hi __builtin_ia32_pmovsxbw128 (v16qi)
  v2di __builtin_ia32_pmovsxdq128 (v4si)
  v4si __builtin_ia32_pmovsxwd128 (v8hi)
  v2di __builtin_ia32_pmovsxwq128 (v8hi)
  v4si __builtin_ia32_pmovzxbd128 (v16qi)
  v2di __builtin_ia32_pmovzxbq128 (v16qi)
  v8hi __builtin_ia32_pmovzxbw128 (v16qi)
  v2di __builtin_ia32_pmovzxdq128 (v4si)
  v4si __builtin_ia32_pmovzxwd128 (v8hi)
  v2di __builtin_ia32_pmovzxwq128 (v8hi)
  v2di __builtin_ia32_pmuldq128 (v4si, v4si)
  v4si __builtin_ia32_pmulld128 (v4si, v4si)
  int __builtin_ia32_ptestc128 (v2di, v2di)
  int __builtin_ia32_ptestnzc128 (v2di, v2di)
  int __builtin_ia32_ptestz128 (v2di, v2di)
  v2df __builtin_ia32_roundpd (v2df, const int)
  v4sf __builtin_ia32_roundps (v4sf, const int)
  v2df __builtin_ia32_roundsd (v2df, v2df, const int)
  v4sf __builtin_ia32_roundss (v4sf, v4sf, const int)

The following built-in functions are available when :option:`-msse4.1` is
used.

v4sf __builtin_ia32_vec_set_v4sf (v4sf, float, const int)
  Generates the ``insertps`` machine instruction.

int __builtin_ia32_vec_ext_v16qi (v16qi, const int)
  Generates the ``pextrb`` machine instruction.

v16qi __builtin_ia32_vec_set_v16qi (v16qi, int, const int)
  Generates the ``pinsrb`` machine instruction.

v4si __builtin_ia32_vec_set_v4si (v4si, int, const int)
  Generates the ``pinsrd`` machine instruction.

v2di __builtin_ia32_vec_set_v2di (v2di, long long, const int)
  Generates the ``pinsrq`` machine instruction in 64bit mode.

The following built-in functions are changed to generate new SSE4.1
instructions when :option:`-msse4.1` is used.

float __builtin_ia32_vec_ext_v4sf (v4sf, const int)
  Generates the ``extractps`` machine instruction.

int __builtin_ia32_vec_ext_v4si (v4si, const int)
  Generates the ``pextrd`` machine instruction.

long long __builtin_ia32_vec_ext_v2di (v2di, const int)
  Generates the ``pextrq`` machine instruction in 64bit mode.

The following built-in functions are available when :option:`-msse4.2` is
used.  All of them generate the machine instruction that is part of the
name.

.. code-block:: c++

  v16qi __builtin_ia32_pcmpestrm128 (v16qi, int, v16qi, int, const int)
  int __builtin_ia32_pcmpestri128 (v16qi, int, v16qi, int, const int)
  int __builtin_ia32_pcmpestria128 (v16qi, int, v16qi, int, const int)
  int __builtin_ia32_pcmpestric128 (v16qi, int, v16qi, int, const int)
  int __builtin_ia32_pcmpestrio128 (v16qi, int, v16qi, int, const int)
  int __builtin_ia32_pcmpestris128 (v16qi, int, v16qi, int, const int)
  int __builtin_ia32_pcmpestriz128 (v16qi, int, v16qi, int, const int)
  v16qi __builtin_ia32_pcmpistrm128 (v16qi, v16qi, const int)
  int __builtin_ia32_pcmpistri128 (v16qi, v16qi, const int)
  int __builtin_ia32_pcmpistria128 (v16qi, v16qi, const int)
  int __builtin_ia32_pcmpistric128 (v16qi, v16qi, const int)
  int __builtin_ia32_pcmpistrio128 (v16qi, v16qi, const int)
  int __builtin_ia32_pcmpistris128 (v16qi, v16qi, const int)
  int __builtin_ia32_pcmpistriz128 (v16qi, v16qi, const int)
  v2di __builtin_ia32_pcmpgtq (v2di, v2di)

The following built-in functions are available when :option:`-msse4.2` is
used.

unsigned int __builtin_ia32_crc32qi (unsigned int, unsigned char)
  Generates the ``crc32b`` machine instruction.

unsigned int __builtin_ia32_crc32hi (unsigned int, unsigned short)
  Generates the ``crc32w`` machine instruction.

unsigned int __builtin_ia32_crc32si (unsigned int, unsigned int)
  Generates the ``crc32l`` machine instruction.

unsigned long long __builtin_ia32_crc32di (unsigned long long, unsigned long long)
  Generates the ``crc32q`` machine instruction.

The following built-in functions are changed to generate new SSE4.2
instructions when :option:`-msse4.2` is used.

int __builtin_popcount (unsigned int)
  Generates the ``popcntl`` machine instruction.

int __builtin_popcountl (unsigned long)
  Generates the ``popcntl`` or ``popcntq`` machine instruction,
  depending on the size of ``unsigned long``.

int __builtin_popcountll (unsigned long long)
  Generates the ``popcntq`` machine instruction.

The following built-in functions are available when :option:`-mavx` is
used. All of them generate the machine instruction that is part of the
name.

.. code-block:: c++

  v4df __builtin_ia32_addpd256 (v4df,v4df)
  v8sf __builtin_ia32_addps256 (v8sf,v8sf)
  v4df __builtin_ia32_addsubpd256 (v4df,v4df)
  v8sf __builtin_ia32_addsubps256 (v8sf,v8sf)
  v4df __builtin_ia32_andnpd256 (v4df,v4df)
  v8sf __builtin_ia32_andnps256 (v8sf,v8sf)
  v4df __builtin_ia32_andpd256 (v4df,v4df)
  v8sf __builtin_ia32_andps256 (v8sf,v8sf)
  v4df __builtin_ia32_blendpd256 (v4df,v4df,int)
  v8sf __builtin_ia32_blendps256 (v8sf,v8sf,int)
  v4df __builtin_ia32_blendvpd256 (v4df,v4df,v4df)
  v8sf __builtin_ia32_blendvps256 (v8sf,v8sf,v8sf)
  v2df __builtin_ia32_cmppd (v2df,v2df,int)
  v4df __builtin_ia32_cmppd256 (v4df,v4df,int)
  v4sf __builtin_ia32_cmpps (v4sf,v4sf,int)
  v8sf __builtin_ia32_cmpps256 (v8sf,v8sf,int)
  v2df __builtin_ia32_cmpsd (v2df,v2df,int)
  v4sf __builtin_ia32_cmpss (v4sf,v4sf,int)
  v4df __builtin_ia32_cvtdq2pd256 (v4si)
  v8sf __builtin_ia32_cvtdq2ps256 (v8si)
  v4si __builtin_ia32_cvtpd2dq256 (v4df)
  v4sf __builtin_ia32_cvtpd2ps256 (v4df)
  v8si __builtin_ia32_cvtps2dq256 (v8sf)
  v4df __builtin_ia32_cvtps2pd256 (v4sf)
  v4si __builtin_ia32_cvttpd2dq256 (v4df)
  v8si __builtin_ia32_cvttps2dq256 (v8sf)
  v4df __builtin_ia32_divpd256 (v4df,v4df)
  v8sf __builtin_ia32_divps256 (v8sf,v8sf)
  v8sf __builtin_ia32_dpps256 (v8sf,v8sf,int)
  v4df __builtin_ia32_haddpd256 (v4df,v4df)
  v8sf __builtin_ia32_haddps256 (v8sf,v8sf)
  v4df __builtin_ia32_hsubpd256 (v4df,v4df)
  v8sf __builtin_ia32_hsubps256 (v8sf,v8sf)
  v32qi __builtin_ia32_lddqu256 (pcchar)
  v32qi __builtin_ia32_loaddqu256 (pcchar)
  v4df __builtin_ia32_loadupd256 (pcdouble)
  v8sf __builtin_ia32_loadups256 (pcfloat)
  v2df __builtin_ia32_maskloadpd (pcv2df,v2df)
  v4df __builtin_ia32_maskloadpd256 (pcv4df,v4df)
  v4sf __builtin_ia32_maskloadps (pcv4sf,v4sf)
  v8sf __builtin_ia32_maskloadps256 (pcv8sf,v8sf)
  void __builtin_ia32_maskstorepd (pv2df,v2df,v2df)
  void __builtin_ia32_maskstorepd256 (pv4df,v4df,v4df)
  void __builtin_ia32_maskstoreps (pv4sf,v4sf,v4sf)
  void __builtin_ia32_maskstoreps256 (pv8sf,v8sf,v8sf)
  v4df __builtin_ia32_maxpd256 (v4df,v4df)
  v8sf __builtin_ia32_maxps256 (v8sf,v8sf)
  v4df __builtin_ia32_minpd256 (v4df,v4df)
  v8sf __builtin_ia32_minps256 (v8sf,v8sf)
  v4df __builtin_ia32_movddup256 (v4df)
  int __builtin_ia32_movmskpd256 (v4df)
  int __builtin_ia32_movmskps256 (v8sf)
  v8sf __builtin_ia32_movshdup256 (v8sf)
  v8sf __builtin_ia32_movsldup256 (v8sf)
  v4df __builtin_ia32_mulpd256 (v4df,v4df)
  v8sf __builtin_ia32_mulps256 (v8sf,v8sf)
  v4df __builtin_ia32_orpd256 (v4df,v4df)
  v8sf __builtin_ia32_orps256 (v8sf,v8sf)
  v2df __builtin_ia32_pd_pd256 (v4df)
  v4df __builtin_ia32_pd256_pd (v2df)
  v4sf __builtin_ia32_ps_ps256 (v8sf)
  v8sf __builtin_ia32_ps256_ps (v4sf)
  int __builtin_ia32_ptestc256 (v4di,v4di,ptest)
  int __builtin_ia32_ptestnzc256 (v4di,v4di,ptest)
  int __builtin_ia32_ptestz256 (v4di,v4di,ptest)
  v8sf __builtin_ia32_rcpps256 (v8sf)
  v4df __builtin_ia32_roundpd256 (v4df,int)
  v8sf __builtin_ia32_roundps256 (v8sf,int)
  v8sf __builtin_ia32_rsqrtps_nr256 (v8sf)
  v8sf __builtin_ia32_rsqrtps256 (v8sf)
  v4df __builtin_ia32_shufpd256 (v4df,v4df,int)
  v8sf __builtin_ia32_shufps256 (v8sf,v8sf,int)
  v4si __builtin_ia32_si_si256 (v8si)
  v8si __builtin_ia32_si256_si (v4si)
  v4df __builtin_ia32_sqrtpd256 (v4df)
  v8sf __builtin_ia32_sqrtps_nr256 (v8sf)
  v8sf __builtin_ia32_sqrtps256 (v8sf)
  void __builtin_ia32_storedqu256 (pchar,v32qi)
  void __builtin_ia32_storeupd256 (pdouble,v4df)
  void __builtin_ia32_storeups256 (pfloat,v8sf)
  v4df __builtin_ia32_subpd256 (v4df,v4df)
  v8sf __builtin_ia32_subps256 (v8sf,v8sf)
  v4df __builtin_ia32_unpckhpd256 (v4df,v4df)
  v8sf __builtin_ia32_unpckhps256 (v8sf,v8sf)
  v4df __builtin_ia32_unpcklpd256 (v4df,v4df)
  v8sf __builtin_ia32_unpcklps256 (v8sf,v8sf)
  v4df __builtin_ia32_vbroadcastf128_pd256 (pcv2df)
  v8sf __builtin_ia32_vbroadcastf128_ps256 (pcv4sf)
  v4df __builtin_ia32_vbroadcastsd256 (pcdouble)
  v4sf __builtin_ia32_vbroadcastss (pcfloat)
  v8sf __builtin_ia32_vbroadcastss256 (pcfloat)
  v2df __builtin_ia32_vextractf128_pd256 (v4df,int)
  v4sf __builtin_ia32_vextractf128_ps256 (v8sf,int)
  v4si __builtin_ia32_vextractf128_si256 (v8si,int)
  v4df __builtin_ia32_vinsertf128_pd256 (v4df,v2df,int)
  v8sf __builtin_ia32_vinsertf128_ps256 (v8sf,v4sf,int)
  v8si __builtin_ia32_vinsertf128_si256 (v8si,v4si,int)
  v4df __builtin_ia32_vperm2f128_pd256 (v4df,v4df,int)
  v8sf __builtin_ia32_vperm2f128_ps256 (v8sf,v8sf,int)
  v8si __builtin_ia32_vperm2f128_si256 (v8si,v8si,int)
  v2df __builtin_ia32_vpermil2pd (v2df,v2df,v2di,int)
  v4df __builtin_ia32_vpermil2pd256 (v4df,v4df,v4di,int)
  v4sf __builtin_ia32_vpermil2ps (v4sf,v4sf,v4si,int)
  v8sf __builtin_ia32_vpermil2ps256 (v8sf,v8sf,v8si,int)
  v2df __builtin_ia32_vpermilpd (v2df,int)
  v4df __builtin_ia32_vpermilpd256 (v4df,int)
  v4sf __builtin_ia32_vpermilps (v4sf,int)
  v8sf __builtin_ia32_vpermilps256 (v8sf,int)
  v2df __builtin_ia32_vpermilvarpd (v2df,v2di)
  v4df __builtin_ia32_vpermilvarpd256 (v4df,v4di)
  v4sf __builtin_ia32_vpermilvarps (v4sf,v4si)
  v8sf __builtin_ia32_vpermilvarps256 (v8sf,v8si)
  int __builtin_ia32_vtestcpd (v2df,v2df,ptest)
  int __builtin_ia32_vtestcpd256 (v4df,v4df,ptest)
  int __builtin_ia32_vtestcps (v4sf,v4sf,ptest)
  int __builtin_ia32_vtestcps256 (v8sf,v8sf,ptest)
  int __builtin_ia32_vtestnzcpd (v2df,v2df,ptest)
  int __builtin_ia32_vtestnzcpd256 (v4df,v4df,ptest)
  int __builtin_ia32_vtestnzcps (v4sf,v4sf,ptest)
  int __builtin_ia32_vtestnzcps256 (v8sf,v8sf,ptest)
  int __builtin_ia32_vtestzpd (v2df,v2df,ptest)
  int __builtin_ia32_vtestzpd256 (v4df,v4df,ptest)
  int __builtin_ia32_vtestzps (v4sf,v4sf,ptest)
  int __builtin_ia32_vtestzps256 (v8sf,v8sf,ptest)
  void __builtin_ia32_vzeroall (void)
  void __builtin_ia32_vzeroupper (void)
  v4df __builtin_ia32_xorpd256 (v4df,v4df)
  v8sf __builtin_ia32_xorps256 (v8sf,v8sf)

The following built-in functions are available when :option:`-mavx2` is
used. All of them generate the machine instruction that is part of the
name.

.. code-block:: c++

  v32qi __builtin_ia32_mpsadbw256 (v32qi,v32qi,int)
  v32qi __builtin_ia32_pabsb256 (v32qi)
  v16hi __builtin_ia32_pabsw256 (v16hi)
  v8si __builtin_ia32_pabsd256 (v8si)
  v16hi __builtin_ia32_packssdw256 (v8si,v8si)
  v32qi __builtin_ia32_packsswb256 (v16hi,v16hi)
  v16hi __builtin_ia32_packusdw256 (v8si,v8si)
  v32qi __builtin_ia32_packuswb256 (v16hi,v16hi)
  v32qi __builtin_ia32_paddb256 (v32qi,v32qi)
  v16hi __builtin_ia32_paddw256 (v16hi,v16hi)
  v8si __builtin_ia32_paddd256 (v8si,v8si)
  v4di __builtin_ia32_paddq256 (v4di,v4di)
  v32qi __builtin_ia32_paddsb256 (v32qi,v32qi)
  v16hi __builtin_ia32_paddsw256 (v16hi,v16hi)
  v32qi __builtin_ia32_paddusb256 (v32qi,v32qi)
  v16hi __builtin_ia32_paddusw256 (v16hi,v16hi)
  v4di __builtin_ia32_palignr256 (v4di,v4di,int)
  v4di __builtin_ia32_andsi256 (v4di,v4di)
  v4di __builtin_ia32_andnotsi256 (v4di,v4di)
  v32qi __builtin_ia32_pavgb256 (v32qi,v32qi)
  v16hi __builtin_ia32_pavgw256 (v16hi,v16hi)
  v32qi __builtin_ia32_pblendvb256 (v32qi,v32qi,v32qi)
  v16hi __builtin_ia32_pblendw256 (v16hi,v16hi,int)
  v32qi __builtin_ia32_pcmpeqb256 (v32qi,v32qi)
  v16hi __builtin_ia32_pcmpeqw256 (v16hi,v16hi)
  v8si __builtin_ia32_pcmpeqd256 (c8si,v8si)
  v4di __builtin_ia32_pcmpeqq256 (v4di,v4di)
  v32qi __builtin_ia32_pcmpgtb256 (v32qi,v32qi)
  v16hi __builtin_ia32_pcmpgtw256 (16hi,v16hi)
  v8si __builtin_ia32_pcmpgtd256 (v8si,v8si)
  v4di __builtin_ia32_pcmpgtq256 (v4di,v4di)
  v16hi __builtin_ia32_phaddw256 (v16hi,v16hi)
  v8si __builtin_ia32_phaddd256 (v8si,v8si)
  v16hi __builtin_ia32_phaddsw256 (v16hi,v16hi)
  v16hi __builtin_ia32_phsubw256 (v16hi,v16hi)
  v8si __builtin_ia32_phsubd256 (v8si,v8si)
  v16hi __builtin_ia32_phsubsw256 (v16hi,v16hi)
  v32qi __builtin_ia32_pmaddubsw256 (v32qi,v32qi)
  v16hi __builtin_ia32_pmaddwd256 (v16hi,v16hi)
  v32qi __builtin_ia32_pmaxsb256 (v32qi,v32qi)
  v16hi __builtin_ia32_pmaxsw256 (v16hi,v16hi)
  v8si __builtin_ia32_pmaxsd256 (v8si,v8si)
  v32qi __builtin_ia32_pmaxub256 (v32qi,v32qi)
  v16hi __builtin_ia32_pmaxuw256 (v16hi,v16hi)
  v8si __builtin_ia32_pmaxud256 (v8si,v8si)
  v32qi __builtin_ia32_pminsb256 (v32qi,v32qi)
  v16hi __builtin_ia32_pminsw256 (v16hi,v16hi)
  v8si __builtin_ia32_pminsd256 (v8si,v8si)
  v32qi __builtin_ia32_pminub256 (v32qi,v32qi)
  v16hi __builtin_ia32_pminuw256 (v16hi,v16hi)
  v8si __builtin_ia32_pminud256 (v8si,v8si)
  int __builtin_ia32_pmovmskb256 (v32qi)
  v16hi __builtin_ia32_pmovsxbw256 (v16qi)
  v8si __builtin_ia32_pmovsxbd256 (v16qi)
  v4di __builtin_ia32_pmovsxbq256 (v16qi)
  v8si __builtin_ia32_pmovsxwd256 (v8hi)
  v4di __builtin_ia32_pmovsxwq256 (v8hi)
  v4di __builtin_ia32_pmovsxdq256 (v4si)
  v16hi __builtin_ia32_pmovzxbw256 (v16qi)
  v8si __builtin_ia32_pmovzxbd256 (v16qi)
  v4di __builtin_ia32_pmovzxbq256 (v16qi)
  v8si __builtin_ia32_pmovzxwd256 (v8hi)
  v4di __builtin_ia32_pmovzxwq256 (v8hi)
  v4di __builtin_ia32_pmovzxdq256 (v4si)
  v4di __builtin_ia32_pmuldq256 (v8si,v8si)
  v16hi __builtin_ia32_pmulhrsw256 (v16hi, v16hi)
  v16hi __builtin_ia32_pmulhuw256 (v16hi,v16hi)
  v16hi __builtin_ia32_pmulhw256 (v16hi,v16hi)
  v16hi __builtin_ia32_pmullw256 (v16hi,v16hi)
  v8si __builtin_ia32_pmulld256 (v8si,v8si)
  v4di __builtin_ia32_pmuludq256 (v8si,v8si)
  v4di __builtin_ia32_por256 (v4di,v4di)
  v16hi __builtin_ia32_psadbw256 (v32qi,v32qi)
  v32qi __builtin_ia32_pshufb256 (v32qi,v32qi)
  v8si __builtin_ia32_pshufd256 (v8si,int)
  v16hi __builtin_ia32_pshufhw256 (v16hi,int)
  v16hi __builtin_ia32_pshuflw256 (v16hi,int)
  v32qi __builtin_ia32_psignb256 (v32qi,v32qi)
  v16hi __builtin_ia32_psignw256 (v16hi,v16hi)
  v8si __builtin_ia32_psignd256 (v8si,v8si)
  v4di __builtin_ia32_pslldqi256 (v4di,int)
  v16hi __builtin_ia32_psllwi256 (16hi,int)
  v16hi __builtin_ia32_psllw256(v16hi,v8hi)
  v8si __builtin_ia32_pslldi256 (v8si,int)
  v8si __builtin_ia32_pslld256(v8si,v4si)
  v4di __builtin_ia32_psllqi256 (v4di,int)
  v4di __builtin_ia32_psllq256(v4di,v2di)
  v16hi __builtin_ia32_psrawi256 (v16hi,int)
  v16hi __builtin_ia32_psraw256 (v16hi,v8hi)
  v8si __builtin_ia32_psradi256 (v8si,int)
  v8si __builtin_ia32_psrad256 (v8si,v4si)
  v4di __builtin_ia32_psrldqi256 (v4di, int)
  v16hi __builtin_ia32_psrlwi256 (v16hi,int)
  v16hi __builtin_ia32_psrlw256 (v16hi,v8hi)
  v8si __builtin_ia32_psrldi256 (v8si,int)
  v8si __builtin_ia32_psrld256 (v8si,v4si)
  v4di __builtin_ia32_psrlqi256 (v4di,int)
  v4di __builtin_ia32_psrlq256(v4di,v2di)
  v32qi __builtin_ia32_psubb256 (v32qi,v32qi)
  v32hi __builtin_ia32_psubw256 (v16hi,v16hi)
  v8si __builtin_ia32_psubd256 (v8si,v8si)
  v4di __builtin_ia32_psubq256 (v4di,v4di)
  v32qi __builtin_ia32_psubsb256 (v32qi,v32qi)
  v16hi __builtin_ia32_psubsw256 (v16hi,v16hi)
  v32qi __builtin_ia32_psubusb256 (v32qi,v32qi)
  v16hi __builtin_ia32_psubusw256 (v16hi,v16hi)
  v32qi __builtin_ia32_punpckhbw256 (v32qi,v32qi)
  v16hi __builtin_ia32_punpckhwd256 (v16hi,v16hi)
  v8si __builtin_ia32_punpckhdq256 (v8si,v8si)
  v4di __builtin_ia32_punpckhqdq256 (v4di,v4di)
  v32qi __builtin_ia32_punpcklbw256 (v32qi,v32qi)
  v16hi __builtin_ia32_punpcklwd256 (v16hi,v16hi)
  v8si __builtin_ia32_punpckldq256 (v8si,v8si)
  v4di __builtin_ia32_punpcklqdq256 (v4di,v4di)
  v4di __builtin_ia32_pxor256 (v4di,v4di)
  v4di __builtin_ia32_movntdqa256 (pv4di)
  v4sf __builtin_ia32_vbroadcastss_ps (v4sf)
  v8sf __builtin_ia32_vbroadcastss_ps256 (v4sf)
  v4df __builtin_ia32_vbroadcastsd_pd256 (v2df)
  v4di __builtin_ia32_vbroadcastsi256 (v2di)
  v4si __builtin_ia32_pblendd128 (v4si,v4si)
  v8si __builtin_ia32_pblendd256 (v8si,v8si)
  v32qi __builtin_ia32_pbroadcastb256 (v16qi)
  v16hi __builtin_ia32_pbroadcastw256 (v8hi)
  v8si __builtin_ia32_pbroadcastd256 (v4si)
  v4di __builtin_ia32_pbroadcastq256 (v2di)
  v16qi __builtin_ia32_pbroadcastb128 (v16qi)
  v8hi __builtin_ia32_pbroadcastw128 (v8hi)
  v4si __builtin_ia32_pbroadcastd128 (v4si)
  v2di __builtin_ia32_pbroadcastq128 (v2di)
  v8si __builtin_ia32_permvarsi256 (v8si,v8si)
  v4df __builtin_ia32_permdf256 (v4df,int)
  v8sf __builtin_ia32_permvarsf256 (v8sf,v8sf)
  v4di __builtin_ia32_permdi256 (v4di,int)
  v4di __builtin_ia32_permti256 (v4di,v4di,int)
  v4di __builtin_ia32_extract128i256 (v4di,int)
  v4di __builtin_ia32_insert128i256 (v4di,v2di,int)
  v8si __builtin_ia32_maskloadd256 (pcv8si,v8si)
  v4di __builtin_ia32_maskloadq256 (pcv4di,v4di)
  v4si __builtin_ia32_maskloadd (pcv4si,v4si)
  v2di __builtin_ia32_maskloadq (pcv2di,v2di)
  void __builtin_ia32_maskstored256 (pv8si,v8si,v8si)
  void __builtin_ia32_maskstoreq256 (pv4di,v4di,v4di)
  void __builtin_ia32_maskstored (pv4si,v4si,v4si)
  void __builtin_ia32_maskstoreq (pv2di,v2di,v2di)
  v8si __builtin_ia32_psllv8si (v8si,v8si)
  v4si __builtin_ia32_psllv4si (v4si,v4si)
  v4di __builtin_ia32_psllv4di (v4di,v4di)
  v2di __builtin_ia32_psllv2di (v2di,v2di)
  v8si __builtin_ia32_psrav8si (v8si,v8si)
  v4si __builtin_ia32_psrav4si (v4si,v4si)
  v8si __builtin_ia32_psrlv8si (v8si,v8si)
  v4si __builtin_ia32_psrlv4si (v4si,v4si)
  v4di __builtin_ia32_psrlv4di (v4di,v4di)
  v2di __builtin_ia32_psrlv2di (v2di,v2di)
  v2df __builtin_ia32_gathersiv2df (v2df, pcdouble,v4si,v2df,int)
  v4df __builtin_ia32_gathersiv4df (v4df, pcdouble,v4si,v4df,int)
  v2df __builtin_ia32_gatherdiv2df (v2df, pcdouble,v2di,v2df,int)
  v4df __builtin_ia32_gatherdiv4df (v4df, pcdouble,v4di,v4df,int)
  v4sf __builtin_ia32_gathersiv4sf (v4sf, pcfloat,v4si,v4sf,int)
  v8sf __builtin_ia32_gathersiv8sf (v8sf, pcfloat,v8si,v8sf,int)
  v4sf __builtin_ia32_gatherdiv4sf (v4sf, pcfloat,v2di,v4sf,int)
  v4sf __builtin_ia32_gatherdiv4sf256 (v4sf, pcfloat,v4di,v4sf,int)
  v2di __builtin_ia32_gathersiv2di (v2di, pcint64,v4si,v2di,int)
  v4di __builtin_ia32_gathersiv4di (v4di, pcint64,v4si,v4di,int)
  v2di __builtin_ia32_gatherdiv2di (v2di, pcint64,v2di,v2di,int)
  v4di __builtin_ia32_gatherdiv4di (v4di, pcint64,v4di,v4di,int)
  v4si __builtin_ia32_gathersiv4si (v4si, pcint,v4si,v4si,int)
  v8si __builtin_ia32_gathersiv8si (v8si, pcint,v8si,v8si,int)
  v4si __builtin_ia32_gatherdiv4si (v4si, pcint,v2di,v4si,int)
  v4si __builtin_ia32_gatherdiv4si256 (v4si, pcint,v4di,v4si,int)

The following built-in functions are available when :option:`-maes` is
used.  All of them generate the machine instruction that is part of the
name.

.. code-block:: c++

  v2di __builtin_ia32_aesenc128 (v2di, v2di)
  v2di __builtin_ia32_aesenclast128 (v2di, v2di)
  v2di __builtin_ia32_aesdec128 (v2di, v2di)
  v2di __builtin_ia32_aesdeclast128 (v2di, v2di)
  v2di __builtin_ia32_aeskeygenassist128 (v2di, const int)
  v2di __builtin_ia32_aesimc128 (v2di)

The following built-in function is available when :option:`-mpclmul` is
used.

v2di __builtin_ia32_pclmulqdq128 (v2di, v2di, const int)
  Generates the ``pclmulqdq`` machine instruction.

The following built-in function is available when :option:`-mfsgsbase` is
used.  All of them generate the machine instruction that is part of the
name.

.. code-block:: c++

  unsigned int __builtin_ia32_rdfsbase32 (void)
  unsigned long long __builtin_ia32_rdfsbase64 (void)
  unsigned int __builtin_ia32_rdgsbase32 (void)
  unsigned long long __builtin_ia32_rdgsbase64 (void)
  void _writefsbase_u32 (unsigned int)
  void _writefsbase_u64 (unsigned long long)
  void _writegsbase_u32 (unsigned int)
  void _writegsbase_u64 (unsigned long long)

The following built-in function is available when :option:`-mrdrnd` is
used.  All of them generate the machine instruction that is part of the
name.

.. code-block:: c++

  unsigned int __builtin_ia32_rdrand16_step (unsigned short *)
  unsigned int __builtin_ia32_rdrand32_step (unsigned int *)
  unsigned int __builtin_ia32_rdrand64_step (unsigned long long *)

The following built-in functions are available when :option:`-msse4a` is used.
All of them generate the machine instruction that is part of the name.

.. code-block:: c++

  void __builtin_ia32_movntsd (double *, v2df)
  void __builtin_ia32_movntss (float *, v4sf)
  v2di __builtin_ia32_extrq  (v2di, v16qi)
  v2di __builtin_ia32_extrqi (v2di, const unsigned int, const unsigned int)
  v2di __builtin_ia32_insertq (v2di, v2di)
  v2di __builtin_ia32_insertqi (v2di, v2di, const unsigned int, const unsigned int)

The following built-in functions are available when :option:`-mxop` is used.

.. code-block:: c++

  v2df __builtin_ia32_vfrczpd (v2df)
  v4sf __builtin_ia32_vfrczps (v4sf)
  v2df __builtin_ia32_vfrczsd (v2df)
  v4sf __builtin_ia32_vfrczss (v4sf)
  v4df __builtin_ia32_vfrczpd256 (v4df)
  v8sf __builtin_ia32_vfrczps256 (v8sf)
  v2di __builtin_ia32_vpcmov (v2di, v2di, v2di)
  v2di __builtin_ia32_vpcmov_v2di (v2di, v2di, v2di)
  v4si __builtin_ia32_vpcmov_v4si (v4si, v4si, v4si)
  v8hi __builtin_ia32_vpcmov_v8hi (v8hi, v8hi, v8hi)
  v16qi __builtin_ia32_vpcmov_v16qi (v16qi, v16qi, v16qi)
  v2df __builtin_ia32_vpcmov_v2df (v2df, v2df, v2df)
  v4sf __builtin_ia32_vpcmov_v4sf (v4sf, v4sf, v4sf)
  v4di __builtin_ia32_vpcmov_v4di256 (v4di, v4di, v4di)
  v8si __builtin_ia32_vpcmov_v8si256 (v8si, v8si, v8si)
  v16hi __builtin_ia32_vpcmov_v16hi256 (v16hi, v16hi, v16hi)
  v32qi __builtin_ia32_vpcmov_v32qi256 (v32qi, v32qi, v32qi)
  v4df __builtin_ia32_vpcmov_v4df256 (v4df, v4df, v4df)
  v8sf __builtin_ia32_vpcmov_v8sf256 (v8sf, v8sf, v8sf)
  v16qi __builtin_ia32_vpcomeqb (v16qi, v16qi)
  v8hi __builtin_ia32_vpcomeqw (v8hi, v8hi)
  v4si __builtin_ia32_vpcomeqd (v4si, v4si)
  v2di __builtin_ia32_vpcomeqq (v2di, v2di)
  v16qi __builtin_ia32_vpcomequb (v16qi, v16qi)
  v4si __builtin_ia32_vpcomequd (v4si, v4si)
  v2di __builtin_ia32_vpcomequq (v2di, v2di)
  v8hi __builtin_ia32_vpcomequw (v8hi, v8hi)
  v8hi __builtin_ia32_vpcomeqw (v8hi, v8hi)
  v16qi __builtin_ia32_vpcomfalseb (v16qi, v16qi)
  v4si __builtin_ia32_vpcomfalsed (v4si, v4si)
  v2di __builtin_ia32_vpcomfalseq (v2di, v2di)
  v16qi __builtin_ia32_vpcomfalseub (v16qi, v16qi)
  v4si __builtin_ia32_vpcomfalseud (v4si, v4si)
  v2di __builtin_ia32_vpcomfalseuq (v2di, v2di)
  v8hi __builtin_ia32_vpcomfalseuw (v8hi, v8hi)
  v8hi __builtin_ia32_vpcomfalsew (v8hi, v8hi)
  v16qi __builtin_ia32_vpcomgeb (v16qi, v16qi)
  v4si __builtin_ia32_vpcomged (v4si, v4si)
  v2di __builtin_ia32_vpcomgeq (v2di, v2di)
  v16qi __builtin_ia32_vpcomgeub (v16qi, v16qi)
  v4si __builtin_ia32_vpcomgeud (v4si, v4si)
  v2di __builtin_ia32_vpcomgeuq (v2di, v2di)
  v8hi __builtin_ia32_vpcomgeuw (v8hi, v8hi)
  v8hi __builtin_ia32_vpcomgew (v8hi, v8hi)
  v16qi __builtin_ia32_vpcomgtb (v16qi, v16qi)
  v4si __builtin_ia32_vpcomgtd (v4si, v4si)
  v2di __builtin_ia32_vpcomgtq (v2di, v2di)
  v16qi __builtin_ia32_vpcomgtub (v16qi, v16qi)
  v4si __builtin_ia32_vpcomgtud (v4si, v4si)
  v2di __builtin_ia32_vpcomgtuq (v2di, v2di)
  v8hi __builtin_ia32_vpcomgtuw (v8hi, v8hi)
  v8hi __builtin_ia32_vpcomgtw (v8hi, v8hi)
  v16qi __builtin_ia32_vpcomleb (v16qi, v16qi)
  v4si __builtin_ia32_vpcomled (v4si, v4si)
  v2di __builtin_ia32_vpcomleq (v2di, v2di)
  v16qi __builtin_ia32_vpcomleub (v16qi, v16qi)
  v4si __builtin_ia32_vpcomleud (v4si, v4si)
  v2di __builtin_ia32_vpcomleuq (v2di, v2di)
  v8hi __builtin_ia32_vpcomleuw (v8hi, v8hi)
  v8hi __builtin_ia32_vpcomlew (v8hi, v8hi)
  v16qi __builtin_ia32_vpcomltb (v16qi, v16qi)
  v4si __builtin_ia32_vpcomltd (v4si, v4si)
  v2di __builtin_ia32_vpcomltq (v2di, v2di)
  v16qi __builtin_ia32_vpcomltub (v16qi, v16qi)
  v4si __builtin_ia32_vpcomltud (v4si, v4si)
  v2di __builtin_ia32_vpcomltuq (v2di, v2di)
  v8hi __builtin_ia32_vpcomltuw (v8hi, v8hi)
  v8hi __builtin_ia32_vpcomltw (v8hi, v8hi)
  v16qi __builtin_ia32_vpcomneb (v16qi, v16qi)
  v4si __builtin_ia32_vpcomned (v4si, v4si)
  v2di __builtin_ia32_vpcomneq (v2di, v2di)
  v16qi __builtin_ia32_vpcomneub (v16qi, v16qi)
  v4si __builtin_ia32_vpcomneud (v4si, v4si)
  v2di __builtin_ia32_vpcomneuq (v2di, v2di)
  v8hi __builtin_ia32_vpcomneuw (v8hi, v8hi)
  v8hi __builtin_ia32_vpcomnew (v8hi, v8hi)
  v16qi __builtin_ia32_vpcomtrueb (v16qi, v16qi)
  v4si __builtin_ia32_vpcomtrued (v4si, v4si)
  v2di __builtin_ia32_vpcomtrueq (v2di, v2di)
  v16qi __builtin_ia32_vpcomtrueub (v16qi, v16qi)
  v4si __builtin_ia32_vpcomtrueud (v4si, v4si)
  v2di __builtin_ia32_vpcomtrueuq (v2di, v2di)
  v8hi __builtin_ia32_vpcomtrueuw (v8hi, v8hi)
  v8hi __builtin_ia32_vpcomtruew (v8hi, v8hi)
  v4si __builtin_ia32_vphaddbd (v16qi)
  v2di __builtin_ia32_vphaddbq (v16qi)
  v8hi __builtin_ia32_vphaddbw (v16qi)
  v2di __builtin_ia32_vphadddq (v4si)
  v4si __builtin_ia32_vphaddubd (v16qi)
  v2di __builtin_ia32_vphaddubq (v16qi)
  v8hi __builtin_ia32_vphaddubw (v16qi)
  v2di __builtin_ia32_vphaddudq (v4si)
  v4si __builtin_ia32_vphadduwd (v8hi)
  v2di __builtin_ia32_vphadduwq (v8hi)
  v4si __builtin_ia32_vphaddwd (v8hi)
  v2di __builtin_ia32_vphaddwq (v8hi)
  v8hi __builtin_ia32_vphsubbw (v16qi)
  v2di __builtin_ia32_vphsubdq (v4si)
  v4si __builtin_ia32_vphsubwd (v8hi)
  v4si __builtin_ia32_vpmacsdd (v4si, v4si, v4si)
  v2di __builtin_ia32_vpmacsdqh (v4si, v4si, v2di)
  v2di __builtin_ia32_vpmacsdql (v4si, v4si, v2di)
  v4si __builtin_ia32_vpmacssdd (v4si, v4si, v4si)
  v2di __builtin_ia32_vpmacssdqh (v4si, v4si, v2di)
  v2di __builtin_ia32_vpmacssdql (v4si, v4si, v2di)
  v4si __builtin_ia32_vpmacsswd (v8hi, v8hi, v4si)
  v8hi __builtin_ia32_vpmacssww (v8hi, v8hi, v8hi)
  v4si __builtin_ia32_vpmacswd (v8hi, v8hi, v4si)
  v8hi __builtin_ia32_vpmacsww (v8hi, v8hi, v8hi)
  v4si __builtin_ia32_vpmadcsswd (v8hi, v8hi, v4si)
  v4si __builtin_ia32_vpmadcswd (v8hi, v8hi, v4si)
  v16qi __builtin_ia32_vpperm (v16qi, v16qi, v16qi)
  v16qi __builtin_ia32_vprotb (v16qi, v16qi)
  v4si __builtin_ia32_vprotd (v4si, v4si)
  v2di __builtin_ia32_vprotq (v2di, v2di)
  v8hi __builtin_ia32_vprotw (v8hi, v8hi)
  v16qi __builtin_ia32_vpshab (v16qi, v16qi)
  v4si __builtin_ia32_vpshad (v4si, v4si)
  v2di __builtin_ia32_vpshaq (v2di, v2di)
  v8hi __builtin_ia32_vpshaw (v8hi, v8hi)
  v16qi __builtin_ia32_vpshlb (v16qi, v16qi)
  v4si __builtin_ia32_vpshld (v4si, v4si)
  v2di __builtin_ia32_vpshlq (v2di, v2di)
  v8hi __builtin_ia32_vpshlw (v8hi, v8hi)

The following built-in functions are available when :option:`-mfma4` is used.
All of them generate the machine instruction that is part of the name.

.. code-block:: c++

  v2df __builtin_ia32_vfmaddpd (v2df, v2df, v2df)
  v4sf __builtin_ia32_vfmaddps (v4sf, v4sf, v4sf)
  v2df __builtin_ia32_vfmaddsd (v2df, v2df, v2df)
  v4sf __builtin_ia32_vfmaddss (v4sf, v4sf, v4sf)
  v2df __builtin_ia32_vfmsubpd (v2df, v2df, v2df)
  v4sf __builtin_ia32_vfmsubps (v4sf, v4sf, v4sf)
  v2df __builtin_ia32_vfmsubsd (v2df, v2df, v2df)
  v4sf __builtin_ia32_vfmsubss (v4sf, v4sf, v4sf)
  v2df __builtin_ia32_vfnmaddpd (v2df, v2df, v2df)
  v4sf __builtin_ia32_vfnmaddps (v4sf, v4sf, v4sf)
  v2df __builtin_ia32_vfnmaddsd (v2df, v2df, v2df)
  v4sf __builtin_ia32_vfnmaddss (v4sf, v4sf, v4sf)
  v2df __builtin_ia32_vfnmsubpd (v2df, v2df, v2df)
  v4sf __builtin_ia32_vfnmsubps (v4sf, v4sf, v4sf)
  v2df __builtin_ia32_vfnmsubsd (v2df, v2df, v2df)
  v4sf __builtin_ia32_vfnmsubss (v4sf, v4sf, v4sf)
  v2df __builtin_ia32_vfmaddsubpd  (v2df, v2df, v2df)
  v4sf __builtin_ia32_vfmaddsubps  (v4sf, v4sf, v4sf)
  v2df __builtin_ia32_vfmsubaddpd  (v2df, v2df, v2df)
  v4sf __builtin_ia32_vfmsubaddps  (v4sf, v4sf, v4sf)
  v4df __builtin_ia32_vfmaddpd256 (v4df, v4df, v4df)
  v8sf __builtin_ia32_vfmaddps256 (v8sf, v8sf, v8sf)
  v4df __builtin_ia32_vfmsubpd256 (v4df, v4df, v4df)
  v8sf __builtin_ia32_vfmsubps256 (v8sf, v8sf, v8sf)
  v4df __builtin_ia32_vfnmaddpd256 (v4df, v4df, v4df)
  v8sf __builtin_ia32_vfnmaddps256 (v8sf, v8sf, v8sf)
  v4df __builtin_ia32_vfnmsubpd256 (v4df, v4df, v4df)
  v8sf __builtin_ia32_vfnmsubps256 (v8sf, v8sf, v8sf)
  v4df __builtin_ia32_vfmaddsubpd256 (v4df, v4df, v4df)
  v8sf __builtin_ia32_vfmaddsubps256 (v8sf, v8sf, v8sf)
  v4df __builtin_ia32_vfmsubaddpd256 (v4df, v4df, v4df)
  v8sf __builtin_ia32_vfmsubaddps256 (v8sf, v8sf, v8sf)

The following built-in functions are available when :option:`-mlwp` is used.

.. code-block:: c++

  void __builtin_ia32_llwpcb16 (void *);
  void __builtin_ia32_llwpcb32 (void *);
  void __builtin_ia32_llwpcb64 (void *);
  void * __builtin_ia32_llwpcb16 (void);
  void * __builtin_ia32_llwpcb32 (void);
  void * __builtin_ia32_llwpcb64 (void);
  void __builtin_ia32_lwpval16 (unsigned short, unsigned int, unsigned short)
  void __builtin_ia32_lwpval32 (unsigned int, unsigned int, unsigned int)
  void __builtin_ia32_lwpval64 (unsigned __int64, unsigned int, unsigned int)
  unsigned char __builtin_ia32_lwpins16 (unsigned short, unsigned int, unsigned short)
  unsigned char __builtin_ia32_lwpins32 (unsigned int, unsigned int, unsigned int)
  unsigned char __builtin_ia32_lwpins64 (unsigned __int64, unsigned int, unsigned int)

The following built-in functions are available when :option:`-mbmi` is used.
All of them generate the machine instruction that is part of the name.

.. code-block:: c++

  unsigned int __builtin_ia32_bextr_u32(unsigned int, unsigned int);
  unsigned long long __builtin_ia32_bextr_u64 (unsigned long long, unsigned long long);

The following built-in functions are available when :option:`-mbmi2` is used.
All of them generate the machine instruction that is part of the name.

.. code-block:: c++

  unsigned int _bzhi_u32 (unsigned int, unsigned int)
  unsigned int _pdep_u32 (unsigned int, unsigned int)
  unsigned int _pext_u32 (unsigned int, unsigned int)
  unsigned long long _bzhi_u64 (unsigned long long, unsigned long long)
  unsigned long long _pdep_u64 (unsigned long long, unsigned long long)
  unsigned long long _pext_u64 (unsigned long long, unsigned long long)

The following built-in functions are available when :option:`-mlzcnt` is used.
All of them generate the machine instruction that is part of the name.

.. code-block:: c++

  unsigned short __builtin_ia32_lzcnt_16(unsigned short);
  unsigned int __builtin_ia32_lzcnt_u32(unsigned int);
  unsigned long long __builtin_ia32_lzcnt_u64 (unsigned long long);

The following built-in functions are available when :option:`-mfxsr` is used.
All of them generate the machine instruction that is part of the name.

.. code-block:: c++

  void __builtin_ia32_fxsave (void *)
  void __builtin_ia32_fxrstor (void *)
  void __builtin_ia32_fxsave64 (void *)
  void __builtin_ia32_fxrstor64 (void *)

The following built-in functions are available when :option:`-mxsave` is used.
All of them generate the machine instruction that is part of the name.

.. code-block:: c++

  void __builtin_ia32_xsave (void *, long long)
  void __builtin_ia32_xrstor (void *, long long)
  void __builtin_ia32_xsave64 (void *, long long)
  void __builtin_ia32_xrstor64 (void *, long long)

The following built-in functions are available when :option:`-mxsaveopt` is used.
All of them generate the machine instruction that is part of the name.

.. code-block:: c++

  void __builtin_ia32_xsaveopt (void *, long long)
  void __builtin_ia32_xsaveopt64 (void *, long long)

The following built-in functions are available when :option:`-mtbm` is used.
Both of them generate the immediate form of the bextr machine instruction.

.. code-block:: c++

  unsigned int __builtin_ia32_bextri_u32 (unsigned int, const unsigned int);
  unsigned long long __builtin_ia32_bextri_u64 (unsigned long long, const unsigned long long);

The following built-in functions are available when :option:`-m3dnow` is used.
All of them generate the machine instruction that is part of the name.

.. code-block:: c++

  void __builtin_ia32_femms (void)
  v8qi __builtin_ia32_pavgusb (v8qi, v8qi)
  v2si __builtin_ia32_pf2id (v2sf)
  v2sf __builtin_ia32_pfacc (v2sf, v2sf)
  v2sf __builtin_ia32_pfadd (v2sf, v2sf)
  v2si __builtin_ia32_pfcmpeq (v2sf, v2sf)
  v2si __builtin_ia32_pfcmpge (v2sf, v2sf)
  v2si __builtin_ia32_pfcmpgt (v2sf, v2sf)
  v2sf __builtin_ia32_pfmax (v2sf, v2sf)
  v2sf __builtin_ia32_pfmin (v2sf, v2sf)
  v2sf __builtin_ia32_pfmul (v2sf, v2sf)
  v2sf __builtin_ia32_pfrcp (v2sf)
  v2sf __builtin_ia32_pfrcpit1 (v2sf, v2sf)
  v2sf __builtin_ia32_pfrcpit2 (v2sf, v2sf)
  v2sf __builtin_ia32_pfrsqrt (v2sf)
  v2sf __builtin_ia32_pfsub (v2sf, v2sf)
  v2sf __builtin_ia32_pfsubr (v2sf, v2sf)
  v2sf __builtin_ia32_pi2fd (v2si)
  v4hi __builtin_ia32_pmulhrw (v4hi, v4hi)

The following built-in functions are available when both :option:`-m3dnow`
and :option:`-march=athlon` are used.  All of them generate the machine
instruction that is part of the name.

.. code-block:: c++

  v2si __builtin_ia32_pf2iw (v2sf)
  v2sf __builtin_ia32_pfnacc (v2sf, v2sf)
  v2sf __builtin_ia32_pfpnacc (v2sf, v2sf)
  v2sf __builtin_ia32_pi2fw (v2si)
  v2sf __builtin_ia32_pswapdsf (v2sf)
  v2si __builtin_ia32_pswapdsi (v2si)

The following built-in functions are available when :option:`-mrtm` is used
They are used for restricted transactional memory. These are the internal
low level functions. Normally the functions in 
x86 transactional memory intrinsics should be used instead.

.. code-block:: c++

  int __builtin_ia32_xbegin ()
  void __builtin_ia32_xend ()
  void __builtin_ia32_xabort (status)
  int __builtin_ia32_xtest ()

:: _x86-transactional-memory-intrinsics:

x86 Transactional Memory Intrinsics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These hardware transactional memory intrinsics for x86 allow you to use
memory transactions with RTM (Restricted Transactional Memory).
This support is enabled with the :option:`-mrtm` option.
For using HLE (Hardware Lock Elision) see 
x86 specific memory model extensions for transactional memory instead.

A memory transaction commits all changes to memory in an atomic way,
as visible to other threads. If the transaction fails it is rolled back
and all side effects discarded.

Generally there is no guarantee that a memory transaction ever succeeds
and suitable fallback code always needs to be supplied.

.. index:: _xbegin

  RTM Function unsigned _xbegin ()
Start a RTM (Restricted Transactional Memory) transaction. 
Returns ``_XBEGIN_STARTED`` when the transaction
started successfully (note this is not 0, so the constant has to be 
explicitly tested).  

If the transaction aborts, all side-effects 
are undone and an abort code encoded as a bit mask is returned.
The following macros are defined:

_XABORT_EXPLICIT
  Transaction was explicitly aborted with ``_xabort``.  The parameter passed
  to ``_xabort`` is available with ``_XABORT_CODE(status)``.

_XABORT_RETRY
  Transaction retry is possible.

_XABORT_CONFLICT
  Transaction abort due to a memory conflict with another thread.

_XABORT_CAPACITY
  Transaction abort due to the transaction using too much memory.

_XABORT_DEBUG
  Transaction abort due to a debug trap.

_XABORT_NESTED
  Transaction abort in an inner nested transaction.

There is no guarantee
any transaction ever succeeds, so there always needs to be a valid
fallback path.

.. index:: _xend

  RTM Function void _xend ()
Commit the current transaction. When no transaction is active this faults.
All memory side-effects of the transaction become visible
to other threads in an atomic manner.

.. index:: _xtest

  RTM Function int _xtest ()
Return a nonzero value if a transaction is currently active, otherwise 0.

.. index:: _xabort

  RTM Function void _xabort (status)
Abort the current transaction. When no transaction is active this is a no-op.
The ``status`` is an 8-bit constant; its value is encoded in the return 
value from ``_xbegin``.

Here is an example showing handling for ``_XABORT_RETRY``
and a fallback path for other failures:

.. code-block:: c++

  #include <immintrin.h>

  int n_tries, max_tries;
  unsigned status = _XABORT_EXPLICIT;
  ...

  for (n_tries = 0; n_tries < max_tries; n_tries++) 
    {
      status = _xbegin ();
      if (status == _XBEGIN_STARTED || !(status & _XABORT_RETRY))
        break;
    }
  if (status == _XBEGIN_STARTED) 
    {
      ... transaction code...
      _xend ();
    } 
  else 
    {
      ... non-transactional fallback path...
    }

Note that, in most cases, the transactional and non-transactional code
must synchronize together to ensure consistency.

