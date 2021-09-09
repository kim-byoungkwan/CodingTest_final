###.1

# N = int(input())
#
# list_all = list(map(int,input().split()))
#
# list_set = set(list_all)
#
# print(len(list_set))


###.2

# N = int(input())
#
# list_all = list(map(int,input().split()))
#
# list_all.sort()
#
# answer = []
#
# value_min = min(list_all)
#
# answer.append(value_min)
#
# for i in list_all:
#
#     if value_min < i:
#
#         value_min = i
#
#         answer.append(value_min)
#
#     else:
#
#         continue
#
# print(len(answer))

###.3

import sys

N = int(sys.stdin.readline())

dp = [1]*N

list_all = list(map(int,sys.stdin.readline().split()))


for i in range(N):

    for j in range(i):

        if list_all[i] > list_all[j]:

            dp[i] = max(dp[i],(dp[j]+1))

print(max(dp))













