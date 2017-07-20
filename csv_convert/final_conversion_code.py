# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 15:49:19 2017

@author: ASHISH KUMAR JAYANT
"""
import re

f = open("/home/nishank/Desktop/csv_1.txt",'r')

ans1=""
head = "X,Y,Z,RES"
for i in f.readlines():
    out = {}
    i = i.replace('\n','')
    if 'X' in i:
        x = i.split(' ')
        
        for j in x:
            if j.isdigit():
                #ans1 += j
                #ans1 += ","
                out['X']=j
    if 'Y' in i:
        x = i.split(' ')
        for j in x:
            if j.isdigit():
                #ans1 += j
                #ans1 += ","
                out['Y']=j
    if 'Z' in i:
        x = i.split(' ')
        for j in x:
            if j.isdigit():
                #ans1 += j
                #ans1 += ","
                out['Z']=j
    if 'RES' in i:
        q = re.compile(r'-?\d+\.\d+')
        negatives = [float(j) for j in q.findall(i)]
        for j in negatives:
            #ans1 += str(j)
            #ans1 += ","
            out['RES']=str(j)
    try:
     ans1 = ans1+out['X']+","
    except:
        pass
    try:
     ans1 = ans1+out['Y']+","
    except:
        pass
    try:
     ans1 = ans1+out['Z']+","
    except:
        pass
    try:
     ans1 = ans1+out['RES']
    except:
        pass
    if 'POINT' in i:
        ans1 += '\n'
        
f.close()
f2 = open("/home/nishank/Desktop/csv_1.csv",'w')
f2.write(head)
f2.write('\n')

ans1 = ans1.split('\n')

for j in ans1:
    if j is not None:
        f2.write(j)
        f2.write('\n')
f2.close()
    
    