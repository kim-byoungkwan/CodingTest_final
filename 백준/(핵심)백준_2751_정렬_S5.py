###.1

# import sys
#
# N = int(sys.stdin.readline())
#
# list = []
#
# for _ in range(N):
#
#     list.append(int(sys.stdin.readline()))
#
# def rise(list):
#
#     term = 0
#
#     for _ in range(N):
#
#         for i in range(1,N):
#
#             while list[i-1] > list[i]:
#
#                 term = list[i]
#
#                 list[i] = list[i-1]
#
#                 list[i-1] = term
#
#     return list
#
# for i in rise(list):
#
#     print(i)

###.2

import sys

N = int(sys.stdin.readline())

arr = []

for _ in range(N):

    arr.append(int(sys.stdin.readline()))

for i in sorted(arr):

    print(i)





