import sys

from collections import deque

input = sys.stdin.readline

N = int(input())

start_x,start_y,end_x,end_y = map(int,input().split())

matrix = [[0]*N for _ in range(N)]

visited = [[False]*(N) for _ in range(N)]

queue = deque()

dx = [-2,-2,0,0,2,2]

dy = [-1,1,-2,2,-1,1]


def bfs(x,y,p,q):

    queue.append((x,y))

    visited[x][y] = True

    while queue:

        a,b = queue.popleft()

        for i in range(6):

            nx = dx[i] + a

            ny = dy[i] + b

            if nx < 0 or nx >= N or ny < 0 or ny >= N:

                continue

            if not visited[nx][ny]:

                matrix[nx][ny] = matrix[a][b] + 1

                queue.append((nx,ny))

                visited[nx][ny] = True

            if (nx,ny) == (p,q):

                return matrix[nx][ny]

    return -1


print(bfs(start_x,start_y,end_x,end_y))



