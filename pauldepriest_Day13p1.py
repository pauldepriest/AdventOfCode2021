#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import numpy


f1 = open("day13.txt",'r')
indata = f1.readlines()
f1.close()

for i in range(0,len(indata),1):
    indata[i] = indata[i][0:-1]
    
print(indata)

folds = []
data = []

for i in indata:
    if len(i) < 3:
        continue
    elif i[0] == 'f' :
        direction,val = i.split('=')
        folds.append([direction[-1],int(val)])
    else:
        x,y = i.split(',')
        data.append([int(x),int(y)])

        
#print(folds,data)

xmax = 0
xmin = 1000000
ymax = 0
ymin = 1000000

for x,y in data:
    xmin = min(x,xmin)
    xmax = max(x,xmax)
    ymin = min(y,ymax)
    ymax = max(y,ymax)

print(xmin,xmax,ymin,ymax)


for i in range(0,1,1):
    d,val = folds[i]
    newdata = []
    if d == 'x' :
        for i in range(0,len(data),1):
            x,y = data[i]
            if x > val :
                x = val*2 - x
                if [x,y] not in data:
                    newdata.append([x,y])
        for i in range(len(data)-1,-1,-1):
            x,y = data[i]
            if x  > val:
                data.pop(i)
        if len(newdata) > 0:
            data.extend(newdata)

print(len(data))


