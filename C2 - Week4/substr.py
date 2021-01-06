#Python3
#week -4 - assign4
from random import randint
def Hashing(T):
    m1 = 10**9 +7
    m2 = 10**9 +9
    x1 = randint(1,m1-1)
    x2 = randint(1,m2-1)
    h1 = [None]*(len(T) +1)
    h2 = [None]*(len(T) +1)
    h1 = PrecomputeHashes(T, m1, x1,h1)
    h2 = PrecomputeHashes(T, m2, x2,h2)
    query = int(input())
    result = []
    for i in range(query):
        qry = list(map(int,input().split()))
        k1 = pow(x1, qry[2], m1)
        k2 = pow(x2, qry[2], m2)
        hash11 = h1[qry[0] + qry[2]] - (k1)*h1[qry[0]]
        hash12 = h1[qry[1] + qry[2]] - (k1)*h1[qry[1]]
        hash21 = h2[qry[0] + qry[2]] - (k2)*h2[qry[0]]
        hash22 = h2[qry[1] + qry[2]] - (k2)*h2[qry[1]]
        if hash11%m1 == hash12%m1 and hash21%m2 == hash22%m2:
            result.append("Yes")
        else:
            result.append("No")
    return result
def PrecomputeHashes(T, p, x,h):
    h[0] = 0
    for i in range(1,len(T)+1):
        h[i] = (x*h[i-1] + ord(T[i-1]))%p
    return h

T = input()
result = Hashing(T)
for i in result:
    print(i)
