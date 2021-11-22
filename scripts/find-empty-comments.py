#!/usr/bin/env python3

import os

counter = 0

with open('qf.txt', 'w') as qf:
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.rst'):
                full = os.path.join(root, file)
                lines = open(full).read().strip().splitlines()
                i = len(lines) - 1
                while True:
                    if not lines[i].startswith('  '):
                        break
                    i -= 1

                line = lines[i]
                if (line.startswith('.. ') and '::' not in line and 'hook-end' not in line
                        and '[#' not in line and 'TODO' not in line):
                    counter += 1
                    qf.write(f'{full}:100000:error\n')
                    print(f'=== {full} (#{counter})===')
                    print(lines[i:])
