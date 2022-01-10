#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import numpy
from heapq import heappop, heappush

def spin():
    global dice, spincount
    dice += 1
    if dice == 101:
        dice = 1
    spincount += 1
    if spincount < 110:
        print(dice,spincount)
    return dice
    
def move(p,a):
    ans = (p + a) % 10
    if ans == 0:
        ans = 10
    return ans
    






f1 = open("day21.txt",'r')
indata = f1.readlines()
f1.close()

pos1 = int(indata[0].split(':')[1])
pos2 = int(indata[1].split(':')[1])

dice = 0
spincount = 0

score1 = 0
score2 = 0



while True:
    #player 1 move
    m = spin() + spin() + spin()
    pos1 = move(pos1,m)
    score1 += pos1
    if score1 >= 1000:
        break
    #player 2 move
    m = spin() + spin() + spin()
    pos2 = move(pos2,m)
    score2 += pos2
    if score2 >= 1000:
        break
    
    
print(spincount,score1,score2)


pos1 = int(indata[0].split(':')[1])
pos2 = int(indata[1].split(':')[1])

pos1 -= 1
pos2 -= 1
saved = {} #saved game state

def countwins(p1,p2,s1,s2):
    if s1 >= 21:
        return (1,0)
    if s2 >= 21:
        return (0,1)
    if (p1,p2,s1,s2) in saved:
        return saved[(p1,p2,s1,s2)]
    ans = (0,0)
    for dice1 in [1,2,3]:
        for dice2 in [1,2,3]:
            for dice3 in [1,2,3]:
                newp1 = (p1 + dice1 + dice2 + dice3)%10
                news1 = s1 + newp1 + 1
                x1,y1 = countwins(p2,newp1,s2,news1)
                ans = (ans[0]+y1,ans[1]+x1)
    saved[(p1,p2,s1,s2)] = ans
    return ans
answer = countwins(pos1,pos2,0,0)

print(max(answer))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



