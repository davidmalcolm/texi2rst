C Implementation-Defined Behavior
---------------------------------

.. index:: implementation-defined behavior, C language

A conforming implementation of ISO C is required to document its
choice of behavior in each of the areas that are designated
implementation defined.  The following lists all such areas,
along with the section numbers from the ISO/IEC 9899:1990, ISO/IEC
9899:1999 and ISO/IEC 9899:2011 standards.  Some areas are only
implementation-defined in one version of the standard.

Some choices depend on the externally determined ABI for the platform
(including standard character encodings) which GCC follows; these are
listed as determined by ABI below.  CompatibilityBinary
Compatibility, and http://gcc.gnu.org/readings.html.  Some
choices are documented in the preprocessor manual.
Implementation-defined behaviorImplementation-defined
behaviorcppThe C Preprocessor.  Some choices are made by the
library and operating system (or other environment when compiling for
a freestanding environment); refer to their documentation for details.

.. toctree::

   <translation-implementation>
   <environment-implementation>
   <identifiers-implementation>
   <characters-implementation>
   <integers-implementation>
   <floating-point-implementation>
   <arrays-and-pointers-implementation>
   <hints-implementation>
   <structures-unions-enumerations-and-bit-fields-implementation>
   <qualifiers-implementation>
   <declarators-implementation>
   <statements-implementation>
   <preprocessing-directives-implementation>
   <library-functions-implementation>
   <architecture-implementation>
   <locale-specific-behavior-implementation>

:: _translation-implementation:

.. toctree::

  translation
  environment
  identifiers
  characters
  integers
  floating-point
  arrays-and-pointers
  hints
  structures,-unions,-enumerations,-and-bit-fields
  qualifiers
  declarators
  statements
  preprocessing-directives
  library-functions
  architecture
  locale-specific-behavior
:: _environment-implementation:

:: _identifiers-implementation:

:: _characters-implementation:

:: _integers-implementation:

:: _floating-point-implementation:

:: _arrays-and-pointers-implementation:

:: _hints-implementation:

:: _structures-unions-enumerations-and-bit-fields-implementation:

:: _qualifiers-implementation:

:: _declarators-implementation:

:: _statements-implementation:

:: _preprocessing-directives-implementation:

:: _library-functions-implementation:

:: _architecture-implementation:

:: _locale-specific-behavior-implementation:

