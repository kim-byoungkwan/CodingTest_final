from collections import deque

N,M = map(int,input().split())

matrix = [[] for _ in range(N)]

for i in range(N):

    arr = list(map(int,input().split()))

    matrix[i] = arr

distance = [[False]*M for _ in range(N)]

visited = [[False]*M for _ in range(N)]

queue = deque()

dx = [0,0,1,-1,1,1,-1,-1]

dy = [1,-1,0,0,1,-1,1,-1]


def bfs(x,y):

    count = 0

    visited[x][y] = True

    queue.append((x,y))

    while queue:

        current = queue.popleft()

        for i in range(8):

            row_y = current[0] + dy[i]

            column_x = current[1] + dx[i]

            if row_y < 0 or row_y >= N or column_x < 0 or column_x >=M:

                continue

            else:

                if visited[row_y][column_x] == False:

                    if matrix[current[0]][current[1]] == 0 and matrix[row_y][column_x] == 1:

                        count += 1

                        distance[current[0]][current[1]] = count

                        count = 0

                    elif matrix[current[0]][current[1]] == 0 and matrix[row_y][column_x] == 0:

                            visited[row_y][column_x] = True

                            queue.append((row_y,column_x))

                    else:

                        continue

for i in range(N):

    for j in range(M):

        if matrix[i][j] == 1 or visited[i][j] == True:

            continue

        else:

            bfs(i,j)

print(visited)

print(distance)






