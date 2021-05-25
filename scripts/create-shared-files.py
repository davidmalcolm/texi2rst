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
os.chdir(args.rst_dir)


def include_rst(path, link):
    with open(path, 'w') as f:
        f.write(f'.. include:: {link}\n')


shutil.copy('gcc/contributors-to-gcc.rst', 'share/contrib.rst')
include_rst('gcc/contributors-to-gcc.rst', '../share/contrib.rst')
include_rst('gccint/contributors-to-gcc.rst', '../share/contrib.rst')
