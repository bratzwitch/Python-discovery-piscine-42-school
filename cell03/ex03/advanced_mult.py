#!/usr/bin/env python3

import sys

if(len(sys.argv) == 1):
    table = 0
    mult = 0
    while(table <= 10):
        print("Table of",table,":",end = " ")
        while(mult <= 10):
            print(table * mult,end = " ")
            mult += 1
        table += 1
        mult = 0
        print("")    
else:
    print("none")