from collections import deque

import copy

import sys

N = int(sys.stdin.readline())

matrix = [list(sys.stdin.readline()) for i in range(N)]

visited = [[0]*N for m in range(N)]

visited_new = copy.deepcopy(visited)


dx = [1,-1,0,0]

dy = [0,0,1,-1]

def bfs(x,y,color):

    queue = deque()

    queue.append((x,y))

    visited[x][y] = 1

    while queue:

        a,b = queue.popleft()

        for k in range(4):

            nx = a + dx[k]

            ny = b + dy[k]

            if nx >= N or nx < 0 or ny >= N or ny < 0:

                continue

            else:

                if visited[nx][ny] == 0 and matrix[nx][ny] == color:

                    visited[nx][ny] = visited[a][b] + 1

                    queue.append((nx,ny))


count = 1

box = []

box_2 = []

for i in range(N):

    for j in range(N):

        if visited[i][j] == 0:

            color = matrix[i][j]

            bfs(i,j,color)

            box.append(count)


for m in range(N):

    for n in range(N):

        if matrix[m][n] == "R":

            matrix[m][n] = "G"

visited = visited_new


for p in range(N):

    for q in range(N):

        if visited[p][q] == 0:

            color = matrix[p][q]

            bfs(p,q,color)

            box_2.append(count)

print(sum(box),end=' ')

print(sum(box_2))
