#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""



f1 = open("day7.txt",'r')
indata = f1.readlines()
f1.close()

crabs = []

for i in indata[0].split(','):
    crabs.append(int(i))

crabmin = crabs[0]
crabmax = crabs[0]

for i in crabs:
    crabmin = min(crabmin, i)
    crabmax = max(crabmax, i)
    
print(crabmin,crabmax)

first = True

fuelmin = 0


for loc in range(crabmin,crabmax+1, 1):
    fuel = 0
    for crab in crabs:
        distance = abs(crab - loc)
        cost = (distance*(distance+1))/2
        fuel += cost
    print(first,loc,fuel)
    if not first:
        if fuelmin > fuel:
            fuelmin = fuel
            location = loc
    else:
        first = False
        fuelmin = fuel
        location = loc
    print(first,loc,fuel,location,fuelmin)    
print(location,fuelmin)
        
