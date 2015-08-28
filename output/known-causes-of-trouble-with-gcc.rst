.. _trouble:

Known Causes of Trouble with GCC
--------------------------------

.. index:: bugs, known

.. index:: installation trouble

.. index:: known causes of trouble

This section describes known problems that affect users of GCC.  Most
of these are not GCC bugs per se-if they were, we would fix them.
But the result for a user may be like the result of a bug.

Some of these problems are due to bugs in other software, some are
missing features that are too much work to add, and some are places
where people's opinions differ as to what is best.

.. toctree::

  Bugs we will fix later. <actual-bugs>
  Problems using GCC with other compilers,
                          and with certain linkers, assemblers and debuggers. <interoperation>
  GCC is incompatible with traditional C. <incompatibilities>
  GCC uses corrected versions of system header files.
                          This is necessary, but doesn't always work smoothly. <fixed-headers>
  GCC uses the system C library, which might not be
                          compliant with the ISO C standard. <standard-libraries>
  Regrettable things we can't change, but not quite bugs. <disappointments>
  Common misunderstandings with GNU C++. <c++-misunderstandings>
  Things we think are right, but some others disagree. <non-bugs>
  Which problems in your code get warnings,
                          and which get errors. <warnings-and-errors>

.. toctree::

  actual-bugs-we-haven't-fixed-yet
  interoperation
  incompatibilities-of-gcc
  fixed-header-files
  standard-libraries
  disappointments-and-misunderstandings
  common-misunderstandings-with-gnu-c++
  certain-changes-we-don't-want-to-make
  warning-messages-and-error-messages

