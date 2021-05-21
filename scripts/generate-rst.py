#!/usr/bin/env python3

import argparse
import concurrent.futures
import os
import shutil
import subprocess

parser = argparse.ArgumentParser(description='Convert XML files to RST')
parser.add_argument('xml_dir', help='Directory with XML files')
parser.add_argument('output', help='Output directory')
args = parser.parse_args()

shutil.rmtree(args.output, ignore_errors=True)
os.mkdir(args.output)
shutil.copy('templates/baseconf.py', args.output)
shutil.copy('templates/Makefile.root', os.path.join(args.output, 'Makefile'))


def generate(xml):
    base, _ = os.path.splitext(xml)
    outdir = os.path.join(args.output, base)
    cmd = f'../texi2rst.py {args.xml_dir}/{xml} -o {outdir}'
    if xml == 'install.xml':
        cmd += ' --default-language=bash'
    subprocess.check_output(cmd, shell=True, encoding='utf8')
    config = f'templates/{base}/conf.py'
    shutil.copy(config, os.path.join(args.output, base))
    shutil.copy('templates/Makefile', outdir)
    shutil.copy('templates/gnu_free_documentation_license.rst', outdir)
    shutil.copy('templates/gpl-3.0.rst', outdir)
    shutil.copy('templates/funding.rst', outdir)
    with open(os.path.join(args.output, base, 'index.rst'), 'w') as w:
        w.write(open('templates/index.rst').read().replace('__doc__', base))


with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = []
    for xml in os.listdir(args.xml_dir):
        futures.append(executor.submit(generate, xml))
    concurrent.futures.wait(futures)
    for future in futures:
        ex = future.exception()
        if ex:
            raise ex
