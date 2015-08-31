.. %**start of header

.. INTERNALS is used by md.texi to determine whether to include the
   whole of that file, in the internals manual, or only the part
   dealing with constraints, in the user manual.

.. NOTE: checks/things to do:
    c
   -have bob do a search in all seven files for "mew" (ideally -mew,
    but i may have forgotten the occasional "-"..).
       Just checked... all have `-'!  Bob 22Jul96
       Use this to search:   grep -n '\-\-mew' *.texi
   -item/itemx, text after all (sub/sub)section titles, etc..
   -consider putting the lists of options on pp 17-> etc in columns or
    some such.
   -overfulls.  do a search for "mew" in the files, and you will see
     overfulls that i noted but could not deal with.
   -have to add text:  beginning of chapter 8
    c
   anything else?                       -mew 10feb93
   Copyright (C) 2001-2015 Free Software Foundation, Inc.
   This is part of the GCC manual.
   For copying conditions, see the file gcc.texi.
   Version number and development mode.
   version-GCC is @set to the base GCC version number.
   DEVELOPMENT is @set for an in-development version, @clear for a
   release version (corresponding to ``experimental''/anything else
   in gcc/DEV-PHASE).

.. Common macros to support generating man pages:

.. Makeinfo handles the above macro OK, TeX needs manual line breaks;
   they get lost at some point in handling the macro.  But if @macro is
   used here rather than @alias, it produces double line breaks.

.. For FSF printing, define FSFPRINT.  Also update the ISBN and last
   printing date for the manual being printed.
   @set FSFPRINT
   Macro to generate a "For the N.N.N version" subtitle on the title
   page of TeX documentation.  This macro should be used in the
   titlepage environment after the title and any other subtitles have
   been placed, and before any authors are placed.

.. Create a separate index for command line options.

.. Merge the standard indexes into a single one.

.. %**end of header

Copyright (C) 1988-2015 Free Software Foundation, Inc.

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3 or
any later version published by the Free Software Foundation; with the
Invariant Sections being 'Funding Free Software', the Front-Cover
Texts being (a) (see below), and with the Back-Cover Texts being (b)
(see below).  A copy of the license is included in the section entitled
'GNU Free Documentation License'.

(a) The FSF's Front-Cover Text is:

A GNU Manual

(b) The FSF's Back-Cover Text is:

You have freedom to copy and modify this GNU Manual, like GNU
     software.  Copies published by the Free Software Foundation raise
     funds for GNU development.

Software developmentThe GNU Compiler Collection. <(gcc)>
The GNU C++ compiler. <(gcc)>
:command:`gcov`-a test coverage program. <(gcc)-gcov>
:command:`gcov-tool`-an offline gcda profile processing program. <(gcc)-gcov-tool>
This file documents the use of the GNU compilers.

Using the GNU Compiler CollectionFor gcc version 6.0.0 (pre-release)(GCC)
.. Even if there are no authors, the second titlepage line should be
   forced to the bottom of the page.

 0pt plus 1filllRichard M. Stallman and the GCC Developer Community 0pt plus 1filllPublished by:

===============================  ================================
GNU Press                        Website: http://www.gnupress.org
===============================  ================================
a division of the                General: press@gnu.org
Free Software Foundation         Orders:  sales@gnu.org
51 Franklin Street, Fifth Floor  Tel 617-542-5942
Boston, MA 02110-1301 USA        Fax 617-542-2652
===============================  ================================
Last printed October 2003 for GCC 3.3.1.

Printed copies are available for $45 each.

.. _top:

Introduction
============

.. index:: introduction

This manual documents how to use the GNU compilers,
as well as their features and incompatibilities, and how to report
bugs.  It corresponds to the compilers
(GCC)
version 6.0.0.
The internals of the GNU compilers, including how to port them to new
targets and some information about how to write front ends for new
languages, are documented in a separate manual.  See :ref:`Introduction <top>`.

.. toctree::

  You can compile C or C++ programs. <g++-and-gcc>
  Language standards supported by GCC. <standards>
  Command options supported by :samp:`gcc`. <invoking-gcc>
  How GCC implements the ISO C specification. <c-implementation>
  How GCC implements the ISO C++ specification. <c++-implementation>
  GNU extensions to the C language family. <c-extensions>
  GNU extensions to the C++ language. <c++-extensions>
  GNU Objective-C runtime features. <objective-c>
  Binary Compatibility <compatibility>
  :command:`gcov`-a test coverage program. <gcov>
  :command:`gcov-tool`-an offline gcda profile processing program. <gcov-tool>
  If you have trouble using GCC. <trouble>
  How, why and where to report bugs. <bugs>
  How To Get Help with GCC <service>
  How to contribute to testing and developing GCC. <contributing>

  How to help assure funding for free software. <funding>
  The GNU Project and GNU/Linux. <gnu-project>

  GNU General Public License says
                      how you can copy and share GCC. <copying>
  How you can copy and share this manual. <gnu-free-documentation-license>
  People who have contributed to GCC. <contributors>

  Index to command line options. <option-index>
  Index of concepts and symbol names. <keyword-index>

.. Copyright (C) 1988-2015 Free Software Foundation, Inc.
   This is part of the GCC manual.
   For copying conditions, see the file gcc.texi.

.. toctree::

  programming-languages-supported-by-gcc
  language-standards-supported-by-gcc
  gcc-command-options
  c-implementation-defined-behavior
  c++-implementation-defined-behavior
  extensions-to-the-c-language-family
  extensions-to-the-c++-language
  gnu-objective-c-features
  binary-compatibility
  gcov-a-test-coverage-program
  gcov-tool-an-offline-gcda-profile-processing-tool
  known-causes-of-trouble-with-gcc
  reporting-bugs
  how-to-get-help-with-gcc
  contributing-to-gcc-development

..  comment  node-name,  next,  previous,  up


.. man begin DESCRIPTION

.. _funding:

Funding Free Software
=====================

If you want to have more free software a few years from now, it makes
sense for you to help encourage people to contribute funds for its
development.  The most effective approach known is to encourage
commercial redistributors to donate.

Users of free software systems can boost the pace of development by
encouraging for-a-fee distributors to donate part of their selling price
to free software developers-the Free Software Foundation, and others.

The way to convince distributors to do this is to demand it and expect
it from them.  So when you compare distributors, judge them partly by
how much they give to free software development.  Show distributors
they must compete to be the one who gives the most.

To make this approach work, you must insist on numbers that you can
compare, such as, 'We will donate ten dollars to the Frobnitz project
for each disk sold.'  Don't be satisfied with a vague promise, such as
'A portion of the profits are donated,' since it doesn't give a basis
for comparison.

Even a precise fraction 'of the profits from this disk' is not very
meaningful, since creative accounting and unrelated business decisions
can greatly alter what fraction of the sales price counts as profit.
If the price you pay is $50, ten percent of the profit is probably
less than a dollar; it might be a few cents, or nothing at all.

Some redistributors do development work themselves.  This is useful too;
but to keep everyone honest, you need to inquire how much they do, and
what kind.  Some kinds of development make much more long-term
difference than others.  For example, maintaining a separate version of
a program contributes very little; maintaining the standard version of a
program for the whole community contributes much.  Easy new ports
contribute little, since someone else would surely do them; difficult
ports such as adding a new CPU to the GNU Compiler Collection contribute more;
major new features or packages contribute the most.

By establishing the idea that supporting further development is 'the
proper thing to do' when distributing free software for a fee, we can
assure a steady flow of resources into making more free software.

.. man end

.. man begin COPYRIGHT

Copyright (C) 1994 Free Software Foundation, Inc.
Verbatim copying and redistribution of this section is permitted
without royalty; alteration is not permitted.

.. man end

.. Copyright (C) 2001 Free Software Foundation, Inc.
   This is part of the GCC manual.
   For copying conditions, see the file gcc.texi.

.. _gnu-project:

The GNU Project and GNU/Linux
=============================

The GNU Project was launched in 1984 to develop a complete Unix-like
operating system which is free software: the GNU system.  (GNU is a
recursive acronym for 'GNU's Not Unix'; it is pronounced
'guh-NEW'.)  Variants of the GNU operating system, which use the
kernel Linux, are now widely used; though these systems are often
referred to as 'Linux', they are more accurately called GNU/Linux
systems.

For more information, see:

.. code-block:: c++

  http://www.gnu.org/
  http://www.gnu.org/gnu/linux-and-gnu.html

@c Set file name and title for man page.
@setfilename gpl
@settitle GNU General Public License
@c man begin SEEALSO
gfdl(7), fsf-funding(7).
@c man end
@c man begin COPYRIGHT
Copyright @copyright{} 2007 Free Software Foundation, Inc.

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.
@c man end

.. man begin DESCRIPTION

.. _copying:

GNU General Public License
==========================

Version 3, 29 June 2007
.. This file is intended to be included in another file.

Copyright (C) 2007 Free Software Foundation, Inc. http://fsf.org/

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.
PreambleThe GNU General Public License is a free, copyleft license for
software and other kinds of works.

The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom
to share and change all versions of a program-to make sure it remains
free software for all its users.  We, the Free Software Foundation,
use the GNU General Public License for most of our software; it
applies also to any other work released this way by its authors.  You
can apply it to your programs, too.

When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you
have certain responsibilities if you distribute copies of the
software, or if you modify it: responsibilities to respect the freedom
of others.

For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too,
receive or can get the source code.  And you must show them these
terms so they know their rights.

Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the
manufacturer can do so.  This is fundamentally incompatible with the
aim of protecting users' freedom to change the software.  The
systematic pattern of such abuse occurs in the area of products for
individuals to use, which is precisely where it is most unacceptable.
Therefore, we have designed this version of the GPL to prohibit the
practice for those products.  If such problems arise substantially in
other domains, we stand ready to extend this provision to those
domains in future versions of the GPL, as needed to protect the
freedom of users.

Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish
to avoid the special danger that patents applied to a free program
could make it effectively proprietary.  To prevent this, the GPL
assures that patents cannot be used to render the program non-free.

The precise terms and conditions for copying, distribution and
modification follow.

TERMS AND CONDITIONS0* Definitions.

  'This License' refers to version 3 of the GNU General Public License.

  'Copyright' also means copyright-like laws that apply to other kinds
  of works, such as semiconductor masks.

  'The Program' refers to any copyrightable work licensed under this
  License.  Each licensee is addressed as 'you'.  'Licensees' and
  'recipients' may be individuals or organizations.

  To 'modify' a work means to copy from or adapt all or part of the work
  in a fashion requiring copyright permission, other than the making of
  an exact copy.  The resulting work is called a 'modified version' of
  the earlier work or a work 'based on' the earlier work.

  A 'covered work' means either the unmodified Program or a work based
  on the Program.

  To 'propagate' a work means to do anything with it that, without
  permission, would make you directly or secondarily liable for
  infringement under applicable copyright law, except executing it on a
  computer or modifying a private copy.  Propagation includes copying,
  distribution (with or without modification), making available to the
  public, and in some countries other activities as well.

  To 'convey' a work means any kind of propagation that enables other
  parties to make or receive copies.  Mere interaction with a user
  through a computer network, with no transfer of a copy, is not
  conveying.

  An interactive user interface displays 'Appropriate Legal Notices' to
  the extent that it includes a convenient and prominently visible
  feature that (1) displays an appropriate copyright notice, and (2)
  tells the user that there is no warranty for the work (except to the
  extent that warranties are provided), that licensees may convey the
  work under this License, and how to view a copy of this License.  If
  the interface presents a list of user commands or options, such as a
  menu, a prominent item in the list meets this criterion.

* Source Code.

  The 'source code' for a work means the preferred form of the work for
  making modifications to it.  'Object code' means any non-source form
  of a work.

  A 'Standard Interface' means an interface that either is an official
  standard defined by a recognized standards body, or, in the case of
  interfaces specified for a particular programming language, one that
  is widely used among developers working in that language.

  The 'System Libraries' of an executable work include anything, other
  than the work as a whole, that (a) is included in the normal form of
  packaging a Major Component, but which is not part of that Major
  Component, and (b) serves only to enable use of the work with that
  Major Component, or to implement a Standard Interface for which an
  implementation is available to the public in source code form.  A
  'Major Component', in this context, means a major essential component
  (kernel, window system, and so on) of the specific operating system
  (if any) on which the executable work runs, or a compiler used to
  produce the work, or an object code interpreter used to run it.

  The 'Corresponding Source' for a work in object code form means all
  the source code needed to generate, install, and (for an executable
  work) run the object code and to modify the work, including scripts to
  control those activities.  However, it does not include the work's
  System Libraries, or general-purpose tools or generally available free
  programs which are used unmodified in performing those activities but
  which are not part of the work.  For example, Corresponding Source
  includes interface definition files associated with source files for
  the work, and the source code for shared libraries and dynamically
  linked subprograms that the work is specifically designed to require,
  such as by intimate data communication or control flow between those
  subprograms and other parts of the work.

  The Corresponding Source need not include anything that users can
  regenerate automatically from other parts of the Corresponding Source.

  The Corresponding Source for a work in source code form is that same
  work.

* Basic Permissions.

  All rights granted under this License are granted for the term of
  copyright on the Program, and are irrevocable provided the stated
  conditions are met.  This License explicitly affirms your unlimited
  permission to run the unmodified Program.  The output from running a
  covered work is covered by this License only if the output, given its
  content, constitutes a covered work.  This License acknowledges your
  rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not convey,
  without conditions so long as your license otherwise remains in force.
  You may convey covered works to others for the sole purpose of having
  them make modifications exclusively for you, or provide you with
  facilities for running those works, provided that you comply with the
  terms of this License in conveying all material for which you do not
  control copyright.  Those thus making or running the covered works for
  you must do so exclusively on your behalf, under your direction and
  control, on terms that prohibit them from making any copies of your
  copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under the
  conditions stated below.  Sublicensing is not allowed; section 10
  makes it unnecessary.

* Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
  measure under any applicable law fulfilling obligations under article
  11 of the WIPO copyright treaty adopted on 20 December 1996, or
  similar laws prohibiting or restricting circumvention of such
  measures.

  When you convey a covered work, you waive any legal power to forbid
  circumvention of technological measures to the extent such
  circumvention is effected by exercising rights under this License with
  respect to the covered work, and you disclaim any intention to limit
  operation or modification of the work as a means of enforcing, against
  the work's users, your or third parties' legal rights to forbid
  circumvention of technological measures.

* Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
  receive it, in any medium, provided that you conspicuously and
  appropriately publish on each copy an appropriate copyright notice;
  keep intact all notices stating that this License and any
  non-permissive terms added in accord with section 7 apply to the code;
  keep intact all notices of the absence of any warranty; and give all
  recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
  and you may offer support or warranty protection for a fee.

* Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
  produce it from the Program, in the form of source code under the
  terms of section 4, provided that you also meet all of these
  conditions:

  a* The work must carry prominent notices stating that you modified it,
    and giving a relevant date.

  * The work must carry prominent notices stating that it is released
    under this License and any conditions added under section 7.  This
    requirement modifies the requirement in section 4 to 'keep intact all
    notices'.

  * You must license the entire work, as a whole, under this License to
    anyone who comes into possession of a copy.  This License will
    therefore apply, along with any applicable section 7 additional terms,
    to the whole of the work, and all its parts, regardless of how they
    are packaged.  This License gives no permission to license the work in
    any other way, but it does not invalidate such permission if you have
    separately received it.

  * If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your work
    need not make them do so.

  A compilation of a covered work with other separate and independent
  works, which are not by their nature extensions of the covered work,
  and which are not combined with it such as to form a larger program,
  in or on a volume of a storage or distribution medium, is called an
  'aggregate' if the compilation and its resulting copyright are not
  used to limit the access or legal rights of the compilation's users
  beyond what the individual works permit.  Inclusion of a covered work
  in an aggregate does not cause this License to apply to the other
  parts of the aggregate.

* Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms of
  sections 4 and 5, provided that you also convey the machine-readable
  Corresponding Source under the terms of this License, in one of these
  ways:

  a* Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium customarily
    used for software interchange.

  * Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a written
    offer, valid for at least three years and valid for as long as you
    offer spare parts or customer support for that product model, to give
    anyone who possesses the object code either (1) a copy of the
    Corresponding Source for all the software in the product that is
    covered by this License, on a durable physical medium customarily used
    for software interchange, for a price no more than your reasonable
    cost of physically performing this conveying of source, or (2) access
    to copy the Corresponding Source from a network server at no charge.

  * Convey individual copies of the object code with a copy of the written
    offer to provide the Corresponding Source.  This alternative is
    allowed only occasionally and noncommercially, and only if you
    received the object code with such an offer, in accord with subsection
    6b.

  * Convey the object code by offering access from a designated place
    (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to copy
    the object code is a network server, the Corresponding Source may be
    on a different server (operated by you or a third party) that supports
    equivalent copying facilities, provided you maintain clear directions
    next to the object code saying where to find the Corresponding Source.
    Regardless of what server hosts the Corresponding Source, you remain
    obligated to ensure that it is available for as long as needed to
    satisfy these requirements.

  * Convey the object code using peer-to-peer transmission, provided you
    inform other peers where the object code and Corresponding Source of
    the work are being offered to the general public at no charge under
    subsection 6d.

  A separable portion of the object code, whose source code is excluded
  from the Corresponding Source as a System Library, need not be
  included in conveying the object code work.

  A 'User Product' is either (1) a 'consumer product', which means any
  tangible personal property which is normally used for personal,
  family, or household purposes, or (2) anything designed or sold for
  incorporation into a dwelling.  In determining whether a product is a
  consumer product, doubtful cases shall be resolved in favor of
  coverage.  For a particular product received by a particular user,
  'normally used' refers to a typical or common use of that class of
  product, regardless of the status of the particular user or of the way
  in which the particular user actually uses, or expects or is expected
  to use, the product.  A product is a consumer product regardless of
  whether the product has substantial commercial, industrial or
  non-consumer uses, unless such uses represent the only significant
  mode of use of the product.

  'Installation Information' for a User Product means any methods,
  procedures, authorization keys, or other information required to
  install and execute modified versions of a covered work in that User
  Product from a modified version of its Corresponding Source.  The
  information must suffice to ensure that the continued functioning of
  the modified object code is in no case prevented or interfered with
  solely because modification has been made.

  If you convey an object code work under this section in, or with, or
  specifically for use in, a User Product, and the conveying occurs as
  part of a transaction in which the right of possession and use of the
  User Product is transferred to the recipient in perpetuity or for a
  fixed term (regardless of how the transaction is characterized), the
  Corresponding Source conveyed under this section must be accompanied
  by the Installation Information.  But this requirement does not apply
  if neither you nor any third party retains the ability to install
  modified object code on the User Product (for example, the work has
  been installed in ROM).

  The requirement to provide Installation Information does not include a
  requirement to continue to provide support service, warranty, or
  updates for a work that has been modified or installed by the
  recipient, or for the User Product in which it has been modified or
  installed.  Access to a network may be denied when the modification
  itself materially and adversely affects the operation of the network
  or violates the rules and protocols for communication across the
  network.

  Corresponding Source conveyed, and Installation Information provided,
  in accord with this section must be in a format that is publicly
  documented (and with an implementation available to the public in
  source code form), and must require no special password or key for
  unpacking, reading or copying.

* Additional Terms.

  'Additional permissions' are terms that supplement the terms of this
  License by making exceptions from one or more of its conditions.
  Additional permissions that are applicable to the entire Program shall
  be treated as though they were included in this License, to the extent
  that they are valid under applicable law.  If additional permissions
  apply only to part of the Program, that part may be used separately
  under those permissions, but the entire Program remains governed by
  this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
  remove any additional permissions from that copy, or from any part of
  it.  (Additional permissions may be written to require their own
  removal in certain cases when you modify the work.)  You may place
  additional permissions on material, added by you to a covered work,
  for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
  add to a covered work, you may (if authorized by the copyright holders
  of that material) supplement the terms of this License with terms:

  a* Disclaiming warranty or limiting liability differently from the terms
    of sections 15 and 16 of this License; or

  * Requiring preservation of specified reasonable legal notices or author
    attributions in that material or in the Appropriate Legal Notices
    displayed by works containing it; or

  * Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

  * Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

  * Declining to grant rights under trademark law for use of some trade
    names, trademarks, or service marks; or

  * Requiring indemnification of licensors and authors of that material by
    anyone who conveys the material (or modified versions of it) with
    contractual assumptions of liability to the recipient, for any
    liability that these contractual assumptions directly impose on those
    licensors and authors.

  All other non-permissive additional terms are considered 'further
  restrictions' within the meaning of section 10.  If the Program as you
  received it, or any part of it, contains a notice stating that it is
  governed by this License along with a term that is a further
  restriction, you may remove that term.  If a license document contains
  a further restriction but permits relicensing or conveying under this
  License, you may add to a covered work material governed by the terms
  of that license document, provided that the further restriction does
  not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
  must place, in the relevant source files, a statement of the
  additional terms that apply to those files, or a notice indicating
  where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
  form of a separately written license, or stated as exceptions; the
  above requirements apply either way.

* Termination.

  You may not propagate or modify a covered work except as expressly
  provided under this License.  Any attempt otherwise to propagate or
  modify it is void, and will automatically terminate your rights under
  this License (including any patent licenses granted under the third
  paragraph of section 11).

  However, if you cease all violation of this License, then your license
  from a particular copyright holder is reinstated (a) provisionally,
  unless and until the copyright holder explicitly and finally
  terminates your license, and (b) permanently, if the copyright holder
  fails to notify you of the violation by some reasonable means prior to
  60 days after the cessation.

  Moreover, your license from a particular copyright holder is
  reinstated permanently if the copyright holder notifies you of the
  violation by some reasonable means, this is the first time you have
  received notice of violation of this License (for any work) from that
  copyright holder, and you cure the violation prior to 30 days after
  your receipt of the notice.

  Termination of your rights under this section does not terminate the
  licenses of parties who have received copies or rights from you under
  this License.  If your rights have been terminated and not permanently
  reinstated, you do not qualify to receive new licenses for the same
  material under section 10.

* Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or run
  a copy of the Program.  Ancillary propagation of a covered work
  occurring solely as a consequence of using peer-to-peer transmission
  to receive a copy likewise does not require acceptance.  However,
  nothing other than this License grants you permission to propagate or
  modify any covered work.  These actions infringe copyright if you do
  not accept this License.  Therefore, by modifying or propagating a
  covered work, you indicate your acceptance of this License to do so.

* Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
  receives a license from the original licensors, to run, modify and
  propagate that work, subject to this License.  You are not responsible
  for enforcing compliance by third parties with this License.

  An 'entity transaction' is a transaction transferring control of an
  organization, or substantially all assets of one, or subdividing an
  organization, or merging organizations.  If propagation of a covered
  work results from an entity transaction, each party to that
  transaction who receives a copy of the work also receives whatever
  licenses to the work the party's predecessor in interest had or could
  give under the previous paragraph, plus a right to possession of the
  Corresponding Source of the work from the predecessor in interest, if
  the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
  rights granted or affirmed under this License.  For example, you may
  not impose a license fee, royalty, or other charge for exercise of
  rights granted under this License, and you may not initiate litigation
  (including a cross-claim or counterclaim in a lawsuit) alleging that
  any patent claim is infringed by making, using, selling, offering for
  sale, or importing the Program or any portion of it.

* Patents.

  A 'contributor' is a copyright holder who authorizes use under this
  License of the Program or a work on which the Program is based.  The
  work thus licensed is called the contributor's 'contributor version'.

  A contributor's 'essential patent claims' are all patent claims owned
  or controlled by the contributor, whether already acquired or
  hereafter acquired, that would be infringed by some manner, permitted
  by this License, of making, using, or selling its contributor version,
  but do not include claims that would be infringed only as a
  consequence of further modification of the contributor version.  For
  purposes of this definition, 'control' includes the right to grant
  patent sublicenses in a manner consistent with the requirements of
  this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
  patent license under the contributor's essential patent claims, to
  make, use, sell, offer for sale, import and otherwise run, modify and
  propagate the contents of its contributor version.

  In the following three paragraphs, a 'patent license' is any express
  agreement or commitment, however denominated, not to enforce a patent
  (such as an express permission to practice a patent or covenant not to
  sue for patent infringement).  To 'grant' such a patent license to a
  party means to make such an agreement or commitment not to enforce a
  patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
  and the Corresponding Source of the work is not available for anyone
  to copy, free of charge and under the terms of this License, through a
  publicly available network server or other readily accessible means,
  then you must either (1) cause the Corresponding Source to be so
  available, or (2) arrange to deprive yourself of the benefit of the
  patent license for this particular work, or (3) arrange, in a manner
  consistent with the requirements of this License, to extend the patent
  license to downstream recipients.  'Knowingly relying' means you have
  actual knowledge that, but for the patent license, your conveying the
  covered work in a country, or your recipient's use of the covered work
  in a country, would infringe one or more identifiable patents in that
  country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
  arrangement, you convey, or propagate by procuring conveyance of, a
  covered work, and grant a patent license to some of the parties
  receiving the covered work authorizing them to use, propagate, modify
  or convey a specific copy of the covered work, then the patent license
  you grant is automatically extended to all recipients of the covered
  work and works based on it.

  A patent license is 'discriminatory' if it does not include within the
  scope of its coverage, prohibits the exercise of, or is conditioned on
  the non-exercise of one or more of the rights that are specifically
  granted under this License.  You may not convey a covered work if you
  are a party to an arrangement with a third party that is in the
  business of distributing software, under which you make payment to the
  third party based on the extent of your activity of conveying the
  work, and under which the third party grants, to any of the parties
  who would receive the covered work from you, a discriminatory patent
  license (a) in connection with copies of the covered work conveyed by
  you (or copies made from those copies), or (b) primarily for and in
  connection with specific products or compilations that contain the
  covered work, unless you entered into that arrangement, or that patent
  license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
  any implied license or other defenses to infringement that may
  otherwise be available to you under applicable patent law.

* No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
  otherwise) that contradict the conditions of this License, they do not
  excuse you from the conditions of this License.  If you cannot convey
  a covered work so as to satisfy simultaneously your obligations under
  this License and any other pertinent obligations, then as a
  consequence you may not convey it at all.  For example, if you agree
  to terms that obligate you to collect a royalty for further conveying
  from those to whom you convey the Program, the only way you could
  satisfy both those terms and this License would be to refrain entirely
  from conveying the Program.

* Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
  permission to link or combine any covered work with a work licensed
  under version 3 of the GNU Affero General Public License into a single
  combined work, and to convey the resulting work.  The terms of this
  License will continue to apply to the part which is the covered work,
  but the special requirements of the GNU Affero General Public License,
  section 13, concerning interaction through a network will apply to the
  combination as such.

* Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions
  of the GNU General Public License from time to time.  Such new
  versions will be similar in spirit to the present version, but may
  differ in detail to address new problems or concerns.

  Each version is given a distinguishing version number.  If the Program
  specifies that a certain numbered version of the GNU General Public
  License 'or any later version' applies to it, you have the option of
  following the terms and conditions either of that numbered version or
  of any later version published by the Free Software Foundation.  If
  the Program does not specify a version number of the GNU General
  Public License, you may choose any version ever published by the Free
  Software Foundation.

  If the Program specifies that a proxy can decide which future versions
  of the GNU General Public License can be used, that proxy's public
  statement of acceptance of a version permanently authorizes you to
  choose that version for the Program.

  Later license versions may give you additional or different
  permissions.  However, no additional obligations are imposed on any
  author or copyright holder as a result of your choosing to follow a
  later version.

* Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
  APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
  HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM 'AS IS' WITHOUT
  WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT
  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
  A PARTICULAR PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND
  PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE PROGRAM PROVE
  DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR
  CORRECTION.

* Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
  WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR
  CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
  INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES
  ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT
  NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR
  LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM
  TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER
  PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

* Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
  above cannot be given local legal effect according to their terms,
  reviewing courts shall apply local law that most closely approximates
  an absolute waiver of all civil liability in connection with the
  Program, unless a warranty or assumption of liability accompanies a
  copy of the Program in return for a fee.

END OF TERMS AND CONDITIONSHow to Apply These Terms to Your New ProgramsIf you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these
terms.

To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the 'copyright' line and a pointer to where the full notice is found.

.. code-block:: c++

  ``one line to give the program's name and a brief idea of what it does.``  
  Copyright (C) ``year`` ``name of author``

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or (at
  your option) any later version.

  This program is distributed in the hope that it will be useful, but
  WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see http://www.gnu.org/licenses/.

Also add information on how to contact you by electronic and paper mail.

If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

.. code-block:: c++

  ``program`` Copyright (C) ``year`` ``name of author`` 
  This program comes with ABSOLUTELY NO WARRANTY; for details type :samp:`show w`.
  This is free software, and you are welcome to redistribute it
  under certain conditions; type :samp:`show c` for details.

The hypothetical commands :samp:`show w` and :samp:`show c` should show
the appropriate parts of the General Public License.  Of course, your
program's commands might be different; for a GUI interface, you would
use an 'about box'.

You should also get your employer (if you work as a programmer) or school,
if any, to sign a 'copyright disclaimer' for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
http://www.gnu.org/licenses/.

The GNU General Public License does not permit incorporating your
program into proprietary programs.  If your program is a subroutine
library, you may consider it more useful to permit linking proprietary
applications with the library.  If this is what you want to do, use
the GNU Lesser General Public License instead of this License.  But
first, please read http://www.gnu.org/philosophy/why-not-lgpl.html.

.. man end

.. -
   GFDL
   -

@c Set file name and title for man page.
@setfilename gfdl
@settitle GNU Free Documentation License
@c man begin SEEALSO
gpl(7), fsf-funding(7).
@c man end
@c man begin COPYRIGHT
Copyright @copyright{} 2000, 2001, 2002, 2007, 2008 Free Software Foundation, Inc.
@uref{http://fsf.org/}

Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.
@c This file is intended to be included within another document,
@c hence no sectioning command or @node.
@c man end

.. Special handling for inclusion in the install manual.
   man begin DESCRIPTION

.. _gnu-free-documentation-license:

GNU Free Documentation License
==============================

.. index:: FDL, GNU Free Documentation License

Version 1.3, 3 November 2008Copyright (C) 2000, 2001, 2002, 2007, 2008 Free Software Foundation, Inc.
http://fsf.org/

Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.
0* PREAMBLE

  The purpose of this License is to make a manual, textbook, or other
  functional and useful document :dfn:`free` in the sense of freedom: to
  assure everyone the effective freedom to copy and redistribute it,
  with or without modifying it, either commercially or noncommercially.
  Secondarily, this License preserves for the author and publisher a way
  to get credit for their work, while not being considered responsible
  for modifications made by others.

  This License is a kind of 'copyleft', which means that derivative
  works of the document must themselves be free in the same sense.  It
  complements the GNU General Public License, which is a copyleft
  license designed for free software.

  We have designed this License in order to use it for manuals for free
  software, because free software needs free documentation: a free
  program should come with manuals providing the same freedoms that the
  software does.  But this License is not limited to software manuals;
  it can be used for any textual work, regardless of subject matter or
  whether it is published as a printed book.  We recommend this License
  principally for works whose purpose is instruction or reference.

* APPLICABILITY AND DEFINITIONS

  This License applies to any manual or other work, in any medium, that
  contains a notice placed by the copyright holder saying it can be
  distributed under the terms of this License.  Such a notice grants a
  world-wide, royalty-free license, unlimited in duration, to use that
  work under the conditions stated herein.  The 'Document', below,
  refers to any such manual or work.  Any member of the public is a
  licensee, and is addressed as 'you'.  You accept the license if you
  copy, modify or distribute the work in a way requiring permission
  under copyright law.

  A 'Modified Version' of the Document means any work containing the
  Document or a portion of it, either copied verbatim, or with
  modifications and/or translated into another language.

  A 'Secondary Section' is a named appendix or a front-matter section
  of the Document that deals exclusively with the relationship of the
  publishers or authors of the Document to the Document's overall
  subject (or to related matters) and contains nothing that could fall
  directly within that overall subject.  (Thus, if the Document is in
  part a textbook of mathematics, a Secondary Section may not explain
  any mathematics.)  The relationship could be a matter of historical
  connection with the subject or with related matters, or of legal,
  commercial, philosophical, ethical or political position regarding
  them.

  The 'Invariant Sections' are certain Secondary Sections whose titles
  are designated, as being those of Invariant Sections, in the notice
  that says that the Document is released under this License.  If a
  section does not fit the above definition of Secondary then it is not
  allowed to be designated as Invariant.  The Document may contain zero
  Invariant Sections.  If the Document does not identify any Invariant
  Sections then there are none.

  The 'Cover Texts' are certain short passages of text that are listed,
  as Front-Cover Texts or Back-Cover Texts, in the notice that says that
  the Document is released under this License.  A Front-Cover Text may
  be at most 5 words, and a Back-Cover Text may be at most 25 words.

  A 'Transparent' copy of the Document means a machine-readable copy,
  represented in a format whose specification is available to the
  general public, that is suitable for revising the document
  straightforwardly with generic text editors or (for images composed of
  pixels) generic paint programs or (for drawings) some widely available
  drawing editor, and that is suitable for input to text formatters or
  for automatic translation to a variety of formats suitable for input
  to text formatters.  A copy made in an otherwise Transparent file
  format whose markup, or absence of markup, has been arranged to thwart
  or discourage subsequent modification by readers is not Transparent.
  An image format is not Transparent if used for any substantial amount
  of text.  A copy that is not 'Transparent' is called 'Opaque'.

  Examples of suitable formats for Transparent copies include plain
  ascii without markup, Texinfo input format, LaTex input
  format, SGML or XML using a publicly available
  DTD, and standard-conforming simple HTML,
  PostScript or PDF designed for human modification.  Examples
  of transparent image formats include PNG, XCF and
  JPG.  Opaque formats include proprietary formats that can be
  read and edited only by proprietary word processors, SGML or
  XML for which the DTD and/or processing tools are
  not generally available, and the machine-generated HTML,
  PostScript or PDF produced by some word processors for
  output purposes only.

  The 'Title Page' means, for a printed book, the title page itself,
  plus such following pages as are needed to hold, legibly, the material
  this License requires to appear in the title page.  For works in
  formats which do not have any title page as such, 'Title Page' means
  the text near the most prominent appearance of the work's title,
  preceding the beginning of the body of the text.

  The 'publisher' means any person or entity that distributes copies
  of the Document to the public.

  A section 'Entitled XYZ' means a named subunit of the Document whose
  title either is precisely XYZ or contains XYZ in parentheses following
  text that translates XYZ in another language.  (Here XYZ stands for a
  specific section name mentioned below, such as 'Acknowledgements',
  'Dedications', 'Endorsements', or 'History'.)  To 'Preserve the Title'
  of such a section when you modify the Document means that it remains a
  section 'Entitled XYZ' according to this definition.

  The Document may include Warranty Disclaimers next to the notice which
  states that this License applies to the Document.  These Warranty
  Disclaimers are considered to be included by reference in this
  License, but only as regards disclaiming warranties: any other
  implication that these Warranty Disclaimers may have is void and has
  no effect on the meaning of this License.

* VERBATIM COPYING

  You may copy and distribute the Document in any medium, either
  commercially or noncommercially, provided that this License, the
  copyright notices, and the license notice saying this License applies
  to the Document are reproduced in all copies, and that you add no other
  conditions whatsoever to those of this License.  You may not use
  technical measures to obstruct or control the reading or further
  copying of the copies you make or distribute.  However, you may accept
  compensation in exchange for copies.  If you distribute a large enough
  number of copies you must also follow the conditions in section 3.

  You may also lend copies, under the same conditions stated above, and
  you may publicly display copies.

* COPYING IN QUANTITY

  If you publish printed copies (or copies in media that commonly have
  printed covers) of the Document, numbering more than 100, and the
  Document's license notice requires Cover Texts, you must enclose the
  copies in covers that carry, clearly and legibly, all these Cover
  Texts: Front-Cover Texts on the front cover, and Back-Cover Texts on
  the back cover.  Both covers must also clearly and legibly identify
  you as the publisher of these copies.  The front cover must present
  the full title with all words of the title equally prominent and
  visible.  You may add other material on the covers in addition.
  Copying with changes limited to the covers, as long as they preserve
  the title of the Document and satisfy these conditions, can be treated
  as verbatim copying in other respects.

  If the required texts for either cover are too voluminous to fit
  legibly, you should put the first ones listed (as many as fit
  reasonably) on the actual cover, and continue the rest onto adjacent
  pages.

  If you publish or distribute Opaque copies of the Document numbering
  more than 100, you must either include a machine-readable Transparent
  copy along with each Opaque copy, or state in or with each Opaque copy
  a computer-network location from which the general network-using
  public has access to download using public-standard network protocols
  a complete Transparent copy of the Document, free of added material.
  If you use the latter option, you must take reasonably prudent steps,
  when you begin distribution of Opaque copies in quantity, to ensure
  that this Transparent copy will remain thus accessible at the stated
  location until at least one year after the last time you distribute an
  Opaque copy (directly or through your agents or retailers) of that
  edition to the public.

  It is requested, but not required, that you contact the authors of the
  Document well before redistributing any large number of copies, to give
  them a chance to provide you with an updated version of the Document.

* MODIFICATIONS

  You may copy and distribute a Modified Version of the Document under
  the conditions of sections 2 and 3 above, provided that you release
  the Modified Version under precisely this License, with the Modified
  Version filling the role of the Document, thus licensing distribution
  and modification of the Modified Version to whoever possesses a copy
  of it.  In addition, you must do these things in the Modified Version:

  A* Use in the Title Page (and on the covers, if any) a title distinct
    from that of the Document, and from those of previous versions
    (which should, if there were any, be listed in the History section
    of the Document).  You may use the same title as a previous version
    if the original publisher of that version gives permission.

  * List on the Title Page, as authors, one or more persons or entities
    responsible for authorship of the modifications in the Modified
    Version, together with at least five of the principal authors of the
    Document (all of its principal authors, if it has fewer than five),
    unless they release you from this requirement.

  * State on the Title page the name of the publisher of the
    Modified Version, as the publisher.

  * Preserve all the copyright notices of the Document.

  * Add an appropriate copyright notice for your modifications
    adjacent to the other copyright notices.

  * Include, immediately after the copyright notices, a license notice
    giving the public permission to use the Modified Version under the
    terms of this License, in the form shown in the Addendum below.

  * Preserve in that license notice the full lists of Invariant Sections
    and required Cover Texts given in the Document's license notice.

  * Include an unaltered copy of this License.

  * Preserve the section Entitled 'History', Preserve its Title, and add
    to it an item stating at least the title, year, new authors, and
    publisher of the Modified Version as given on the Title Page.  If
    there is no section Entitled 'History' in the Document, create one
    stating the title, year, authors, and publisher of the Document as
    given on its Title Page, then add an item describing the Modified
    Version as stated in the previous sentence.

  * Preserve the network location, if any, given in the Document for
    public access to a Transparent copy of the Document, and likewise
    the network locations given in the Document for previous versions
    it was based on.  These may be placed in the 'History' section.
    You may omit a network location for a work that was published at
    least four years before the Document itself, or if the original
    publisher of the version it refers to gives permission.

  * For any section Entitled 'Acknowledgements' or 'Dedications', Preserve
    the Title of the section, and preserve in the section all the
    substance and tone of each of the contributor acknowledgements and/or
    dedications given therein.

  * Preserve all the Invariant Sections of the Document,
    unaltered in their text and in their titles.  Section numbers
    or the equivalent are not considered part of the section titles.

  * Delete any section Entitled 'Endorsements'.  Such a section
    may not be included in the Modified Version.

  * Do not retitle any existing section to be Entitled 'Endorsements' or
    to conflict in title with any Invariant Section.

  * Preserve any Warranty Disclaimers.

  If the Modified Version includes new front-matter sections or
  appendices that qualify as Secondary Sections and contain no material
  copied from the Document, you may at your option designate some or all
  of these sections as invariant.  To do this, add their titles to the
  list of Invariant Sections in the Modified Version's license notice.
  These titles must be distinct from any other section titles.

  You may add a section Entitled 'Endorsements', provided it contains
  nothing but endorsements of your Modified Version by various
  parties-for example, statements of peer review or that the text has
  been approved by an organization as the authoritative definition of a
  standard.

  You may add a passage of up to five words as a Front-Cover Text, and a
  passage of up to 25 words as a Back-Cover Text, to the end of the list
  of Cover Texts in the Modified Version.  Only one passage of
  Front-Cover Text and one of Back-Cover Text may be added by (or
  through arrangements made by) any one entity.  If the Document already
  includes a cover text for the same cover, previously added by you or
  by arrangement made by the same entity you are acting on behalf of,
  you may not add another; but you may replace the old one, on explicit
  permission from the previous publisher that added the old one.

  The author(s) and publisher(s) of the Document do not by this License
  give permission to use their names for publicity for or to assert or
  imply endorsement of any Modified Version.

* COMBINING DOCUMENTS

  You may combine the Document with other documents released under this
  License, under the terms defined in section 4 above for modified
  versions, provided that you include in the combination all of the
  Invariant Sections of all of the original documents, unmodified, and
  list them all as Invariant Sections of your combined work in its
  license notice, and that you preserve all their Warranty Disclaimers.

  The combined work need only contain one copy of this License, and
  multiple identical Invariant Sections may be replaced with a single
  copy.  If there are multiple Invariant Sections with the same name but
  different contents, make the title of each such section unique by
  adding at the end of it, in parentheses, the name of the original
  author or publisher of that section if known, or else a unique number.
  Make the same adjustment to the section titles in the list of
  Invariant Sections in the license notice of the combined work.

  In the combination, you must combine any sections Entitled 'History'
  in the various original documents, forming one section Entitled
  'History'; likewise combine any sections Entitled 'Acknowledgements',
  and any sections Entitled 'Dedications'.  You must delete all
  sections Entitled 'Endorsements.'

* COLLECTIONS OF DOCUMENTS

  You may make a collection consisting of the Document and other documents
  released under this License, and replace the individual copies of this
  License in the various documents with a single copy that is included in
  the collection, provided that you follow the rules of this License for
  verbatim copying of each of the documents in all other respects.

  You may extract a single document from such a collection, and distribute
  it individually under this License, provided you insert a copy of this
  License into the extracted document, and follow this License in all
  other respects regarding verbatim copying of that document.

* AGGREGATION WITH INDEPENDENT WORKS

  A compilation of the Document or its derivatives with other separate
  and independent documents or works, in or on a volume of a storage or
  distribution medium, is called an 'aggregate' if the copyright
  resulting from the compilation is not used to limit the legal rights
  of the compilation's users beyond what the individual works permit.
  When the Document is included in an aggregate, this License does not
  apply to the other works in the aggregate which are not themselves
  derivative works of the Document.

  If the Cover Text requirement of section 3 is applicable to these
  copies of the Document, then if the Document is less than one half of
  the entire aggregate, the Document's Cover Texts may be placed on
  covers that bracket the Document within the aggregate, or the
  electronic equivalent of covers if the Document is in electronic form.
  Otherwise they must appear on printed covers that bracket the whole
  aggregate.

* TRANSLATION

  Translation is considered a kind of modification, so you may
  distribute translations of the Document under the terms of section 4.
  Replacing Invariant Sections with translations requires special
  permission from their copyright holders, but you may include
  translations of some or all Invariant Sections in addition to the
  original versions of these Invariant Sections.  You may include a
  translation of this License, and all the license notices in the
  Document, and any Warranty Disclaimers, provided that you also include
  the original English version of this License and the original versions
  of those notices and disclaimers.  In case of a disagreement between
  the translation and the original version of this License or a notice
  or disclaimer, the original version will prevail.

  If a section in the Document is Entitled 'Acknowledgements',
  'Dedications', or 'History', the requirement (section 4) to Preserve
  its Title (section 1) will typically require changing the actual
  title.

* TERMINATION

  You may not copy, modify, sublicense, or distribute the Document
  except as expressly provided under this License.  Any attempt
  otherwise to copy, modify, sublicense, or distribute it is void, and
  will automatically terminate your rights under this License.

  However, if you cease all violation of this License, then your license
  from a particular copyright holder is reinstated (a) provisionally,
  unless and until the copyright holder explicitly and finally
  terminates your license, and (b) permanently, if the copyright holder
  fails to notify you of the violation by some reasonable means prior to
  60 days after the cessation.

  Moreover, your license from a particular copyright holder is
  reinstated permanently if the copyright holder notifies you of the
  violation by some reasonable means, this is the first time you have
  received notice of violation of this License (for any work) from that
  copyright holder, and you cure the violation prior to 30 days after
  your receipt of the notice.

  Termination of your rights under this section does not terminate the
  licenses of parties who have received copies or rights from you under
  this License.  If your rights have been terminated and not permanently
  reinstated, receipt of a copy of some or all of the same material does
  not give you any rights to use it.

* FUTURE REVISIONS OF THIS LICENSE

  The Free Software Foundation may publish new, revised versions
  of the GNU Free Documentation License from time to time.  Such new
  versions will be similar in spirit to the present version, but may
  differ in detail to address new problems or concerns.  See
  http://www.gnu.org/copyleft/.

  Each version of the License is given a distinguishing version number.
  If the Document specifies that a particular numbered version of this
  License 'or any later version' applies to it, you have the option of
  following the terms and conditions either of that specified version or
  of any later version that has been published (not as a draft) by the
  Free Software Foundation.  If the Document does not specify a version
  number of this License, you may choose any version ever published (not
  as a draft) by the Free Software Foundation.  If the Document
  specifies that a proxy can decide which future versions of this
  License can be used, that proxy's public statement of acceptance of a
  version permanently authorizes you to choose that version for the
  Document.

* RELICENSING

  'Massive Multiauthor Collaboration Site' (or 'MMC Site') means any
  World Wide Web server that publishes copyrightable works and also
  provides prominent facilities for anybody to edit those works.  A
  public wiki that anybody can edit is an example of such a server.  A
  'Massive Multiauthor Collaboration' (or 'MMC') contained in the
  site means any set of copyrightable works thus published on the MMC
  site.

  'CC-BY-SA' means the Creative Commons Attribution-Share Alike 3.0
  license published by Creative Commons Corporation, a not-for-profit
  corporation with a principal place of business in San Francisco,
  California, as well as future copyleft versions of that license
  published by that same organization.

  'Incorporate' means to publish or republish a Document, in whole or
  in part, as part of another Document.

  An MMC is 'eligible for relicensing' if it is licensed under this
  License, and if all works that were first published under this License
  somewhere other than this MMC, and subsequently incorporated in whole
  or in part into the MMC, (1) had no cover texts or invariant sections,
  and (2) were thus incorporated prior to November 1, 2008.

  The operator of an MMC Site may republish an MMC contained in the site
  under CC-BY-SA on the same site at any time before August 1, 2009,
  provided the MMC is eligible for relicensing.

ADDENDUM: How to use this License for your documents
====================================================

To use this License in a document you have written, include a copy of
the License in the document and put the following copyright and
license notices just after the title page:

.. code-block:: c++

    Copyright (C)  ``year``  ``your name``.
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3
    or any later version published by the Free Software Foundation;
    with no Invariant Sections, no Front-Cover Texts, and no Back-Cover
    Texts.  A copy of the license is included in the section entitled ``GNU
    Free Documentation License''.

If you have Invariant Sections, Front-Cover Texts and Back-Cover Texts,
replace the 'with...Texts.' line with this:

.. code-block:: c++

      with the Invariant Sections being ``list their titles``, with
      the Front-Cover Texts being ``list``, and with the Back-Cover Texts
      being ``list``.

If you have Invariant Sections without Cover Texts, or some other
combination of the three, merge those two alternatives to suit the
situation.

If your document contains nontrivial examples of program code, we
recommend releasing these examples in parallel under your choice of
free software license, such as the GNU General Public License,
to permit their use in free software.

.. Local Variables:
   ispell-local-pdict: "ispell-dict"
   End:
   man end
   Copyright (C) 1988-2015 Free Software Foundation, Inc.
   This is part of the GCC manual.
   For copying conditions, see the file gcc.texi.

.. _contributors:

Contributors to GCC
===================

.. index:: contributors

The GCC project would like to thank its many contributors.  Without them the
project would not have been nearly as successful as it has been.  Any omissions
in this list are accidental.  Feel free to contact
law@redhat.com or gerald@pfeifer.com if you have been left
out or some of your contributions are not listed.  Please keep this list in
alphabetical order.

* Analog Devices helped implement the support for complex data types
  and iterators.

* John David Anglin for threading-related fixes and improvements to
  libstdc++-v3, and the HP-UX port.

* James van Artsdalen wrote the code that makes efficient use of
  the Intel 80387 register stack.

* Abramo and Roberto Bagnara for the SysV68 Motorola 3300 Delta Series
  port.

* Alasdair Baird for various bug fixes.

* Giovanni Bajo for analyzing lots of complicated C++ problem reports.

* Peter Barada for his work to improve code generation for new
  ColdFire cores.

* Gerald Baumgartner added the signature extension to the C++ front end.

* Godmar Back for his Java improvements and encouragement.

* Scott Bambrough for help porting the Java compiler.

* Wolfgang Bangerth for processing tons of bug reports.

* Jon Beniston for his Microsoft Windows port of Java and port to Lattice Mico32.

* Daniel Berlin for better DWARF2 support, faster/better optimizations,
  improved alias analysis, plus migrating GCC to Bugzilla.

* Geoff Berry for his Java object serialization work and various patches.

* David Binderman tests weekly snapshots of GCC trunk against Fedora Rawhide
  for several architectures.

* Laurynas Biveinis for memory management work and DJGPP port fixes.

* Uros Bizjak for the implementation of x87 math built-in functions and
  for various middle end and i386 back end improvements and bug fixes.

* Eric Blake for helping to make GCJ and libgcj conform to the
  specifications.

* Janne Blomqvist for contributions to GNU Fortran.

* Segher Boessenkool for various fixes.

* Hans-J. Boehm for his http://www.hpl.hp.com//personal//Hans_Boehm//gc/garbage collector, IA-64 libffi port, and other Java work.

* Neil Booth for work on cpplib, lang hooks, debug hooks and other
  miscellaneous clean-ups.

* Steven Bosscher for integrating the GNU Fortran front end into GCC and for
  contributing to the tree-ssa branch.

* Eric Botcazou for fixing middle- and backend bugs left and right.

* Per Bothner for his direction via the steering committee and various
  improvements to the infrastructure for supporting new languages.  Chill
  front end implementation.  Initial implementations of
  cpplib, fix-header, config.guess, libio, and past C++ library (libg++)
  maintainer.  Dreaming up, designing and implementing much of GCJ.

* Devon Bowen helped port GCC to the Tahoe.

* Don Bowman for mips-vxworks contributions.

* Dave Brolley for work on cpplib and Chill.

* Paul Brook for work on the ARM architecture and maintaining GNU Fortran.

* Robert Brown implemented the support for Encore 32000 systems.

* Christian Bruel for improvements to local store elimination.

* Herman A.J. ten Brugge for various fixes.

* Joerg Brunsmann for Java compiler hacking and help with the GCJ FAQ.

* Joe Buck for his direction via the steering committee from its creation
  to 2013.

* Craig Burley for leadership of the G77 Fortran effort.

* Stephan Buys for contributing Doxygen notes for libstdc++.

* Paolo Carlini for libstdc++ work: lots of efficiency improvements to
  the C++ strings, streambufs and formatted I/O, hard detective work on
  the frustrating localization issues, and keeping up with the problem reports.

* John Carr for his alias work, SPARC hacking, infrastructure improvements,
  previous contributions to the steering committee, loop optimizations, etc.

* Stephane Carrez for 68HC11 and 68HC12 ports.

* Steve Chamberlain for support for the Renesas SH and H8 processors
  and the PicoJava processor, and for GCJ config fixes.

* Glenn Chambers for help with the GCJ FAQ.

* John-Marc Chandonia for various libgcj patches.

* Denis Chertykov for contributing and maintaining the AVR port, the first GCC port
  for an 8-bit architecture.

* Scott Christley for his Objective-C contributions.

* Eric Christopher for his Java porting help and clean-ups.

* Branko Cibej for more warning contributions.

* The http://www.gnu.org/software/classpath/GNU Classpath project
  for all of their merged runtime code.

* Nick Clifton for arm, mcore, fr30, v850, m32r, msp430 rx work,
  :option:`--help`, and other random hacking.

* Michael Cook for libstdc++ cleanup patches to reduce warnings.

* R. Kelley Cook for making GCC buildable from a read-only directory as
  well as other miscellaneous build process and documentation clean-ups.

* Ralf Corsepius for SH testing and minor bug fixing.

* Stan Cox for care and feeding of the x86 port and lots of behind
  the scenes hacking.

* Alex Crain provided changes for the 3b1.

* Ian Dall for major improvements to the NS32k port.

* Paul Dale for his work to add uClinux platform support to the
  m68k backend.

* Dario Dariol contributed the four varieties of sample programs
  that print a copy of their source.

* Russell Davidson for fstream and stringstream fixes in libstdc++.

* Bud Davis for work on the G77 and GNU Fortran compilers.

* Mo DeJong for GCJ and libgcj bug fixes.

* DJ Delorie for the DJGPP port, build and libiberty maintenance,
  various bug fixes, and the M32C, MeP, MSP430, and RL78 ports.

* Arnaud Desitter for helping to debug GNU Fortran.

* Gabriel Dos Reis for contributions to G++, contributions and
  maintenance of GCC diagnostics infrastructure, libstdc++-v3,
  including ``valarray<>``, ``complex<>``, maintaining the numerics library
  (including that pesky ``<limits>`` :-) and keeping up-to-date anything
  to do with numbers.

* Ulrich Drepper for his work on glibc, testing of GCC using glibc, ISO C99
  support, CFG dumping support, etc., plus support of the C++ runtime
  libraries including for all kinds of C interface issues, contributing and
  maintaining ``complex<>``, sanity checking and disbursement, configuration
  architecture, libio maintenance, and early math work.

* Francois Dumont for his work on libstdc++-v3, especially maintaining and
  improving ``debug-mode`` and associative and unordered containers.

* Zdenek Dvorak for a new loop unroller and various fixes.

* Michael Eager for his work on the Xilinx MicroBlaze port.

* Richard Earnshaw for his ongoing work with the ARM.

* David Edelsohn for his direction via the steering committee, ongoing work
  with the RS6000/PowerPC port, help cleaning up Haifa loop changes,
  doing the entire AIX port of libstdc++ with his bare hands, and for
  ensuring GCC properly keeps working on AIX.

* Kevin Ediger for the floating point formatting of num_put::do_put in
  libstdc++.

* Phil Edwards for libstdc++ work including configuration hackery,
  documentation maintainer, chief breaker of the web pages, the occasional
  iostream bug fix, and work on shared library symbol versioning.

* Paul Eggert for random hacking all over GCC.

* Mark Elbrecht for various DJGPP improvements, and for libstdc++
  configuration support for locales and fstream-related fixes.

* Vadim Egorov for libstdc++ fixes in strings, streambufs, and iostreams.

* Christian Ehrhardt for dealing with bug reports.

* Ben Elliston for his work to move the Objective-C runtime into its
  own subdirectory and for his work on autoconf.

* Revital Eres for work on the PowerPC 750CL port.

* Marc Espie for OpenBSD support.

* Doug Evans for much of the global optimization framework, arc, m32r,
  and SPARC work.

* Christopher Faylor for his work on the Cygwin port and for caring and
  feeding the gcc.gnu.org box and saving its users tons of spam.

* Fred Fish for BeOS support and Ada fixes.

* Ivan Fontes Garcia for the Portuguese translation of the GCJ FAQ.

* Peter Gerwinski for various bug fixes and the Pascal front end.

* Kaveh R. Ghazi for his direction via the steering committee, amazing
  work to make :samp:`-W -Wall -W* -Werror` useful, and 
  testing GCC on a plethora of platforms.  Kaveh extends his gratitude to
  the CAIP Center at Rutgers University for providing him with computing
  resources to work on Free Software from the late 1980s to 2010.

* John Gilmore for a donation to the FSF earmarked improving GNU Java.

* Judy Goldberg for c++ contributions.

* Torbjorn Granlund for various fixes and the c-torture testsuite,
  multiply- and divide-by-constant optimization, improved long long
  support, improved leaf function register allocation, and his direction
  via the steering committee.

* Jonny Grant for improvements to ``collect2's`` :option:`--help` documentation.

* Anthony Green for his :option:`-Os` contributions, the moxie port, and
  Java front end work.

* Stu Grossman for gdb hacking, allowing GCJ developers to debug Java code.

* Michael K. Gschwind contributed the port to the PDP-11.

* Richard Biener for his ongoing middle-end contributions and bug fixes
  and for release management.

* Ron Guilmette implemented the :command:`protoize` and :command:`unprotoize`
  tools, the support for Dwarf symbolic debugging information, and much of
  the support for System V Release 4.  He has also worked heavily on the
  Intel 386 and 860 support.

* Sumanth Gundapaneni for contributing the CR16 port.

* Mostafa Hagog for Swing Modulo Scheduling (SMS) and post reload GCSE.

* Bruno Haible for improvements in the runtime overhead for EH, new
  warnings and assorted bug fixes.

* Andrew Haley for his amazing Java compiler and library efforts.

* Chris Hanson assisted in making GCC work on HP-UX for the 9000 series 300.

* Michael Hayes for various thankless work he's done trying to get
  the c30/c40 ports functional.  Lots of loop and unroll improvements and
  fixes.

* Dara Hazeghi for wading through myriads of target-specific bug reports.

* Kate Hedstrom for staking the G77 folks with an initial testsuite.

* Richard Henderson for his ongoing SPARC, alpha, ia32, and ia64 work, loop
  opts, and generally fixing lots of old problems we've ignored for
  years, flow rewrite and lots of further stuff, including reviewing
  tons of patches.

* Aldy Hernandez for working on the PowerPC port, SIMD support, and
  various fixes.

* Nobuyuki Hikichi of Software Research Associates, Tokyo, contributed
  the support for the Sony NEWS machine.

* Kazu Hirata for caring and feeding the Renesas H8/300 port and various fixes.

* Katherine Holcomb for work on GNU Fortran.

* Manfred Hollstein for his ongoing work to keep the m88k alive, lots
  of testing and bug fixing, particularly of GCC configury code.

* Steve Holmgren for MachTen patches.

* Mat Hostetter for work on the TILE-Gx and TILEPro ports.

* Jan Hubicka for his x86 port improvements.

* Falk Hueffner for working on C and optimization bug reports.

* Bernardo Innocenti for his m68k work, including merging of
  ColdFire improvements and uClinux support.

* Christian Iseli for various bug fixes.

* Kamil Iskra for general m68k hacking.

* Lee Iverson for random fixes and MIPS testing.

* Balaji V. Iyer for Cilk+ development and merging.

* Andreas Jaeger for testing and benchmarking of GCC and various bug fixes.

* Martin Jambor for his work on inter-procedural optimizations, the
  switch conversion pass, and scalar replacement of aggregates.

* Jakub Jelinek for his SPARC work and sibling call optimizations as well
  as lots of bug fixes and test cases, and for improving the Java build
  system.

* Janis Johnson for ia64 testing and fixes, her quality improvement
  sidetracks, and web page maintenance.

* Kean Johnston for SCO OpenServer support and various fixes.

* Tim Josling for the sample language treelang based originally on Richard
  Kenner's 'toy' language.

* Nicolai Josuttis for additional libstdc++ documentation.

* Klaus Kaempf for his ongoing work to make alpha-vms a viable target.

* Steven G. Kargl for work on GNU Fortran.

* David Kashtan of SRI adapted GCC to VMS.

* Ryszard Kabatek for many, many libstdc++ bug fixes and optimizations of
  strings, especially member functions, and for auto_ptr fixes.

* Geoffrey Keating for his ongoing work to make the PPC work for GNU/Linux
  and his automatic regression tester.

* Brendan Kehoe for his ongoing work with G++ and for a lot of early work
  in just about every part of libstdc++.

* Oliver M. Kellogg of Deutsche Aerospace contributed the port to the
  MIL-STD-1750A.

* Richard Kenner of the New York University Ultracomputer Research
  Laboratory wrote the machine descriptions for the AMD 29000, the DEC
  Alpha, the IBM RT PC, and the IBM RS/6000 as well as the support for
  instruction attributes.  He also made changes to better support RISC
  processors including changes to common subexpression elimination,
  strength reduction, function calling sequence handling, and condition
  code support, in addition to generalizing the code for frame pointer
  elimination and delay slot scheduling.  Richard Kenner was also the
  head maintainer of GCC for several years.

* Mumit Khan for various contributions to the Cygwin and Mingw32 ports and
  maintaining binary releases for Microsoft Windows hosts, and for massive libstdc++
  porting work to Cygwin/Mingw32.

* Robin Kirkham for cpu32 support.

* Mark Klein for PA improvements.

* Thomas Koenig for various bug fixes.

* Bruce Korb for the new and improved fixincludes code.

* Benjamin Kosnik for his G++ work and for leading the libstdc++-v3 effort.

* Maxim Kuvyrkov for contributions to the instruction scheduler, the Android 
  and m68k/Coldfire ports, and optimizations.

* Charles LaBrec contributed the support for the Integrated Solutions
  68020 system.

* Asher Langton and Mike Kumbera for contributing Cray pointer support
  to GNU Fortran, and for other GNU Fortran improvements.

* Jeff Law for his direction via the steering committee, coordinating the
  entire egcs project and GCC 2.95, rolling out snapshots and releases,
  handling merges from GCC2, reviewing tons of patches that might have
  fallen through the cracks else, and random but extensive hacking.

* Walter Lee for work on the TILE-Gx and TILEPro ports.

* Marc Lehmann for his direction via the steering committee and helping
  with analysis and improvements of x86 performance.

* Victor Leikehman for work on GNU Fortran.

* Ted Lemon wrote parts of the RTL reader and printer.

* Kriang Lerdsuwanakij for C++ improvements including template as template
  parameter support, and many C++ fixes.

* Warren Levy for tremendous work on libgcj (Java Runtime Library) and
  random work on the Java front end.

* Alain Lichnewsky ported GCC to the MIPS CPU.

* Oskar Liljeblad for hacking on AWT and his many Java bug reports and
  patches.

* Robert Lipe for OpenServer support, new testsuites, testing, etc.

* Chen Liqin for various S+core related fixes/improvement, and for
  maintaining the S+core port.

* Weiwen Liu for testing and various bug fixes.

* Manuel Lopez-Ibanez for improving :option:`-Wconversion` and
  many other diagnostics fixes and improvements.

* Dave Love for his ongoing work with the Fortran front end and
  runtime libraries.

* Martin von Lowis for internal consistency checking infrastructure,
  various C++ improvements including namespace support, and tons of
  assistance with libstdc++/compiler merges.

* H.J. Lu for his previous contributions to the steering committee, many x86
  bug reports, prototype patches, and keeping the GNU/Linux ports working.

* Greg McGary for random fixes and (someday) bounded pointers.

* Andrew MacLeod for his ongoing work in building a real EH system,
  various code generation improvements, work on the global optimizer, etc.

* Vladimir Makarov for hacking some ugly i960 problems, PowerPC hacking
  improvements to compile-time performance, overall knowledge and
  direction in the area of instruction scheduling, and design and
  implementation of the automaton based instruction scheduler.

* Bob Manson for his behind the scenes work on dejagnu.

* John Marino for contributing the DragonFly BSD port.

* Philip Martin for lots of libstdc++ string and vector iterator fixes and
  improvements, and string clean up and testsuites.

* Michael Matz for his work on dominance tree discovery, the x86-64 port,
  link-time optimization framework and general optimization improvements.

* All of the Mauve project
  http://sourceware.org/cgi-bin/cvsweb.cgi/~checkout~/mauve/THANKS?rev=1.2&cvsroot=mauve&only_with_tag=HEADcontributors,
  for Java test code.

* Bryce McKinlay for numerous GCJ and libgcj fixes and improvements.

* Adam Megacz for his work on the Microsoft Windows port of GCJ.

* Michael Meissner for LRS framework, ia32, m32r, v850, m88k, MIPS,
  powerpc, haifa, ECOFF debug support, and other assorted hacking.

* Jason Merrill for his direction via the steering committee and leading
  the G++ effort.

* Martin Michlmayr for testing GCC on several architectures using the
  entire Debian archive.

* David Miller for his direction via the steering committee, lots of
  SPARC work, improvements in jump.c and interfacing with the Linux kernel
  developers.

* Gary Miller ported GCC to Charles River Data Systems machines.

* Alfred Minarik for libstdc++ string and ios bug fixes, and turning the
  entire libstdc++ testsuite namespace-compatible.

* Mark Mitchell for his direction via the steering committee, mountains of
  C++ work, load/store hoisting out of loops, alias analysis improvements,
  ISO C ``restrict`` support, and serving as release manager from 2000
  to 2011.

* Alan Modra for various GNU/Linux bits and testing.

* Toon Moene for his direction via the steering committee, Fortran
  maintenance, and his ongoing work to make us make Fortran run fast.

* Jason Molenda for major help in the care and feeding of all the services
  on the gcc.gnu.org (formerly egcs.cygnus.com) machine-mail, web
  services, ftp services, etc etc.  Doing all this work on scrap paper and
  the backs of envelopes would have been... difficult.

* Catherine Moore for fixing various ugly problems we have sent her
  way, including the haifa bug which was killing the Alpha & PowerPC
  Linux kernels.

* Mike Moreton for his various Java patches.

* David Mosberger-Tang for various Alpha improvements, and for the initial
  IA-64 port.

* Stephen Moshier contributed the floating point emulator that assists in
  cross-compilation and permits support for floating point numbers wider
  than 64 bits and for ISO C99 support.

* Bill Moyer for his behind the scenes work on various issues.

* Philippe De Muyter for his work on the m68k port.

* Joseph S. Myers for his work on the PDP-11 port, format checking and ISO
  C99 support, and continuous emphasis on (and contributions to) documentation.

* Nathan Myers for his work on libstdc++-v3: architecture and authorship
  through the first three snapshots, including implementation of locale
  infrastructure, string, shadow C headers, and the initial project
  documentation (DESIGN, CHECKLIST, and so forth).  Later, more work on
  MT-safe string and shadow headers.

* Felix Natter for documentation on porting libstdc++.

* Nathanael Nerode for cleaning up the configuration/build process.

* NeXT, Inc. donated the front end that supports the Objective-C
  language.

* Hans-Peter Nilsson for the CRIS and MMIX ports, improvements to the search
  engine setup, various documentation fixes and other small fixes.

* Geoff Noer for his work on getting cygwin native builds working.

* Diego Novillo for his work on Tree SSA, OpenMP, SPEC performance
  tracking web pages, GIMPLE tuples, and assorted fixes.

* David O'Brien for the FreeBSD/alpha, FreeBSD/AMD x86-64, FreeBSD/ARM,
  FreeBSD/PowerPC, and FreeBSD/SPARC64 ports and related infrastructure
  improvements.

* Alexandre Oliva for various build infrastructure improvements, scripts and
  amazing testing work, including keeping libtool issues sane and happy.

* Stefan Olsson for work on mt_alloc.

* Melissa O'Neill for various NeXT fixes.

* Rainer Orth for random MIPS work, including improvements to GCC's o32
  ABI support, improvements to dejagnu's MIPS support, Java configuration
  clean-ups and porting work, and maintaining the IRIX, Solaris 2, and
  Tru64 UNIX ports.

* Hartmut Penner for work on the s390 port.

* Paul Petersen wrote the machine description for the Alliant FX/8.

* Alexandre Petit-Bianco for implementing much of the Java compiler and
  continued Java maintainership.

* Matthias Pfaller for major improvements to the NS32k port.

* Gerald Pfeifer for his direction via the steering committee, pointing
  out lots of problems we need to solve, maintenance of the web pages, and
  taking care of documentation maintenance in general.

* Andrew Pinski for processing bug reports by the dozen.

* Ovidiu Predescu for his work on the Objective-C front end and runtime
  libraries.

* Jerry Quinn for major performance improvements in C++ formatted I/O.

* Ken Raeburn for various improvements to checker, MIPS ports and various
  cleanups in the compiler.

* Rolf W. Rasmussen for hacking on AWT.

* David Reese of Sun Microsystems contributed to the Solaris on PowerPC
  port.

* Volker Reichelt for keeping up with the problem reports.

* Joern Rennecke for maintaining the sh port, loop, regmove & reload
  hacking and developing and maintaining the Epiphany port.

* Loren J. Rittle for improvements to libstdc++-v3 including the FreeBSD
  port, threading fixes, thread-related configury changes, critical
  threading documentation, and solutions to really tricky I/O problems,
  as well as keeping GCC properly working on FreeBSD and continuous testing.

* Craig Rodrigues for processing tons of bug reports.

* Ola Ronnerup for work on mt_alloc.

* Gavin Romig-Koch for lots of behind the scenes MIPS work.

* David Ronis inspired and encouraged Craig to rewrite the G77
  documentation in texinfo format by contributing a first pass at a
  translation of the old g77-0.5.16/f/DOC file.

* Ken Rose for fixes to GCC's delay slot filling code.

* Ira Rosen for her contributions to the auto-vectorizer.

* Paul Rubin wrote most of the preprocessor.

* Petur Runolfsson for major performance improvements in C++ formatted I/O and
  large file support in C++ filebuf.

* Chip Salzenberg for libstdc++ patches and improvements to locales, traits,
  Makefiles, libio, libtool hackery, and 'long long' support.

* Juha Sarlin for improvements to the H8 code generator.

* Greg Satz assisted in making GCC work on HP-UX for the 9000 series 300.

* Roger Sayle for improvements to constant folding and GCC's RTL optimizers
  as well as for fixing numerous bugs.

* Bradley Schatz for his work on the GCJ FAQ.

* Peter Schauer wrote the code to allow debugging to work on the Alpha.

* William Schelter did most of the work on the Intel 80386 support.

* Tobias Schluter for work on GNU Fortran.

* Bernd Schmidt for various code generation improvements and major
  work in the reload pass, serving as release manager for
  GCC 2.95.3, and work on the Blackfin and C6X ports.

* Peter Schmid for constant testing of libstdc++-especially application
  testing, going above and beyond what was requested for the release
  criteria-and libstdc++ header file tweaks.

* Jason Schroeder for jcf-dump patches.

* Andreas Schwab for his work on the m68k port.

* Lars Segerlund for work on GNU Fortran.

* Dodji Seketeli for numerous C++ bug fixes and debug info improvements.

* Tim Shen for major work on ``<regex>``.

* Joel Sherrill for his direction via the steering committee, RTEMS
  contributions and RTEMS testing.

* Nathan Sidwell for many C++ fixes/improvements.

* Jeffrey Siegal for helping RMS with the original design of GCC, some
  code which handles the parse tree and RTL data structures, constant
  folding and help with the original VAX & m68k ports.

* Kenny Simpson for prompting libstdc++ fixes due to defect reports from
  the LWG (thereby keeping GCC in line with updates from the ISO).

* Franz Sirl for his ongoing work with making the PPC port stable
  for GNU/Linux.

* Andrey Slepuhin for assorted AIX hacking.

* Trevor Smigiel for contributing the SPU port.

* Christopher Smith did the port for Convex machines.

* Danny Smith for his major efforts on the Mingw (and Cygwin) ports.
  Retired from GCC maintainership August 2010, having mentored two 
  new maintainers into the role.

* Randy Smith finished the Sun FPA support.

* Ed Smith-Rowland for his continuous work on libstdc++-v3, special functions,
  ``<random>``, and various improvements to C++11 features.

* Scott Snyder for queue, iterator, istream, and string fixes and libstdc++
  testsuite entries.  Also for providing the patch to G77 to add
  rudimentary support for ``INTEGER*1``, ``INTEGER*2``, and
  ``LOGICAL*1``.

* Zdenek Sojka for running automated regression testing of GCC and reporting
  numerous bugs.

* Jayant Sonar for contributing the CR16 port.

* Brad Spencer for contributions to the GLIBCPP_FORCE_NEW technique.

* Richard Stallman, for writing the original GCC and launching the GNU project.

* Jan Stein of the Chalmers Computer Society provided support for
  Genix, as well as part of the 32000 machine description.

* Nigel Stephens for various mips16 related fixes/improvements.

* Jonathan Stone wrote the machine description for the Pyramid computer.

* Graham Stott for various infrastructure improvements.

* John Stracke for his Java HTTP protocol fixes.

* Mike Stump for his Elxsi port, G++ contributions over the years and more
  recently his vxworks contributions

* Jeff Sturm for Java porting help, bug fixes, and encouragement.

* Shigeya Suzuki for this fixes for the bsdi platforms.

* Ian Lance Taylor for the Go frontend, the initial mips16 and mips64
  support, general configury hacking, fixincludes, etc.

* Holger Teutsch provided the support for the Clipper CPU.

* Gary Thomas for his ongoing work to make the PPC work for GNU/Linux.

* Philipp Thomas for random bug fixes throughout the compiler

* Jason Thorpe for thread support in libstdc++ on NetBSD.

* Kresten Krab Thorup wrote the run time support for the Objective-C
  language and the fantastic Java bytecode interpreter.

* Michael Tiemann for random bug fixes, the first instruction scheduler,
  initial C++ support, function integration, NS32k, SPARC and M88k
  machine description work, delay slot scheduling.

* Andreas Tobler for his work porting libgcj to Darwin.

* Teemu Torma for thread safe exception handling support.

* Leonard Tower wrote parts of the parser, RTL generator, and RTL
  definitions, and of the VAX machine description.

* Daniel Towner and Hariharan Sandanagobalane contributed and
  maintain the picoChip port.

* Tom Tromey for internationalization support and for his many Java
  contributions and libgcj maintainership.

* Lassi Tuura for improvements to config.guess to determine HP processor
  types.

* Petter Urkedal for libstdc++ CXXFLAGS, math, and algorithms fixes.

* Andy Vaught for the design and initial implementation of the GNU Fortran
  front end.

* Brent Verner for work with the libstdc++ cshadow files and their
  associated configure steps.

* Todd Vierling for contributions for NetBSD ports.

* Jonathan Wakely for contributing libstdc++ Doxygen notes and XHTML
  guidance.

* Dean Wakerley for converting the install documentation from HTML to texinfo
  in time for GCC 3.0.

* Krister Walfridsson for random bug fixes.

* Feng Wang for contributions to GNU Fortran.

* Stephen M. Webb for time and effort on making libstdc++ shadow files
  work with the tricky Solaris 8+ headers, and for pushing the build-time
  header tree. Also, for starting and driving the ``<regex>`` effort.

* John Wehle for various improvements for the x86 code generator,
  related infrastructure improvements to help x86 code generation,
  value range propagation and other work, WE32k port.

* Ulrich Weigand for work on the s390 port.

* Zack Weinberg for major work on cpplib and various other bug fixes.

* Matt Welsh for help with Linux Threads support in GCJ.

* Urban Widmark for help fixing java.io.

* Mark Wielaard for new Java library code and his work integrating with
  Classpath.

* Dale Wiles helped port GCC to the Tahoe.

* Bob Wilson from Tensilica, Inc. for the Xtensa port.

* Jim Wilson for his direction via the steering committee, tackling hard
  problems in various places that nobody else wanted to work on, strength
  reduction and other loop optimizations.

* Paul Woegerer and Tal Agmon for the CRX port.

* Carlo Wood for various fixes.

* Tom Wood for work on the m88k port.

* Chung-Ju Wu for his work on the Andes NDS32 port.

* Canqun Yang for work on GNU Fortran.

* Masanobu Yuhara of Fujitsu Laboratories implemented the machine
  description for the Tron architecture (specifically, the Gmicro).

* Kevin Zachmann helped port GCC to the Tahoe.

* Ayal Zaks for Swing Modulo Scheduling (SMS).

* Xiaoqiang Zhang for work on GNU Fortran.

* Gilles Zunino for help porting Java to Irix.

The following people are recognized for their contributions to GNAT,
the Ada front end of GCC:

* Bernard Banner

* Romain Berrendonner

* Geert Bosch

* Emmanuel Briot

* Joel Brobecker

* Ben Brosgol

* Vincent Celier

* Arnaud Charlet

* Chien Chieng

* Cyrille Comar

* Cyrille Crozes

* Robert Dewar

* Gary Dismukes

* Robert Duff

* Ed Falis

* Ramon Fernandez

* Sam Figueroa

* Vasiliy Fofanov

* Michael Friess

* Franco Gasperoni

* Ted Giering

* Matthew Gingell

* Laurent Guerby

* Jerome Guitton

* Olivier Hainque

* Jerome Hugues

* Hristian Kirtchev

* Jerome Lambourg

* Bruno Leclerc

* Albert Lee

* Sean McNeil

* Javier Miranda

* Laurent Nana

* Pascal Obry

* Dong-Ik Oh

* Laurent Pautet

* Brett Porter

* Thomas Quinot

* Nicolas Roche

* Pat Rogers

* Jose Ruiz

* Douglas Rupp

* Sergey Rybin

* Gail Schenker

* Ed Schonberg

* Nicolas Setton

* Samuel Tardieu

The following people are recognized for their contributions of new
features, bug reports, testing and integration of classpath/libgcj for
GCC version 4.1:

* Lillian Angel for ``JTree`` implementation and lots Free Swing
  additions and bug fixes.

* Wolfgang Baer for ``GapContent`` bug fixes.

* Anthony Balkissoon for ``JList``, Free Swing 1.5 updates and mouse event
  fixes, lots of Free Swing work including ``JTable`` editing.

* Stuart Ballard for RMI constant fixes.

* Goffredo Baroncelli for ``HTTPURLConnection`` fixes.

* Gary Benson for ``MessageFormat`` fixes.

* Daniel Bonniot for ``Serialization`` fixes.

* Chris Burdess for lots of gnu.xml and http protocol fixes, ``StAX``
  and ``DOM xml:id`` support.

* Ka-Hing Cheung for ``TreePath`` and ``TreeSelection`` fixes.

* Archie Cobbs for build fixes, VM interface updates,
  ``URLClassLoader`` updates.

* Kelley Cook for build fixes.

* Martin Cordova for Suggestions for better ``SocketTimeoutException``.

* David Daney for ``BitSet`` bug fixes, ``HttpURLConnection``
  rewrite and improvements.

* Thomas Fitzsimmons for lots of upgrades to the gtk+ AWT and Cairo 2D
  support. Lots of imageio framework additions, lots of AWT and Free
  Swing bug fixes.

* Jeroen Frijters for ``ClassLoader`` and nio cleanups, serialization fixes,
  better ``Proxy`` support, bug fixes and IKVM integration.

* Santiago Gala for ``AccessControlContext`` fixes.

* Nicolas Geoffray for ``VMClassLoader`` and ``AccessController``
  improvements.

* David Gilbert for ``basic`` and ``metal`` icon and plaf support
  and lots of documenting, Lots of Free Swing and metal theme
  additions. ``MetalIconFactory`` implementation.

* Anthony Green for ``MIDI`` framework, ``ALSA`` and ``DSSI``
  providers.

* Andrew Haley for ``Serialization`` and ``URLClassLoader`` fixes,
  gcj build speedups.

* Kim Ho for ``JFileChooser`` implementation.

* Andrew John Hughes for ``Locale`` and net fixes, URI RFC2986
  updates, ``Serialization`` fixes, ``Properties`` XML support and
  generic branch work, VMIntegration guide update.

* Bastiaan Huisman for ``TimeZone`` bug fixing.

* Andreas Jaeger for mprec updates.

* Paul Jenner for better :option:`-Werror` support.

* Ito Kazumitsu for ``NetworkInterface`` implementation and updates.

* Roman Kennke for ``BoxLayout``, ``GrayFilter`` and
  ``SplitPane``, plus bug fixes all over. Lots of Free Swing work
  including styled text.

* Simon Kitching for ``String`` cleanups and optimization suggestions.

* Michael Koch for configuration fixes, ``Locale`` updates, bug and
  build fixes.

* Guilhem Lavaux for configuration, thread and channel fixes and Kaffe
  integration. JCL native ``Pointer`` updates. Logger bug fixes.

* David Lichteblau for JCL support library global/local reference
  cleanups.

* Aaron Luchko for JDWP updates and documentation fixes.

* Ziga Mahkovec for ``Graphics2D`` upgraded to Cairo 0.5 and new regex
  features.

* Sven de Marothy for BMP imageio support, CSS and ``TextLayout``
  fixes. ``GtkImage`` rewrite, 2D, awt, free swing and date/time fixes and
  implementing the Qt4 peers.

* Casey Marshall for crypto algorithm fixes, ``FileChannel`` lock,
  ``SystemLogger`` and ``FileHandler`` rotate implementations, NIO
  ``FileChannel.map`` support, security and policy updates.

* Bryce McKinlay for RMI work.

* Audrius Meskauskas for lots of Free Corba, RMI and HTML work plus
  testing and documenting.

* Kalle Olavi Niemitalo for build fixes.

* Rainer Orth for build fixes.

* Andrew Overholt for ``File`` locking fixes.

* Ingo Proetel for ``Image``, ``Logger`` and ``URLClassLoader``
  updates.

* Olga Rodimina for ``MenuSelectionManager`` implementation.

* Jan Roehrich for ``BasicTreeUI`` and ``JTree`` fixes.

* Julian Scheid for documentation updates and gjdoc support.

* Christian Schlichtherle for zip fixes and cleanups.

* Robert Schuster for documentation updates and beans fixes,
  ``TreeNode`` enumerations and ``ActionCommand`` and various
  fixes, XML and URL, AWT and Free Swing bug fixes.

* Keith Seitz for lots of JDWP work.

* Christian Thalinger for 64-bit cleanups, Configuration and VM
  interface fixes and ``CACAO`` integration, ``fdlibm`` updates.

* Gael Thomas for ``VMClassLoader`` boot packages support suggestions.

* Andreas Tobler for Darwin and Solaris testing and fixing, ``Qt4``
  support for Darwin/OS X, ``Graphics2D`` support, ``gtk+``
  updates.

* Dalibor Topic for better ``DEBUG`` support, build cleanups and
  Kaffe integration. ``Qt4`` build infrastructure, ``SHA1PRNG``
  and ``GdkPixbugDecoder`` updates.

* Tom Tromey for Eclipse integration, generics work, lots of bug fixes
  and gcj integration including coordinating The Big Merge.

* Mark Wielaard for bug fixes, packaging and release management,
  ``Clipboard`` implementation, system call interrupts and network
  timeouts and ``GdkPixpufDecoder`` fixes.

In addition to the above, all of which also contributed time and energy in
testing GCC, we would like to thank the following for their contributions
to testing:

* Michael Abd-El-Malek

* Thomas Arend

* Bonzo Armstrong

* Steven Ashe

* Chris Baldwin

* David Billinghurst

* Jim Blandy

* Stephane Bortzmeyer

* Horst von Brand

* Frank Braun

* Rodney Brown

* Sidney Cadot

* Bradford Castalia

* Robert Clark

* Jonathan Corbet

* Ralph Doncaster

* Richard Emberson

* Levente Farkas

* Graham Fawcett

* Mark Fernyhough

* Robert A. French

* Jorgen Freyh

* Mark K. Gardner

* Charles-Antoine Gauthier

* Yung Shing Gene

* David Gilbert

* Simon Gornall

* Fred Gray

* John Griffin

* Patrik Hagglund

* Phil Hargett

* Amancio Hasty

* Takafumi Hayashi

* Bryan W. Headley

* Kevin B. Hendricks

* Joep Jansen

* Christian Joensson

* Michel Kern

* David Kidd

* Tobias Kuipers

* Anand Krishnaswamy

* A. O. V. Le Blanc

* llewelly

* Damon Love

* Brad Lucier

* Matthias Klose

* Martin Knoblauch

* Rick Lutowski

* Jesse Macnish

* Stefan Morrell

* Anon A. Mous

* Matthias Mueller

* Pekka Nikander

* Rick Niles

* Jon Olson

* Magnus Persson

* Chris Pollard

* Richard Polton

* Derk Reefman

* David Rees

* Paul Reilly

* Tom Reilly

* Torsten Rueger

* Danny Sadinoff

* Marc Schifer

* Erik Schnetter

* Wayne K. Schroll

* David Schuler

* Vin Shelton

* Tim Souder

* Adam Sulmicki

* Bill Thorson

* George Talbot

* Pedro A. M. Vazquez

* Gregory Warnes

* Ian Watson

* David E. Young

* And many others

And finally we'd like to thank everyone who uses the compiler, provides
feedback and generally reminds us why we're doing this work in the first
place.

.. -
   Indexes
   -

.. _option-index:

Option Index
============

GCC's command line options are indexed here without any initial :samp:`-`
or :samp:`--`.  Where an option has both positive and negative forms
(such as :option:`-f``option``` and :option:`-fno-``option```),
relevant entries in the manual are indexed under the most appropriate
form; it may sometimes be useful to look up both forms.

.. _keyword-index:

Keyword Index
=============

.. -
   Epilogue
   -

