# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:28:35 2020

@author: Juhi Srivastava
"""

n = int(input())
nodes = list(map(int,input().split()))
li ={}
c =0 
for i in range(n):
    if nodes[i] == -1:
        c = i
    else:
        if li.get(nodes[i]) == None:
            li[nodes[i]] = [i]
        else:
            li[nodes[i]] = li[nodes[i]] + [i]
count = 1
a = [c]
while len(li) > 0:
    b =[]
    flag = False
    print(li,a)
    for i in a:
        if li.get(i) != None:
            b = b + li[i]
            flag = True
            del li[i]
    if flag:
        count = count +1
        a = b
print(count) 
