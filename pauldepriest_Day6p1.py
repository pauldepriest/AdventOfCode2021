#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""



f1 = open("day6.txt",'r')
indata = f1.readlines()
f1.close()

fish = []

for i in indata[0].split(','):
    fish.append(int(i))
    

for day in range(0,80,1):
    t = len(fish)
    for i in range(0,t,1):
        if fish[i] > 0:
            fish[i] = fish[i] -1
        else:
            fish[i] = 6
            fish.append(8)
            
print(len(fish))


               