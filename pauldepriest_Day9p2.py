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
                basins.append([column,row,0])
        elif (row == 0) and (column > 0) and (column < 99) :
            if (val < ocean[column-1,row]) and (val < ocean[column+1,row]) and (val < ocean[column,row+1]):
                total += val + 1
                basins.append([column,row,0])
        elif (row > 0) and (row < 99) and (column == 0) :
            if (val < ocean[column+1,row]) and (val < ocean[column,row-1]) and (val < ocean[column,row+1]) :
                total += val + 1
                basins.append([column,row,0])
        elif (row == 99) and (column > 0) and (column < 99) :
            if (val < ocean[column-1,row]) and (val < ocean[column+1,row]) and (val < ocean[column,row-1]) :
                total += val + 1
                basins.append([column,row,0])
        elif (row > 0) and (row < 99) and (column == 99) :
            if (val < ocean[column-1,row]) and (val < ocean[column,row-1]) and (val < ocean[column,row+1]) :
                total += val + 1
                basins.append([column,row,0])
        elif (row == 0) and (column == 0) :
            if (val < ocean[column+1,row]) and (val < ocean[column,row+1]) :
                total += val + 1
                basins.append([column,row,0])
        elif (row == 0) and (column == 99) :
            if (val < ocean[column-1,row]) and (val < ocean[column,row+1]) :
                total += val + 1
                basins.append([column,row,0])
        elif (row == 99) and (column == 0) :
            if (val < ocean[column+1,row]) and (val < ocean[column,row-1]) :
                total += val + 1
                basins.append([column,row,0])
        elif (row == 99) and (column == 99) :
            if (val < ocean[column-1,row]) and (val < ocean[column,row-1]) :
                total += val + 1
                basins.append([column,row,0])


print(total)

ttt = 0

for row in range(0,100,1):
    for column in range(0,100,1):
        if ocean[column,row] != 9 :
           # find which basin this point is in 
            found = False
            for i in range(0,len(basins),1):
                c,r,t = basins[i]
                if (c == column) and (r == row) :
                    basins[i][2] += 1 
                    ttt += 1
                    found = True
                elif c == column :
                    found = True
                    for y in range(min(r,row),max(r,row)+1,1):
                        if ocean[c,y] == 9 :
                            found = False
                    if found:
                        basins[i][2] += 1
                elif r == row :
                    found = True
                    for x in range(min(c,column),max(c,column)+1,1):
                        if ocean[x,r] == 9 :
                            found = False
                    if found:
                        basins[i][2] += 1
                else:
                    f = [True,True,True,True]
                    found = False
                    fi = 0
                    for x in (min(c,column),max(c,column)):
                        f[fi] = True
                        for y in range(min(r,row),max(r,row)+1,1):
                            if ocean[x,y] == 9:
                                f[fi] = False
                        fi += 1
                    for y in (min(r,row),max(r,row)):
                        f[fi] = True
                        for x in range(min(c,column),max(c,column)+1,1):
                            if ocean[x,y] == 9:
                                f[fi] = False
                        fi += 1
                    
                        
                    if (c < column) and (r < row):
                        if (f[0] and f[3]) or (f[1] and f[2]):
                            basins[i][2] += 1
                            found = True
                    elif (c > column) and (r < row):
                        if (f[0] and f[2]) or (f[1] and f[3]):
                            basins[i][2] += 1
                            found = True
                    elif (c < column) and (r > row):
                        if (f[0] and f[2]) or (f[1] and f[3]):
                            basins[i][2] += 1
                            found = True
                    else:
                        if (f[0] and f[3]) or (f[1] and f[2]):
                            basins[i][2] += 1
                            found = True

                if found:
                    found = False
                    break

total = 0
for i in range(0,len(basins),1):
    total += basins[i][2]

print("points", ttt,len(basins))
for i in range(0,len(basins)-1,1):
    for j in range(i+1,len(basins),1):
        if basins[i][2] < basins[j][2] :
            temp = basins[i][2]
            basins[i][2] = basins[j][2]
            basins[j][2] = temp

tot = 0
for x in range(0,100,1):
    for y in range(0,100,1):
        if ocean[x,y] == 9:
            tot += 1

print("count of nines ",tot)


print(total)



print(basins[0][2]*basins[1][2]*basins[2][2])
                
            
    








