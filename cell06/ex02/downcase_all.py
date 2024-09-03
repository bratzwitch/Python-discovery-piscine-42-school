#!/usr/bin/env python3

import sys

def downcase_it(word):
    return word.lower()

if(len(sys.argv) > 1):
    i = 1
    while(i < len(sys.argv)):
        str = downcase_it(sys.argv[i])
        print(str)
        i += 1
else:
    print("none")