#!/bin/python3

import sys


n = int(input().strip())
inp = [int(i) for i in input().strip().split()]
p = n = z = 0
for i in inp:
    if i<0:
        n += 1
    elif i>0:
        p += 1
    else:
        z += 1
print(p/len(inp))
print(n/len(inp))
print(z/len(inp))
