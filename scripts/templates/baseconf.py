# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

# The full version, including alpha/beta/rc tags

# FIXME
folder = os.path.dirname(os.path.realpath(__file__))
gcc_srcdir = os.path.join(folder, './objdir')

def __read_file(name):
    path = os.path.join(gcc_srcdir, name)
    if os.path.exists(path):
        return open(path).read().strip()
    else:
        return ''

gcc_BASEVER = __read_file('BASE-VER')
gcc_DEVPHASE = __read_file('DEV-PHASE')
gcc_DATESTAMP = __read_file('DATESTAMP')
gcc_REVISION = __read_file('REVISION')

VERSION_PACKAGE = os.getenv('VERSION_PACKAGE', '(GCC)')
BUGURL = os.getenv('BUGURL', 'https://gcc.gnu.org/bugs/')

# The short X.Y version.
version = gcc_BASEVER

# The full version, including alpha/beta/rc tags.
release = ('%s (%s %s%s)'
           % (gcc_BASEVER, gcc_DEVPHASE, gcc_DATESTAMP,
              (' %s' % gcc_REVISION) if gcc_REVISION else ''))

rst_epilog = '''
.. |gcc_version| replace:: %s
.. |package_version| replace:: %s
.. |bugurl| replace:: %s
''' % (gcc_BASEVER, VERSION_PACKAGE, BUGURL)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'gcc_sphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']

# For legacy Sphinx versions (< 2.0)
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'prev_next_buttons_location': 'both'
}

# By default, do not generate any manual pages
man_pages = []

# FIXME: handle WARNINGs: unknown option issues and cross refs
suppress_warnings = [
    'ref.option',
    'ref.ref'
]

# RTD template requires at least Sphinx 1.6
# sphinx-build -j auto is supported since 1.7
needs_sphinx = '1.7'

# Use xelatex by default
latex_engine = 'xelatex'

texinfo_elements = { 'preamble': """
@definfoenclose strong,*,*
@definfoenclose emph,','
"""
}
