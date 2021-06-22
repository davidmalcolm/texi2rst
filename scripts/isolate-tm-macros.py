#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description='Parse and modify target .def files')
parser.add_argument('rst_dir', help='Directory with RST files')
parser.add_argument('gcc_dir', help='Directory GCC source')
parser.add_argument('--replace', action='store_true', help='Replace .def files in a repo')
args = parser.parse_args()

folder = os.path.join(args.rst_dir, 'gccint/target-description-macros-and-functions')

d = {}

for root, _, files in os.walk(folder):
    for filename in files:
        lines = open(os.path.join(root, filename)).read().splitlines()

        name = None
        for line in lines:
            line = line.lstrip()
            if line.startswith('xxxHOOK'):
                name = line.split(':')[-1]
                assert name not in d
                d[name] = []
            elif line.startswith('yyyHOOK'):
                assert name
                name = None
            elif name:
                assert '.. function' not in line
                d[name].append(line)

folder = os.path.join(args.gcc_dir, 'gcc')
files = ('target.def', 'c-family/c-target.def', 'common/common-target.def', 'd/d-target.def')

for filename in files:
    lines = open(os.path.join(folder, filename)).read().splitlines()
    prefix = None
    hooknow = True

    if not args.replace:
        filename += '.new'
    with open(os.path.join(folder, filename), 'w') as f:
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.startswith('#define HOOK_PREFIX '):
                prefix = line.split(' ')[-1].strip('"')
            elif line in ('DEFHOOK', 'DEFHOOKPOD'):
                hookname = lines[i + 1]
                f.write(line + '\n')
                f.write(lines[i + 1] + '\n')
                i += 2
                assert hookname.startswith('(') and hookname.endswith(',')
                fullname = prefix + hookname[1:-1]
                while not lines[i].endswith('",'):
                    assert lines[i].endswith('\\n\\')
                    assert 'DEFHOOK' not in lines[i]
                    i += 1
                i += 1
                f.write(' "')

                # strip leading empty lines
                newlines = d[fullname]
                while newlines and not newlines[-1]:
                    newlines = newlines[:-1]
                for j in range(len(newlines)):
                    newlines[j] = newlines[j].replace('\\', '\\\\').replace('"', '\\"')

                f.write('\\n\\\n'.join(newlines))
                f.write('",\n')

                # remove fullname from d
                del d[fullname]
                continue

            f.write(line + '\n')
            i += 1

assert not d
