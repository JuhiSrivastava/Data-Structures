#Python3
#week -3 - assign1
def Parent(i):
    return (int)((i-1)/2)
def LeftChild(i):
    return 2*i +1
def RightChild(i):
    return 2*i +2
def ShiftUp(arr,i,a):
    while i>1 and arr[Parent(i)] > arr[i]:
        a.append([Parent(i),i])
        arr[Parent(i)],arr[i] = arr[i],arr[Parent(i)]
        i = Parent(i)
    return arr,a
def ShiftDown(arr,i,a):
    leng = len(arr) 
    while (LeftChild(i)<leng and arr[LeftChild(i)] < arr[i]) or (RightChild(i)<leng and arr[RightChild(i)] < arr[i]):
        maxIndex = -1
        if (LeftChild(i)<leng and RightChild(i)<leng) and arr[LeftChild(i)] < arr[i] and arr[RightChild(i)] < arr[i]:
            if arr[LeftChild(i)] < arr[RightChild(i)]:
                maxIndex = LeftChild(i)
            else:
                maxIndex = RightChild(i)
        elif LeftChild(i)<leng and arr[LeftChild(i)] < arr[i]:
            maxIndex = LeftChild(i)
        elif RightChild(i)<leng:
            maxIndex = RightChild(i)
        a.append([i, maxIndex])
        arr[maxIndex],arr[i] = arr[i],arr[maxIndex]
        i = maxIndex
    return arr,a
def BuildHeap(arr):
    a =[]
    for i in range(int(len(arr)/2), -1, -1):
        arr,a = ShiftDown(arr,i,a)
    return a,arr
n = int(input())
arr = list(map(int,input().split()))
a,arr =  BuildHeap(arr)
print(len(a))  
for i in range(len(a)):
    print(str(a[i][0]) +" " + str(a[i][1]))