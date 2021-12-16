#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description='Fix option tables')
parser.add_argument('rst_dir', help='Directory with RST files')
args = parser.parse_args()

FILES = ['gcc-command-options/option-summary.rst', 'gcc-command-options/options-that-control-optimization.rst']

for root, _, files in os.walk(args.rst_dir):
    for f in files:
        if f.endswith('.rst'):
            full = os.path.join(root, f)
            if any(full.endswith(x) for x in FILES):
                lines = open(full).read().splitlines()
                with open(full, 'w') as out:
                    options = []
                    for i, line in enumerate(lines):
                        last = line.rstrip()[-1]
                        if (line.startswith('  :option:') and lines[i + 1].strip()
                                and '|gol|' not in line and last in ('`', ']')):
                            line = line.rstrip() + ' |gol|'
                        out.write(line + '\n')
