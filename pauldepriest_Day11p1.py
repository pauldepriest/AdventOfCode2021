#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import numpy
from scipy import ndimage

f1 = open("day11.txt",'r')
indata = f1.readlines()
f1.close()

ocean = numpy.zeros((10,10),dtype=int)
done = numpy.zeros((10,10),dtype=int)

for row in range(0,10,1):
    for column in range(0,10,1):
        ocean[row,column] = int(indata[row][column])

counter = 0

for days in range(0,100,1):
    # add one to all values
    for x in range(0,10,1):
        for y in range(0,10,1):
            ocean[x,y] += 1
    # process nines until all done
    nines = True
    while nines:
        no_nines = True
        for x in range(0,10,1):
            for y in range(0,10,1):
                if (ocean[x,y] > 9) and (done[x,y] == 0) :
                    for xx in range(max(0,x-1),min(9,x+1)+1,1):
                        for yy in range(max(0,y-1),min(9,y+1)+1,1):
                            ocean[xx,yy] += 1
                    no_nines = False
                    done[x,y] = 1
        if no_nines:
            nines = False
            done = numpy.zeros((10,10),dtype=int)
    # convert nines to zores and increment counter
    
    for x in range(0,10,1):
        for y in range(0,10,1):
            if ocean[x,y] > 9:
                ocean[x,y] = 0
                counter += 1

print(counter)
print(ocean)





