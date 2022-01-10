#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:26:08 2021

@author: pauldepriest
"""

f1 = open("day4.txt",'r')
indata = f1.readlines()
f1.close()

numbers = indata[0].split(',')

cards = []
current = 0
for i in range(2,len(indata),6):
    row1 = indata[i].split()
    row2 = indata[i+1].split()
    row3 = indata[i+2].split()
    row4 = indata[i+3].split()
    row5 = indata[i+4].split()
    cards.append([[[0,0],[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0],[0,0]]])
    
    for j in range(0,5,1):
        cards[current][0][j][0] = int(row1[j])
        cards[current][1][j][0] = int(row2[j])
        cards[current][2][j][0] = int(row3[j])
        cards[current][3][j][0] = int(row4[j])
        cards[current][4][j][0] = int(row5[j])
    current += 1
# Part 2    
# play bingo

bingo = False

bingocount = 0

bingoinfo = []

for i in range(0,len(cards),1):
    bingoinfo.append(0)

done = False

for n in numbers:
    number = int(n)
    for i in range(0,len(cards),1):
        if bingoinfo[i] == 0 :
            
            possiblebingo = False
            for j in range(0,5,1):
                for k in range(0,5,1):
                    if cards[i][j][k][0] == number:
                        cards[i][j][k][1] = 1
                        possiblebingo = True
            if possiblebingo:
            
                for j in range(0,5,1):  #check rows
                    count = 0
                    for k in range(0,5,1):
                        count += cards[i][j][k][1]
                    if count == 5:
                        bingo = True
                        cardnumber = i
                        lastnumber = number
            
                for j in range(0,5,1):  #check columns
                    count = 0
                    for k in range(0,5,1):
                        count += cards[i][k][j][1]
                    if count == 5:
                        bingo = True
                        cardnumber = i
                        lastnumber = number
                
            if bingo:
                if bingoinfo[cardnumber] == 0:
                    bingoinfo[cardnumber] = 1
                    bingocount += 1
                bingo = False
            print(bingocount)
            if bingocount == len(cards) :
                done = True
    if done:
        break
                

print(cardnumber,lastnumber,cards[cardnumber])


total = 0

for j in range(0,5,1):
    for k in range(0,5,1):
        if cards[cardnumber][j][k][1] == 0 :
            total += cards[cardnumber][j][k][0]

print(total * lastnumber)



                    