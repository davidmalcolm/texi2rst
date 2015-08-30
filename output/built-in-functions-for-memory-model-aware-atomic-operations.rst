  .. ___atomic-builtins:

Built-in Functions for Memory Model Aware Atomic Operations
***********************************************************

The following built-in functions approximately match the requirements
for C++11 concurrency and memory models.  They are all
identified by being prefixed with __atomic and most are
overloaded so that they work with multiple types.

These functions are intended to replace the legacy __sync
builtins.  The main difference is that the memory model to be used is a
parameter to the functions.  New code should always use the
__atomic builtins rather than the __sync builtins.

Note that the __atomic builtins assume that programs will
conform to the C++11 model for concurrency.  In particular, they assume
that programs are free of data races.  See the C++11 standard for
detailed definitions.

The __atomic builtins can be used with any integral scalar or
pointer type that is 1, 2, 4, or 8 bytes in length.  16-byte integral
types are also allowed if __int128 (see :ref:`__int128`) is
supported by the architecture.

The four non-arithmetic functions (load, store, exchange, and 
compare_exchange) all have a generic version as well.  This generic
version works on any data type.  If the data type size maps to one
of the integral sizes that may have lock free support, the generic
version uses the lock free built-in function.  Otherwise an
external call is left to be resolved at run time.  This external call is
the same format with the addition of a size_t parameter inserted
as the first parameter indicating the size of the object being pointed to.
All objects must be the same size.

There are 6 different memory models that can be specified.  These map
to the C++11 memory models with the same names, see the C++11 standard
or the http://gcc.gnu.org/wiki/Atomic/GCCMM/AtomicSyncGCC wiki
on atomic synchronization for detailed definitions.  Individual
targets may also support additional memory models for use on specific
architectures.  Refer to the target documentation for details of
these.

The memory models integrate both barriers to code motion as well as
synchronization requirements with other threads.  They are listed here
in approximately ascending order of strength.

__ATOMIC_RELAXED
  No barriers or synchronization.

__ATOMIC_CONSUME
  Data dependency only for both barrier and synchronization with another
  thread.

__ATOMIC_ACQUIRE
  Barrier to hoisting of code and synchronizes with release (or stronger)
  semantic stores from another thread.

__ATOMIC_RELEASE
  Barrier to sinking of code and synchronizes with acquire (or stronger)
  semantic loads from another thread.

__ATOMIC_ACQ_REL
  Barrier in both directions and synchronizes with acquire loads and
  release stores in another thread.

__ATOMIC_SEQ_CST
  Barrier in both directions and synchronizes with acquire loads and
  release stores in all threads.

  Note that the scope of a C++11 memory model depends on whether or not
the function being called is a *fence* (such as
__atomic_thread_fence).  In a fence, all memory accesses are
subject to the restrictions of the memory model.  When the function is
an operation on a location, the restrictions apply only to those
memory accesses that could affect or that could depend on the
location.

Target architectures are encouraged to provide their own patterns for
each of these built-in functions.  If no target is provided, the original
non-memory model set of __sync atomic built-in functions are
used, along with any required synchronization fences surrounding it in
order to achieve the proper behavior.  Execution in this case is subject
to the same restrictions as those built-in functions.

If there is no pattern or mechanism to provide a lock free instruction
sequence, a call is made to an external routine with the same parameters
to be resolved at run time.

When implementing patterns for these built-in functions, the memory model
parameter can be ignored as long as the pattern implements the most
restrictive ``__ATOMIC_SEQ_CST`` model.  Any of the other memory models
execute correctly with this memory model but they may not execute as
efficiently as they could with a more appropriate implementation of the
relaxed requirements.

Note that the C++11 standard allows for the memory model parameter to be
determined at run time rather than at compile time.  These built-in
functions map any run-time value to ``__ATOMIC_SEQ_CST`` rather
than invoke a runtime library call or inline a switch statement.  This is
standard compliant, safe, and the simplest approach for now.

The memory model parameter is a signed int, but only the lower 16 bits are
reserved for the memory model.  The remainder of the signed int is reserved
for target use and should be 0.  Use of the predefined atomic values
ensures proper usage.

.. index:: __atomic_load_n

