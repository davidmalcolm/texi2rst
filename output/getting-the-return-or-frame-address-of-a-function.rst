Getting the Return or Frame Address of a Function
*************************************************

These functions may be used to get information about the callers of a
function.

.. index:: __builtin_return_address

  Built-in Function void * __builtin_return_address (unsigned int ``level``)
This function returns the return address of the current function, or of
one of its callers.  The ``level`` argument is number of frames to
scan up the call stack.  A value of ``0`` yields the return address
of the current function, a value of ``1`` yields the return address
of the caller of the current function, and so forth.  When inlining
the expected behavior is that the function returns the address of
the function that is returned to.  To work around this behavior use
the ``noinline`` function attribute.

The ``level`` argument must be a constant integer.

On some machines it may be impossible to determine the return address of
any function other than the current one; in such cases, or when the top
of the stack has been reached, this function returns ``0`` or a
random value.  In addition, ``__builtin_frame_address`` may be used
to determine if the top of the stack has been reached.

Additional post-processing of the returned value may be needed, see
``__builtin_extract_return_addr``.

This function should only be used with a nonzero argument for debugging
purposes.

.. index:: __builtin_extract_return_addr

  Built-in Function void * __builtin_extract_return_addr (void *``addr``)
The address as returned by ``__builtin_return_address`` may have to be fed
through this function to get the actual encoded address.  For example, on the
31-bit S/390 platform the highest bit has to be masked out, or on SPARC
platforms an offset has to be added for the true next instruction to be
executed.

If no fixup is needed, this function simply passes through ``addr``.

.. index:: __builtin_frob_return_address

  Built-in Function void * __builtin_frob_return_address (void *``addr``)
This function does the reverse of ``__builtin_extract_return_addr``.

.. index:: __builtin_frame_address

  Built-in Function void * __builtin_frame_address (unsigned int ``level``)
This function is similar to ``__builtin_return_address``, but it
returns the address of the function frame rather than the return address
of the function.  Calling ``__builtin_frame_address`` with a value of
``0`` yields the frame address of the current function, a value of
``1`` yields the frame address of the caller of the current function,
and so forth.

The frame is the area on the stack that holds local variables and saved
registers.  The frame address is normally the address of the first word
pushed on to the stack by the function.  However, the exact definition
depends upon the processor and the calling convention.  If the processor
has a dedicated frame pointer register, and the function has a frame,
then ``__builtin_frame_address`` returns the value of the frame
pointer register.

On some machines it may be impossible to determine the frame address of
any function other than the current one; in such cases, or when the top
of the stack has been reached, this function returns ``0`` if
the first frame pointer is properly initialized by the startup code.

This function should only be used with a nonzero argument for debugging
purposes.

