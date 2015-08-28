
Compiling C++ Programs
**********************

.. index:: suffixes for C++ source

.. index:: C++ source file suffixes

C++ source files conventionally use one of the suffixes .C,
.cc, .cpp, .CPP, .c++, .cp, or
.cxx; C++ header files often use .hh, .hpp,
.H, or (for shared template code) .tcc; and
preprocessed C++ files use the suffix .ii.  GCC recognizes
files with these names and compiles them as C++ programs even if you
call the compiler the same way as for compiling C programs (usually
with the name :command:`gcc`).

.. index:: g++

.. index:: c++

However, the use of :command:`gcc` does not add the C++ library.
:command:`g++` is a program that calls GCC and automatically specifies linking
against the C++ library.  It treats .c,
.h and .i files as C++ source files instead of C source
files unless :option:`-x` is used.  This program is also useful when
precompiling a C header file with a .h extension for use in C++
compilations.  On many systems, :command:`g++` is also installed with
the name :command:`c++`.

invoking :command:`g++`When you compile C++ programs, you may specify many of the same
command-line options that you use for compiling programs in any
language; or command-line options meaningful for C and related
languages; or options that are meaningful only for C++ programs.
See :ref:`Options Controlling C Dialect <c-dialect-options>`, for
explanations of options for languages related to C.
See :ref:`Options Controlling C++ Dialect <c++-dialect-options>`, for
explanations of options that are meaningful only for C++ programs.