Built-in Function``type``__atomic_load_n(``type``*ptr,intmemmodel)This built-in function implements an atomic load operation.  It returns the
contents of ``*``ptr````.

The valid memory model variants are
``__ATOMIC_RELAXED``, ``__ATOMIC_SEQ_CST``, ``__ATOMIC_ACQUIRE``,
and ``__ATOMIC_CONSUME``.

.. index:: __atomic_load

Built-in Functionvoid__atomic_load(``type``*ptr,``type``*ret,intmemmodel)This is the generic version of an atomic load.  It returns the
contents of ``*``ptr```` in ``*``ret````.

.. index:: __atomic_store_n

Built-in Functionvoid__atomic_store_n(``type``*ptr,``type``val,intmemmodel)This built-in function implements an atomic store operation.  It writes 
````val```` into ``*``ptr````.  

The valid memory model variants are
``__ATOMIC_RELAXED``, ``__ATOMIC_SEQ_CST``, and ``__ATOMIC_RELEASE``.

.. index:: __atomic_store

Built-in Functionvoid__atomic_store(``type``*ptr,``type``*val,intmemmodel)This is the generic version of an atomic store.  It stores the value
of ``*``val```` into ``*``ptr````.

.. index:: __atomic_exchange_n

Built-in Function``type``__atomic_exchange_n(``type``*ptr,``type``val,intmemmodel)This built-in function implements an atomic exchange operation.  It writes
``val`` into ``*``ptr````, and returns the previous contents of
``*``ptr````.

The valid memory model variants are
``__ATOMIC_RELAXED``, ``__ATOMIC_SEQ_CST``, ``__ATOMIC_ACQUIRE``,
``__ATOMIC_RELEASE``, and ``__ATOMIC_ACQ_REL``.

.. index:: __atomic_exchange

Built-in Functionvoid__atomic_exchange(``type``*ptr,``type``*val,``type``*ret,intmemmodel)This is the generic version of an atomic exchange.  It stores the
contents of ``*``val```` into ``*``ptr````. The original value
of ``*``ptr```` is copied into ``*``ret````.

.. index:: __atomic_compare_exchange_n

Built-in Functionbool__atomic_compare_exchange_n(``type``*ptr,``type``*expected,``type``desired,boolweak,intsuccess_memmodel,intfailure_memmodel)This built-in function implements an atomic compare and exchange operation.
This compares the contents of ``*``ptr```` with the contents of
``*``expected````. If equal, the operation is a *read-modify-write*
which writes ``desired`` into ``*``ptr````.  If they are not
equal, the operation is a *read* and the current contents of
``*``ptr```` is written into ``*``expected````.  ``weak`` is true
for weak compare_exchange, and false for the strong variation.  Many targets 
only offer the strong variation and ignore the parameter.  When in doubt, use
the strong variation.

True is returned if ``desired`` is written into
``*``ptr```` and the operation is considered to conform to the
memory model specified by ``success_memmodel``.  There are no
restrictions on what memory model can be used here.

False is returned otherwise, and the operation is considered to conform
to ``failure_memmodel``. This memory model cannot be
``__ATOMIC_RELEASE`` nor ``__ATOMIC_ACQ_REL``.  It also cannot be a
stronger model than that specified by ``success_memmodel``.

.. index:: __atomic_compare_exchange

Built-in Functionbool__atomic_compare_exchange(``type``*ptr,``type``*expected,``type``*desired,boolweak,intsuccess_memmodel,intfailure_memmodel)This built-in function implements the generic version of
``__atomic_compare_exchange``.  The function is virtually identical to
``__atomic_compare_exchange_n``, except the desired value is also a
pointer.

.. index:: __atomic_add_fetch

Built-in Function``type``__atomic_add_fetch(``type``*ptr,``type``val,intmemmodel)
.. index:: __atomic_sub_fetch

Built-in Function``type``__atomic_sub_fetch(``type``*ptr,``type``val,intmemmodel)
.. index:: __atomic_and_fetch

Built-in Function``type``__atomic_and_fetch(``type``*ptr,``type``val,intmemmodel)
.. index:: __atomic_xor_fetch

