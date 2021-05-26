#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description='Create conditional directives')
parser.add_argument('rst_dir', help='Directory with RST files')
args = parser.parse_args()

share = os.path.join(args.rst_dir, 'share')
os.chdir(share)


def make_condition(path, condition, start_line, end_line=None):
    lines = open(path).read().splitlines()
    prefix = ' ' * (len(start_line) - len(start_line.lstrip()))
    with open(path, 'w') as f:
        in_condition = False
        for line in lines:
            dropped = False
            if line == start_line:
                in_condition = True
                f.write(f'\n{prefix}.. only:: {condition}\n\n')
            elif line == end_line:
                in_condition = False
                dropped = True
            if in_condition:
                f.write('  ')
            f.write(line + '\n')
            if in_condition and not end_line:
                in_condition = False
                dropped = True
            if dropped:
                f.write('\n')


for start_line in ('  See :ref:`search-path`.', '  See :ref:`system-headers`.'):
    make_condition('cppdiropts.rst', 'cpp', start_line)
