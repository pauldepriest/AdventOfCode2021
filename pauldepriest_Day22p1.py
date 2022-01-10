#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import numpy
from heapq import heappop, heappush

    





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
                        
    