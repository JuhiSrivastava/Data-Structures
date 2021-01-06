#Python3
#week -1 - assign2
import sys, threading
import numpy as np
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
def ComputeHeight(maxiheight,li,a,count,current):
    if li == [[]]*n:
        return maxiheight,li,a,1
    if li[current] == []:
        return maxiheight,li,a,1
    b = li[current]
    a[current] = li[current]
    li[current] = []
    for i in b:
        count = count + 1
        maxiheight = max(maxiheight,count)
        if li[i] !=[]:
            maxiheight,li,a,count  = ComputeHeight(maxiheight,li,a,count,i)
            count = count -1
        else:
            count = count -1
    return maxiheight,li,a,count

n = int(input())
nodes = list(map(int,input().split()))
li =[[]]*n
a = [[]]*n
c =0 
k =[]
for i in range(n):
    if i != n-1 and nodes[i] == nodes[i+1]:
        k.append(i)
    else:
        if nodes[i] == -1:
            c = i
        else:
            li[nodes[i]] = li[nodes[i]] + k + [i]
            k = []
print(li,a,c)
maxiheight,li,a,count = ComputeHeight(1,li,a,1,c)
print(maxiheight)


