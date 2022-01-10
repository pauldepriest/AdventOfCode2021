#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import numpy
from heapq import heappop, heappush

def get_neighbor(r,c):
    return [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]


f1 = open("day15.txt",'r')
indata = f1.readlines()
f1.close()

a = indata[0]

data = [[int(l) for l in line.strip()] for line in indata]

rowmax = len(data)
colmax = len(data[0])
locked = set()
queue = [(0,(0,0))]


while queue:
    risk,pos = heappop(queue)
    if pos == (rowmax-1,colmax-1) :
        break
    if pos in locked:
        continue
    locked.add(pos)
    for r,c in get_neighbor(*pos):
        if 0 <= r < rowmax and 0 <= c < colmax :
            heappush(queue,(risk + data[r][c],(r,c)))

print("part 1 answer",risk)


rowmax2 = rowmax*5
colmax2 = colmax*5

data2 = [[0]*colmax2 for _ in range(rowmax2)]

for r2 in range(0,rowmax2,1):
    for c2 in range(0,colmax2,1):
        r = r2 % rowmax
        c = c2 % colmax
        val = data[r][c]
        val = val + r2//rowmax + c2//colmax
        if val > 9:
            val = val - 9
        data2[r2][c2] = val

locked = set()
queue = [(0,(0,0))]


while queue:
    risk,pos = heappop(queue)
    if pos == (rowmax2-1,colmax2-1) :
        break
    if pos in locked:
        continue
    locked.add(pos)
    for r,c in get_neighbor(*pos):
        if 0 <= r < rowmax2 and 0 <= c < colmax2 :
            heappush(queue,(risk + data2[r][c],(r,c)))

print("part 2 answer",risk)














