#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description='Add copyright')
parser.add_argument('rst_dir', help='Directory with RST files')
args = parser.parse_args()

for root, _, files in os.walk(args.rst_dir):
    for f in files:
        if f.endswith('.rst'):
            full = os.path.join(root, f)
            data = open(full).read()
            with open(full, 'w') as out:
                out.write('..\n')
                out.write('  Copyright 1988-2022 Free Software Foundation, Inc.\n')
                out.write('  This is part of the GCC manual.\n')
                out.write('  For copying conditions, see the copyright.rst file.\n')
                out.write('\n')
                out.write(data)
