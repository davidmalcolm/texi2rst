# Configuration file for the Sphinx documentation builder.

import sys
sys.path.append('..')

from baseconf import *

project = 'Demo project'
copyright = '2001-2022 Free Software Foundation, Inc.'
authors = 'Martin Liska'

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
latex_documents = [
  ('index', 'demo.tex', project, authors, 'manual'),
]

texinfo_documents = [
  ('index', 'demo', project, authors, None, None, None, True)
]

tags.add('demo')
