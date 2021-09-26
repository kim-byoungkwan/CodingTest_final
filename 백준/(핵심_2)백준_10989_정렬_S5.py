###.1

# import sys
#
# N = int(sys.stdin.readline())
#
# arr = [int(sys.stdin.readline()) for _ in range(N)]
#
#
# term = 0
#
# for _ in range(N):
#
#     for i in range(1,N):
#
#         if arr[i-1] > arr[i]:
#
#             term = arr[i]
#
#             arr[i] = arr[i-1]
#
#             arr[i-1] = term
#
# for i in arr:
#
#     print(i)


###.2

import sys

N = int(sys.stdin.readline())

arr = [0] *10001

for _ in range(N):

    num = int(sys.stdin.readline())

    arr[num] = arr[num] + 1


for i in range(1,10001):

    for j in range(arr[i]):

        if arr[i] != 0:

            print(i)
