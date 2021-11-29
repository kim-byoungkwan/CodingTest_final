import sys

input = sys.stdin.readline

N,M = map(int,input().split())

INF = int(1e9)

matrix = [[0]*(N+1) for _ in range(N+1)]


for _ in range(M):

    a,b = map(int,input().split())

    matrix[a][b] = 1


for mid in range(1,N+1):

    for p in range(1,N+1):

        for q in range(1,N+1):

            if matrix[p][mid] and matrix[mid][q]:

                matrix[p][q] = 1


answer = [0]*(N+1)

for m in range(1,N+1):

    for n in range(1,N+1):

        if matrix[m][n] == 1:

            answer[m] += 1

            answer[n] += 1

print(answer.count(N-1))
