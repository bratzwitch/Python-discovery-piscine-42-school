#!/usr/bin/env python3

import sys

if(len(sys.argv) == 2):
    main = sys.argv[1]
    count = 0
    start = 0
    for i in range(len(main)):
        j = main.find("z",start)
        if(j != -1):
            start = j + 1
            count += 1
    while(count > 0):
        print("z",end="")
        count -= 1
    print()
else:
    print("none")