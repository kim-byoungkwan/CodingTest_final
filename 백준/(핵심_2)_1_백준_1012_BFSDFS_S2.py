###.2

from collections import deque

T = int(input())

for _ in range(T):

    M,N,K = map(int,input().split())

    matrix = [[0]*M for _ in range(N)]

    for _ in range(K):

        X,Y = map(int,input().split())

        matrix[Y][X] = 1


    visited = [[False]*M for _ in range(N)]

    dx = [1,-1,0,0]

    dy = [0,0,1,-1]


    def bfs(x,y):

        queue = deque()

        queue.append((x,y))

        visited[x][y] = True

        while queue:

            (a,b) = queue.popleft()

            for i in range(4):

                nx = dx[i] + a

                ny = dy[i] + b

                if nx < 0 or ny < 0 or nx >= N or ny >= M:

                    continue

                else:

                    if visited[nx][ny] == False and matrix[nx][ny] == 1:

                        queue.append((nx,ny))

                        visited[nx][ny] = True

    count = 0

    for p in range(N):

        for q in range(M):

            if visited[p][q] == True or matrix[p][q] == 0:

                continue

            bfs(p,q)

            count +=1

    print(count)





















































###.1

# import sys
#
# sys.setrecursionlimit(10000)
#
# def dfs(x,y):
#
#     if x < 0 or x > N-1 or y < 0 or y > M-1:
#
#         return False
#
#     if matrix[x][y] == 1:
#
#         matrix[x][y] = 0
#
#         dfs(x+1,y)
#
#         dfs(x-1,y)
#
#         dfs(x,y+1)
#
#         dfs(x,y-1)
#
#         return True
#
#     return False
#
#
#
# T = int(input())
#
# for m in range(T):
#
#     M,N,K = map(int,input().split())
#
#     matrix = [[0]*M for i in range(N)]
#
#     for i in range(K):
#
#         a,b = map(int,input().split())
#
#         matrix[b][a] = 1
#
#     count = 0
#
#     for i in range(M):
#
#         for j in range(N):
#
#             if dfs(j,i) == True:
#
#                 count += 1
#
#             else:
#
#                 continue
#
#     print(count)

