#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import numpy
from heapq import heappop, heappush

def getnumber(im,a,b):
    if a == 0 and b==0:
        ans = str(im[a,b]) + str(im[a,b]) + str(im[a,b+1])
        ans = ans + str(im[a,b]) + str(im[a,b]) + str(im[a,b+1])
        ans = ans + str(im[a+1,b]) + str(im[a+1,b]) + str(im[a+1,b+1])
        print(a,b,int(ans,2))
        return int(ans,2)
    elif a == 0 and b == (yimage-1):
        ans = str(im[a,b-1]) + str(im[a,b]) + str(im[a,b])
        ans = ans + str(im[a,b-1]) + str(im[a,b]) + str(im[a,b])
        ans = ans + str(im[a+1,b-1]) + str(im[a+1,b]) + str(im[a+1,b])
        print(a,b,int(ans,2))
        return int(ans,2)
    elif a == (ximage-1) and b == 0:
        ans = str(im[a-1,b]) + str(im[a-1,b]) + str(im[a-1,b+1])
        ans = ans + str(im[a,b]) + str(im[a,b]) + str(im[a,b+1])
        ans = ans + str(im[a,b]) + str(im[a,b]) + str(im[a,b+1])
        print(a,b,int(ans,2))
        return int(ans,2)
    elif a == (ximage-1) and b == (yimage-1):
        ans = str(im[a-1,b-1]) + str(im[a-1,b]) + str(im[a-1,b])
        ans = ans + str(im[a,b-1]) + str(im[a,b]) + str(im[a,b])
        ans = ans + str(im[a,b-1]) + str(im[a,b]) + str(im[a,b])
        print(a,b,int(ans,2))
        return int(ans,2)
    elif a == 0:
        ans = str(im[a,b-1]) + str(im[a,b]) + str(im[a,b+1])
        ans = ans + str(im[a,b-1]) + str(im[a,b]) + str(im[a,b+1])
        ans = ans + str(im[a+1,b-1]) + str(im[a+1,b]) + str(im[a+1,b+1])
        print(a,b,int(ans,2))
        return int(ans,2)
    elif a == (ximage-1):
        ans = str(im[a-1,b-1]) + str(im[a-1,b]) + str(im[a-1,b+1])
        ans = ans + str(im[a,b-1]) + str(im[a,b]) + str(im[a,b+1])
        ans = ans + str(im[a,b-1]) + str(im[a,b]) + str(im[a,b+1])
        print(a,b,int(ans,2))
        return int(ans,2)
    elif b == 0:
        ans = str(im[a-1,b]) + str(im[a-1,b]) + str(im[a-1,b+1])
        ans = ans + str(im[a,b]) + str(im[a,b]) + str(im[a,b+1])
        ans = ans + str(im[a+1,b]) + str(im[a+1,b]) + str(im[a+1,b+1])
        print(a,b,int(ans,2))
        return int(ans,2)
    elif b == (yimage-1):
        ans = str(im[a-1,b-1]) + str(im[a-1,b]) + str(im[a-1,b])
        ans = ans + str(im[a,b-1]) + str(im[a,b]) + str(im[a,b])
        ans = ans + str(im[a+1,b-1]) + str(im[a+1,b]) + str(im[a+1,b])
        print(a,b,int(ans,2))
        return int(ans,2)
    else:
        ans = str(im[a-1,b-1]) + str(im[a-1,b]) + str(im[a-1,b+1])
        ans = ans + str(im[a,b-1]) + str(im[a,b]) + str(im[a,b+1])
        ans = ans + str(im[a+1,b-1]) + str(im[a+1,b]) + str(im[a+1,b+1])
        return int(ans,2)




f1 = open("day20.txt",'r')
indata = f1.readlines()
f1.close()

data = []

for i in indata:
    data.append(i.strip())

enhance = data[0]
passes = 50
xsize = len(data[2])
ysize = len(data) - 2
ximage = ysize + 6*passes
yimage = xsize + 6*passes
image1 = numpy.zeros((ximage,yimage),dtype=int)
image2 = numpy.zeros((ximage,yimage),dtype=int)
x = 3*passes
y = 3*passes
for i in range(2,len(data),1):
    for j in range(0,len(data[i]),1):
        if data[i][j] == '#' :
            image1[x,y] = 1
        y += 1
    x += 1
    y = 3*passes

for p in range(0,passes,1):
    for x in range(0,ximage,1):
        for y in range(0,yimage,1):
            index = getnumber(image1,x,y)
            if enhance[index] == '#':
                val = 1
            else:
                val = 0
            image2[x,y] = val
    print(image2)
    for x in range(0,ximage,1):
        for y in range(0,yimage,1):
            image1[x,y] = image2[x,y]
    image2 = numpy.zeros((ximage,yimage),dtype=int)



       
count = 0

for x in range(0,ximage,1):
    for y in range(0,yimage,1):
        count += image1[x,y]


print(count)
                
                


