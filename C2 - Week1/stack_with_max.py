#Python3
#week -1 - assign4

def push(stack,top,maxistack,val,maxi):
    stack.append(val)
    if maxi < val:
        maxistack.append(val)
        maxi = val
    else:
        maxistack.append(maxi)
    top = top +1
    return stack,top,maxistack,maxi

def pop(top):
    del stack[top-1]
    del maxistack[top-1]
    top = top -1
    return stack,top,maxistack
    
def maximum(top,maxprint):
    if top != 0:
        maxprint.append(maxistack[top-1])
    else:
        maxprint.append(0)
    return maxprint
    
n = int(input())
stack =[]
maxistack =[]
top = len(stack)
maxi = 0
maxprint = []
for i in range(n):
    string = input()
    if len(string) > 3:
        operation, val = string.split()
    else:
        operation = string
    if operation == "push":
        stack,top,maxistack,maxi = push(stack,top,maxistack,int(val),maxi)
    elif operation == "pop":
        stack,top,maxistack = pop(top)
    else:
        maxprint = maximum(top,maxprint)
for i in maxprint:
    print(i)