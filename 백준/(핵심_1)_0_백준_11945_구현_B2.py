###.1

import sys

input = sys.stdin.readline

N,M = map(int,input().split())

matrix = [[] for _ in range(N)]

for i in range(N):

    matrix[i] = list(input().rstrip())[::-1]

for j in matrix:

    print(''.join(j))




