from collections import deque

N,M = map(int,input().split())

matrix = [[] for _ in range(N)]

for i in range(N):

    matrix[i] = list(map(int,input()))

dx = [1,-1,0,0]

dy = [0,0,1,-1]


def bfs(x,y):

    queue = deque()

    queue.append((x,y))

    while queue:

        x,y = queue.popleft()

        for i in range(4):

            nx = dx[i] + x

            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= N or ny >= M:

                continue

            if matrix[nx][ny] == 0:

                continue

            if matrix[nx][ny] == 1:

                matrix[nx][ny] = matrix[x][y] + 1

                queue.append((nx,ny))

    return matrix[N-1][M-1]

print(bfs(0,0))
























#


