#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import numpy
from heapq import heappop, heappush
from collections import defaultdict


def checkoverlap(b1,b2):
    xl1,xh1,yl1,yh1,zl1,zh1 = b1
    xl2,xh2,yl2,yh2,zl2,zh2 = b2
    if xl1 > xh2 or xl2 > xh1:
        return tuple()
    elif yl1 > yh2 or yl2 > yh1:
        return tuple()
    elif zl1 > zh2 or zl2 > zh1:
        return tuple()
    else:
        ans = (max(xl1,xl2),min(xh1,xh2),max(yl1,yl2),min(yh1,yh2),max(zl1,zl2),min(zh1,zh2))
        return ans
  






f1 = open("day22.txt",'r')
indata = f1.readlines()
f1.close()

boxes = []

for line in indata:
    line = line.strip()
    t,x,y,z = line.split('=')
    if t[2] =='f':
        s = 0
    else:
        s = 1
    xl,xh = [int(l) for l in x[0:-2].split('..')]
    yl,yh = [int(l) for l in y[0:-2].split('..')]
    zl,zh = [int(l) for l in z.split('..')]
    
    boxes.append([s,xl,xh,yl,yh,zl,zh])
    
cubes = set()

for box in boxes:
    s,xl,xh,yl,yh,zl,zh = box
    if xl >= -50 and xh <= 50 and yl >= -50 and yh <= 50 and zl >= -50 and zh <= 50:
        for x in range(xl,xh+1,1):
            for y in range(yl,yh+1,1):
                for z in range(zl,zh+1,1):
                    if s == 1:
                        cubes.add((x,y,z))
                    else:
                        cubes.discard((x,y,z))


print(len(cubes))

cubes = defaultdict(int)

for box in boxes:
    s,xl,xh,yl,yh,zl,zh = box
    newcube = (xl,xh,yl,yh,zl,zh)
    newcubes = defaultdict(int)
    for c in cubes:
        overlap = checkoverlap(newcube,c)
        if len(overlap) > 0:
            newcubes[overlap] -= cubes[c]
    if s == 1:
        cubes[newcube] += 1
    for c in newcubes:
        cubes[c] += newcubes[c]
        
        
total = 0

for c in cubes:
    total += (c[1]-c[0]+1)*(c[3]-c[2]+1)*(c[5]-c[4]+1)*cubes[c]

print(total)

            
            
                        
    