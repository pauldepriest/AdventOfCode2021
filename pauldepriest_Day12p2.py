#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

import collections


f1 = open("day12.txt",'r')
indata = f1.readlines()
f1.close()

for i in range(0,len(indata),1):
    indata[i] = indata[i][0:-1]
    
print(indata)

edges = collections.defaultdict(set)



for i in indata:
    src,dst = i.split('-')
    edges[src].add(dst)
    edges[dst].add(src)

print(edges)

todo = [(('start',),False)]
all_paths = set()



while todo:
    path,twice = todo.pop()
    if path[-1] == 'end':
        all_paths.add(path)
        continue
    for cand in edges[path[-1]]:
        if cand == 'start' :
            continue
        elif cand.isupper() or cand not in path :
            todo.append(((*path,cand),twice))
        elif not twice and path.count(cand) == 1 :
            todo.append(((*path,cand),True))

print(len(all_paths))

