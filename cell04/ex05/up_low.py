#!/usr/bin/env python3

res = str(input())
for char in res:
    if char.isupper():
        print(f"{char.lower()}", end="")
    elif char.islower():
        print(f"{char.upper()}", end="")