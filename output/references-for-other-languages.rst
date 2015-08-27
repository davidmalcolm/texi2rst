References for Other Languages
******************************

TopGNAT Reference ManualAbout This Guidegnat_rmGNAT Reference Manual, for information on standard
conformance and compatibility of the Ada compiler.

StandardsStandardsgfortranThe GNU Fortran Compiler, for details
of standards supported by GNU Fortran.

CompatibilityCompatibility with the Java PlatformgcjGNU gcj,
for details of compatibility between :command:`gcj` and the Java Platform.

.. Copyright (C) 1988-2015 Free Software Foundation, Inc.

.. This is part of the GCC manual.

.. For copying conditions, see the file gcc.texi.

@c man begin INCLUDE
@include gcc-vers.texi
@c man end

@c man begin COPYRIGHT
Copyright @copyright{} 1988-2015 Free Software Foundation, Inc.

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
@setfilename gcc
@settitle GNU project C and C++ compiler
@c man begin SYNOPSIS
gcc [@option{-c}|@option{-S}|@option{-E}] [@option{-std=}@var{standard}]
    [@option{-g}] [@option{-pg}] [@option{-O}@var{level}]
    [@option{-W}@var{warn}@dots{}] [@option{-Wpedantic}]
    [@option{-I}@var{dir}@dots{}] [@option{-L}@var{dir}@dots{}]
    [@option{-D}@var{macro}[=@var{defn}]@dots{}] [@option{-U}@var{macro}]
    [@option{-f}@var{option}@dots{}] [@option{-m}@var{machine-option}@dots{}]
    [@option{-o} @var{outfile}] [@@@var{file}] @var{infile}@dots{}

Only the most useful options are listed here; see below for the
remainder.  @command{g++} accepts mostly the same options as @command{gcc}.
@c man end
@c man begin SEEALSO
gpl(7), gfdl(7), fsf-funding(7),
cpp(1), gcov(1), as(1), ld(1), gdb(1), adb(1), dbx(1), sdb(1)
and the Info entries for @file{gcc}, @file{cpp}, @file{as},
@file{ld}, @file{binutils} and @file{gdb}.
@c man end
@c man begin BUGS
For instructions on reporting bugs, see
@w{@value{BUGURL}}.
@c man end
@c man begin AUTHOR
See the Info entry for @command{gcc}, or
@w{@uref{http://gcc.gnu.org/onlinedocs/gcc/Contributors.html}},
for contributors to GCC@.
@c man end
