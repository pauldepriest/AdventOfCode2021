#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

f1 = open("day2.txt",'r')
indata = f1.readlines()
f1.close()

position = 0

depth = 0

for i in indata:
    direction, j = i.split(' ')
    k = int(j)
    if direction == "forward" :
        position += k
    elif direction == "down" :
        depth += k
    elif direction == "up" :
        depth -= k
    else :
        print("invalid input")

answer = position * depth

print("answer is ", answer)

    
position = 0
aim = 0
depth = 0

for i in indata:
    direction, j = i.split(' ')
    k = int(j)
    if direction == "forward" :
        position += k
        depth = depth + aim * k
    elif direction == "down" :
        aim += k
    elif direction == "up" :
        aim -= k
    else :
        print("invalid input")

answer = position * depth

print("answer is ", answer)
