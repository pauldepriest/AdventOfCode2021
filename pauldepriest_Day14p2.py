#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import numpy
from collections import Counter


f1 = open("day14.txt",'r')
indata = f1.readlines()
f1.close()

for i in range(0,len(indata),1):
    indata[i] = indata[i][0:-1]
    
print(indata)

template = list(indata[0])
rules = {}

for i in indata[2:]:
    a,b = i.split(' -> ')
    rules.setdefault(a,b)
for r in range(0,10,1):
    
    for i in range(len(template)-1,0,-1):
        pair = template[i-1]+template[i]
        new = rules[pair]
        template.insert(i,new)
    #print(r+1,template)


print(len(template))

counts =[]

cc = Counter(template)
print(cc)

data = sorted(template)

current = data[0]
count = 1

for c in data[1:]:
    if c == current :
        count += 1
    else:
        print(current,count)
        counts.append(count)
        count = 1
        current = c
        
counts.append        

scounts = sorted(counts)

print(scounts[len(scounts)-1] - scounts[0])

#part 2

template = list(indata[0])

pairs = Counter()

for i in range(0,len(template)-1,1):
    pair = template[i] + template[i+1]
    pairs[pair] += 1

print(pairs)

for n in range(0,40):
    pairs2 = Counter()
    for p in pairs:
        pairs2[p[0]+rules[p]] += pairs[p]
        pairs2[rules[p]+p[1]] += pairs[p]
    pairs = pairs2
    
tots = Counter()
for p in pairs:
    tots[p[0]] += pairs[p]
    
tots[template[-1]] += 1

print(max(tots.values()) - min(tots.values()))

    
    







        