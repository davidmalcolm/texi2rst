.. _pointer-bounds-checker-builtins:

Pointer Bounds Checker Built-in Functions
*****************************************

.. index:: Pointer Bounds Checker builtins

.. index:: __builtin___bnd_set_ptr_bounds

.. index:: __builtin___bnd_narrow_ptr_bounds

.. index:: __builtin___bnd_copy_ptr_bounds

.. index:: __builtin___bnd_init_ptr_bounds

.. index:: __builtin___bnd_null_ptr_bounds

.. index:: __builtin___bnd_store_ptr_bounds

.. index:: __builtin___bnd_chk_ptr_lbounds

.. index:: __builtin___bnd_chk_ptr_ubounds

.. index:: __builtin___bnd_chk_ptr_bounds

.. index:: __builtin___bnd_get_ptr_lbound

.. index:: __builtin___bnd_get_ptr_ubound

GCC provides a set of built-in functions to control Pointer Bounds Checker
instrumentation.  Note that all Pointer Bounds Checker builtins can be used
even if you compile with Pointer Bounds Checker off
(:option:`-fno-check-pointer-bounds`).
The behavior may differ in such case as documented below.

.. index:: __builtin___bnd_set_ptr_bounds

Built-in Functionvoid *__builtin___bnd_set_ptr_bounds(constvoid*``q``,size_t``size``)This built-in function returns a new pointer with the value of ``q``, and
associate it with the bounds [``q``, ``q``+``size``-1].  With Pointer
Bounds Checker off, the built-in function just returns the first argument.

.. code-block:: c++

  extern void *__wrap_malloc (size_t n)
  {
    void *p = (void *)__real_malloc (n);
    if (!p) return __builtin___bnd_null_ptr_bounds (p);
    return __builtin___bnd_set_ptr_bounds (p, n);
  }

.. index:: __builtin___bnd_narrow_ptr_bounds

Built-in Functionvoid *__builtin___bnd_narrow_ptr_bounds(constvoid*``p``,constvoid*``q``,size_t``size``)This built-in function returns a new pointer with the value of ``p``
and associates it with the narrowed bounds formed by the intersection
of bounds associated with ``q`` and the bounds
[``p``, ``p`` + ``size`` - 1].
With Pointer Bounds Checker off, the built-in function just returns the first
argument.

.. code-block:: c++

  void init_objects (object *objs, size_t size)
  {
    size_t i;
    /* Initialize objects one-by-one passing pointers with bounds of 
       an object, not the full array of objects.  */
    for (i = 0; i < size; i++)
      init_object (__builtin___bnd_narrow_ptr_bounds (objs + i, objs,
                                                      sizeof(object)));
  }

.. index:: __builtin___bnd_copy_ptr_bounds

Built-in Functionvoid *__builtin___bnd_copy_ptr_bounds(constvoid*``q``,constvoid*``r``)This built-in function returns a new pointer with the value of ``q``,
and associates it with the bounds already associated with pointer ``r``.
With Pointer Bounds Checker off, the built-in function just returns the first
argument.

.. code-block:: c++

  /* Here is a way to get pointer to object's field but
     still with the full object's bounds.  */
  int *field_ptr = __builtin___bnd_copy_ptr_bounds (&objptr->int_field, 
                                                    objptr);

.. index:: __builtin___bnd_init_ptr_bounds

Built-in Functionvoid *__builtin___bnd_init_ptr_bounds(constvoid*``q``)This built-in function returns a new pointer with the value of ``q``, and
associates it with INIT (allowing full memory access) bounds. With Pointer
Bounds Checker off, the built-in function just returns the first argument.

.. index:: __builtin___bnd_null_ptr_bounds

Built-in Functionvoid *__builtin___bnd_null_ptr_bounds(constvoid*``q``)This built-in function returns a new pointer with the value of ``q``, and
associates it with NULL (allowing no memory access) bounds. With Pointer
Bounds Checker off, the built-in function just returns the first argument.

.. index:: __builtin___bnd_store_ptr_bounds

Built-in Functionvoid__builtin___bnd_store_ptr_bounds(constvoid**``ptr_addr``,constvoid*``ptr_val``)This built-in function stores the bounds associated with pointer ``ptr_val``
and location ``ptr_addr`` into Bounds Table.  This can be useful to propagate
bounds from legacy code without touching the associated pointer's memory when
pointers are copied as integers.  With Pointer Bounds Checker off, the built-in
function call is ignored.

.. index:: __builtin___bnd_chk_ptr_lbounds

Built-in Functionvoid__builtin___bnd_chk_ptr_lbounds(constvoid*``q``)This built-in function checks if the pointer ``q`` is within the lower
bound of its associated bounds.  With Pointer Bounds Checker off, the built-in
function call is ignored.

.. code-block:: c++

  extern void *__wrap_memset (void *dst, int c, size_t len)
  {
    if (len > 0)
      {
        __builtin___bnd_chk_ptr_lbounds (dst);
        __builtin___bnd_chk_ptr_ubounds ((char *)dst + len - 1);
        __real_memset (dst, c, len);
      }
    return dst;
  }

.. index:: __builtin___bnd_chk_ptr_ubounds

Built-in Functionvoid__builtin___bnd_chk_ptr_ubounds(constvoid*``q``)This built-in function checks if the pointer ``q`` is within the upper
bound of its associated bounds.  With Pointer Bounds Checker off, the built-in
function call is ignored.

.. index:: __builtin___bnd_chk_ptr_bounds

Built-in Functionvoid__builtin___bnd_chk_ptr_bounds(constvoid*``q``,size_t``size``)This built-in function checks if [``q``, ``q`` + ``size`` - 1] is within
the lower and upper bounds associated with ``q``.  With Pointer Bounds Checker
off, the built-in function call is ignored.

.. code-block:: c++

  extern void *__wrap_memcpy (void *dst, const void *src, size_t n)
  {
    if (n > 0)
      {
        __bnd_chk_ptr_bounds (dst, n);
        __bnd_chk_ptr_bounds (src, n);
        __real_memcpy (dst, src, n);
      }
    return dst;
  }

.. index:: __builtin___bnd_get_ptr_lbound

Built-in Functionconst void *__builtin___bnd_get_ptr_lbound(constvoid*``q``)This built-in function returns the lower bound associated
with the pointer ``q``, as a pointer value.  
This is useful for debugging using ``printf``.
With Pointer Bounds Checker off, the built-in function returns 0.

.. code-block:: c++

  void *lb = __builtin___bnd_get_ptr_lbound (q);
  void *ub = __builtin___bnd_get_ptr_ubound (q);
  printf ("q = %p  lb(q) = %p  ub(q) = %p", q, lb, ub);

.. index:: __builtin___bnd_get_ptr_ubound

Built-in Functionconst void *__builtin___bnd_get_ptr_ubound(constvoid*``q``)This built-in function returns the upper bound (which is a pointer) associated
with the pointer ``q``.  With Pointer Bounds Checker off,
the built-in function returns -1.

