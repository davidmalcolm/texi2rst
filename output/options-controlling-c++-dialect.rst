.. _c++-dialect-options:

Options Controlling C++ Dialect
*******************************

.. index:: compiler options, C++

.. index:: C++ options, command-line

.. index:: options, C++

This section describes the command-line options that are only meaningful
for C++ programs.  You can also use most of the GNU compiler options
regardless of what language your program is in.  For example, you
might compile a file firstClass.C like this:

.. code-block:: c++

  g++ -g -frepo -O -c firstClass.C

In this example, only :option:`-frepo` is an option meant
only for C++ programs; you can use the other options with any
language supported by GCC.

Here is a list of options that are *only* for compiling C++ programs:

.. option:: -fabi-version=n

  Use version ``n`` of the C++ ABI.  The default is version 0.

  Version 0 refers to the version conforming most closely to
  the C++ ABI specification.  Therefore, the ABI obtained using version 0
  will change in different versions of G++ as ABI bugs are fixed.

  Version 1 is the version of the C++ ABI that first appeared in G++ 3.2.

  Version 2 is the version of the C++ ABI that first appeared in G++
  3.4, and was the default through G++ 4.9.

  Version 3 corrects an error in mangling a constant address as a
  template argument.

  Version 4, which first appeared in G++ 4.5, implements a standard
  mangling for vector types.

  Version 5, which first appeared in G++ 4.6, corrects the mangling of
  attribute const/volatile on function pointer types, decltype of a
  plain decl, and use of a function parameter in the declaration of
  another parameter.

  Version 6, which first appeared in G++ 4.7, corrects the promotion
  behavior of C++11 scoped enums and the mangling of template argument
  packs, const/static_cast, prefix ++ and -, and a class scope function
  used as a template argument.

  Version 7, which first appeared in G++ 4.8, that treats nullptr_t as a
  builtin type and corrects the mangling of lambdas in default argument
  scope.

  Version 8, which first appeared in G++ 4.9, corrects the substitution
  behavior of function types with function-cv-qualifiers.

  See also :option:`-Wabi`.

.. option:: -fabi-compat-version=n

  On targets that support strong aliases, G++
  works around mangling changes by creating an alias with the correct
  mangled name when defining a symbol with an incorrect mangled name.
  This switch specifies which ABI version to use for the alias.

  With :option:`-fabi-version=0` (the default), this defaults to 2.  If
  another ABI version is explicitly selected, this defaults to 0.

  The compatibility version is also set by :option:`-Wabi=``n```.

.. option:: -fno-access-control

  Turn off all access checking.  This switch is mainly useful for working
  around bugs in the access control code.

.. option:: -fcheck-new

  Check that the pointer returned by ``operator new`` is non-null
  before attempting to modify the storage allocated.  This check is
  normally unnecessary because the C++ standard specifies that
  ``operator new`` only returns ``0`` if it is declared
  ``throw()``, in which case the compiler always checks the
  return value even without this option.  In all other cases, when
  ``operator new`` has a non-empty exception specification, memory
  exhaustion is signalled by throwing ``std::bad_alloc``.  See also
  new (nothrow).

.. option:: -fconstexpr-depth=n

  Set the maximum nested evaluation depth for C++11 constexpr functions
  to ``n``.  A limit is needed to detect endless recursion during
  constant expression evaluation.  The minimum specified by the standard
  is 512.

.. option:: -fdeduce-init-list

  Enable deduction of a template type parameter as
  ``std::initializer_list`` from a brace-enclosed initializer list, i.e.

  .. code-block:: c++

    template <class T> auto forward(T t) -> decltype (realfn (t))
    {
      return realfn (t);
    }

    void f()
    {
      forward({1,2}); // call forward<std::initializer_list<int>>
    }

  This deduction was implemented as a possible extension to the
  originally proposed semantics for the C++11 standard, but was not part
  of the final standard, so it is disabled by default.  This option is
  deprecated, and may be removed in a future version of G++.

.. option:: -ffriend-injection

  Inject friend functions into the enclosing namespace, so that they are
  visible outside the scope of the class in which they are declared.
  Friend functions were documented to work this way in the old Annotated
  C++ Reference Manual.  
  However, in ISO C++ a friend function that is not declared
  in an enclosing scope can only be found using argument dependent
  lookup.  GCC defaults to the standard behavior.

  This option is for compatibility, and may be removed in a future
  release of G++.

