.. _gcov-data-files:

Brief Description of :command:`gcov` Data Files:command:`gcov` uses two files for profiling.  The names of these files
are derived from the original *object* file by substituting the
file suffix with either .gcno, or .gcda.  The files
contain coverage and profile data stored in a platform-independent format.
The .gcno files are placed in the same directory as the object
file.  By default, the .gcda files are also stored in the same
directory as the object file, but the GCC :option:`-fprofile-dir` option
may be used to store the .gcda files in a separate directory.

The .gcno notes file is generated when the source file is compiled
with the GCC :option:`-ftest-coverage` option.  It contains information to
reconstruct the basic block graphs and assign source line numbers to
blocks.

The .gcda count data file is generated when a program containing
object files built with the GCC :option:`-fprofile-arcs` option is executed.
A separate .gcda file is created for each object file compiled with
this option.  It contains arc transition counts, value profile counts, and
some summary information.

The full details of the file format is specified in gcov-io.h,
and functions provided in that header file should be used to access the
coverage files.

