#!/usr/bin/env python3

import os
import sys

for root, _, files in os.walk(sys.argv[1]):
    for f in files:
        if f.endswith('.rst'):
            full = os.path.join(root, f)
            lines = open(full).read().strip().splitlines()
            newlines = []
            for line in lines:
                line = line.rstrip()
                prefix = '.. include:: ../share/'
                if line.startswith(prefix):
                    parts = len(root.split('/'))
                    up = '../' * (parts - 1)
                    newline = f'.. include:: {up}doc/{line[len(prefix):]}'
                    newlines.append(newline)
                    print(root, line, newline)
                else:
                    newlines.append(line)

            with open(full, 'w') as f:
                f.write('\n'.join(newlines))