.. option:: -fno-elide-constructors

  The C++ standard allows an implementation to omit creating a temporary
  that is only used to initialize another object of the same type.
  Specifying this option disables that optimization, and forces G++ to
  call the copy constructor in all cases.

.. option:: -fno-enforce-eh-specs

  Don't generate code to check for violation of exception specifications
  at run time.  This option violates the C++ standard, but may be useful
  for reducing code size in production builds, much like defining
  ``NDEBUG``.  This does not give user code permission to throw
  exceptions in violation of the exception specifications; the compiler
  still optimizes based on the specifications, so throwing an
  unexpected exception results in undefined behavior at run time.

.. option:: -fextern-tls-init, -fno-extern-tls-init

  The C++11 and OpenMP standards allow ``thread_local`` and
  ``threadprivate`` variables to have dynamic (runtime)
  initialization.  To support this, any use of such a variable goes
  through a wrapper function that performs any necessary initialization.
  When the use and definition of the variable are in the same
  translation unit, this overhead can be optimized away, but when the
  use is in a different translation unit there is significant overhead
  even if the variable doesn't actually need dynamic initialization.  If
  the programmer can be sure that no use of the variable in a
  non-defining TU needs to trigger dynamic initialization (either
  because the variable is statically initialized, or a use of the
  variable in the defining TU will be executed before any uses in
  another TU), they can avoid this overhead with the
  :option:`-fno-extern-tls-init` option.

  On targets that support symbol aliases, the default is
  :option:`-fextern-tls-init`.  On targets that do not support symbol
  aliases, the default is :option:`-fno-extern-tls-init`.

.. option:: -ffor-scope, -fno-for-scope

  If :option:`-ffor-scope` is specified, the scope of variables declared in
  a for-init-statement is limited to the ``for`` loop itself,
  as specified by the C++ standard.
  If :option:`-fno-for-scope` is specified, the scope of variables declared in
  a for-init-statement extends to the end of the enclosing scope,
  as was the case in old versions of G++, and other (traditional)
  implementations of C++.

  If neither flag is given, the default is to follow the standard,
  but to allow and give a warning for old-style code that would
  otherwise be invalid, or have different behavior.

.. option:: -fno-gnu-keywords

  Do not recognize ``typeof`` as a keyword, so that code can use this
  word as an identifier.  You can use the keyword ``__typeof__`` instead.
  :option:`-ansi` implies :option:`-fno-gnu-keywords`.

.. option:: -fno-implicit-templates

  Never emit code for non-inline templates that are instantiated
  implicitly (i.e. by use); only emit code for explicit instantiations.
  See :ref:`template-instantiation`, for more information.

.. option:: -fno-implicit-inline-templates

  Don't emit code for implicit instantiations of inline templates, either.
  The default is to handle inlines differently so that compiles with and
  without optimization need the same set of explicit instantiations.

.. option:: -fno-implement-inlines

  To save space, do not emit out-of-line copies of inline functions
  controlled by ``#pragma implementation``.  This causes linker
  errors if these functions are not inlined everywhere they are called.

.. option:: -fms-extensions

  Disable Wpedantic warnings about constructs used in MFC, such as implicit
  int and getting a pointer to member function via non-standard syntax.

.. option:: -fno-nonansi-builtins

  Disable built-in declarations of functions that are not mandated by
  ANSI/ISO C.  These include ``ffs``, ``alloca``, ``_exit``,
  ``index``, ``bzero``, ``conjf``, and other related functions.

.. option:: -fnothrow-opt

  Treat a ``throw()`` exception specification as if it were a
  ``noexcept`` specification to reduce or eliminate the text size
  overhead relative to a function with no exception specification.  If
  the function has local variables of types with non-trivial
  destructors, the exception specification actually makes the
  function smaller because the EH cleanups for those variables can be
  optimized away.  The semantic effect is that an exception thrown out of
  a function with such an exception specification results in a call
  to ``terminate`` rather than ``unexpected``.