Built-in Function``type``__atomic_xor_fetch(``type``*ptr,``type``val,intmemmodel)
.. index:: __atomic_or_fetch

Built-in Function``type``__atomic_or_fetch(``type``*ptr,``type``val,intmemmodel)
.. index:: __atomic_nand_fetch

Built-in Function``type``__atomic_nand_fetch(``type``*ptr,``type``val,intmemmodel)These built-in functions perform the operation suggested by the name, and
return the result of the operation. That is,

.. code-block:: c++

  { *ptr ``op``= val; return *ptr; }

All memory models are valid.

.. index:: __atomic_fetch_add

Built-in Function``type``__atomic_fetch_add(``type``*ptr,``type``val,intmemmodel)
.. index:: __atomic_fetch_sub

Built-in Function``type``__atomic_fetch_sub(``type``*ptr,``type``val,intmemmodel)
.. index:: __atomic_fetch_and

Built-in Function``type``__atomic_fetch_and(``type``*ptr,``type``val,intmemmodel)
.. index:: __atomic_fetch_xor

Built-in Function``type``__atomic_fetch_xor(``type``*ptr,``type``val,intmemmodel)
.. index:: __atomic_fetch_or

Built-in Function``type``__atomic_fetch_or(``type``*ptr,``type``val,intmemmodel)
.. index:: __atomic_fetch_nand

Built-in Function``type``__atomic_fetch_nand(``type``*ptr,``type``val,intmemmodel)These built-in functions perform the operation suggested by the name, and
return the value that had previously been in ``*``ptr````.  That is,

.. code-block:: c++

  { tmp = *ptr; *ptr ``op``= val; return tmp; }

All memory models are valid.

.. index:: __atomic_test_and_set

Built-in Functionbool__atomic_test_and_set(void*ptr,intmemmodel)This built-in function performs an atomic test-and-set operation on
the byte at ``*``ptr````.  The byte is set to some implementation
defined nonzero 'set' value and the return value is ``true`` if and only
if the previous contents were 'set'.
It should be only used for operands of type ``bool`` or ``char``. For 
other types only part of the value may be set.

All memory models are valid.

.. index:: __atomic_clear

Built-in Functionvoid__atomic_clear(bool*ptr,intmemmodel)This built-in function performs an atomic clear operation on
``*``ptr````.  After the operation, ``*``ptr```` contains 0.
It should be only used for operands of type ``bool`` or ``char`` and 
in conjunction with ``__atomic_test_and_set``.
For other types it may only clear partially. If the type is not ``bool``
prefer using ``__atomic_store``.

The valid memory model variants are
``__ATOMIC_RELAXED``, ``__ATOMIC_SEQ_CST``, and
``__ATOMIC_RELEASE``.

.. index:: __atomic_thread_fence

Built-in Functionvoid__atomic_thread_fence(intmemmodel)This built-in function acts as a synchronization fence between threads
based on the specified memory model.

All memory orders are valid.

.. index:: __atomic_signal_fence

Built-in Functionvoid__atomic_signal_fence(intmemmodel)This built-in function acts as a synchronization fence between a thread
and signal handlers based in the same thread.

All memory orders are valid.

.. index:: __atomic_always_lock_free

Built-in Functionbool__atomic_always_lock_free(size_tsize,void*ptr)This built-in function returns true if objects of ``size`` bytes always
generate lock free atomic instructions for the target architecture.  
``size`` must resolve to a compile-time constant and the result also
resolves to a compile-time constant.

``ptr`` is an optional pointer to the object that may be used to determine
alignment.  A value of 0 indicates typical alignment should be used.  The 
compiler may also ignore this parameter.

.. code-block:: c++

  if (_atomic_always_lock_free (sizeof (long long), 0))

.. index:: __atomic_is_lock_free

Built-in Functionbool__atomic_is_lock_free(size_tsize,void*ptr)This built-in function returns true if objects of ``size`` bytes always
generate lock free atomic instructions for the target architecture.  If
it is not known to be lock free a call is made to a runtime routine named
``__atomic_is_lock_free``.

``ptr`` is an optional pointer to the object that may be used to determine
alignment.  A value of 0 indicates typical alignment should be used.  The 
compiler may also ignore this parameter.

