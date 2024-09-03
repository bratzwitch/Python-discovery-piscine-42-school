#!/usr/bin/env python3

import sys

if(len(sys.argv) == 2):
    target = sys.argv[1]
    test = input("What was the parameter? ")
    if(test == target):
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")