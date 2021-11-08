###.2

from collections import deque

N = int(input())

M = int(input())

adjacency_list = [[] for _ in range(N+1)]

for _ in range(M):

    a,b = map(int,input().split())

    adjacency_list[a].append(b)

    adjacency_list[b].append(a)

visited = [False]*(N+1)

def bfs(V):

    queue = deque()

    queue.append(V)

    count = 0

    while queue:

        current = queue.popleft()

        visited[current] = True

        for i in adjacency_list[current]:

            if visited[i] == False:

                queue.append(i)

                visited[i] = True

                count +=1

    return count

print(bfs(1))



























































###.1

# from collections import deque
#
# N = int(input())
#
# M = int(input())
#
#
# matrix = [[0]*(N+1) for i in range(N+1)]
#
# for i in range(M):
#
#     a,b = map(int,input().split())
#
#     matrix[a][b] = matrix[b][a] = 1
#
#
# queue = deque([1])
#
# visited_list = [0]*(N+1)
#
# visited_list[1] = 1
#
#
# while queue:
#
#     current = queue.popleft()
#
#     for i in range(1,N+1):
#
#         if visited_list[i] == 0 and matrix[current][i] == 1:
#
#             queue.append(i)
#
#             visited_list[i] = 1
#
#
# print(sum(visited_list)-1)
#

