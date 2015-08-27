Data File Relocation to Support Cross-Profiling
***********************************************

Running the program will cause profile output to be generated.  For each
source file compiled with :option:`-fprofile-arcs`, an accompanying .gcda
file will be placed in the object file directory. That implicitly requires
running the program on the same system as it was built or having the same
absolute directory structure on the target system. The program will try
to create the needed directory structure, if it is not already present.

To support cross-profiling, a program compiled with :option:`-fprofile-arcs`
can relocate the data files based on two environment variables:

* GCOV_PREFIX contains the prefix to add to the absolute paths
  in the object file. Prefix can be absolute, or relative.  The
  default is no prefix.

  * GCOV_PREFIX_STRIP indicates the how many initial directory names to strip off
  the hardwired absolute paths. Default value is 0.

  Note: If GCOV_PREFIX_STRIP is set without GCOV_PREFIX is undefined,
   then a relative path is made out of the hardwired absolute paths.

For example, if the object file /user/build/foo.o was built with
:option:`-fprofile-arcs`, the final executable will try to create the data file
/user/build/foo.gcda when running on the target system.  This will
fail if the corresponding directory does not exist and it is unable to create
it.  This can be overcome by, for example, setting the environment as
GCOV_PREFIX=/target/run and GCOV_PREFIX_STRIP=1.  Such a
setting will name the data file /target/run/build/foo.gcda.

You must move the data files to the expected directory tree in order to
use them for profile directed optimizations (:option:`--use-profile`), or to
use the :command:`gcov` tool.

.. Copyright (C) 2014-2015 Free Software Foundation, Inc. 
   This is part of the GCC manual. 

.. For copying conditions, see the file gcc.texi. 

@c man begin COPYRIGHT
Copyright @copyright{} 2014-2015 Free Software Foundation, Inc.

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3 or
any later version published by the Free Software Foundation; with the
Invariant Sections being ``GNU General Public License'' and ``Funding
Free Software'', the Front-Cover texts being (a) (see below), and with
the Back-Cover Texts being (b) (see below).  A copy of the license is
included in the gfdl(7) man page.

(a) The FSF's Front-Cover Text is:

     A GNU Manual

(b) The FSF's Back-Cover Text is:

     You have freedom to copy and modify this GNU Manual, like GNU
     software.  Copies published by the Free Software Foundation raise
     funds for GNU development.
@c man end
@c Set file name and title for the man page.
@setfilename gcov-tool
@settitle offline gcda profile processing tool

