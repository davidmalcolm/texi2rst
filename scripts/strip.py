#!/usr/bin/env python3

import os
import sys

for root, _, files in os.walk(sys.argv[1]):
    for f in files:
        full = os.path.join(root, f)
        parts = root.split('/')
        up2 = '../' * (len(parts) - 1)
        print(full)
        while parts:
            if os.path.exists(os.path.join(*parts, 'conf.py')):
                break
            parts = parts[:-1]

        up1 = '../' * (len(parts) - 2) if parts else None

        if f.endswith('.rst'):
            lines = open(full).read().strip().splitlines()
            newlines = []
            for line in lines:
                line = line.rstrip()
                if '.. include:: ' in line and 'share' in line:
                    line = line.replace('share', f'{up1}doc')
                newlines.append(line)

            with open(full, 'w') as f:
                f.write('\n'.join(newlines))
        elif f == 'conf.py':
            lines = open(full).read().splitlines()
            newlines = []
            for line in lines:
                if line.startswith('sys.path.append'):
                    line = f"sys.path.append('{up2}/doc')"
                newlines.append(line)
            with open(full, 'w') as f:
                f.write('\n'.join(newlines))
