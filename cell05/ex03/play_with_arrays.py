#!/usr/bin/env python

arr =  [2, 8, 9, 48, 8, 22, -12, 2]
keep = set()

for i in arr:
    if i > 5:
        i += 2
        keep.add(i)

print(arr)
print(keep)