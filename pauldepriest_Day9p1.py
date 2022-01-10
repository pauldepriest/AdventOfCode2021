#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import numpy

f1 = open("day9.txt",'r')
indata = f1.readlines()
f1.close()

ocean = numpy.zeros((100,100),dtype=int)
basin = numpy.zeros((100,100),dtype=int)

for row in range(0,100,1):
    for column in range(0,100,1):
        ocean[column,row] = int(indata[row][column])

total = 0
basins = []

for row in range(0,100,1):
    for column in range(0,100,1):
        val = ocean[column,row]
        if (row > 0) and (column > 0) and (row < 99) and (column < 99) :
            if (val < ocean[column-1,row]) and (val < ocean[column+1,row]) and (val < ocean[column,row-1]) and (val < ocean[column,row+1]) :
                # local min found
                total += val + 1
                basins.append([colum,row,0])
        elif (row == 0) and (column > 0) and (column < 99) :
            if (val < ocean[column-1,row]) and (val < ocean[column+1,row]) and (val < ocean[column,row+1]):
                total += val + 1
                basins.append([colum,row,0])
        elif (row > 0) and (row < 99) and (column == 0) :
            if (val < ocean[column+1,row]) and (val < ocean[column,row-1]) and (val < ocean[column,row+1]) :
                total += val + 1
                basins.append([colum,row,0])
        elif (row == 99) and (column > 0) and (column < 99) :
            if (val < ocean[column-1,row]) and (val < ocean[column+1,row]) and (val < ocean[column,row-1]) :
                total += val + 1
                basins.append([colum,row,0])
        elif (row > 0) and (row < 99) and (column == 99) :
            if (val < ocean[column-1,row]) and (val < ocean[column,row-1]) and (val < ocean[column,row+1]) :
                total += val + 1
                basins.append([colum,row,0])
        elif (row == 0) and (column == 0) :
            if (val < ocean[column+1,row]) and (val < ocean[column,row+1]) :
                total += val + 1
                basins.append([colum,row,0])
        elif (row == 0) and (column == 99) :
            if (val < ocean[column-1,row]) and (val < ocean[column,row+1]) :
                total += val + 1
                basins.append([colum,row,0])
        elif (row == 99) and (column == 0) :
            if (val < ocean[column+1,row]) and (val < ocean[column,row-1]) :
                total += val + 1
                basins.append([colum,row,0])
        elif (row == 99) and (column == 99) :
            if (val < ocean[column-1,row]) and (val < ocean[column,row-1]) :
                total += val + 1
                basins.append([colum,row,0])


print(total)
            
    








