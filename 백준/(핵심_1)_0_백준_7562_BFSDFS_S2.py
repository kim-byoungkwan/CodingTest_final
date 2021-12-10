from collections import deque

import sys

input = sys.stdin.readline


def bfs(start_x,start_y,end_x,end_y):

    answer = 0

    queue = deque()

    queue.append((start_x,start_y))

    visited[start_x][start_y] = True

    while queue:

        a,b = queue.popleft()

        for i in range(8):

            nx = dx[i] + a

            ny = dy[i] + b

            if nx < 0 or nx > Line-1 or ny < 0 or ny > Line-1:

                continue

            if not visited[nx][ny]:

                matrix[nx][ny] = matrix[a][b] + 1

                visited[nx][ny] = True

                queue.append((nx,ny))

            if (nx,ny) == (end_x,end_y):

                answer = matrix[nx][ny]

                return answer

T = int(input())

for _ in range(T):

    Line = int(input())

    matrix = [[0]*(Line) for _ in range(Line)]

    visited = [[False]*(Line) for _ in range(Line)]


    start_x,start_y = map(int,input().split())

    end_x,end_y = map(int,input().split())


    dx = [2,-2,1,1,-1,-1,2,-2]

    dy = [1,1,2,-2,2,-2,-1,-1]

    print(bfs(start_x,start_y,end_x,end_y))

