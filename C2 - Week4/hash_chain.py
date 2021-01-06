#Python3
#week -4 - assign2
def hashing(string,m):
    p = 1000000007
    x = 263
    value = 0
    for i in range(len(string)):
        value = value + ((ord(string[i])*(x**i))%p)
    value = (value%p)%m
    return value
def find(chain,string,printlis,strval):
    templis = [] + chain[strval]
    if string in templis:
        printlis.append("yes") 
    else:
        printlis.append("no")
    return printlis
def add(chain,string,strval):
    templis =[] + chain[strval]
    if string not in templis:
        templis.insert(0, string)
        chain[strval] = templis
    return chain
def delete(chain,string,strval):
    templis = [] + chain[strval]
    if string in templis:
        templis.remove(string)
        chain[strval] = templis
    return chain
def check(lis,printlis):
    val = ""
    for i in range(len(lis)):
        if i!=(len(lis) -1):
            val = val +lis[i] + " "
        else:
            val = val +lis[i]
    printlis.append(val)
    return printlis
    
m = int(input())
chain = [[]]*m
n = int (input())
printlis = []
for i in range(n):
    inputstr = list(input().split())
    strval = hashing(inputstr[1],m)
    if inputstr[0] == "add":
        chain = add(chain, inputstr[1],strval)
    elif inputstr[0] == "find":
        printlis = find(chain, inputstr[1],printlis,strval)
    elif inputstr[0] == "del":
        chain = delete(chain, inputstr[1],strval)
    elif inputstr[0] == "check":
        printlis = check(chain[int(inputstr[1])], printlis)
for i in range(len(printlis)):
    print(printlis[i])