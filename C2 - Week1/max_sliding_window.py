#Python3
#week -1 - assign5
def push(stack,top,maxistack,val,maxi):
    stack.append(val)
    if maxi < val:
        maxistack.append(val)
        maxi = val
    else:
        maxistack.append(maxi)
    top = top +1
    return stack,top,maxistack,maxi

def pop(stack,top,maxistack):
    del stack[top-1]
    del maxistack[top-1]
    top = top -1
    return stack,top,maxistack

def move(stack1,stack2,top1,top2,maxistack1,maxistack2,maxi2):
    maxistack1 = []
    while top1 !=0:
        stack2,top2,maxistack2,maxi2 = push(stack2,top2,maxistack2,stack1[top1-1],maxi2)
        del stack1[top1-1]
        top1 = top1 -1
    return stack1,stack2,top1,top2,maxistack1,maxistack2,maxi2

n = int(input())
li = list(map(int,input().split()))
m = int(input()) 
stack1 =[]
stack2 =[]
maxistack1 =[]
maxistack2 =[]
top1 = len(stack1)
top2 = len(stack2)
maxi1 = 0
maxi2 = 0
value =""
flag = True
for i in range(n):
    if len(stack2) != m and flag:
        stack2,top2,maxistack2,maxi2 = push(stack2,top2,maxistack2,li[m - i - 1],maxi2)
    if len(stack2) == m and flag:
        value = str(maxistack2[top2-1])
        flag = False
        continue
    if not flag:
        stack2,top2,maxistack2 = pop(stack2,top2,maxistack2)
        stack1,top1,maxistack1,maxi1 = push(stack1,top1,maxistack1,li[i],maxi1)
        if len(stack2) == 0:
            value = value + " " + str(maxistack1[top1-1])
            stack1,stack2,top1,top2,maxistack1,maxistack2,maxi2 = move(stack1,stack2,top1,top2,maxistack1,maxistack2,0)
            maxi1 = 0
        else:
            value = value + " " + str(max(maxistack2[top2-1],maxistack1[top1-1]))
print(value)