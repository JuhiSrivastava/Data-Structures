#Python3
#week -1 - assign3
import numpy as np
buffer,packets = map(int,input().split())
queue = []
a =np.zeros(packets,int)
c=[]
countc = 0
j =0
k=0
for i in range(packets):
    arrival,processing = map(int,input().split())
    if k == 0  and processing == 0:
        a[i] = arrival
    else:
        c.append([arrival,processing])
        k = k + processing
if len(c) > 0:
    j = c[0][0]
    countc = 0
    k = max(c[len(c)-1][0],k)
for i in range(j,k+1):
    if len(queue) > 0 and (queue[0][0][1] == 0):
        del queue[0]
        if len(queue) > 0:
            a[queue[0][1]] = i
    while countc < len(c) and c[countc][0] == i:
        if len(queue) < buffer:
            queue.append([c[countc],countc,c[countc][1]])
            if len(queue) == 1:
                a[queue[0][1]] = i
        else:
            a[countc] = -1
        countc = countc+1
    flag = False
    while len(queue) > 0:
        if queue[0][0][1] == 0:
            a[queue[0][1]] = i
            del queue[0]
            flag = True
        else:
            queue[0][0][1] = queue[0][0][1] -1
            if flag:
                a[queue[0][1]] = i
            break
for i in a:
    print(i)


