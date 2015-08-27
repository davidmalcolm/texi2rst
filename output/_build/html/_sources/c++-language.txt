C++ Language
************

GCC supports the original ISO C++ standard (1998) and contains
experimental support for the second ISO C++ standard (2011).

The original ISO C++ standard was published as the ISO standard (ISO/IEC
14882:1998) and amended by a Technical Corrigenda published in 2003
(ISO/IEC 14882:2003). These standards are referred to as C++98 and
C++03, respectively. GCC implements the majority of C++98 (``export``
is a notable exception) and most of the changes in C++03.  To select
this standard in GCC, use one of the options :option:`-ansi`,
:option:`-std=c++98`, or :option:`-std=c++03`; to obtain all the diagnostics
required by the standard, you should also specify :option:`-pedantic` (or
:option:`-pedantic-errors` if you want them to be errors rather than
warnings).

A revised ISO C++ standard was published in 2011 as ISO/IEC
14882:2011, and is referred to as C++11; before its publication it was
commonly referred to as C++0x.  C++11 contains several
changes to the C++ language, most of which have been implemented in an
experimental C++11 mode in GCC.  For information
regarding the C++11 features available in the experimental C++11 mode,
see http://gcc.gnu.org/projects/cxx0x.html. To select this
standard in GCC, use the option :option:`-std=c++11`; to obtain all the
diagnostics required by the standard, you should also specify
:option:`-pedantic` (or :option:`-pedantic-errors` if you want them to
be errors rather than warnings).

More information about the C++ standards is available on the ISO C++
committees web site at http://www.open-std.org/jtc1/sc22/wg21/.

By default, GCC provides some extensions to the C++ language; C++
Dialect OptionsOptions Controlling C++ Dialect.  Use of the
:option:`-std` option listed above will disable these extensions.  You
may also select an extended version of the C++ language explicitly with
:option:`-std=gnu++98` (for C++98 with GNU extensions) or
:option:`-std=gnu++11` (for C++11 with GNU extensions).  The default, if
no C++ language dialect options are given, is :option:`-std=gnu++98`.

