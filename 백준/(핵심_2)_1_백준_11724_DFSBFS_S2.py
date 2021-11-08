###.2


from collections import deque

import sys

N,M = map(int,sys.stdin.readline().split())

adjacency_list = [[] for _ in range(N+1)]

for _ in range(M):

    u,v = map(int,sys.stdin.readline().split())

    adjacency_list[u].append(v)

    adjacency_list[v].append(u)

visited = [False]*(N+1)

def bfs(V):

    queue = deque()

    queue.append(V)

    visited[V] = True

    while queue:

        current = queue.popleft()

        for i in adjacency_list[current]:

            if visited[i] == False:

                queue.append(i)

                visited[i] = True

count = 0

for p in range(1,N+1):

    if visited[p] == True:

        continue

    bfs(p)

    count += 1

print(count)
























































###.1

# from collections import deque
#
# N,M = map(int,sys.stdin.readline().split())
#
# adjacency_list = [[] for _ in range(N+1)]
#
# for _ in range(M):
#
#     a,b = map(int,sys.stdin.readline().split())
#
#     adjacency_list[a].append(b)
#
#     adjacency_list[b].append(a)
#
# visited = [0]*(N+1)
#
#
# def bfs(V):
#
#     count = 0
#
#     queue = deque([V])
#
#     while queue:
#
#         current = queue.popleft()
#
#         for i in adjacency_list[current]:
#
#             if visited[i] == 0:
#
#                 queue.append(i)
#
#                 visited[i] = 1
#
#                 count += 1
#
#     return count
#
# answer = 0
#
# ##.Q 이부분에서 어떤 반례가 존재하게 되는 것일가?
#
# for m in range(1,N+1):
#
#     x = bfs(m)
#
#     if x != 0:
#
#         answer += 1
#
#     else:
#
#         continue
#
# print(answer)


###.sol

# from collections import deque
#
# import sys
#
# N,M = map(int,sys.stdin.readline().split())
#
# adjacency_list = [[] for _ in range(N+1)]
#
# for _ in range(M):
#
#     a,b = map(int,sys.stdin.readline().split())
#
#     adjacency_list[a].append(b)
#
#     adjacency_list[b].append(a)
#
# visited = [0]*(N+1)
#
#
# def bfs(V):
#
#     queue = deque([V])
#
#     while queue:
#
#         current = queue.popleft()
#
#         for i in adjacency_list[current]:
#
#             if visited[i] == 0:
#
#                 queue.append(i)
#
#                 visited[i] = 1
#
#
# answer = 0
#
# for m in range(1,N+1):
#
#     if visited[m] == 0:
#
#         bfs(m)
#
#         answer += 1
#
# print(answer)
