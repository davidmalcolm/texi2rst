#!/usr/bin/env python3

import os

for root, _, files in os.walk('.'):
    for f in files:
        if f.endswith('.rst'):
            full = os.path.join(root, f)
            lines = reversed(open(full).read().splitlines())
            for line in lines:
                if line.startswith('  '):
                    pass
                elif line.startswith('..') and ':' not in line and '.. hook' not in line and '[#' not in line:
                    print(f'{full}:{line}')
                    break
                else:
                    break
