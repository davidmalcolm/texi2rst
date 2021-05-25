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


def include_rst(path, link):
    with open(path, 'w') as f:
        f.write(f'.. include:: {link}\n')


# Licence files
shutil.copy('templates/gnu_free_documentation_license.rst', share)
shutil.copy('templates/gpl-3.0.rst', share)
shutil.copy('templates/funding.rst', share)

# Modify generated files
os.chdir(args.rst_dir)

for folder in os.listdir('.'):
    if os.path.isdir(folder) and folder != 'share':
        include_rst(f'{folder}/general-public-license-3.rst', '../share/gpl-3.0.rst')
        include_rst(f'{folder}/gnu-free-documentation-license.rst', '../share/gnu_free_documentation_license.rst')
        include_rst(f'{folder}/funding.rst', '../share/funding.rst')

shutil.copy('gcc/contributors-to-gcc.rst', 'share/contrib.rst')
include_rst('gcc/contributors-to-gcc.rst', '../share/contrib.rst')
include_rst('gccint/contributors-to-gcc.rst', '../share/contrib.rst')
