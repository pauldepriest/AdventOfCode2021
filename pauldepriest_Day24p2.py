#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import numpy
from heapq import heappop, heappush
from collections import defaultdict







f1 = open("day24.txt",'r')
indata = f1.readlines()
f1.close()


data = []

for line in indata:
    row = line.strip()
    data.append(row.split())

#def execute(offset,w,x,y,z):
#    global data
#    vars = {'w':w,'x':x,'y':y,'z':z,'c':0}
#    for line in range(offset,len(data),1):
#        if len(data[line]) == 3:
#            inst,a,b = data[line]
#            #print(data[line])
#            if b.isnumeric() or b[0] == '-':
#                vars['c'] = int(b)
#                b = 'c'
#                if vars['c'] < 0:
#                    print(vars['c'])
#            if inst == 'add' :
#                ans = vars[a] + vars[b]
#                vars[a] = ans
#            elif inst == 'mul' :
#                ans = vars[a] * vars[b]
#                vars[a] = ans
#            elif inst == 'div':
#                ans = vars[a] // vars[b]
#                vars[a] = ans
#            elif inst == 'mod' :
#                ans = vars[a] % vars[b]
#                vars[a] = ans
#            elif inst == 'eql' :
#                ans = 0
#                if vars[a] == vars[b] :
#                    ans = 1
#                vars[a] = ans
#            else:
#                print('something is wrong - invalid op code')
#        else:
#            return line, vars['w'],vars['x'],vars['y'],vars['z']
#    return 0, vars['w'],vars['x'],vars['y'],vars['z']
#
#offset,w,x,y,z = execute(1,1,0,0,0)
#print(w,x,y,z,offset)
#offset,w,x,y,z = execute(offset+1,1,x,y,z) 
#print(w,x,y,z,offset)
#offset,w,x,y,z = execute(offset+1,9,x,y,z) 
#print(w,x,y,z,offset)
#offset,w,x,y,z = execute(offset+1,9,x,y,z) 
#print(w,x,y,z)
#offset,w,x,y,z = execute(offset+1,1,x,y,z) 
#print(w,x,y,z)
#offset,w,x,y,z = execute(offset+1,9,x,y,z) 
#print(w,x,y,z)
#offset,w,x,y,z = execute(offset+1,9,x,y,z) 
#print(w,x,y,z)
#offset,w,x,y,z = execute(offset+1,9,x,y,z) 
#print(w,x,y,z)
#offset,w,x,y,z = execute(offset+1,9,x,y,z) 
#print(w,x,y,z)
#offset,w,x,y,z = execute(offset+1,9,x,y,z) 
#print(w,x,y,z)
#offset,w,x,y,z = execute(offset+1,1,x,y,z) 
#print(w,x,y,z)
#offset,w,x,y,z = execute(offset+1,9,x,y,z) 
#print(w,x,y,z)
#offset,w,x,y,z = execute(offset+1,1,x,y,z) 
#print(w,x,y,z)
#offset,w,x,y,z = execute(offset+1,9,x,y,z) 
#
#
#print(w,x,y,z)




def findsolution():
    solution = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    addconst = {1:6,2:14,3:14,5:9,6:12,10:6,11:9,4:-8,7:-11,8:-4,9:-15,12:-1,13:-8,14:-14}
    type1 = [1,2,3,5,6,10,11]
    type2 = [4,7,8,9,12,13,14]
    for c1 in range(1,10,1):
        solution[1] = c1
        for c2 in range(1,10,1):
            solution[2] = c2
            for c3 in range(1,10,1):
                solution[3] = c3
                for c5 in range(1,10,1):
                    solution[5] = c5
                    for c6 in range(1,10,1):
                        solution[6] = c6
                        for c10 in range(1,10,1):
                            solution[10] = c10
                            for c11 in range(1,10,1):
                                solution[11] = c11
                                solved = True
                                z = 0
                                for i in range(1,15,1):
                                    if i in type1:
                                        w = solution[i]
                                        z = z * 26 + w + addconst[i]
                                        
                                    else:
                                        w = (z % 26) + addconst[i]
                                        if 1 <= w <= 9:
                                            solution[i] = w
                                            z = z // 26
                                        else:
                                            solved = False
                                            break
                                if solved:
                                    return solution


s = findsolution()

print(s)









