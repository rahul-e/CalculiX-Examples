#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

for contact in ('tie', 'pc-ss'):
    os.system("param.py par.pre.fbd contact=\"'"+contact+"'\"")
    os.system("cgx -b par.pre.fbd")
    os.system("ccx Tjoint")
    os.system("cgx -b post.fbd")
