.. _object-size-checking:

Object Size Checking Built-in Functions
***************************************

.. index:: __builtin_object_size

.. index:: __builtin___memcpy_chk

.. index:: __builtin___mempcpy_chk

.. index:: __builtin___memmove_chk

.. index:: __builtin___memset_chk

.. index:: __builtin___strcpy_chk

.. index:: __builtin___stpcpy_chk

.. index:: __builtin___strncpy_chk

.. index:: __builtin___strcat_chk

.. index:: __builtin___strncat_chk

.. index:: __builtin___sprintf_chk

.. index:: __builtin___snprintf_chk

.. index:: __builtin___vsprintf_chk

.. index:: __builtin___vsnprintf_chk

.. index:: __builtin___printf_chk

.. index:: __builtin___vprintf_chk

.. index:: __builtin___fprintf_chk

.. index:: __builtin___vfprintf_chk

GCC implements a limited buffer overflow protection mechanism
that can prevent some buffer overflow attacks.

.. index:: __builtin_object_size

Built-in Functionsize_t__builtin_object_size(void*``ptr``,int``type``)is a built-in construct that returns a constant number of bytes from
``ptr`` to the end of the object ``ptr`` pointer points to
(if known at compile time).  ``__builtin_object_size`` never evaluates
its arguments for side-effects.  If there are any side-effects in them, it
returns ``(size_t) -1`` for ``type`` 0 or 1 and ``(size_t) 0``
for ``type`` 2 or 3.  If there are multiple objects ``ptr`` can
point to and all of them are known at compile time, the returned number
is the maximum of remaining byte counts in those objects if ``type`` & 2 is
0 and minimum if nonzero.  If it is not possible to determine which objects
``ptr`` points to at compile time, ``__builtin_object_size`` should
return ``(size_t) -1`` for ``type`` 0 or 1 and ``(size_t) 0``
for ``type`` 2 or 3.

``type`` is an integer constant from 0 to 3.  If the least significant
bit is clear, objects are whole variables, if it is set, a closest
surrounding subobject is considered the object a pointer points to.
The second bit determines if maximum or minimum of remaining bytes
is computed.

.. code-block:: c++

  struct V { char buf1[10]; int b; char buf2[10]; } var;
  char *p = &var.buf1[1], *q = &var.b;

  /* Here the object p points to is var.  */
  assert (__builtin_object_size (p, 0) == sizeof (var) - 1);
  /* The subobject p points to is var.buf1.  */
  assert (__builtin_object_size (p, 1) == sizeof (var.buf1) - 1);
  /* The object q points to is var.  */
  assert (__builtin_object_size (q, 0)
          == (char *) (&var + 1) - (char *) &var.b);
  /* The subobject q points to is var.b.  */
  assert (__builtin_object_size (q, 1) == sizeof (var.b));

There are built-in functions added for many common string operation
functions, e.g., for ``memcpy`` ``__builtin___memcpy_chk``
built-in is provided.  This built-in has an additional last argument,
which is the number of bytes remaining in object the ``dest``
argument points to or ``(size_t) -1`` if the size is not known.

The built-in functions are optimized into the normal string functions
like ``memcpy`` if the last argument is ``(size_t) -1`` or if
it is known at compile time that the destination object will not
be overflown.  If the compiler can determine at compile time the
object will be always overflown, it issues a warning.

The intended use can be e.g.

.. code-block:: c++

  #undef memcpy
  #define bos0(dest) __builtin_object_size (dest, 0)
  #define memcpy(dest, src, n) \
    __builtin___memcpy_chk (dest, src, n, bos0 (dest))

  char *volatile p;
  char buf[10];
  /* It is unknown what object p points to, so this is optimized
     into plain memcpy - no checking is possible.  */
  memcpy (p, "abcde", n);
  /* Destination is known and length too.  It is known at compile
     time there will be no overflow.  */
  memcpy (&buf[5], "abcde", 5);
  /* Destination is known, but the length is not known at compile time.
     This will result in __memcpy_chk call that can check for overflow
     at run time.  */
  memcpy (&buf[5], "abcde", n);
  /* Destination is known and it is known at compile time there will
     be overflow.  There will be a warning and __memcpy_chk call that
     will abort the program at run time.  */
  memcpy (&buf[6], "abcde", 5);

Such built-in functions are provided for ``memcpy``, ``mempcpy``,
``memmove``, ``memset``, ``strcpy``, ``stpcpy``, ``strncpy``,
``strcat`` and ``strncat``.

There are also checking built-in functions for formatted output functions.

.. code-block:: c++

  int __builtin___sprintf_chk (char *s, int flag, size_t os, const char *fmt, ...);
  int __builtin___snprintf_chk (char *s, size_t maxlen, int flag, size_t os,
                                const char *fmt, ...);
  int __builtin___vsprintf_chk (char *s, int flag, size_t os, const char *fmt,
                                va_list ap);
  int __builtin___vsnprintf_chk (char *s, size_t maxlen, int flag, size_t os,
                                 const char *fmt, va_list ap);

The added ``flag`` argument is passed unchanged to ``__sprintf_chk``
etc. functions and can contain implementation specific flags on what
additional security measures the checking function might take, such as
handling ``%n`` differently.

The ``os`` argument is the object size ``s`` points to, like in the
other built-in functions.  There is a small difference in the behavior
though, if ``os`` is ``(size_t) -1``, the built-in functions are
optimized into the non-checking functions only if ``flag`` is 0, otherwise
the checking function is called with ``os`` argument set to
``(size_t) -1``.

In addition to this, there are checking built-in functions
``__builtin___printf_chk``, ``__builtin___vprintf_chk``,
``__builtin___fprintf_chk`` and ``__builtin___vfprintf_chk``.
These have just one additional argument, ``flag``, right before
format string ``fmt``.  If the compiler is able to optimize them to
``fputc`` etc. functions, it does, otherwise the checking function
is called and the ``flag`` argument passed to it.

