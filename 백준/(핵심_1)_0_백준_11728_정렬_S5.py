###.2

import sys

A,B = map(int,sys.stdin.readline().split())

arr_A = list(map(int,sys.stdin.readline().split()))

arr_B = list(map(int,sys.stdin.readline().split()))

arr_total = arr_A + arr_B

print(*sorted(arr_total))






















###.1

# A,B = map(int,input().split())
#
# arr_A = list(map(int,input().split()))
#
# arr_B = list(map(int,input().split()))
#
# for i in arr_B:
#
#     arr_A.append(i)
#
# print(*sorted(arr_A))
