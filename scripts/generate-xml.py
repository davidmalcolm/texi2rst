#!/usr/bin/env python3

import argparse
import concurrent.futures
import os
import subprocess

parser = argparse.ArgumentParser(description='Convert TEXI files to XML')
parser.add_argument('gcc_dir', help='GCC source directory')
parser.add_argument('gcc_objdir', help='GCC object directory')
parser.add_argument('output', help='Output directory')
args = parser.parse_args()

includes = f'-I{args.gcc_dir}/gcc/doc -I{args.gcc_dir}/gcc/doc/include -I{args.gcc_objdir}/gcc'
cmd = 'makeinfo --xml'

if not os.path.exists(args.output):
    os.mkdir(args.output)


def generate(cmd):
    subprocess.check_output(cmd, shell=True)


with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = []
    cmds = []
    cmds.append(f'{cmd} {includes} {args.gcc_dir}/gcc/doc/install.texi -o {args.output}/install.xml')
    cmds.append(f'{cmd} {includes} {args.gcc_dir}/gcc/doc/gcc.texi -o {args.output}/gcc.xml')
    cmds.append(f'{cmd} {includes} {args.gcc_dir}/gcc/fortran/gfortran.texi -I{args.gcc_dir}/gcc/fortran -o '
                f'{args.output}/gfortran.xml')
    cmds.append(f'{cmd} {includes} {args.gcc_dir}/gcc/go/gccgo.texi -I{args.gcc_dir}/gcc/go -o '
                f'{args.output}/gccgo.xml')
    cmds.append(f'{cmd} {includes} {args.gcc_dir}/gcc/doc/cpp.texi -o {args.output}/cpp.xml')
    for lib in ('libgomp', 'libquadmath', 'libitm'):
        cmds.append(f'{cmd} {includes} {args.gcc_dir}/{lib}/{lib}.texi -o {args.output}/{lib}.xml')
    cmds.append(f'{cmd} {includes} {args.gcc_dir}/gcc/doc/gccint.texi -o {args.output}/gccint.xml')
    cmds.append(f'{cmd} {includes} {args.gcc_dir}/gcc/doc/cppinternals.texi -o {args.output}/cppinternals.xml')
    cmds.append(f'{cmd} {includes} {args.gcc_dir}/gcc/fortran/gfc-internals.texi -o '
                f'{args.output}/gfc-internals.xml')
    cmds.append(f'{cmd} {includes} {args.gcc_dir}/libiberty/libiberty.texi -o {args.output}/libiberty.xml')

    for cmd in cmds:
        futures.append(executor.submit(generate, cmd))
    concurrent.futures.wait(futures)
    for future in futures:
        assert not future.exception()
