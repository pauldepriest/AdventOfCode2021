#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

f1 = open("day1.txt",'r')
indata = f1.readlines()
f1.close()

icount = 0
for i in range(0,len(indata)-1,1):
    if int(indata[i]) < int(indata[i+1]) :
        icount += 1
        
print("answer is", icount)

# Part 2

sums = []
for i in range(0,len(indata)-2,1):
    s = int(indata[i]) + int(indata[i+1]) + int(indata[i+2])
    sums.append(s)
    
print("length of sums is", len(sums))


icount = 0

for i in range(0,len(sums)-1,1):
    if sums[i] < sums[i+1] :
        icount += 1




print("answer is ", icount)

