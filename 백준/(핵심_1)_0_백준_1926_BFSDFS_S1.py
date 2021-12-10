import sys

from collections import deque

N,M = map(int,input().split())

matrix = [[] for _ in range(N)]

visited = [[False]*(M) for _ in range(N)]

for i in range(N):

    matrix[i] = list(map(int,input().split()))

dx = [0,0,1,-1]

dy = [1,-1,0,0]

queue = deque()


def bfs(x,y):

    queue.append((x,y))

    visited[x][y] = True

    count = 1

    while queue:

        a,b = queue.popleft()

        for i in range(4):

            nx = dx[i] + a

            ny = dy[i] + b

            if nx < 0 or nx >= N or ny < 0 or ny >= M:

                continue

            if not visited[nx][ny] and matrix[nx][ny] != 0:

                count +=1

                matrix[nx][ny] = count

                queue.append((nx,ny))

                visited[nx][ny] = True

    return matrix[a][b]

max = 0

count = 0

for p in range(N):

    for q in range(M):

        if matrix[p][q] == 1 and not visited[p][q]:

            value = bfs(p,q)

            count +=1

            if value > max:

                max = value

print(count)

print(max)
