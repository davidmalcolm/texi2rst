
Where's the Template?
*********************

.. index:: template instantiation

C++ templates are the first language feature to require more
intelligence from the environment than one usually finds on a UNIX
system.  Somehow the compiler and linker have to make sure that each
template instance occurs exactly once in the executable if it is needed,
and not at all otherwise.  There are two basic approaches to this
problem, which are referred to as the Borland model and the Cfront model.

Borland model
  Borland C++ solved the template instantiation problem by adding the code
  equivalent of common blocks to their linker; the compiler emits template
  instances in each translation unit that uses them, and the linker
  collapses them together.  The advantage of this model is that the linker
  only has to consider the object files themselves; there is no external
  complexity to worry about.  This disadvantage is that compilation time
  is increased because the template code is being compiled repeatedly.
  Code written for this model tends to include definitions of all
  templates in the header file, since they must be seen to be
  instantiated.

Cfront model
  The AT&T C++ translator, Cfront, solved the template instantiation
  problem by creating the notion of a template repository, an
  automatically maintained place where template instances are stored.  A
  more modern version of the repository works as follows: As individual
  object files are built, the compiler places any template definitions and
  instantiations encountered in the repository.  At link time, the link
  wrapper adds in the objects in the repository and compiles any needed
  instances that were not previously emitted.  The advantages of this
  model are more optimal compilation speed and the ability to use the
  system linker; to implement the Borland model a compiler vendor also
  needs to replace the linker.  The disadvantages are vastly increased
  complexity, and thus potential for error; for some code this can be
  just as transparent, but in practice it can been very difficult to build
  multiple programs in one directory and one program in multiple
  directories.  Code written for this model tends to separate definitions
  of non-inline member templates into a separate file, which should be
  compiled separately.

  When used with GNU ld version 2.8 or later on an ELF system such as
GNU/Linux or Solaris 2, or on Microsoft Windows, G++ supports the
Borland model.  On other systems, G++ implements neither automatic
model.

You have the following options for dealing with template instantiations:

* 
  .. index:: frepo

  Compile your template-using code with :option:`-frepo`.  The compiler
  generates files with the extension .rpo listing all of the
  template instantiations used in the corresponding object files that
  could be instantiated there; the link wrapper, collect2,
  then updates the .rpo files to tell the compiler where to place
  those instantiations and rebuild any affected object files.  The
  link-time overhead is negligible after the first pass, as the compiler
  continues to place the instantiations in the same files.

  This is your best option for application code written for the Borland
  model, as it just works.  Code written for the Cfront model 
  needs to be modified so that the template definitions are available at
  one or more points of instantiation; usually this is as simple as adding
  ``#include <tmethods.cc>`` to the end of each template header.

  For library code, if you want the library to provide all of the template
  instantiations it needs, just try to link all of its object files
  together; the link will fail, but cause the instantiations to be
  generated as a side effect.  Be warned, however, that this may cause
  conflicts if multiple libraries try to provide the same instantiations.
  For greater control, use explicit instantiation as described in the next
  option.

* 
  .. index:: fno-implicit-templates

  Compile your code with :option:`-fno-implicit-templates` to disable the
  implicit generation of template instances, and explicitly instantiate
  all the ones you use.  This approach requires more knowledge of exactly
  which instances you need than do the others, but it's less
  mysterious and allows greater control.  You can scatter the explicit
  instantiations throughout your program, perhaps putting them in the
  translation units where the instances are used or the translation units
  that define the templates themselves; you can put all of the explicit
  instantiations you need into one big file; or you can create small files
  like

  .. code-block:: c++

    #include "Foo.h"
    #include "Foo.cc"

    template class Foo<int>;
    template ostream& operator <<
                    (ostream&, const Foo<int>&);

  for each of the instances you need, and create a template instantiation
  library from those.

  If you are using Cfront-model code, you can probably get away with not
  using :option:`-fno-implicit-templates` when compiling files that don't
  #include the member template definitions.

  If you use one big file to do the instantiations, you may want to
  compile it without :option:`-fno-implicit-templates` so you get all of the
  instances required by your explicit instantiations (but not by any
  other files) without having to specify them as well.

  The ISO C++ 2011 standard allows forward declaration of explicit
  instantiations (with ``extern``). G++ supports explicit instantiation
  declarations in C++98 mode and has extended the template instantiation
  syntax to support instantiation of the compiler support data for a
  template class (i.e. the vtable) without instantiating any of its
  members (with ``inline``), and instantiation of only the static data
  members of a template class, without the support data or member
  functions (with ``static``):

  .. code-block:: c++

    extern template int max (int, int);
    inline template class Foo<int>;
    static template class Foo<int>;

* Do nothing.  Pretend G++ does implement automatic instantiation
  management.  Code written for the Borland model works fine, but
  each translation unit contains instances of each of the templates it
  uses.  In a large program, this can lead to an unacceptable amount of code
  duplication.

