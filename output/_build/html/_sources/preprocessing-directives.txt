Preprocessing Directives
************************

Implementation-defined behaviorImplementation-defined
behaviorcppThe C Preprocessor, for details of these aspects of
implementation-defined behavior.

* The locations within ``#pragma`` directives where header name
  preprocessing tokens are recognized (C11 6.4, C11 6.4.7).

  * How sequences in both forms of header names are mapped to headers
  or external source file names (C90 6.1.7, C99 and C11 6.4.7).

  * Whether the value of a character constant in a constant expression
  that controls conditional inclusion matches the value of the same character
  constant in the execution character set (C90 6.8.1, C99 and C11 6.10.1).

  * Whether the value of a single-character character constant in a
  constant expression that controls conditional inclusion may have a
  negative value (C90 6.8.1, C99 and C11 6.10.1).

  * The places that are searched for an included <> delimited
  header, and how the places are specified or the header is
  identified (C90 6.8.2, C99 and C11 6.10.2).

  * How the named source file is searched for in an included ""
  delimited header (C90 6.8.2, C99 and C11 6.10.2).

  * The method by which preprocessing tokens (possibly resulting from
  macro expansion) in a ``#include`` directive are combined into a header
  name (C90 6.8.2, C99 and C11 6.10.2).

  * The nesting limit for ``#include`` processing (C90 6.8.2, C99
  and C11 6.10.2).

  * Whether the # operator inserts a \ character before
  the \ character that begins a universal character name in a
  character constant or string literal (C99 and C11 6.10.3.2).

  * The behavior on each recognized non-``STDC #pragma``
  directive (C90 6.8.6, C99 and C11 6.10.6).

  PragmasPragmascppThe C Preprocessor, for details of
  pragmas accepted by GCC on all targets.  PragmasPragmas
  Accepted by GCC, for details of target-specific pragmas.

  * The definitions for ``__DATE__`` and ``__TIME__`` when
  respectively, the date and time of translation are not available (C90
  6.8.8, C99 6.10.8, C11 6.10.8.1).

