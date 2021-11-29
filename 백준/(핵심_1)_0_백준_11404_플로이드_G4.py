###.1

import sys

input = sys.stdin.readline

N = int(input())

M = int(input())

INF = int(1e9)

matrix = [[INF]*(N+1) for _ in range(N+1)]


for _ in range(M):

    a,b,c = map(int,input().split())

    if matrix[a][b] > c:

        matrix[a][b] = c

for x in range(N+1):

    for y in range(N+1):

        if x == y:

            matrix[x][y] = 0

for k in range(1,N+1):

    for p in range(1,N+1):

        for q in range(1,N+1):

            matrix[p][q] = min(matrix[p][q],matrix[p][k]+matrix[k][q])

for g in range(1,N+1):

    for h in range(1,N+1):

        if matrix[g][h] == INF:

            matrix[g][h] = 0

        else:

            continue

for n in range(1,N+1):

    for m in range(1,N+1):

        if matrix[n][m] == INF:

            print(matrix[n][m],end=' ')

        else:

            print(matrix[n][m],end=' ')

    print()

