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

print(risk)