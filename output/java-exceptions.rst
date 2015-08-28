  .. _java-exceptions:

Java Exceptions
***************

The Java language uses a slightly different exception handling model
from C++.  Normally, GNU C++ automatically detects when you are
writing C++ code that uses Java exceptions, and handle them
appropriately.  However, if C++ code only needs to execute destructors
when Java exceptions are thrown through it, GCC guesses incorrectly.
Sample problematic code is:

.. code-block:: c++

    struct S { ~S(); };
    extern void bar();    // is written in Java, and may throw exceptions
    void foo()
    {
      S s;
      bar();
    }

The usual effect of an incorrect guess is a link failure, complaining of
a missing routine called __gxx_personality_v0.

You can inform the compiler that Java exceptions are to be used in a
translation unit, irrespective of what it might think, by writing
#pragma GCC java_exceptions at the head of the file.  This
#pragma must appear before any functions that throw or catch
exceptions, or run destructors when exceptions are thrown through them.

You cannot mix Java and C++ exceptions in the same translation unit.  It
is believed to be safe to throw a C++ exception from one file through
another file compiled for the Java exception model, or vice versa, but
there may be bugs in this area.

