###.2

from collections import deque

N = int(input())

matrix = [[] for _ in range(N)]

for i in range(N):

    matrix[i] = list(map(int,input()))

dx = [1,-1,0,0]

dy = [0,0,1,-1]

visited = [[False]*N for _ in range(N)]

def bfs(x,y):

    queue = deque()

    queue.append((x,y))

    count = 0

    while queue:

        count +=1

        (a,b) = queue.popleft()

        matrix[a][b] = count

        if matrix[a][b] == 0:

            continue

        else:

            visited[a][b] = True

            for i in range(4):

                nx = dx[i] + a

                ny = dy[i] + b

                if nx < 0 or ny < 0 or nx >= N or ny >= N:

                    continue

                else:

                    if visited[nx][ny] == False and matrix[nx][ny] == 1:

                        queue.append((nx,ny))

                        visited[nx][ny] = True

    return count

answer = 0

final = []

for m in range(N):

    for n in range(N):

        if matrix[m][n] == 0 or visited[m][n] == True:

            continue

        final.append(bfs(m,n))

        answer += 1

print(answer)

for k in sorted(final):

    print(k)
















































###.1

# N = int(input())
#
# adjacency_matrix = [list(map(int,input())) for i in range(N)]
#
# def dfs(x,y):
#
#     global count
#
#     if x < 0 or x > N-1 or y < 0 or y > N-1:
#
#         return False
#
#     if adjacency_matrix[x][y] == 1:
#
#         adjacency_matrix[x][y] = 0
#
#         count = count + 1
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
# count = 0
#
# result = 0
#
# box = []
#
# for i in range(N):
#
#     for j in range(N):
#
#         if dfs(i,j) == True:
#
#             result = result + 1
#
#             box.append(count)
#
#             count = 0
#
#
# print(result)
#
# box.sort()
#
# for i in box:
#
#     print(i)

# return이 발생하는 순간 전역변수에 저장된 값은 초기화 시키지 않는 이상 그대로 유지된다.



