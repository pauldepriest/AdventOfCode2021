#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import numpy
from heapq import heappop, heappush






f1 = open("day17.txt",'r')
indata = f1.readlines()
f1.close()

data = indata[0].strip()

xtmin,xtmax = [int(l) for l in data[data.find('=')+1:data.find(',')].split('..')]
ytmin,ytmax = [int(l) for l in data[data.find('y=')+2:].split('..')]


xpos = 0
ypos = 0
totalymax = -100
solutions = 0
for rx0 in range(15,200,1):
    for ry0 in range(-100,300,1):
        xpos = 0
        ypos = 0
        rx = rx0
        ry = ry0
        ymax = -100
        while True:
            xpos += rx
            ypos += ry
            ymax = max(ymax,ypos)
            if rx > 0:
                rx += -1
            ry += -1
            if xtmin <= xpos <=xtmax and ytmin <= ypos <= ytmax:
                totalymax = max(totalymax,ymax)
                solutions += 1
                break
            if xpos > xtmax or ypos < ytmin:
                break
print(totalymax,solutions)




