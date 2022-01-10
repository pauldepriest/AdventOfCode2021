#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""
from collections import defaultdict


f1 = open("day8.txt",'r')
indata = f1.readlines()
f1.close()

data = []

for i in indata:
    part1,part2 = i.split('|')
    data.append([part1,part2[0:len(part2)-1]])



numbers = [[0,1,2,4,5,6],[2,5],[0,2,3,4,6],[0,2,3,5,6],[1,2,3,5],[0,1,3,5,6],[0,1,3,4,5,6],[0,2,5],[0,1,2,3,4,5,6],[0,1,2,3,5,6]] 

all = 'abcdefg'
values = [list(all),list(all),list(all),list(all),list(all),list(all),list(all)]
    
answer = 0

for p1,p2 in data:
    d = p1.split()
    values = [list(all),list(all),list(all),list(all),list(all),list(all),list(all)]
    ex = [[],[],[],[],[],[],[],[]]
    for i in d:
        ex[len(i)].extend(sorted(list(i)))
    L = len(values[2])
    for i in range(L-1,-1,-1):
        print(i)
        if not (values[2][i] in ex[2]) :
            values[2].pop(i)
            values[5].pop(i)
    
    for i in (0,1,3,4,6):
        for j in ex[2]:
            values[i].remove(j)
    # process three segment number
    for i in ex[3]:
        if not (i in values[2]):
            for j in range(len(values[0])-1,-1,-1):
                if values[0][j] != i:
                    values[0].pop(j)
    for i in (1,3,4,6):
        values[i].remove(values[0][0])
    # process four segment number
    keep = []
    print(values[5])
    for i in ex[4]:
        if i not in values[2] :
            keep.append(i)
    for i in range(len(values[1])-1,-1,-1):
        if values[1][i] not in keep:
            values[1].pop(i)
            values[3].pop(i)
    for i in keep:
        for j in range(len(values[4])-1,-1,-1):
            if i == values[4][j] :
                values[4].pop(j)
                values[6].pop(j)
    #process 5 segment numbers
    parts = []
    for i in (0,5,10):
        letters = ex[5][i] + ex[5][i+1] + ex[5][i+2] + ex[5][i+3] + ex[5][i+4]
        print(letters)
        n = []
        if values[0][0] in letters:
            n.append([0])
        if values[1][0] in letters and values[1][1] in letters:
            n.append([1])
            n.append([3])
        elif values[1][0] in letters or values[1][1] in letters:
            n.append([1,3])
        if values[2][0] in letters and values[2][1] in letters:
            n.append([2])
            n.append([5])
        elif values[2][0] in letters or values[2][1] in letters:
            n.append([2,5])
        if values[4][0] in letters and values[4][1] in letters:
            n.append([4])
            n.append([6])
        elif values[4][0] in letters or values[4][1] in letters:
            n.append([4,6])
        print(n)
        for a0 in range(0,len(n[0]),1):
            for a1 in range(0,len(n[1]),1):
                for a2 in range(0,len(n[2]),1):
                    for a3 in range(0,len(n[3]),1):
                        for a4 in range(0,len(n[4]),1):
                            guess = [n[0][a0],n[1][a1],n[2][a2],n[3][a3],n[4][a4]]
                            guess = sorted(guess)
                            if guess in numbers:
                                parts.append([guess,letters])
    for g,letters in parts:
        if g[1] == 1:
            if values[5][0] in letters:
                values[5].pop(1)
                values[2].pop(0)
            else:
                values[5].pop(0)
                values[2].pop(1)
            if values[6][0] in letters:
                values[6].pop(1)
                values[4].pop(0)
            else:
                values[6].pop(0)
                values[4].pop(1)
        elif g[3] == 4:
            if values[3][0] in letters:
                values[3].pop(1)
                values[1].pop(0)
            else:
                values[3].pop(0)
                values[1].pop(1)
                
    code = defaultdict(int)
    for i in range(0,7,1):
        code[values[i][0]] =  i
    n = '' 
    for num in p2.split():
        print(num)
        m = []
        for i in num:
            m.append(code[i])
        n += str(numbers.index(sorted(m)))
    answer += int(n)
        
        
        
        
print(answer)
        
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    