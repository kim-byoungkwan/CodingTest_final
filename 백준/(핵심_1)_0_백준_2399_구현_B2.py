###.1

import sys

input = sys.stdin.readline

N = int(input())

num_list = list(map(int,input().split()))

sum_value = 0

for i in num_list:

    for j in num_list:

        if i == j:

            continue

        sum_value += abs(i-j)

print(sum_value)

