#Python3
#week -4 - assign1
#direct addressing
def add(lis, num,name):
    lis[int(num)] = name
    return lis
def find(lis, num):
    if lis[int(num)] != None:
        return lis[int(num)]
    else:
        return "not found"
def delete(lis, num):
    lis[int(num)] = None
    return lis
n= int(input())
val =[]
lis = [None]*10000000
for i in range(n):
    inputstr = list(input().split())
    if inputstr[0] == "add":
        lis = add(lis, inputstr[1], inputstr[2])
    if inputstr[0] == "find":
        val.append(find(lis, inputstr[1]))
    if inputstr[0] == "del":
        lis = delete(lis, inputstr[1])
for i in range(len(val)):
    print(val[i])
    
