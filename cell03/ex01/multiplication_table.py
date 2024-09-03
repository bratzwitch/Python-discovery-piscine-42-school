#!/usr/bin/env python3

table = 0
print("Enter a number")
num = int(input())
while(table <= 9):
    print(table,"x",num,"=",table * num)
    table += 1