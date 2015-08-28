.. _target-format-checks:

Format Checks Specific to Particular Target Machines
****************************************************

For some target machines, GCC supports additional options to the
format attribute
(Function AttributesDeclaring Attributes of Functions).

.. toctree::

   <solaris-format-checks>
   <darwin-format-checks>

.. _solaris-format-checks:

Solaris Format Checks
^^^^^^^^^^^^^^^^^^^^^

Solaris targets support the ``cmn_err`` (or ``__cmn_err__``) format
check.  ``cmn_err`` accepts a subset of the standard ``printf``
conversions, and the two-argument ``%b`` conversion for displaying
bit-fields.  See the Solaris man page for ``cmn_err`` for more information.

.. _darwin-format-checks:

Darwin Format Checks
^^^^^^^^^^^^^^^^^^^^

Darwin targets support the ``CFString`` (or ``__CFString__``) in the format
attribute context.  Declarations made with such attribution are parsed for correct syntax
and format argument types.  However, parsing of the format string itself is currently undefined
and is not carried out by this version of the compiler.

Additionally, ``CFStringRefs`` (defined by the ``CoreFoundation`` headers) may
also be used as format arguments.  Note that the relevant headers are only likely to be
available on Darwin (OSX) installations.  On such installations, the XCode and system
documentation provide descriptions of ``CFString``, ``CFStringRefs`` and
associated functions.

