.. _invoking-gcov:

Invoking :command:`gcov`
.. code-block:: c++

  gcov [``options``] ``files``

:command:`gcov` accepts the following options:

@c man begin SYNOPSIS
gcov [@option{-v}|@option{--version}] [@option{-h}|@option{--help}]
     [@option{-a}|@option{--all-blocks}]
     [@option{-b}|@option{--branch-probabilities}]
     [@option{-c}|@option{--branch-counts}]
     [@option{-d}|@option{--display-progress}]
     [@option{-f}|@option{--function-summaries}]
     [@option{-i}|@option{--intermediate-format}]
     [@option{-l}|@option{--long-file-names}]
     [@option{-m}|@option{--demangled-names}]
     [@option{-n}|@option{--no-output}]
     [@option{-o}|@option{--object-directory} @var{directory|file}]
     [@option{-p}|@option{--preserve-paths}]
     [@option{-r}|@option{--relative-only}]
     [@option{-s}|@option{--source-prefix} @var{directory}]
     [@option{-u}|@option{--unconditional-branches}]
     @var{files}
@c man end
@c man begin SEEALSO
gpl(7), gfdl(7), fsf-funding(7), gcc(1) and the Info entry for @file{gcc}.
@c man end

.. man begin OPTIONS

-h --help
  Display help about using :command:`gcov` (on the standard output), and
  exit without doing any further processing.

-v --version
  Display the :command:`gcov` version number (on the standard output),
  and exit without doing any further processing.

-a --all-blocks
  Write individual execution counts for every basic block.  Normally gcov
  outputs execution counts only for the main blocks of a line.  With this
  option you can determine if blocks within a single line are not being
  executed.

-b --branch-probabilities
  Write branch frequencies to the output file, and write branch summary
  info to the standard output.  This option allows you to see how often
  each branch in your program was taken.  Unconditional branches will not
  be shown, unless the :option:`-u` option is given.

-c --branch-counts
  Write branch frequencies as the number of branches taken, rather than
  the percentage of branches taken.

-n --no-output
  Do not create the :command:`gcov` output file.

-l --long-file-names
  Create long file names for included source files.  For example, if the
  header file x.h contains code, and was included in the file
  a.c, then running :command:`gcov` on the file a.c will
  produce an output file called a.c##x.h.gcov instead of
  x.h.gcov.  This can be useful if x.h is included in
  multiple source files and you want to see the individual
  contributions.  If you use the :samp:`-p` option, both the including
  and included file names will be complete path names.

-p --preserve-paths
  Preserve complete path information in the names of generated
  .gcov files.  Without this option, just the filename component is
  used.  With this option, all directories are used, with :samp:`/` characters
  translated to :samp:`#` characters, . directory components
  removed and unremoveable ..
  components renamed to :samp:`^`.  This is useful if sourcefiles are in several
  different directories.

-r --relative-only
  Only output information about source files with a relative pathname
  (after source prefix elision).  Absolute paths are usually system
  header files and coverage of any inline functions therein is normally
  uninteresting.

-f --function-summaries
  Output summaries for each function in addition to the file level summary.

-o ``directory|file`` --object-directory ``directory`` --object-file ``file``
  Specify either the directory containing the gcov data files, or the
  object path name.  The .gcno, and
  .gcda data files are searched for using this option.  If a directory
  is specified, the data files are in that directory and named after the
  input file name, without its extension.  If a file is specified here,
  the data files are named after that file, without its extension.

-s ``directory`` --source-prefix ``directory``
  A prefix for source file names to remove when generating the output
  coverage files.  This option is useful when building in a separate
  directory, and the pathname to the source directory is not wanted when
  determining the output file names.  Note that this prefix detection is
  applied before determining whether the source file is absolute.

-u --unconditional-branches
  When branch probabilities are given, include those of unconditional branches.
  Unconditional branches are normally not interesting.

-d --display-progress
  Display the progress on the standard output.

