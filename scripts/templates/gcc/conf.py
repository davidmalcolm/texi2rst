# Configuration file for the Sphinx documentation builder.

import sys
sys.path.append('..')

from baseconf import *

project = 'Using the GNU Compiler Collection'
copyright = '1988-2021 Free Software Foundation, Inc.'
authors = 'Richard M. Stallman and the GCC Developer Community'

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
latex_documents = [
  ('index', 'gcc.tex', project, authors, 'manual'),
]

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('gcc-command-options', 'gcc', 'GNU project C and C++ compiler', [authors], 1),
    ('gcov-a-test-coverage-program', 'gcov', 'coverage testing tool', [authors], 1),
    ('gcov-dump-an-offline-gcda-and-gcno-profile-dump-tool', 'gcov-dump', 'offline gcda and gcno profile dump tool', [authors], 1),
    ('gcov-tool-an-offline-gcda-profile-processing-tool', 'gcov-tool', 'offline gcda profile processing tool', [authors], 1),
    ('lto-dump-tool-for-dumping-lto-object-files', 'lto-dump', 'Tool for dumping LTO object files', [authors], 1),
]

texinfo_documents = [
  ('gcc-command-options', 'gcc', project, authors, None, None, None, True)
]

tags.add('gcc')
