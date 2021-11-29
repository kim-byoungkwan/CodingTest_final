###.1

import sys

input = sys.stdin.readline

INF = int(1e9)

N,M = map(int,input().split())

matrix = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):

    A,B = map(int,input().split())

    matrix[A][B] = 1

    matrix[B][A] = 1

for k in range(1,N+1):

    for p in range(1,N+1):

        for q in range(1,N+1):

            if matrix[p][k] and matrix[k][q]:

                if matrix[p][q] == 0:

                    matrix[p][q] = matrix[p][k] + matrix[k][q]

                else:

                    matrix[p][q] = min(matrix[p][q], matrix[p][k]+matrix[k][q])

answer = []

for m in range(1,N+1):

    answer.append((m,sum(matrix[m])))

print(sorted(answer,key= lambda x:(x[1],x[0]))[0][0])




