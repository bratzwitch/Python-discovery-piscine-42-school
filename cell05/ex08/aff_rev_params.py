#!/usr/bin/env python3

import sys

lenpar = len(sys.argv)

if(lenpar > 2):
    while(lenpar != 1):
        print(sys.argv[lenpar - 1])
        lenpar -= 1
else:
    print("none")