#Python3
#week -3 - assign2
def Parent(i):
    return (int)((i-1)/2)
def LeftChild(i):
    return 2*i +1
def RightChild(i):
    return 2*i +2
def ShiftUp(arr,i):
    while i>0 and (arr[Parent(i)][1] > arr[i][1] or (arr[Parent(i)][1] == arr[i][1] and arr[Parent(i)][0] > arr[i][0])):
        arr[Parent(i)],arr[i] = arr[i],arr[Parent(i)]
        i = Parent(i)
    return arr
def ShiftDown(arr,i):
    leng = len(arr) 
    while (LeftChild(i)<leng and (arr[LeftChild(i)][1] < arr[i][1] or (arr[LeftChild(i)][1] == arr[i][1] and arr[LeftChild(i)][0] < arr[i][0]))) or (RightChild(i)<leng and (arr[RightChild(i)][1] <= arr[i][1] or (arr[RightChild(i)][1] == arr[i][1] and arr[RightChild(i)][0] < arr[i][0]))):
        maxIndex = -1
        if (LeftChild(i)<leng and RightChild(i)<leng) and arr[LeftChild(i)][1] <= arr[i][1] and arr[RightChild(i)][1] <= arr[i][1]:
            if arr[LeftChild(i)][1] < arr[RightChild(i)][1]:
                maxIndex = LeftChild(i)
            elif arr[LeftChild(i)][1] > arr[RightChild(i)][1]:
                maxIndex = RightChild(i)
            else:
                if arr[LeftChild(i)][0] < arr[RightChild(i)][0]:
                    maxIndex = LeftChild(i)
                else:
                    maxIndex = RightChild(i)
        elif LeftChild(i)<leng and (arr[LeftChild(i)][1] < arr[i][1] or (arr[LeftChild(i)][1] == arr[i][1] and arr[LeftChild(i)][0] < arr[i][0])):
            maxIndex = LeftChild(i)
        elif RightChild(i)<leng and (arr[RightChild(i)][1] < arr[i][1] or (arr[RightChild(i)][1] == arr[i][1] and arr[RightChild(i)][0] < arr[i][0])):
            maxIndex = RightChild(i)
        arr[maxIndex],arr[i] = arr[i],arr[maxIndex]
        i = maxIndex
    return arr
def BuildHeap(arr):
    for i in range(int(len(arr)/2), -1, -1):
        arr = ShiftDown(arr,i)
    return arr
def ExtractMin(arr):
    temp = arr[0]
    arr[0] = arr[len(arr)-1]
    del arr[len(arr)-1]
    arr = ShiftDown(arr,0)
    return temp,arr
def Insert(value,threads):
    arr.append(value)
    arr = ShiftUp(arr,len(arr)-1)
    return arr
m,n = map(int,input().split())
li = list(map(int,input().split()))
threads = [None]*m
j = 0
a = []
while len(li) > 0:
    if j <m and threads[j] == None:
        threads[j] = [j,li[0]]
        a.append([j,0])
        j = j+1
        del li[0]
        if j == m:
            threads = BuildHeap(threads)
    else:
        temp,arr = ExtractMin(threads)
        a.append([temp[0],temp[1]])
        temp[1] = temp[1] + li[0]
        threads.append(temp)
        threads = ShiftUp(threads,len(threads)-1)
        del li[0]
        if len(li) == 0:
            break
a = sorted(a, key =lambda x: (x[1],x[0]))
for i in range(len(a)):
    print(str(a[i][0]) +" " + str(a[i][1]))
    