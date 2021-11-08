import sys

count_A,count_D = map(int,sys.stdin.readline().split())

arr_A = []

arr_D = []

for _ in range(count_A):

    arr_A.append(int(sys.stdin.readline()))

arr_A = sorted(arr_A)

for _ in range(count_D):

    num_D = int(sys.stdin.readline())

    left = 0

    right = len(arr_A)-1

    result = -1

    while left <= right:

        middle = (left + right)//2

        if arr_A[middle] == num_D:

            if right == middle:

                result = middle

                break

            right = middle


        elif arr_A[middle] < num_D:

            left = middle + 1

        elif arr_A[middle] > num_D:

            right = middle -1

    print(result)
