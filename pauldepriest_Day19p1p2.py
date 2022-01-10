#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import numpy
from heapq import heappop, heappush
from collections import defaultdict







f1 = open("day19.txt",'r')
indata = f1.readlines()
f1.close()


data = []
sc = -1
s = []
for line in indata:
    row = line.strip()
    if '---' in row:
        sc += 1
    elif len(row) == 0:
        data.append(s)
        s = []
    else:
        x,y,z = row.split(',')
        s.append((int(x),int(y),int(z)))
        
data.append(s)

#def getdist(ss):
#    ans = {}
#    for i in range(0,len(ss)-1,1):
#        for j in range(i+1,len(ss),1):
#            ans[(abs(ss[i][0]-ss[j][0]),abs(ss[i][1]-ss[j][1]),abs(ss[i][2]-ss[j][2]))] = (ss[i],ss[j])
#            
#    return ans
#
#
#aa = getdist(data[0])
#bb = getdist(data[1])
#
#
#
#
#def comparedist(s1,s2):
#    cc = 0
#    ans1 = set()
#    ans2 = set()
#    for d in s1:
#        if d in s2:
#            a,b = s1[d]
#            c,d = s2[d]
#            ans1.add(a)
#            ans1.add(b)
#            ans2.add(c)
#            ans2.add(d)
#            
#            cc += 1
#    return ans1, ans2
#
#same1,same2 = comparedist(aa,bb)

#def findzero(same1,same2):
#    diffs = {}
#    for x2,y2,z2 in same2:
#        for x1,y1,z1 in same1:
#            
#            x0 = x2 + x1
#            y0 = y2 + y1
#            z0 = z2 + z1
#            cc = 0
#            for x3,y3,z3 in same2:
#                if (-x3+x0,-y3+y0,-z3+z0) in same1:
#                    cc += 1
#            #print(cc)
#            if cc >= 12:
#                return (x0,y0,z0)
#    return (0,0,0)
#            
#
#aaa = findzero(same1,same2)
#                   
            
            
def compare2(w,s1,s2):
    
    for i1 in range(0,24,1):
            
            
        
        diffs = {}
        for j in range(0,len(s2),1):
            x2,y2,z2 = s2[j][i1]
            for k in range(0,len(s1),1):
                x1,y1,z1 = s1[k]
                x0 = x2 - x1
                y0 = y2 - y1
                z0 = z2 - z1
                if (x0,y0,z0) in diffs:
                    diffs[(x0,y0,z0)] += 1
                else:
                    diffs[(x0,y0,z0)] = 1
        if max(diffs.values()) >= 12:
            return i1, max(diffs,key=diffs.get)
    return -1,(0,0,0)

def rotatepoint(x,y,z):
    return [(x,y,z),(z,y,-x),(-x,y,-z),(-z,y,x),(-y,x,z),(z,x,y),
            (y,x,-z),(-z,x,-y),(y,-x,z),(z,-x,-y),(-y,-x,-z),(-z,-x,y),
            (x,-z,y),(y,-z,-x),(-x,-z,-y),(-y,-z,x),(x,-y,-z),(-z,-y,-x),
            (-x,-y,z),(z,-y,x),(x,z,-y),(-y,z,-x),(-x,z,y),(y,z,x)]


def computerotations(s):
    ans = []
    for p in s:
        pall = rotatepoint(*p)
        ans.append(pall)
    return ans
#dataall = []
#dataall.append(computerotations(data[0]))
#dataall.append(computerotations(data[1]))
#dataall.append(computerotations(data[2]))
#dataall.append(computerotations(data[3]))
#dataall.append(computerotations(data[4]))



#coord1,sensorpos1 = compare2(0,dataall[0],dataall[1])
#coord4,sensorpos4 = compare2(0,dataall[1],dataall[4])
sensors = []
for i in range(0,len(data),1):
    sensors.append([i,(0,0,0)])





#def findmatches(s):
#    matches = {}
#    sensorinfo = []
#    for i in range(0,len(s)-1,1):
#        for j in range(i+1,len(s),1):
#            if i != j:
#                coord1,sensorpos = compare2(0,dataall[i],dataall[j])
#            else:
#                continue
#            if coord1 != -1:
#                if i in matches:
#                    matches[i].append(j)
#                else:
#                    matches[i] = [j]
#                #if j in matches:
#                #    matches[j].append(i)
#                #else:
#                #    matches[j] = [i]
#                sensorinfo.append([i,j,coord1,sensorpos])
#    return matches,sensorinfo
#
#m,sensorsssss = findmatches(dataall)



def findandmerge(current,id,s):
    global sensors
    
    currentall = computerotations(current)
    for i in range(len(s)-1,-1,-1):
        coord,sensorpos = compare2(0,s[i],currentall)
        if coord != -1:
            ans = set()
            for p in s[i]:
                ans.add(p)
            
            for q in range(0,len(currentall),1):
                x,y,z = currentall[q][coord]
                ans.add((x-sensorpos[0],y-sensorpos[1],z-sensorpos[2]))
            # update sensor positions
            for u in range(1,len(sensors),1):
                if sensors[u][0] == id:
                    allpos = rotatepoint(sensors[u][1][0],sensors[u][1][1],sensors[u][1][2])
                    sensors[u][0] = i
                    x,y,z = allpos[coord]
                    sensors[u][1] = (x-sensorpos[0],y-sensorpos[1],z-sensorpos[2])
            
            return i,list(ans)
    



while len(data) > 1:
    currentsensor = data.pop()
    currentid = len(data)
    pos,results = findandmerge(currentsensor,currentid,data)
    data[pos] = []
    for w in results:
        data[pos].append(w)
        
maxdist = 0

for i in range(0,len(sensors)-1,1):
    for j in range(i+1,len(sensors),1):
        x1,y1,z1 = sensors[i][1]
        x2,y2,z2 = sensors[j][1]
        dist = abs(x1-x2) + abs(y1-y2) + abs(z1-z2)
        maxdist = max(maxdist,dist)

print(maxdist)
    
    
    







