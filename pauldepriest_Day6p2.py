#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""



f1 = open("day6.txt",'r')
indata = f1.readlines()
f1.close()

fishes = []

for i in indata[0].split(','):
    fishes.append(int(i))

fish = [0,0,0,0,0,0,0,0,0]
fishcount = 0

for i in fishes:
    fish[i] += 1
    fishcount += 1

print(fishcount)

for day in range(0,256,1):
    newfish = fish[0]
    fishcount += newfish
    for i in range(1,9,1):
        fish[i-1] = fish[i]
    fish[8] = newfish
    fish[6] += newfish
    print(day,fish,fishcount)
        
      
print(fishcount)
print(fish)
total = 0
for i in fish:
    total += i
    
print(total)

               