.. _language-independent-options:

Options to Control Diagnostic Messages Formatting
*************************************************

.. index:: options to control diagnostics formatting

.. index:: diagnostic messages

.. index:: message formatting

Traditionally, diagnostic messages have been formatted irrespective of
the output device's aspect (e.g. its width, ...).  You can use the
options described below
to control the formatting algorithm for diagnostic messages, 
e.g. how many characters per line, how often source location
information should be reported.  Note that some language front ends may not
honor these options.

.. option:: -fmessage-length=n

  Try to format error messages so that they fit on lines of about
  ``n`` characters.  If ``n`` is zero, then no line-wrapping is
  done; each error message appears on a single line.  This is the
  default for all front ends.

.. option:: -fdiagnostics-show-location=once

  Only meaningful in line-wrapping mode.  Instructs the diagnostic messages
  reporter to emit source location information once; that is, in
  case the message is too long to fit on a single physical line and has to
  be wrapped, the source location won't be emitted (as prefix) again,
  over and over, in subsequent continuation lines.  This is the default
  behavior.

-fdiagnostics-show-location=every-line
  Only meaningful in line-wrapping mode.  Instructs the diagnostic
  messages reporter to emit the same source location information (as
  prefix) for physical lines that result from the process of breaking
  a message which is too long to fit on a single line.

.. option:: -fdiagnostics-color[=WHEN]

  .. index:: highlight, color, colour

  GCC_COLORS environment variableUse color in diagnostics.  ``WHEN`` is never, always,
  or auto.  The default depends on how the compiler has been configured,
  it can be any of the above ``WHEN`` options or also never
  if :envvar:`GCC_COLORS` environment variable isn't present in the environment,
  and auto otherwise.
  auto means to use color only when the standard error is a terminal.
  The forms :option:`-fdiagnostics-color` and :option:`-fno-diagnostics-color` are
  aliases for :option:`-fdiagnostics-color=always` and
  :option:`-fdiagnostics-color=never`, respectively.

  The colors are defined by the environment variable :envvar:`GCC_COLORS`.
  Its value is a colon-separated list of capabilities and Select Graphic
  Rendition (SGR) substrings. SGR commands are interpreted by the
  terminal or terminal emulator.  (See the section in the documentation
  of your text terminal for permitted values and their meanings as
  character attributes.)  These substring values are integers in decimal
  representation and can be concatenated with semicolons.
  Common values to concatenate include
  1 for bold,
  4 for underline,
  5 for blink,
  7 for inverse,
  39 for default foreground color,
  30 to 37 for foreground colors,
  90 to 97 for 16-color mode foreground colors,
  38;5;0 to 38;5;255
  for 88-color and 256-color modes foreground colors,
  49 for default background color,
  40 to 47 for background colors,
  100 to 107 for 16-color mode background colors,
  and 48;5;0 to 48;5;255
  for 88-color and 256-color modes background colors.

  The default :envvar:`GCC_COLORS` is

  .. code-block:: c++

    error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01

  where 01;31 is bold red, 01;35 is bold magenta,
  01;36 is bold cyan, 01;32 is bold green and
  01 is bold. Setting :envvar:`GCC_COLORS` to the empty
  string disables colors.
  Supported capabilities are as follows.

  error=
    error GCC_COLORS capabilitySGR substring for error: markers.

  warning=
    warning GCC_COLORS capabilitySGR substring for warning: markers.

  note=
    note GCC_COLORS capabilitySGR substring for note: markers.

  caret=
    caret GCC_COLORS capabilitySGR substring for caret line.

  locus=
    locus GCC_COLORS capabilitySGR substring for location information, file:line or
    file:line:column etc.

  quote=
    quote GCC_COLORS capabilitySGR substring for information printed within quotes.

.. option:: -fno-diagnostics-show-option, -fdiagnostics-show-option

  By default, each diagnostic emitted includes text indicating the
  command-line option that directly controls the diagnostic (if such an
  option is known to the diagnostic machinery).  Specifying the
  :option:`-fno-diagnostics-show-option` flag suppresses that behavior.

.. option:: -fno-diagnostics-show-caret, -fdiagnostics-show-caret

  By default, each diagnostic emitted includes the original source line
  and a caret '^' indicating the column.  This option suppresses this
  information.  The source line is truncated to ``n`` characters, if
  the :option:`-fmessage-length=n` option is given.  When the output is done
  to the terminal, the width is limited to the width given by the
  :envvar:`COLUMNS` environment variable or, if not set, to the terminal width.

