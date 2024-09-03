#!/usr/bin/env python3

import sys

def shrink(str):
    return str[:8]
def enlarge(str):
    while(len(str) < 8):
        str += "Z"
    return str

if(len(sys.argv) > 1):
    i = 1
    while(i < len(sys.argv)):
        if(len(sys.argv[i]) > 8):
            sys.argv[i] = shrink(sys.argv[i])
        elif(len(sys.argv[i]) < 8):
            sys.argv[i] = enlarge(sys.argv[i])
        print(sys.argv[i])
        i += 1
else:
    print("none")