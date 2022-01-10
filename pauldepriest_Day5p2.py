#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import numpy

f1 = open("day5.txt",'r')
indata = f1.readlines()
f1.close()

ocean = numpy.zeros((1000,1000),dtype=int)

lines = []

for i in indata:
    point1, trash, point2 = i.split()
    x1,y1 = point1.split(',')
    x2,y2 = point2.split(',')
    lines.append([int(x1),int(y1),int(x2),int(y2)])

xmax = 0
ymax = 0
for x1,y1,x2,y2 in lines:
    xmax = max(xmax,x1,x2)
    ymax = max(ymax,y1,y2)
    
print(xmax,ymax)


for x1,y1,x2,y2 in lines:
    print(x1,y1,x2,y2)
    if x1 == x2 :
        if y1 > y2 :
            temp = y1
            y1 = y2
            y2 = temp
        for y in range(y1,y2+1,1):
            ocean[x1,y] += 1
    elif y1 == y2 :
        if x1 > x2:
            temp = x1
            x1 = x2
            x2 = temp
        for x in range(x1,x2+1,1):
            ocean[x,y1] += 1
    elif (x1 == x2) and (y1 == y2):
        ocean[x1,y1] += 1
    else:
        xline = x2 - x1
        yline = y2 - y1
        xslope = 1
        yslope = 1
        if xline < 0 :
            xslope = -1
        if yline < 0 :
            yslope = -1
        x = x1
        y = y1
        for xinc in range(0,abs(xline)+1,1):
            ocean[x,y] += 1
            x += xslope
            y += yslope
            

total = 0

for x in range (0,1000,1):
    for y in range(0,1000,1):
        if ocean[x,y] > 1:
            total += 1

print(total)
            
    



               