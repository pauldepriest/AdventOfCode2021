#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import numpy
from heapq import heappop, heappush



hex2bin = {'0':'0000','1':'0001','2':'0010','3':'0011',
           '4':'0100','5':'0101','6':'0110','7':'0111',
           '8':'1000','9':'1001','A':'1010','B':'1011',
           'C':'1100','D':'1101','E':'1110','F':'1111'}




f1 = open("day16.txt",'r')
indata = f1.readlines()
f1.close()

data = indata[0][0:-1]
total = 0

btrans = ''

for i in data:
    btrans = btrans + hex2bin[i]

#process packet totaling version numbers
completepackets = []
packets = []
totver = 0

def getpackets(index):
    global packets, total
    vers = int(btrans[index:3+index],2)
    t = int(btrans[3+index:6+index],2)
    index += 6
    total += vers
    
    if t == 4:
        lit = ''
        while btrans[index] == '1':
            lit += btrans[index+1:index+5]
            index += 5
        lit += btrans[index+1:index+5]
        index += 5
        literal = int(lit,2)
        print(literal)
        packets.append([vers,t,literal])
        return index
    else:
        if btrans[index] == '1':
            subcount = int(btrans[index+1:index+12],2)
            index += 12
            packets.append([vers,t,subcount])
            for ii in range(0,subcount,1):
                print(index,1,subcount)
                index = getpackets(index)
            return index
        else:
            lencount = int(btrans[index+1:index+16],2)
            index += 16
            actlencount = index + lencount
            packets.append([vers,t,lencount])
            packetindex = len(packets) -1
            subcount = 0
            while index < actlencount:
                print(index,0)
                subcount += 1
                index = getpackets(index)
            packets[packetindex][2] = subcount
            return index
        
        
index = getpackets(0) 

tot = 0
for v,t,i in packets:
    tot += v
    
print(tot)


st = []
fours = 0
for pack in range(len(packets)-1,-1,-1):
    v,t,i = packets[pack]
    if t == 4:
        st.append(i)
        
    elif t == 7:
        first = st.pop()
        second = st.pop()
        if first == second:
            st.append(1)
        else:
            st.append(0)
    elif t == 6:
        first = st.pop()
        second = st.pop()
        if first < second:
            st.append(1)
        else:
            st.append(0)
    elif t == 5:
        first = st.pop()
        second = st.pop()
        if first > second:
            st.append(1)
        else:
            st.append(0)
    elif t == 3:
        h = st[-1]
        for j in range(max(0,len(st)-i),len(st),1):
            h = max(h,st.pop())
        st.append(h)
    elif t == 2:
        m = st[-1]
        for j in range(max(0,len(st)-i),len(st),1):
            m = min(m,st.pop())
        st.append(m)
    elif t == 1:
        p = 1
        for j in range(max(0,len(st)-i),len(st),1):
            p = p * st.pop()
        st.append(p)
    elif t == 0:
        s = 0
        for j in range(max(0,len(st)-i),len(st),1):
            s += st.pop()
        st.append(s)
        
        
print(st)
    








