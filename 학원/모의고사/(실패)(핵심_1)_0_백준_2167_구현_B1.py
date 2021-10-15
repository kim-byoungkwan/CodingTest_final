





###.1

import sys

N,M = map(int,sys.stdin.readline().split())

matrix = [[] for _ in range(N)]

for p in range(N):

    matrix[p] = list(map(int,sys.stdin.readline().split()))

T = int(sys.stdin.readline())

for _ in range(T):

    result = 0

    i,j,x,y = map(int,sys.stdin.readline().split())

    for r in range(i-1,x):

        for s in range(j-1,y):

            result += matrix[r][s]

    print(result)
