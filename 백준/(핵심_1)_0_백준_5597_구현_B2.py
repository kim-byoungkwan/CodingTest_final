arr = [0]*30

for _ in range(28):

    num = int(input())

    arr[num-1] = 1

for index,value in enumerate(arr):

    if value == 0:

        print(index+1)
