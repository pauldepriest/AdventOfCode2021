#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""



f1 = open("day8.txt",'r')
indata = f1.readlines()
f1.close()

data = []

for i in indata:
    part1,part2 = i.split('|')
    data.append([part1,part2[0:len(part2)-1]])

numbers = [0,0,0,0]

for i in data:
    for j in i[1].split() :
        count = len(j)
        if count == 2 :
            numbers[0] += 1
        elif count == 3 :
            numbers[2] += 1
        elif count == 4 :
            numbers[1] += 1
        elif count == 7 :
            numbers[3] += 1

total = 0

for x in numbers:
    total += x
    
print(total)
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    