.. option:: -fno-operator-names

  Do not treat the operator name keywords ``and``, ``bitand``,
  ``bitor``, ``compl``, ``not``, ``or`` and ``xor`` as
  synonyms as keywords.

.. option:: -fno-optional-diags

  Disable diagnostics that the standard says a compiler does not need to
  issue.  Currently, the only such diagnostic issued by G++ is the one for
  a name having multiple meanings within a class.

.. option:: -fpermissive

  Downgrade some diagnostics about nonconformant code from errors to
  warnings.  Thus, using :option:`-fpermissive` allows some
  nonconforming code to compile.

.. option:: -fno-pretty-templates

  When an error message refers to a specialization of a function
  template, the compiler normally prints the signature of the
  template followed by the template arguments and any typedefs or
  typenames in the signature (e.g. ``void f(T) [with T = int]``
  rather than ``void f(int)``) so that it's clear which template is
  involved.  When an error message refers to a specialization of a class
  template, the compiler omits any template arguments that match
  the default template arguments for that template.  If either of these
  behaviors make it harder to understand the error message rather than
  easier, you can use :option:`-fno-pretty-templates` to disable them.

.. option:: -frepo

  Enable automatic template instantiation at link time.  This option also
  implies :option:`-fno-implicit-templates`.  See :ref:`template-instantiation`, for more information.

.. option:: -fno-rtti

  Disable generation of information about every class with virtual
  functions for use by the C++ run-time type identification features
  (``dynamic_cast`` and ``typeid``).  If you don't use those parts
  of the language, you can save some space by using this flag.  Note that
  exception handling uses the same information, but G++ generates it as
  needed. The ``dynamic_cast`` operator can still be used for casts that
  do not require run-time type information, i.e. casts to ``void *`` or to
  unambiguous base classes.

.. option:: -fsized-deallocation

  Enable the built-in global declarations

  .. code-block:: c++

    void operator delete (void *, std::size_t) noexcept;
    void operator delete[] (void *, std::size_t) noexcept;

  as introduced in C++14.  This is useful for user-defined replacement
  deallocation functions that, for example, use the size of the object
  to make deallocation faster.  Enabled by default under
  :option:`-std=c++14` and above.  The flag :option:`-Wsized-deallocation`
  warns about places that might want to add a definition.

.. option:: -fstats

  Emit statistics about front-end processing at the end of the compilation.
  This information is generally only useful to the G++ development team.

.. option:: -fstrict-enums

  Allow the compiler to optimize using the assumption that a value of
  enumerated type can only be one of the values of the enumeration (as
  defined in the C++ standard; basically, a value that can be
  represented in the minimum number of bits needed to represent all the
  enumerators).  This assumption may not be valid if the program uses a
  cast to convert an arbitrary integer value to the enumerated type.

.. option:: -ftemplate-backtrace-limit=n

  Set the maximum number of template instantiation notes for a single
  warning or error to ``n``.  The default value is 10.

.. option:: -ftemplate-depth=n

  Set the maximum instantiation depth for template classes to ``n``.
  A limit on the template instantiation depth is needed to detect
  endless recursions during template class instantiation.  ANSI/ISO C++
  conforming programs must not rely on a maximum depth greater than 17
  (changed to 1024 in C++11).  The default value is 900, as the compiler
  can run out of stack space before hitting 1024 in some situations.

.. option:: -fno-threadsafe-statics

  Do not emit the extra code to use the routines specified in the C++
  ABI for thread-safe initialization of local statics.  You can use this
  option to reduce code size slightly in code that doesn't need to be
  thread-safe.

.. option:: -fuse-cxa-atexit

  Register destructors for objects with static storage duration with the
  ``__cxa_atexit`` function rather than the ``atexit`` function.
  This option is required for fully standards-compliant handling of static
  destructors, but only works if your C library supports
  ``__cxa_atexit``.

.. option:: -fno-use-cxa-get-exception-ptr

  Don't use the ``__cxa_get_exception_ptr`` runtime routine.  This
  causes ``std::uncaught_exception`` to be incorrect, but is necessary
  if the runtime routine is not available.

