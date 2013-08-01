#!/usr/local/bin/python3
# Linux only!
import os
import os.path
import sys
import re

global _gen

def GetAllProcs():
    return [tup for tup in GetProcs()]

def GetFirstProc():
    global _gen
    
    _gen = _GetProcsEx()
    return next(_gen,False)

def GetNextProc():
    global _gen
    return next(_gen,False)

def _GetProcsEx():
    dir = '/proc'
    for pid in os.listdir(dir):
        if not re.match(r'\d+',pid): continue
        full_name = os.path.join(dir, pid)+'/cmdline'
        try:
            cmdline = open(full_name).read() 
        except OSError as err:
            # Probably permissions
            print('open',err)
            cmdline = None
        full_name = os.path.join(dir, pid)+'/stat'
        try:
            stat = open(full_name).read() 
            ppid = stat.split()[3]
        except OSError as err:
            # Probably permissions
            print('open',err)
            ppid = None
        yield (pid,ppid,cmdline)

