#Python3
#week -1 - assign2
import sys, threading
import numpy as np
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
def ComputeHeight(maxiheight,li,root):
    a = []
    for i in root:
        if i in li.values():
            a = a + [k for k,v in li.items() if v == i]
    [li.pop(key) for key in a]
    if len(a) >0:
        maxiheight = maxiheight+1
        return ComputeHeight(maxiheight,li,a)
    else:
        return maxiheight

n = int(input())
nodes = list(map(int,input().split()))
li ={}
c =0 
k =[]
for i in range(n):
    if nodes[i] == -1:
            c = i
    else:
       li[i] = nodes[i]

maxiheight = ComputeHeight(1,li,[c])
print(maxiheight)