.. option:: -fvisibility-inlines-hidden

  This switch declares that the user does not attempt to compare
  pointers to inline functions or methods where the addresses of the two functions
  are taken in different shared objects.

  The effect of this is that GCC may, effectively, mark inline methods with
  ``__attribute__ ((visibility ("hidden")))`` so that they do not
  appear in the export table of a DSO and do not require a PLT indirection
  when used within the DSO.  Enabling this option can have a dramatic effect
  on load and link times of a DSO as it massively reduces the size of the
  dynamic export table when the library makes heavy use of templates.

  The behavior of this switch is not quite the same as marking the
  methods as hidden directly, because it does not affect static variables
  local to the function or cause the compiler to deduce that
  the function is defined in only one shared object.

  You may mark a method as having a visibility explicitly to negate the
  effect of the switch for that method.  For example, if you do want to
  compare pointers to a particular inline method, you might mark it as
  having default visibility.  Marking the enclosing class with explicit
  visibility has no effect.

  Explicitly instantiated inline methods are unaffected by this option
  as their linkage might otherwise cross a shared library boundary.
  See :ref:`template-instantiation`.

.. option:: -fvisibility-ms-compat

  This flag attempts to use visibility settings to make GCC's C++
  linkage model compatible with that of Microsoft Visual Studio.

  The flag makes these changes to GCC's linkage model:

  * It sets the default visibility to ``hidden``, like
    :option:`-fvisibility=hidden`.

  * Types, but not their members, are not hidden by default.

  * The One Definition Rule is relaxed for types without explicit
    visibility specifications that are defined in more than one
    shared object: those declarations are permitted if they are
    permitted when this option is not used.

  In new code it is better to use :option:`-fvisibility=hidden` and
  export those classes that are intended to be externally visible.
  Unfortunately it is possible for code to rely, perhaps accidentally,
  on the Visual Studio behavior.

  Among the consequences of these changes are that static data members
  of the same type with the same name but defined in different shared
  objects are different, so changing one does not change the other;
  and that pointers to function members defined in different shared
  objects may not compare equal.  When this flag is given, it is a
  violation of the ODR to define types with the same name differently.

.. option:: -fvtable-verify=[std|preinit|none]

  Turn on (or off, if using :option:`-fvtable-verify=none`) the security
  feature that verifies at run time, for every virtual call, that
  the vtable pointer through which the call is made is valid for the type of
  the object, and has not been corrupted or overwritten.  If an invalid vtable
  pointer is detected at run time, an error is reported and execution of the
  program is immediately halted.

  This option causes run-time data structures to be built at program startup,
  which are used for verifying the vtable pointers.  
  The options std and preinit
  control the timing of when these data structures are built.  In both cases the
  data structures are built before execution reaches ``main``.  Using
  :option:`-fvtable-verify=std` causes the data structures to be built after
  shared libraries have been loaded and initialized.
  :option:`-fvtable-verify=preinit` causes them to be built before shared
  libraries have been loaded and initialized.

  If this option appears multiple times in the command line with different
  values specified, none takes highest priority over both std and
  preinit; preinit takes priority over std.

.. option:: -fvtv-debug

  When used in conjunction with :option:`-fvtable-verify=std` or 
  :option:`-fvtable-verify=preinit`, causes debug versions of the 
  runtime functions for the vtable verification feature to be called.  
  This flag also causes the compiler to log information about which 
  vtable pointers it finds for each class.
  This information is written to a file named vtv_set_ptr_data.log 
  in the directory named by the environment variable :envvar:`VTV_LOGS_DIR` 
  if that is defined or the current working directory otherwise.

  Note:  This feature *appends* data to the log file. If you want a fresh log
  file, be sure to delete any existing one.

.. option:: -fvtv-counts

  This is a debugging flag.  When used in conjunction with
  :option:`-fvtable-verify=std` or :option:`-fvtable-verify=preinit`, this
  causes the compiler to keep track of the total number of virtual calls
  it encounters and the number of verifications it inserts.  It also
  counts the number of calls to certain run-time library functions
  that it inserts and logs this information for each compilation unit.
  The compiler writes this information to a file named
  vtv_count_data.log in the directory named by the environment
  variable :envvar:`VTV_LOGS_DIR` if that is defined or the current working
  directory otherwise.  It also counts the size of the vtable pointer sets
  for each class, and writes this information to vtv_class_set_sizes.log
  in the same directory.

  Note:  This feature *appends* data to the log files.  To get fresh log
  files, be sure to delete any existing ones.

