Options Controlling the Preprocessor
************************************

.. index:: preprocessor options

.. index:: options, preprocessor

These options control the C preprocessor, which is run on each C source
file before actual compilation.

If you use the :option:`-E` option, nothing is done except preprocessing.
Some of these options make sense only together with :option:`-E` because
they cause the preprocessor output to be unsuitable for actual
compilation.

.. option:: -Wp,option, -Wp

  You can use :option:`-Wp,``option``` to bypass the compiler driver
  and pass ``option`` directly through to the preprocessor.  If
  ``option`` contains commas, it is split into multiple options at the
  commas.  However, many options are modified, translated or interpreted
  by the compiler driver before being passed to the preprocessor, and
  :option:`-Wp` forcibly bypasses this phase.  The preprocessors direct
  interface is undocumented and subject to change, so whenever possible
  you should avoid using :option:`-Wp` and let the driver handle the
  options instead.

.. option:: -Xpreprocessor option, -Xpreprocessor

  Pass ``option`` as an option to the preprocessor.  You can use this to
  supply system-specific preprocessor options that GCC does not 
  recognize.

  If you want to pass an option that takes an argument, you must use
  :option:`-Xpreprocessor` twice, once for the option and once for the argument.

.. option:: -no-integrated-cpp

  Perform preprocessing as a separate pass before compilation.
  By default, GCC performs preprocessing as an integrated part of
  input tokenization and parsing.
  If this option is provided, the appropriate language front end
  (:command:`cc1`, :command:`cc1plus`, or :command:`cc1obj` for C, C++,
  and Objective-C, respectively) is instead invoked twice,
  once for preprocessing only and once for actual compilation
  of the preprocessed input.
  This option may be useful in conjunction with the :option:`-B` or
  :option:`-wrapper` options to specify an alternate preprocessor or
  perform additional processing of the program source between
  normal preprocessing and compilation.

.. Copyright (C) 1999-2015 Free Software Foundation, Inc. 
   This is part of the CPP and GCC manuals. 

.. For copying conditions, see the file gcc.texi. 

   - 

.. Options affecting the preprocessor 
   - 

.. If this file is included with the flag ``cppmanual'' set, it is 
   formatted for inclusion in the CPP manual; otherwise the main GCC manual. 

