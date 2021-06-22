#!/usr/bin/env python3

import os
import sys

folder = sys.argv[1]
for root, _, files in os.walk(folder):
    for f in files:
        full = os.path.join(root, f)
        assert full.startswith(folder)
        relative = full[len(folder) + 1:]
        ups = '../' * relative.count('/')

        lines = open(full).read().splitlines()
        newlines = []

        name = None
        for i, line in enumerate(lines):
            if line.lstrip().startswith('.. hook-start'):
                name = line.split(':')[-1]
                prev = lines[i - 2].strip()
                assert prev.startswith('.. c:var') or prev.startswith('.. function')
                newlines = newlines[:-2]
                newlines.append(f'.. include:: {ups}tm.rst.in')
                newlines.append(f'  :start-after: [{name}]')
                newlines.append(f'  :end-before: [{name}]')
                newlines.append('')
            elif line.lstrip().startswith('.. hook-end'):
                name = None
            else:
                newlines.append(line)

        with open(full, 'w') as f:
            f.write('\n'.join(newlines))
