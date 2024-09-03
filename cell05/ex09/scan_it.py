#!/usr/bin/env python3

import sys

if(len(sys.argv) == 3):
    target = sys.argv[1]
    search = sys.argv[2]
    count = search.count(target)
    if(count > 0):
        print(count)
    else:
        print("none")
else:
    print("none")