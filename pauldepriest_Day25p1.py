#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import numpy
from heapq import heappop, heappush
from collections import defaultdict







f1 = open("day25.txt",'r')
indata = f1.readlines()
f1.close()


data = []

for line in indata:
    row = line.strip()
    data.append(list(row))

R = len(data)

C = len(data[0])

count = 0
print(data)
while True:
    count += 1
    moved = False
    data2 = [[data[r][c] for c in range(0,C,1)] for r in range(0,R,1)]
    
    for r in range(0,R,1):
        for c in range(0,C,1):
            if data[r][c] == '>':
                if data[r][(c+1)%C] == '.':
                    data2[r][(c+1)%C] = '>'
                    data2[r][c] = '.'
                    moved = True
    data3 = [[data2[r][c] for c in range(0,C,1)] for r in range(0,R,1)]
    
    for r in range(0,R,1):
        for c in range(0,C,1):
            if data2[r][c] == 'v':
                if data2[(r+1)%R][c] == '.':
                    data3[(r+1)%R][c] = 'v'
                    data3[r][c] = '.'
                    moved = True
    if not moved:
        print(count)
        break
    
    
    data = [[data3[r][c] for c in range(0,C,1)] for r in range(0,R,1)]
#    print(count)
#    for r in range(0,R,1):
#        row = ''
#        for c in range(0,C,1):
#            row += data[r][c]
#        print(row)
    
print(count)                    
    