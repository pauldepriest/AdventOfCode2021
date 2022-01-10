#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import numpy
from heapq import heappop, heappush
from collections import defaultdict







f1 = open("day18.txt",'r')
indata = f1.readlines()
f1.close()

data = []
for line in indata:
    line = line.strip()
    data.append([])
    for c in line:
        if c.isdigit():
            data[-1].append(int(c))
        else:
            data[-1].append(c)

def addtwo(s1,s2):
    s1.insert(0,'[')
    s1.append(',')
    s1.extend(s2)
    s1.append(']')
    return s1

def findnumberleft(start,s):
    for i in range(start-1,0,-1):
        if type(s[i]) == int:
            return i
    return 0

def findnumberright(start,s):
    for i in range(start+1,len(s),1):
        if type(s[i]) == int:
            return i
    return 0




def reduce(s):
    #cond1 represents explosions and cond2 represents splits
    #repeat until both conditions are false
    cond1 = True
    cond2 = True
    
    while cond1 or cond2:
        if cond1:
            cond1 = False
            depth = 0
            for i in range(0,len(s),1):
                if s[i] == '[':
                    depth += 1
                elif s[i] == ']':
                    depth -= 1
                elif type(s[i]) == int and depth >= 5 and s[i+1] == ',' and type(s[i+2]) == int:
                    leftnumber = findnumberleft(i-1,s)
                    rightnumber = findnumberright(i+3,s)
                    if leftnumber != 0:
                        s[leftnumber] += s[i]
                    if rightnumber != 0:
                        s[rightnumber] += s[i+2]
                    s[i] = 0
                    s.pop(i+3)
                    s.pop(i+2)
                    s.pop(i+1)
                    s.pop(i-1)
                    cond1 = True
                    break
        if not cond1:
            if cond2:
                cond2 = False
                for i in range(0,len(s),1):
                    if type(s[i]) == int:
                        if s[i] > 9:
                            cond2 = True
                            cond1 = True
                            a = s[i] // 2
                            b = (s[i] + 1) // 2
                            s.insert(i+1,']')
                            s.insert(i+1,b)
                            s.insert(i+1,',')
                            s[i] = a
                            s.insert(i,'[')
                            break
    return s


def magnitude(s):
    morenumbers = True
    while morenumbers:
        morenumbers = False
        for i in range(0,len(s),1):
            if i+2 >=len(s):
                break
            if type(s[i]) == int and s[i+1] == ',' and type(s[i+2]) == int:
                a = s[i] * 3 + s[i+2] * 2
                s[i] = a
                s.pop(i+3)
                s.pop(i+2)
                s.pop(i+1)
                s.pop(i-1)
                morenumbers = True
                break
    return s
                


sum = data[0].copy()
for i in range(1,len(data),1):
    sum = addtwo(sum,data[i])
    sum = reduce(sum)
    
    
mag = magnitude(sum)

print(mag)  


#part 2

maxmag = 0

for i in range(0,len(data)-1,1):
    print(i)
    for j in range(i+1,len(data),1):
        sum = data[i].copy()
        sum = addtwo(sum,data[j])
        sum = reduce(sum)
        m = magnitude(sum)
        maxmag = max(maxmag,m[0])
        sum = data[j].copy()
        sum = addtwo(sum,data[i])
        sum = reduce(sum)
        m = magnitude(sum)
        maxmag = max(maxmag,m[0])

print(maxmag)






