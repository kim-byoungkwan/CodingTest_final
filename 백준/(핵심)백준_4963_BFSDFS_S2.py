









































###.1

# from collections import deque
#
# dx = [0, 0, 1, -1, 1, 1, -1, -1]
#
# dy = [1, -1, 0, 0, 1, -1, 1, -1]
#
# def bfs(x,y):
#
#     queue.append((x,y))
#
#     while queue:
#
#         current = queue.popleft()
#
#         for i in range(8):
#
#             a = current[0] + dx[i]
#
#             b = current[1] + dy[i]
#
#             if a >= height or b >= width or a < 0 or b < 0:
#
#                 continue
#
#             else:
#
#                 if matrix[x][y] == 1 and matrix[x][y] == matrix[a][b]:
#
#                     if visited[a][b] == False:
#
#                         visited[a][b] = True
#
#                         queue.append((a,b))
#
#
# while True:
#
#     width, height = map(int,input().split())
#
#     if width == 0 and height ==0:
#
#         break
#
#     else:
#
#         matrix = [[] for _ in range(height)]
#
#         for height_value in range(height):
#
#             width_value = list(map(int,input().split()))
#
#             matrix[height_value] = width_value
#
#
#         visited = [[False]*width for _ in range(height)]
#
#         queue = deque()
#
#         count = 0
#
#         for m in range(height):
#
#             for n in range(width):
#
#                 if matrix[m][n] == 0 or visited[m][n] == True:
#
#                     continue
#
#                 else:
#
#                     bfs(m, n)
#
#                     count += 1
#
#         print(count)
