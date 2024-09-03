#!/usr/bin/env python3

import sys

lenpar = len(sys.argv) - 1

if(lenpar == 2):
    first = int(sys.argv[1])
    second = int(sys.argv[2])
    res = list(range(first,second + 1))
    print(res)
else:
    print("none")