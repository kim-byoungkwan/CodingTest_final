import sys

INF = int(1e9)

input = sys.stdin.readline

N,M = map(int,input().split())

matrix = [[INF]*(N+1) for _ in range(N+1)]


for _ in range(M):

    a,b,c = map(int,input().split())

    matrix[a][b] = c

    matrix[b][a] = c



for mid in range(1,N+1):

    for p in range(1,N+1):

        for q in range(1,N+1):

            if p == q:

                matrix[p][q] = 0

            if matrix[p][q] > matrix[p][mid] + matrix[mid][q]:

                matrix[p][q] = matrix[p][mid]+matrix[mid][q]

print(matrix)







