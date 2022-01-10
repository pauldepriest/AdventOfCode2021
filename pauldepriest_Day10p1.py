#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""



f1 = open("day10.txt",'r')
indata = f1.readlines()
f1.close()

data = []

total = 0

osym = ['(','[','{','<']
csym = [')',']','}','>']
val = [3,57,1197,25137]

scores = []



for i in indata:
    data.append(i[0:-1])
    
for row in data:
    s = []
    good = True
    for r in row:
        if r in osym:
            s.append(r)
        else:
            c = csym.index(r)
            if len(s) > 0:
                top = osym.index(s[-1])
                if top == c :
                    s.pop(-1)
                else:
                    total += val[c]
                    good = False
        if not good:
            break
        
            

print(total)