-i --intermediate-format
  Output gcov file in an easy-to-parse intermediate text format that can
  be used by :command:`lcov` or other tools. The output is a single
  .gcov file per .gcda file. No source code is required.

  The format of the intermediate .gcov file is plain text with
  one entry per line

  .. code-block:: c++

    file:``source_file_name``
    function:``line_number``,``execution_count``,``function_name``
    lcount:``line number``,``execution_count``
    branch:``line_number``,``branch_coverage_type``

    Where the ``branch_coverage_type`` is
       notexec (Branch not executed)
       taken (Branch executed and taken)
       nottaken (Branch executed, but not taken)

    There can be multiple ``file`` entries in an intermediate gcov
    file. All entries following a ``file`` pertain to that source file
    until the next ``file`` entry.

  Here is a sample when :option:`-i` is used in conjunction with :option:`-b` option:

  .. code-block:: c++

    file:array.cc
    function:11,1,_Z3sumRKSt6vectorIPiSaIS0_EE
    function:22,1,main
    lcount:11,1
    lcount:12,1
    lcount:14,1
    branch:14,taken
    lcount:26,1
    branch:28,nottaken

-m --demangled-names
  Display demangled function names in output. The default is to show
  mangled function names.

  :command:`gcov` should be run with the current directory the same as that
when you invoked the compiler.  Otherwise it will not be able to locate
the source files.  :command:`gcov` produces files called
``mangledname``.gcov in the current directory.  These contain
the coverage information of the source file they correspond to.
One .gcov file is produced for each source (or header) file
containing code,
which was compiled to produce the data files.  The ``mangledname`` part
of the output file name is usually simply the source file name, but can
be something more complicated if the :samp:`-l` or :samp:`-p` options are
given.  Refer to those options for details.

If you invoke :command:`gcov` with multiple input files, the
contributions from each input file are summed.  Typically you would
invoke it with the same list of files as the final link of your executable.

The .gcov files contain the :samp:`:` separated fields along with
program source code.  The format is

.. code-block:: c++

  ``execution_count``:``line_number``:``source line text``

Additional block information may succeed each line, when requested by
command line option.  The ``execution_count`` is :samp:`-` for lines
containing no code.  Unexecuted lines are marked :samp:`#####` or
:samp:`====`, depending on whether they are reachable by
non-exceptional paths or only exceptional paths such as C++ exception
handlers, respectively.

Some lines of information at the start have ``line_number`` of zero.
These preamble lines are of the form

:option:`-:0:```tag``:``value``
The ordering and number of these preamble lines will be augmented as
:command:`gcov` development progresses - do not rely on them remaining
unchanged.  Use ``tag`` to locate a particular preamble line.

The additional block information is of the form

.. code-block:: c++

  ``tag`` ``information``

The ``information`` is human readable, but designed to be simple
enough for machine parsing too.

When printing percentages, 0% and 100% are only printed when the values
are *exactly* 0% and 100% respectively.  Other values which would
conventionally be rounded to 0% or 100% are instead printed as the
nearest non-boundary value.

When using :command:`gcov`, you must first compile your program with two
special GCC options: :samp:`-fprofile-arcs -ftest-coverage`.
This tells the compiler to generate additional information needed by
gcov (basically a flow graph of the program) and also includes
additional code in the object files for generating the extra profiling
information needed by gcov.  These additional files are placed in the
directory where the object file is located.

Running the program will cause profile output to be generated.  For each
source file compiled with :option:`-fprofile-arcs`, an accompanying
.gcda file will be placed in the object file directory.

Running :command:`gcov` with your program's source file names as arguments
will now produce a listing of the code along with frequency of execution
for each line.  For example, if your program is called tmp.c, this
is what you see when you use the basic :command:`gcov` facility:

.. code-block:: c++

  $ gcc -fprofile-arcs -ftest-coverage tmp.c
  $ a.out
  $ gcov tmp.c
  90.00% of 10 source lines executed in file tmp.c
  Creating tmp.c.gcov.

The file tmp.c.gcov contains output from :command:`gcov`.
Here is a sample:

.. code-block:: c++

          -:    0:Source:tmp.c
          -:    0:Graph:tmp.gcno
          -:    0:Data:tmp.gcda
          -:    0:Runs:1
          -:    0:Programs:1
          -:    1:#include <stdio.h>
          -:    2:
          -:    3:int main (void)
          1:    4:{
          1:    5:  int i, total;
          -:    6:
          1:    7:  total = 0;
          -:    8:
         11:    9:  for (i = 0; i < 10; i++)
         10:   10:    total += i;
          -:   11:
          1:   12:  if (total != 45)
      #####:   13:    printf ("Failure\n");
          -:   14:  else
          1:   15:    printf ("Success\n");
          1:   16:  return 0;
          -:   17:}

When you use the :option:`-a` option, you will get individual block
counts, and the output looks like this:

