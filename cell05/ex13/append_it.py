#!/usr/bin/env python3

import sys

lenpar = len(sys.argv)

if(lenpar > 1):
    i = 1
    while(i < lenpar):
        com = sys.argv[i]
        match com:
            case _ if com.endswith("ism"):
                i += 1
            case _:
                print(f"{com}ism")
                i += 1
        
else:
    print("none")