.. option:: -fno-weak

  Do not use weak symbol support, even if it is provided by the linker.
  By default, G++ uses weak symbols if they are available.  This
  option exists only for testing, and should not be used by end-users;
  it results in inferior code and has no benefits.  This option may
  be removed in a future release of G++.

.. option:: -nostdinc++

  Do not search for header files in the standard directories specific to
  C++, but do still search the other standard directories.  (This option
  is used when building the C++ library.)

In addition, these optimization, warning, and code generation options
have meanings only for C++ programs:

.. option:: -Wabi , -Wabi, -Wno-abi

  .. note::

    (C, Objective-C, C++ and Objective-C++ only)

  When an explicit :option:`-fabi-version=``n``` option is used, causes
  G++ to warn when it generates code that is probably not compatible with the
  vendor-neutral C++ ABI.  Since G++ now defaults to
  :option:`-fabi-version=0`, :option:`-Wabi` has no effect unless either
  an older ABI version is selected (with :option:`-fabi-version=``n```)
  or an older compatibility version is selected (with
  :option:`-Wabi=``n``` or :option:`-fabi-compat-version=``n```).

  Although an effort has been made to warn about
  all such cases, there are probably some cases that are not warned about,
  even though G++ is generating incompatible code.  There may also be
  cases where warnings are emitted even though the code that is generated
  is compatible.

  You should rewrite your code to avoid these warnings if you are
  concerned about the fact that code generated by G++ may not be binary
  compatible with code generated by other compilers.

  :option:`-Wabi` can also be used with an explicit version number to
  warn about compatibility with a particular :option:`-fabi-version`
  level, e.g. :option:`-Wabi=2` to warn about changes relative to
  :option:`-fabi-version=2`.  Specifying a version number also sets
  :option:`-fabi-compat-version=``n```.

  The known incompatibilities in :option:`-fabi-version=2` (which was the
  default from GCC 3.4 to 4.9) include:

  * A template with a non-type template parameter of reference type was
    mangled incorrectly:

    .. code-block:: c++

      extern int N;
      template <int &> struct S {};
      void n (S<N>) {2}

    This was fixed in :option:`-fabi-version=3`.

  * SIMD vector types declared using ``__attribute ((vector_size))`` were
    mangled in a non-standard way that does not allow for overloading of
    functions taking vectors of different sizes.

    The mangling was changed in :option:`-fabi-version=4`.

  * ``__attribute ((const))`` and ``noreturn`` were mangled as type
    qualifiers, and ``decltype`` of a plain declaration was folded away.

    These mangling issues were fixed in :option:`-fabi-version=5`.

  * Scoped enumerators passed as arguments to a variadic function are
    promoted like unscoped enumerators, causing ``va_arg`` to complain.
    On most targets this does not actually affect the parameter passing
    ABI, as there is no way to pass an argument smaller than ``int``.

    Also, the ABI changed the mangling of template argument packs,
    ``const_cast``, ``static_cast``, prefix increment/decrement, and
    a class scope function used as a template argument.

    These issues were corrected in :option:`-fabi-version=6`.

  * Lambdas in default argument scope were mangled incorrectly, and the
    ABI changed the mangling of ``nullptr_t``.

    These issues were corrected in :option:`-fabi-version=7`.

  * When mangling a function type with function-cv-qualifiers, the
    un-qualified function type was incorrectly treated as a substitution
    candidate.

    This was fixed in :option:`-fabi-version=8`.

  It also warns about psABI-related changes.  The known psABI changes at this
  point include:

  * For SysV/x86-64, unions with ``long double`` members are 
    passed in memory as specified in psABI.  For example:

    .. code-block:: c++

      union U {
        long double ld;
        int i;
      };

    ``union U`` is always passed in memory.

.. option:: -Wabi-tag , -Wabi-tag

  .. note::

    (C++ and Objective-C++ only)

  Warn when a type with an ABI tag is used in a context that does not
  have that ABI tag.  See C++ Attributes for more information
  about ABI tags.

