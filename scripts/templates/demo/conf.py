# Configuration file for the Sphinx documentation builder.

import sys
sys.path.append('..')

from baseconf import *

project = 'Demo project'
copyright = '2001-2021 Free Software Foundation, Inc.'
authors = 'Martin Liska'

texinfo_documents = [
  ('index', 'demo', project, authors, None, None, None, True)
]

tags.add('demo')
