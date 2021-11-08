###.1

from collections import deque

M,N,K = map(int,input().split())

matrix = [[0]*N for _ in range(M)]

for _ in range(K):

    a,b,c,d = map(int,input().split())

    for p in range(b,d):

        for q in range(a,c):

            matrix[p][q] = 1

visited = [[False]*N for _ in range(M)]

dx = [1,-1,0,0]

dy = [0,0,1,-1]


def bfs(x,y):

    count = 1

    queue = deque()

    queue.append((x,y))

    visited[x][y] = True

    while queue:

        (a,b) = queue.popleft()

        for i in range(4):

            nx = dx[i] + a

            ny = dy[i] + b

            if nx <0 or ny <0 or nx >= M or ny >= N:

                continue

            if visited[nx][ny] == False and matrix[nx][ny] == 0:

                queue.append((nx,ny))

                count += 1

                visited[nx][ny] = True

    return count

answer =0

box = []

for r in range(M):

    for s in range(N):

        if visited[r][s] == True or matrix[r][s] ==1:

            continue

        box.append(bfs(r,s))

        answer +=1

print(answer)

print(' '.join(list(map(str,sorted(box)))))