.. option:: -Wctor-dtor-privacy , -Wctor-dtor-privacy, -Wno-ctor-dtor-privacy

  .. note::

    (C++ and Objective-C++ only)

  Warn when a class seems unusable because all the constructors or
  destructors in that class are private, and it has neither friends nor
  public static member functions.  Also warn if there are no non-private
  methods, and there's at least one private member function that isn't
  a constructor or destructor.

.. option:: -Wdelete-non-virtual-dtor , -Wdelete-non-virtual-dtor, -Wno-delete-non-virtual-dtor

  .. note::

    (C++ and Objective-C++ only)

  Warn when ``delete`` is used to destroy an instance of a class that
  has virtual functions and non-virtual destructor. It is unsafe to delete
  an instance of a derived class through a pointer to a base class if the
  base class does not have a virtual destructor.  This warning is enabled
  by :option:`-Wall`.

.. option:: -Wliteral-suffix , -Wliteral-suffix, -Wno-literal-suffix

  .. note::

    (C++ and Objective-C++ only)

  Warn when a string or character literal is followed by a ud-suffix which does
  not begin with an underscore.  As a conforming extension, GCC treats such
  suffixes as separate preprocessing tokens in order to maintain backwards
  compatibility with code that uses formatting macros from ``<inttypes.h>``.
  For example:

  .. code-block:: c++

    #define __STDC_FORMAT_MACROS
    #include <inttypes.h>
    #include <stdio.h>

    int main() {
      int64_t i64 = 123;
      printf("My int64: %" PRId64"\n", i64);
    }

  In this case, ``PRId64`` is treated as a separate preprocessing token.

  This warning is enabled by default.

.. option:: -Wnarrowing , -Wnarrowing, -Wno-narrowing

  .. note::

    (C++ and Objective-C++ only)

  Warn when a narrowing conversion prohibited by C++11 occurs within
  { }, e.g.

  .. code-block:: c++

    int i = { 2.2 }; // error: narrowing from double to int

  This flag is included in :option:`-Wall` and :option:`-Wc++11-compat`.

  With :option:`-std=c++11`, :option:`-Wno-narrowing` suppresses the diagnostic
  required by the standard.  Note that this does not affect the meaning
  of well-formed code; narrowing conversions are still considered
  ill-formed in SFINAE context.

.. option:: -Wnoexcept , -Wnoexcept, -Wno-noexcept

  .. note::

    (C++ and Objective-C++ only)

  Warn when a noexcept-expression evaluates to false because of a call
  to a function that does not have a non-throwing exception
  specification (i.e. ``throw()`` or ``noexcept``) but is known by
  the compiler to never throw an exception.

.. option:: -Wnon-virtual-dtor , -Wnon-virtual-dtor, -Wno-non-virtual-dtor

  .. note::

    (C++ and Objective-C++ only)

  Warn when a class has virtual functions and an accessible non-virtual
  destructor itself or in an accessible polymorphic base class, in which
  case it is possible but unsafe to delete an instance of a derived
  class through a pointer to the class itself or base class.  This
  warning is automatically enabled if :option:`-Weffc++` is specified.

.. option:: -Wreorder , -Wreorder, -Wno-reorder

  .. note::

    (C++ and Objective-C++ only)

  .. index:: reordering, warning

  .. index:: warning for reordering of member initializers

  Warn when the order of member initializers given in the code does not
  match the order in which they must be executed.  For instance:

  .. code-block:: c++

    struct A {
      int i;
      int j;
      A(): j (0), i (1) { }
    };

  The compiler rearranges the member initializers for ``i``
  and ``j`` to match the declaration order of the members, emitting
  a warning to that effect.  This warning is enabled by :option:`-Wall`.

.. option:: -fext-numeric-literals , -fext-numeric-literals, -fno-ext-numeric-literals

  .. note::

    (C++ and Objective-C++ only)

  Accept imaginary, fixed-point, or machine-defined
  literal number suffixes as GNU extensions.
  When this option is turned off these suffixes are treated
  as C++11 user-defined literal numeric suffixes.
  This is on by default for all pre-C++11 dialects and all GNU dialects:
  :option:`-std=c++98`, :option:`-std=gnu++98`, :option:`-std=gnu++11`,
  :option:`-std=gnu++14`.
  This option is off by default
  for ISO C++11 onwards (:option:`-std=c++11`, ...).

The following :option:`-W...` options are not affected by :option:`-Wall`.

