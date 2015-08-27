
Legacy ``__sync`` Built-in Functions for Atomic Memory AccessThe following built-in functions
are intended to be compatible with those described
in the Intel Itanium Processor-specific Application Binary Interface,
section 7.4.  As such, they depart from normal GCC practice by not using
the __builtin_ prefix and also by being overloaded so that they
work on multiple types.

The definition given in the Intel documentation allows only for the use of
the types ``int``, ``long``, ``long long`` or their unsigned
counterparts.  GCC allows any integral scalar or pointer type that is
1, 2, 4 or 8 bytes in length.

These functions are implemented in terms of the __atomic
builtins (__atomic Builtins).  They should not be used for new
code which should use the __atomic builtins instead.

Not all operations are supported by all target processors.  If a particular
operation cannot be implemented on the target processor, a warning is
generated and a call to an external function is generated.  The external
function carries the same name as the built-in version,
with an additional suffix
_``n`` where ``n`` is the size of the data type.

.. ??? Should we have a mechanism to suppress this warning?  This is almost
   useful for implementing the operation under the control of an external
   mutex.

In most cases, these built-in functions are considered a :dfn:`full barrier`.
That is,
no memory operand is moved across the operation, either forward or
backward.  Further, instructions are issued as necessary to prevent the
processor from speculating loads across the operation and from queuing stores
after the operation.

All of the routines are described in the Intel documentation to take
'an optional list of variables protected by the memory barrier'.  It's
not clear what is meant by that; it could mean that only the
listed variables are protected, or it could mean a list of additional
variables to be protected.  The list is ignored by GCC which treats it as
empty.  GCC interprets an empty list as meaning that all globally
accessible variables should be protected.

``type`` __sync_fetch_and_add (``type`` *ptr, ``type`` value, ...)``type`` __sync_fetch_and_sub (``type`` *ptr, ``type`` value, ...)``type`` __sync_fetch_and_or (``type`` *ptr, ``type`` value, ...)``type`` __sync_fetch_and_and (``type`` *ptr, ``type`` value, ...)``type`` __sync_fetch_and_xor (``type`` *ptr, ``type`` value, ...)``type`` __sync_fetch_and_nand (``type`` *ptr, ``type`` value, ...)

  .. index:: __sync_fetch_and_add

  .. index:: __sync_fetch_and_sub

  .. index:: __sync_fetch_and_or

  .. index:: __sync_fetch_and_and

  .. index:: __sync_fetch_and_xor

  .. index:: __sync_fetch_and_nand

  These built-in functions perform the operation suggested by the name, and
  returns the value that had previously been in memory.  That is,

  .. code-block:: c++

    { tmp = *ptr; *ptr ``op``= value; return tmp; }
    { tmp = *ptr; *ptr = ~(tmp & value); return tmp; }   // nand

  Note: GCC 4.4 and later implement ``__sync_fetch_and_nand``
  as ``*ptr = ~(tmp & value)`` instead of ``*ptr = ~tmp & value``.

``type`` __sync_add_and_fetch (``type`` *ptr, ``type`` value, ...)``type`` __sync_sub_and_fetch (``type`` *ptr, ``type`` value, ...)``type`` __sync_or_and_fetch (``type`` *ptr, ``type`` value, ...)``type`` __sync_and_and_fetch (``type`` *ptr, ``type`` value, ...)``type`` __sync_xor_and_fetch (``type`` *ptr, ``type`` value, ...)``type`` __sync_nand_and_fetch (``type`` *ptr, ``type`` value, ...)

  .. index:: __sync_add_and_fetch

  .. index:: __sync_sub_and_fetch

  .. index:: __sync_or_and_fetch

  .. index:: __sync_and_and_fetch

  .. index:: __sync_xor_and_fetch

  .. index:: __sync_nand_and_fetch

  These built-in functions perform the operation suggested by the name, and
  return the new value.  That is,

  .. code-block:: c++

    { *ptr ``op``= value; return *ptr; }
    { *ptr = ~(*ptr & value); return *ptr; }   // nand

  Note: GCC 4.4 and later implement ``__sync_nand_and_fetch``
  as ``*ptr = ~(*ptr & value)`` instead of
  ``*ptr = ~*ptr & value``.

bool __sync_bool_compare_and_swap (``type`` *ptr, ``type`` oldval, ``type`` newval, ...)``type`` __sync_val_compare_and_swap (``type`` *ptr, ``type`` oldval, ``type`` newval, ...)

  .. index:: __sync_bool_compare_and_swap

  .. index:: __sync_val_compare_and_swap

  These built-in functions perform an atomic compare and swap.
  That is, if the current
  value of ``*``ptr```` is ``oldval``, then write ``newval`` into
  ``*``ptr````.

  The 'bool' version returns true if the comparison is successful and
  ``newval`` is written.  The 'val' version returns the contents
  of ``*``ptr```` before the operation.

__sync_synchronize (...)

  .. index:: __sync_synchronize

  This built-in function issues a full memory barrier.

``type`` __sync_lock_test_and_set (``type`` *ptr, ``type`` value, ...)

  .. index:: __sync_lock_test_and_set

  This built-in function, as described by Intel, is not a traditional test-and-set
  operation, but rather an atomic exchange operation.  It writes ``value``
  into ``*``ptr````, and returns the previous contents of
  ``*``ptr````.

  Many targets have only minimal support for such locks, and do not support
  a full exchange operation.  In this case, a target may support reduced
  functionality here by which the only valid value to store is the
  immediate constant 1.  The exact value actually stored in ``*``ptr````
  is implementation defined.

  This built-in function is not a full barrier,
  but rather an :dfn:`acquire barrier`.
  This means that references after the operation cannot move to (or be
  speculated to) before the operation, but previous memory stores may not
  be globally visible yet, and previous memory loads may not yet be
  satisfied.

void __sync_lock_release (``type`` *ptr, ...)

  .. index:: __sync_lock_release

  This built-in function releases the lock acquired by
  ``__sync_lock_test_and_set``.
  Normally this means writing the constant 0 to ``*``ptr````.

  This built-in function is not a full barrier,
  but rather a :dfn:`release barrier`.
  This means that all previous memory stores are globally visible, and all
  previous memory loads have been satisfied, but following memory reads
  are not prevented from being speculated to before the barrier.

