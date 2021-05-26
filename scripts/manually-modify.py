#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description='Manual changes')
parser.add_argument('rst_dir', help='Directory with RST files')
args = parser.parse_args()


def replace_line(path, needle, replacement):
    lines = open(path).read().splitlines()
    with open(path, 'w') as f:
        for line in lines:
            line = line.replace(needle, replacement)
            f.write(line + '\n')


replace_line(os.path.join(args.rst_dir, 'gccint/operand-constraints.rst'),
             '    .. _disable-insn-alternatives:', '.. _disable-insn-alternatives:')
