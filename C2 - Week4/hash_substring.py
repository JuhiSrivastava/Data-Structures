#Python3
#week -4 - assign3
from random import randint
def RabinKarp(T, P):
    p = 1000000007
    x = randint(1,p-1)
    result = ""
    pHash = PolyHash(P,p,x)
    H = PrecomputeHashes(T, len(P), p, x)
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

def PolyHash(S, p, x):
    hashval = 0
    for i in range(len(S) -1,-1,-1):
        hashval = (hashval*x +ord(S[i]))%p
    return hashval

P = input()
T = input()
print(RabinKarp(T, P))

