###.3

n = int(input())

arr_num = sorted(list(map(int,input().split())))

x = int(input())

count = 0

left = 0

right = len(arr_num)-1

while left < right:

    if arr_num[left] + arr_num[right] < x:

        left = left + 1

    elif arr_num[left] + arr_num[right] > x:

        right = right - 1

    else:

        right = right - 1

        count += 1

print(count)



















































###.2

# import sys
#
# n = int(sys.stdin.readline())
#
# arr_num = list(map(int,sys.stdin.readline().split()))
#
# x = int(sys.stdin.readline())
#
# count = 0
#
# for i in range(len(arr_num)-1):
#
#     for j in range(i+1,len(arr_num)):
#
#         if arr_num[i] + arr_num[j] == x:
#
#             count += 1
#
#         else:
#
#             continue
#
# print(count)





























###.1

# from itertools import combinations
#
# n = int(input())
#
# arr_num = list(map(int,input().split()))
#
# x = int(input())
#
# count = 0
#
# for i in list(combinations(arr_num,2)):
#
#     if sum(i) == x:
#
#         count += 1
#
#     else:
#
#         continue
#
# print(count)
