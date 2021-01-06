#Python3
#week -4 - assign5
from random import randint
def Hashing(T):
    m1 = 10**5 +7
    m2 = 10**5 +9
    x1 = randint(1,m1-1)
    x2 = randint(1,m2-1)
    h1 = [None]*(len(T) +1)
    h2 = [None]*(len(T) +1)
    leng = min(len(T[0]),len(T[1]))
    if leng == len(T[0]):
        h1 = PrecomputeHashes(T[0], m1, x1,h1)
        h2 = PrecomputeHashes(T[0], m2, x2,h2)
        h3 = PrecomputeHashes(T[1], m1, x1,h1)
        h4 = PrecomputeHashes(T[1], m2, x2,h2)
    else:
        h1 = PrecomputeHashes(T[0], m1, x1,h1)
        h2 = PrecomputeHashes(T[0], m2, x2,h2)
        h3 = PrecomputeHashes(T[1], m1, x1,h1)
        h4 = PrecomputeHashes(T[1], m2, x2,h2)
    leng = min(len(T[0]),len(T[1]))
    while leng > 0:
        k1 = pow(x1, leng, m1)
        k2 = pow(x2, leng, m2)
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

def RabinKarp(T, P):
    p1 = 10**5 +7
    p2 = 10**5 +9
    x1 = randint(1,p1-1)
    x2 = randint(1,p2-1)
    result = ""
    leng = min(len(T[0]),len(T[1]))
    pHash1 = PolyHash(P,p1,x1)
    #pHash2 = PolyHash(P,p2,x2)
    pHash3 = PolyHash(T,p1,x1)
    #pHash4 = PolyHash(T,p2,x2)
    H1 = PrecomputeHashes(P, leng, p, x)
    H3 = PrecomputeHashes(T, leng, p, x)
    for i in range(len(T)- len(P)+1):
        if pHash != H[i]:
            continue
        if T[i:i+len(P)] == P:
            result = result + str(i) + " "
    return result[:len(result)-1]

def PrecomputeHashes(T, lenP, p, x):
    lenT = len(T)
    H = [None]*(lenT - lenP +1)
    S = T[lenT - lenP : lenT]
    H[lenT - lenP] = PolyHash(S, p, x)
    y = pow(x, lenP, p)
    for i in range(lenT - lenP -1,-1,-1):
        H[i] = (((x*H[i + 1])%p) + ord(T[i]) - ((y*ord(T[i + lenP]))%p) + p)%p
    return H

def PolyHash(T, p, x,h):
    h[0] = 0
    for i in range(1,len(T)+1):
        h[i] = (x*h[i-1] + ord(T[i-1]))%p
    return h

T = input().split()
result = Hashing(T)
for i in result:
    print(i)

cool toolbox
1234
123456789

4321
987654321