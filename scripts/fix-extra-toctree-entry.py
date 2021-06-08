#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Remove extra TOC tree entries based on warnings')
parser.add_argument('file', help='File with warnings')
args = parser.parse_args()

lines = open(args.file).read().splitlines()
d = {}


def skip(line, tokens):
    if not line.startswith('  '):
        return False
    ending = line.strip().split('/')[-1]
    return ending in tokens


for line in lines:
    parts = line.split(':')
    if 'toctree contains reference to nonexisting document' not in parts[3]:
        print(f'WARNING: skipped: {line}')
        continue
    filename = parts[0]
    token = parts[-1].split(' ')[-1].strip("'")
    d.setdefault(filename, []).append(token.split('/')[-1])

for filename, tokens in d.items():
    lines = open(filename).read().splitlines()
    with open(filename, 'w') as f:
        for line in lines:
            if not skip(line, tokens):
                f.write(line + '\n')
