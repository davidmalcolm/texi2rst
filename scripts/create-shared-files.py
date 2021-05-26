#!/usr/bin/env python3

import argparse
import os
import shutil

parser = argparse.ArgumentParser(description='Factor out shared content')
parser.add_argument('rst_dir', help='Directory with RST files')
args = parser.parse_args()

share = os.path.join(args.rst_dir, 'share')
shutil.rmtree(share, ignore_errors=True)
os.mkdir(share)


def include_rst(path, link, start_line=None, end_line=None):
    assert not link.startswith('..')
    if not start_line or not end_line:
        with open(path, 'w') as f:
            f.write(f'.. include:: ../{link}\n')
    else:
        lines = open(path).read().splitlines()
        with open(path, 'w') as f:
            with open(link, 'w') as shared:
                in_shared = False
                for line in lines:
                    if line == start_line:
                        in_shared = True
                        f.write(f'.. include:: ../{link}\n\n')
                    elif line == end_line:
                        in_shared = False

                    if in_shared:
                        shared.write(line + '\n')
                    else:
                        f.write(line + '\n')


# Licence files
shutil.copy('templates/gnu_free_documentation_license.rst', share)
shutil.copy('templates/gpl-3.0.rst', share)
shutil.copy('templates/funding.rst', share)

# Modify generated files
os.chdir(args.rst_dir)

for folder in os.listdir('.'):
    if os.path.isdir(folder) and folder != 'share':
        include_rst(f'{folder}/general-public-license-3.rst', 'share/gpl-3.0.rst')
        include_rst(f'{folder}/gnu-free-documentation-license.rst', 'share/gnu_free_documentation_license.rst')
        include_rst(f'{folder}/funding.rst', 'share/funding.rst')

shutil.copy('gcc/contributors-to-gcc.rst', 'share/contrib.rst')
include_rst('gcc/contributors-to-gcc.rst', 'share/contrib.rst')
include_rst('gccint/contributors-to-gcc.rst', 'share/contrib.rst')

shutil.copy('gcc/contributing-to-gcc-development.rst', 'share/contribute.rst')
include_rst('gcc/contributing-to-gcc-development.rst', 'share/contribute.rst')
include_rst('gccint/contributing-to-gcc-development.rst', 'share/contribute.rst')

start_line = '.. _gnu-project:'
end_line = '.. _option-index:'
include_rst('gcc/gcc.rst', 'share/gnu.rst', start_line, end_line)
include_rst('gccint/gccint.rst', 'share/gnu.rst', start_line, end_line)

start_line = '.. option:: -I dir, -I, -iquote, -isystem, -idirafter'
end_line = '.. option:: -iplugindir=dir'
include_rst('gcc/options-for-directory-search.rst', 'share/cppdiropts.rst', start_line, end_line)

end_line = '  .. Copyright (C) 1999-2021 Free Software Foundation, Inc.'
include_rst('cpp/invocation.rst', 'share/cppdiropts.rst', start_line, end_line)

start_line = '.. envvar:: CPATHCPATH'
end_line = '  process.'
include_rst('gcc/environment-variables-affecting-gcc.rst', 'share/cppenv.rst', start_line, end_line)
include_rst('cpp/environment-variables.rst', 'share/cppenv.rst', start_line, end_line)
