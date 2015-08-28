
Options for Directory Search
****************************

.. index:: directory options

.. index:: options, directory search

.. index:: search path

These options specify directories to search for header files, for
libraries and for parts of the compiler:

.. option:: -Idir, -I

  Add the directory ``dir`` to the head of the list of directories to be
  searched for header files.  This can be used to override a system header
  file, substituting your own version, since these directories are
  searched before the system header file directories.  However, you should
  not use this option to add directories that contain vendor-supplied
  system header files (use :option:`-isystem` for that).  If you use more than
  one :option:`-I` option, the directories are scanned in left-to-right
  order; the standard system directories come after.

  If a standard system include directory, or a directory specified with
  :option:`-isystem`, is also specified with :option:`-I`, the :option:`-I`
  option is ignored.  The directory is still searched but as a
  system directory at its normal position in the system include chain.
  This is to ensure that GCC's procedure to fix buggy system headers and
  the ordering for the ``include_next`` directive are not inadvertently changed.
  If you really need to change the search order for system directories,
  use the :option:`-nostdinc` and/or :option:`-isystem` options.

.. option:: -iplugindir=dir

  Set the directory to search for plugins that are passed
  by :option:`-fplugin=``name``` instead of
  :option:`-fplugin=``path``/``name``.so`.  This option is not meant
  to be used by the user, but only passed by the driver.

.. option:: -iquotedir, -iquote

  Add the directory ``dir`` to the head of the list of directories to
  be searched for header files only for the case of ``#include
  "``file``"``; they are not searched for ``#include <``file``>``,
  otherwise just like :option:`-I`.

.. option:: -Ldir, -L

  Add directory ``dir`` to the list of directories to be searched
  for :option:`-l`.

.. option:: -Bprefix, -B

  This option specifies where to find the executables, libraries,
  include files, and data files of the compiler itself.

  The compiler driver program runs one or more of the subprograms
  :command:`cpp`, :command:`cc1`, :command:`as` and :command:`ld`.  It tries
  ``prefix`` as a prefix for each program it tries to run, both with and
  without ``machine``/``version``/ (Target Options).

  For each subprogram to be run, the compiler driver first tries the
  :option:`-B` prefix, if any.  If that name is not found, or if :option:`-B`
  is not specified, the driver tries two standard prefixes, 
  /usr/lib/gcc/ and /usr/local/lib/gcc/.  If neither of
  those results in a file name that is found, the unmodified program
  name is searched for using the directories specified in your
  :envvar:`PATH` environment variable.

  The compiler checks to see if the path provided by :option:`-B`
  refers to a directory, and if necessary it adds a directory
  separator character at the end of the path.

  :option:`-B` prefixes that effectively specify directory names also apply
  to libraries in the linker, because the compiler translates these
  options into :option:`-L` options for the linker.  They also apply to
  include files in the preprocessor, because the compiler translates these
  options into :option:`-isystem` options for the preprocessor.  In this case,
  the compiler appends include to the prefix.

  The runtime support file libgcc.a can also be searched for using
  the :option:`-B` prefix, if needed.  If it is not found there, the two
  standard prefixes above are tried, and that is all.  The file is left
  out of the link if it is not found by those means.

  Another way to specify a prefix much like the :option:`-B` prefix is to use
  the environment variable :envvar:`GCC_EXEC_PREFIX`.  See :ref:`environment-variables`.

  As a special kludge, if the path provided by :option:`-B` is
  [dir/]stage``N``/, where ``N`` is a number in the range 0 to
  9, then it is replaced by [dir/]include.  This is to help
  with boot-strapping the compiler.

.. option:: -specs=file

  Process ``file`` after the compiler reads in the standard specs
  file, in order to override the defaults which the :command:`gcc` driver
  program uses when determining what switches to pass to :command:`cc1`,
  :command:`cc1plus`, :command:`as`, :command:`ld`, etc.  More than one
  :option:`-specs=``file``` can be specified on the command line, and they
  are processed in order, from left to right.

.. option:: --sysroot=dir

  Use ``dir`` as the logical root directory for headers and libraries.
  For example, if the compiler normally searches for headers in
  /usr/include and libraries in /usr/lib, it instead
  searches ``dir``/usr/include and ``dir``/usr/lib.

  If you use both this option and the :option:`-isysroot` option, then
  the :option:`--sysroot` option applies to libraries, but the
  :option:`-isysroot` option applies to header files.

  The GNU linker (beginning with version 2.16) has the necessary support
  for this option.  If your linker does not support this option, the
  header file aspect of :option:`--sysroot` still works, but the
  library aspect does not.

.. option:: --no-sysroot-suffix, -no-sysroot-suffix

  For some targets, a suffix is added to the root directory specified
  with :option:`--sysroot`, depending on the other options used, so that
  headers may for example be found in
  ``dir``/``suffix``/usr/include instead of
  ``dir``/usr/include.  This option disables the addition of
  such a suffix.

.. option:: -I-

  This option has been deprecated.  Please use :option:`-iquote` instead for
  :option:`-I` directories before the :option:`-I-` and remove the :option:`-I-`
  option.
  Any directories you specify with :option:`-I` options before the :option:`-I-`
  option are searched only for the case of ``#include "``file``"``;
  they are not searched for ``#include <``file``>``.

  If additional directories are specified with :option:`-I` options after
  the :option:`-I-` option, these directories are searched for all ``#include``
  directives.  (Ordinarily all :option:`-I` directories are used
  this way.)

  In addition, the :option:`-I-` option inhibits the use of the current
  directory (where the current input file came from) as the first search
  directory for ``#include "``file``"``.  There is no way to
  override this effect of :option:`-I-`.  With :option:`-I.` you can specify
  searching the directory that is current when the compiler is
  invoked.  That is not exactly the same as what the preprocessor does
  by default, but it is often satisfactory.

  :option:`-I-` does not inhibit the use of the standard system directories
  for header files.  Thus, :option:`-I-` and :option:`-nostdinc` are
  independent.

.. man end

