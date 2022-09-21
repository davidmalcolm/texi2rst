#!/usr/bin/env python3

import os
import sys
from pathlib import Path


def get_name(lines):
    for line in lines:
        i = line.find('Function Attributes')
        if i != -1:
            return line[:i]


files = sorted(os.listdir(sys.argv[1]))
for file in files:
    path = Path(sys.argv[1], file)
    base = path.name[:path.name.index('-function-attributes.rst')]
    lines = open(path).read().splitlines()
    target_name = get_name(lines)
    print(f"('{target_name}', '{base}'), ", end='')

    with open(path, 'w') as f:
        base += '-'
        if base == 'common-':
            base = ''
        for line in lines:
            line = line.replace('gcc-attr', f'{base}fn-attr')
            f.write(line + '\n')
