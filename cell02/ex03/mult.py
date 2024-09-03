#!/usr/bin/env python3

print("Enter the first number:")
first_num = int(input())
print("Enter the second number:")
second_num = int(input())
result = first_num * second_num
print(first_num,"x",second_num,"=",result)
if result > 0:print("The number is positive.")
elif result == 0:print("The number is positive and negative.")
else:print("The number is negative.")