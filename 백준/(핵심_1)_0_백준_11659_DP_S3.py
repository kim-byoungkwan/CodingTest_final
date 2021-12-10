import sys

input = sys.stdin.readline

N,M = map(int,input().split())

list_num = list(map(int,input().split()))

list_dp = [0]*len(list_num)


accumulated_sum = 0

for i in range(len(list_num)):

    accumulated_sum += list_num[i]

    list_dp[i] = accumulated_sum

for _ in range(M):

    i,j = map(int,input().split())

    end = j-1

    start = i-2

    if i-2 < 0:

        print(list_dp[end]-0)

        continue

    print(list_dp[end] - list_dp[start])