arr = [1,0,0]

M = int(input())

for _ in range(M):

    A,B = map(int,input().split())

    arr[B-1], arr[A-1] = arr[A-1],arr[B-1]

for index,value in enumerate(arr):

    if value ==1:

        print(index+1)
