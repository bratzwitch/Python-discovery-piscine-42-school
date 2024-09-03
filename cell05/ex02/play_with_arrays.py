#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
print(array)
new = array
array[:] = [x + 2 for x in array]
new_filtered = [x for x in new if x > 5]
print(new_filtered)