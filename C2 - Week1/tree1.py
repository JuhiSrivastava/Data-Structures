#Python3
#week -1 - assign2
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
def ComputeHeight(maxiheight,li,a,count,current):
    if len(li) == 0:
        return maxiheight,li,a,1
    if li.get(current) == None:
        return maxiheight,li,a,1
    b = li[current]
    a[current] = li[current]
    del li[current]
    for i in b:
        count = count + 1
        maxiheight = max(maxiheight,count)
        if li.get(i) !=None:
            maxiheight,li,a,count  = ComputeHeight(maxiheight,li,a,count,i)
            count = count -1
        else:
            count = count -1
    return maxiheight,li,a,count

n = int(input())
nodes = list(map(int,input().split()))
li ={}
c =0 
k =[]
for i in range(n):
    if i != n-1 and nodes[i] == nodes[i+1]:
        k.append(i)
    else:
        if nodes[i] == -1:
            c = i
        else:
            if li.get(nodes[i]) == None:
                li[nodes[i]] = k + [i]
            else:
                li[nodes[i]] = li[nodes[i]] + k + [i]
            k = []
maxiheight,li,a,count = ComputeHeight(1,li,{},1,c)
print(maxiheight)

