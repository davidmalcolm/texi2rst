Invoking :command:`gcov-tool`

.. code-block:: c++

  gcov-tool [``global-options``] SUB_COMMAND [``sub_command-options``] ``profile_dir``

:command:`gcov-tool` accepts the following options:

@c man begin SYNOPSIS
gcov-tool [@option{-v}|@option{--version}] [@option{-h}|@option{--help}]

gcov-tool merge [merge-options] @var{directory1} @var{directory2}
     [@option{-v}|@option{--verbose}]
     [@option{-o}|@option{ --output} @var{directory}]
     [@option{-w}|@option{--weight} @var{w1,w2}]

gcov-tool rewrite [rewrite-options] @var{directory}
     [@option{-v}|@option{--verbose}]
     [@option{-o}|@option{--output} @var{directory}]
     [@option{-s}|@option{--scale} @var{float_or_simple-frac_value}]
     [@option{-n}|@option{--normalize} @var{long_long_value}]

gcov-tool overlap [overlap-options] @var{directory1} @var{directory2}
     [@option{-v}|@option{--verbose}]
     [@option{-h}|@option{--hotonly}]
     [@option{-f}|@option{--function}]
     [@option{-F}|@option{--fullname}]
     [@option{-o}|@option{--object}]
     [@option{-t}|@option{--hot_threshold}] @var{float}

@c man end
@c man begin SEEALSO
gpl(7), gfdl(7), fsf-funding(7), gcc(1), gcov(1) and the Info entry for
@file{gcc}.
@c man end

.. man begin OPTIONS 

-h--help
  Display help about using :command:`gcov-tool` (on the standard output), and
  exit without doing any further processing.

-v--version
  Display the :command:`gcov-tool` version number (on the standard output),
  and exit without doing any further processing.

merge
  Merge two profile directories.

  -v--verbose
    Set the verbose mode.

  -o ``directory``--output ``directory``
    Set the output profile directory. Default output directory name is
    ``merged_profile``.

  -w ``w1``,``w2``--weight ``w1``,``w2``
    Set the merge weights of the ``directory1`` and ``directory2``,
    respectively. The default weights are 1 for both.

rewrite
  Read the specified profile directory and rewrite to a new directory.

  -v--verbose
    Set the verbose mode.

  -o ``directory``--output ``directory``
    Set the output profile directory. Default output name is ``rewrite_profile``.

  -s ``float_or_simple-frac_value``--scale ``float_or_simple-frac_value``
    Scale the profile counters. The specified value can be in floating point value,
    or simple fraction value form, such 1, 2, 2/3, and 5/3.

  -n ``long_long_value``--normalize <long_long_value>
    Normalize the profile. The specified value is the max counter value
    in the new profile.

overlap
  Computer the overlap score between the two specified profile directories.
  The overlap score is computed based on the arc profiles. It is defined as
  the sum of min (p1_counter[i] / p1_sum_all, p2_counter[i] / p2_sum_all),
  for all arc counter i, where p1_counter[i] and p2_counter[i] are two
  matched counters and p1_sum_all and p2_sum_all are the sum of counter
  values in profile 1 and profile 2, respectively.

  -v--verbose
    Set the verbose mode.

  -h--hotonly
    Only print info for hot objects/functions.

  -f--function
    Print function level overlap score.

  -F--fullname
    Print full gcda filename.

  -o--object
    Print object level overlap score.

  -t ``float``--hot_threshold <float>
    Set the threshold for hot counter value.

.. man end 
   Copyright (C) 1988-2015 Free Software Foundation, Inc. 

.. This is part of the GCC manual. 
   For copying conditions, see the file gcc.texi. 

