Slightly Looser Rules for Escaped Newlines
******************************************

.. index:: escaped newlines

.. index:: newlines (escaped)

The preprocessor treatment of escaped newlines is more relaxed 
than that specified by the C90 standard, which requires the newline
to immediately follow a backslash.  
GCCs implementation allows whitespace in the form
of spaces, horizontal and vertical tabs, and form feeds between the
backslash and the subsequent newline.  The preprocessor issues a
warning, but treats it as a valid escaped newline and combines the two
lines to form a single logical line.  This works within comments and
tokens, as well as between tokens.  Comments are not treated as
whitespace for the purposes of this relaxation, since they have not
yet been replaced with spaces.