.. code-block:: c++

          -:    0:Source:tmp.c
          -:    0:Graph:tmp.gcno
          -:    0:Data:tmp.gcda
          -:    0:Runs:1
          -:    0:Programs:1
          -:    1:#include <stdio.h>
          -:    2:
          -:    3:int main (void)
          1:    4:{
          1:    4-block  0
          1:    5:  int i, total;
          -:    6:
          1:    7:  total = 0;
          -:    8:
         11:    9:  for (i = 0; i < 10; i++)
         11:    9-block  0
         10:   10:    total += i;
         10:   10-block  0
          -:   11:
          1:   12:  if (total != 45)
          1:   12-block  0
      #####:   13:    printf ("Failure\n");
      $$$$$:   13-block  0
          -:   14:  else
          1:   15:    printf ("Success\n");
          1:   15-block  0
          1:   16:  return 0;
          1:   16-block  0
          -:   17:}

In this mode, each basic block is only shown on one line - the last
line of the block.  A multi-line block will only contribute to the
execution count of that last line, and other lines will not be shown
to contain code, unless previous blocks end on those lines.
The total execution count of a line is shown and subsequent lines show
the execution counts for individual blocks that end on that line.  After each
block, the branch and call counts of the block will be shown, if the
:option:`-b` option is given.

Because of the way GCC instruments calls, a call count can be shown
after a line with no individual blocks.
As you can see, line 13 contains a basic block that was not executed.

When you use the :option:`-b` option, your output looks like this:

.. code-block:: c++

  $ gcov -b tmp.c
  90.00% of 10 source lines executed in file tmp.c
  80.00% of 5 branches executed in file tmp.c
  80.00% of 5 branches taken at least once in file tmp.c
  50.00% of 2 calls executed in file tmp.c
  Creating tmp.c.gcov.

Here is a sample of a resulting tmp.c.gcov file:

.. code-block:: c++

          -:    0:Source:tmp.c
          -:    0:Graph:tmp.gcno
          -:    0:Data:tmp.gcda
          -:    0:Runs:1
          -:    0:Programs:1
          -:    1:#include <stdio.h>
          -:    2:
          -:    3:int main (void)
  function main called 1 returned 1 blocks executed 75%
          1:    4:{
          1:    5:  int i, total;
          -:    6:
          1:    7:  total = 0;
          -:    8:
         11:    9:  for (i = 0; i < 10; i++)
  branch  0 taken 91% (fallthrough)
  branch  1 taken 9%
         10:   10:    total += i;
          -:   11:
          1:   12:  if (total != 45)
  branch  0 taken 0% (fallthrough)
  branch  1 taken 100%
      #####:   13:    printf ("Failure\n");
  call    0 never executed
          -:   14:  else
          1:   15:    printf ("Success\n");
  call    0 called 1 returned 100%
          1:   16:  return 0;
          -:   17:}

For each function, a line is printed showing how many times the function
is called, how many times it returns and what percentage of the
function's blocks were executed.

For each basic block, a line is printed after the last line of the basic
block describing the branch or call that ends the basic block.  There can
be multiple branches and calls listed for a single source line if there
are multiple basic blocks that end on that line.  In this case, the
branches and calls are each given a number.  There is no simple way to map
these branches and calls back to source constructs.  In general, though,
the lowest numbered branch or call will correspond to the leftmost construct
on the source line.

For a branch, if it was executed at least once, then a percentage
indicating the number of times the branch was taken divided by the
number of times the branch was executed will be printed.  Otherwise, the
message 'never executed' is printed.

For a call, if it was executed at least once, then a percentage
indicating the number of times the call returned divided by the number
of times the call was executed will be printed.  This will usually be
100%, but may be less for functions that call ``exit`` or ``longjmp``,
and thus may not return every time they are called.

The execution counts are cumulative.  If the example program were
executed again without removing the .gcda file, the count for the
number of times each line in the source was executed would be added to
the results of the previous run(s).  This is potentially useful in
several ways.  For example, it could be used to accumulate data over a
number of program runs as part of a test verification suite, or to
provide more accurate long-term information over a large number of
program runs.

The data in the .gcda files is saved immediately before the program
exits.  For each source file compiled with :option:`-fprofile-arcs`, the
profiling code first attempts to read in an existing .gcda file; if
the file doesn't match the executable (differing number of basic block
counts) it will ignore the contents of the file.  It then adds in the
new execution counts and finally writes the data to the file.

