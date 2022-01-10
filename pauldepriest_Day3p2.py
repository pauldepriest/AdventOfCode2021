#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

f1 = open("day3.txt",'r')
indata = f1.readlines()
f1.close()

bits = []
for i in range(0,12,1):
    bits.append([0,0])

print(bits)

for i in indata:
    for j in range(0,12,1):
        if i[j] == '0' :
            bits[j][0] += 1
        else:
            bits[j][1] += 1

gammarate = 0
epsilonrate = 0

for i in range(11,-1,-1):
    if bits[i][0] < bits[i][1] :
        gammarate += pow(2, 11-i)
    else:
        epsilonrate += pow(2, 11-i)

powerrate = gammarate * epsilonrate

print(powerrate)

# Part 2

bit = [0,0]

working = []

for i in indata:
    working.append(i)
    
for k in range(0,12,1):
    if len(working) == 1:
        break
    bit = [0, 0]
    for i in working:
        if i[k] == '0' :
            bit[0] += 1
        else:
            bit[1] += 1
    if bit[1] >= bit[0] :
        keep = '1'
    else:
        keep = '0'
    for j in range(len(working) - 1, -1, -1):
        if working[j][k] != keep:
            working.pop(j)
            
print(working)

oxygen = 0

ans = working[0]

for i in range(11, -1, -1):
    if ans[i] == '1' :
        oxygen += pow(2,11-i)

print(oxygen)
    
    
bit = [0,0]

working = []

for i in indata:
    working.append(i)
    
for k in range(0,12,1):
    print(len(working))
    if len(working) == 1:
        break
    bit = [0, 0]
    for i in working:
        if i[k] == '0' :
            bit[0] += 1
        else:
            bit[1] += 1
    if bit[0] <= bit[1] :
        keep = '0'
    else:
        keep = '1'
    for j in range(len(working) - 1, -1, -1):
        if working[j][k] != keep:
            working.pop(j)
            
print(working)

carbon = 0

ans = working[0]

for i in range(11, -1, -1):
    if ans[i] == '1' :
        carbon += pow(2,11-i)

print(carbon)

print(oxygen * carbon)




