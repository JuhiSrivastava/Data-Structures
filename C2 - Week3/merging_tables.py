#Python3
#week -3 - assign3
def MakeSet(parent,rank,n,rows,maxi):
    for i in range(n):
        parent[i] = i
        rank[i] = 0
        if maxi < rows[i]:
            maxi=rows[i]
    return parent,rank,maxi

def Find(parent,i):
    if i != parent[i]:
        parent[i] = Find(parent,parent[i])
    return parent[i]

def Union(i,j,rows,a,parent,rank,maxi):
    parenti = Find(parent,i)
    parentj = Find(parent,j)
    if parenti != parentj:
        if rank[parenti] > rank[parentj]:
            parent[parentj] = parenti
            rows[parenti] = rows[parenti] + rows[parentj]
            rows[parentj] = 0
            if maxi < rows[parenti]:
                maxi = rows[parenti]
        else:
            parent[parenti] = parentj
            rows[parentj] = rows[parentj] + rows[parenti]
            rows[parenti] = 0
            if rank[parenti] == rank[parentj]:
                rank[parentj] = rank[parentj] +1
            if maxi < rows[parentj]:
                maxi = rows[parentj]
    a.append(maxi)
    return rows,a,parent,rank,maxi 
n,m = map(int,input().split())
rows = list(map(int,input().split()))
parent = [None]*n
rank = [None]*n
a =[]
maxi = 0
parent,rank,maxi = MakeSet(parent,rank,n,rows,maxi)
for i in range(m):
    des,source = map(int,input().split())
    des = des - 1
    source = source -1
    rows,a,parent,rank,maxi = Union(source,des,rows,a,parent,rank,maxi)
for i in range(m):
    print(a[i])