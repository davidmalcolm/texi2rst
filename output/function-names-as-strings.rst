.. _function-names:

Function Names as Strings
*************************

``__func__`` identifier``__FUNCTION__`` identifier``__PRETTY_FUNCTION__`` identifierGCC provides three magic variables that hold the name of the current
function, as a string.  The first of these is ``__func__``, which
is part of the C99 standard:

The identifier ``__func__`` is implicitly declared by the translator
as if, immediately following the opening brace of each function
definition, the declaration

.. code-block:: c++

  static const char __func__[] = "function-name";

appeared, where function-name is the name of the lexically-enclosing
function.  This name is the unadorned name of the function.

``__FUNCTION__`` is another name for ``__func__``, provided for
backward compatibility with old versions of GCC.

In C, ``__PRETTY_FUNCTION__`` is yet another name for
``__func__``.  However, in C++, ``__PRETTY_FUNCTION__`` contains
the type signature of the function as well as its bare name.  For
example, this program:

.. code-block:: c++

  extern "C" {
  extern int printf (char *, ...);
  }

  class a {
   public:
    void sub (int i)
      {
        printf ("__FUNCTION__ = %s\n", __FUNCTION__);
        printf ("__PRETTY_FUNCTION__ = %s\n", __PRETTY_FUNCTION__);
      }
  };

  int
  main (void)
  {
    a ax;
    ax.sub (0);
    return 0;
  }

gives this output:

.. code-block:: c++

  __FUNCTION__ = sub
  __PRETTY_FUNCTION__ = void a::sub(int)

These identifiers are variables, not preprocessor macros, and may not
be used to initialize ``char`` arrays or be concatenated with other string
literals.

