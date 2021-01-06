#Python3
#week -3 - assign2
m,n = map(int,input().split())
li = list(map(int,input().split()))
threads = {}
j = 0
a = []
while len(li) > 0:
    if j <m and threads.get(j) == None:
        threads[j] = li[0]
        a.append([j,0])
        j = j+1
        del li[0]
    else:
        mini = min(threads.values())
        for k in threads:
            if threads[k] == mini and len(li) >0:
                a.append([k,threads[k]])
                threads[k] = threads[k] + li[0]
                del li[0]
                if len(li) == 0:
                    break
a = sorted(a, key =lambda x: x[1])
for i in range(len(a)):
    print(str(a[i][0]) +" " + str(a[i][1]))