.. option:: -Weffc++ , -Weffc++, -Wno-effc++

  .. note::

    (C++ and Objective-C++ only)

  Warn about violations of the following style guidelines from Scott Meyers'
  Effective C++ series of books:

  * Define a copy constructor and an assignment operator for classes
    with dynamically-allocated memory.

  * Prefer initialization to assignment in constructors.

  * Have ``operator=`` return a reference to ``*this``.

  * Don't try to return a reference when you must return an object.

  * Distinguish between prefix and postfix forms of increment and
    decrement operators.

  * Never overload ``&&``, ``||``, or ``,``.

  This option also enables :option:`-Wnon-virtual-dtor`, which is also
  one of the effective C++ recommendations.  However, the check is
  extended to warn about the lack of virtual destructor in accessible
  non-polymorphic bases classes too.

  When selecting this option, be aware that the standard library
  headers do not obey all of these guidelines; use grep -v
  to filter out those warnings.

.. option:: -Wstrict-null-sentinel , -Wstrict-null-sentinel, -Wno-strict-null-sentinel

  .. note::

    (C++ and Objective-C++ only)

  Warn about the use of an uncasted ``NULL`` as sentinel.  When
  compiling only with GCC this is a valid sentinel, as ``NULL`` is defined
  to ``__null``.  Although it is a null pointer constant rather than a
  null pointer, it is guaranteed to be of the same size as a pointer.
  But this use is not portable across different compilers.

.. option:: -Wno-non-template-friend , -Wno-non-template-friend, -Wnon-template-friend

  .. note::

    (C++ and Objective-C++ only)

  Disable warnings when non-templatized friend functions are declared
  within a template.  Since the advent of explicit template specification
  support in G++, if the name of the friend is an unqualified-id (i.e.,
  friend foo(int)), the C++ language specification demands that the
  friend declare or define an ordinary, nontemplate function.  (Section
  14.5.3).  Before G++ implemented explicit specification, unqualified-ids
  could be interpreted as a particular specialization of a templatized
  function.  Because this non-conforming behavior is no longer the default
  behavior for G++, :option:`-Wnon-template-friend` allows the compiler to
  check existing code for potential trouble spots and is on by default.
  This new compiler behavior can be turned off with
  :option:`-Wno-non-template-friend`, which keeps the conformant compiler code
  but disables the helpful warning.

.. option:: -Wold-style-cast , -Wold-style-cast, -Wno-old-style-cast

  .. note::

    (C++ and Objective-C++ only)

  Warn if an old-style (C-style) cast to a non-void type is used within
  a C++ program.  The new-style casts (``dynamic_cast``,
  ``static_cast``, ``reinterpret_cast``, and ``const_cast``) are
  less vulnerable to unintended effects and much easier to search for.

.. option:: -Woverloaded-virtual , -Woverloaded-virtual, -Wno-overloaded-virtual

  .. note::

    (C++ and Objective-C++ only)

  .. index:: overloaded virtual function, warning

  .. index:: warning for overloaded virtual function

  Warn when a function declaration hides virtual functions from a
  base class.  For example, in:

  .. code-block:: c++

    struct A {
      virtual void f();
    };

    struct B: public A {
      void f(int);
    };

  the ``A`` class version of ``f`` is hidden in ``B``, and code
  like:

  .. code-block:: c++

    B* b;
    b->f();

  fails to compile.

.. option:: -Wno-pmf-conversions , -Wno-pmf-conversions, -Wpmf-conversions

  .. note::

    (C++ and Objective-C++ only)

  Disable the diagnostic for converting a bound pointer to member function
  to a plain pointer.

.. option:: -Wsign-promo , -Wsign-promo, -Wno-sign-promo

  .. note::

    (C++ and Objective-C++ only)

  Warn when overload resolution chooses a promotion from unsigned or
  enumerated type to a signed type, over a conversion to an unsigned type of
  the same size.  Previous versions of G++ tried to preserve
  unsignedness, but the standard mandates the current behavior.

.. option:: -Wno-terminate , -Wterminate, -Wno-terminate

  .. note::

    (C++ and Objective-C++ only)

  Disable the warning about a throw-expression that will immediately
  result in a call to ``terminate``.

