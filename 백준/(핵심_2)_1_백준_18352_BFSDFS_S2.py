###.2

import sys

from collections import deque

N,M,K,X = map(int,sys.stdin.readline().split())

adjacency_list = [[] for _ in range(N+1)]

for _ in range(M):

    a,b = map(int,sys.stdin.readline().split())

    adjacency_list[a].append(b)

visited = [-1]*(N+1)

def bfs(X):

    queue = deque()

    queue.append(X)

    visited[X] = 0

    while queue:

        current = queue.popleft()

        for i in adjacency_list[current]:

            if visited[i] == -1:

                queue.append(i)

                visited[i] = visited[current] + 1

    return visited

answer = []

for index,value in enumerate(bfs(X)):

    if value == K:

        answer.append(index)

if answer:

    for i in answer:

        print(i)

else:

    print(-1)














































###.1

# from collections import deque
#
# import sys
#
# N,M,K,X = map(int,sys.stdin.readline().split())
#
# adjacency_list = [[] for _ in range(N+1)]
#
#
# for i in range(M):
#
#     a,b = map(int,sys.stdin.readline().split())
#
#     adjacency_list[a].append(b)
#
#
# visited = [-1]*(N+1)
#
#
# queue = deque([X])
#
# visited[X] = 0
#
# while queue:
#
#     current = queue.popleft()
#
#     for i in adjacency_list[current]:
#
#         if visited[i] == -1:
#
#             visited[i] = visited[current] + 1
#
#             queue.append(i)
#
#
# if K in visited:
#
#     for index,value in enumerate(visited):
#
#         if value == K:
#
#             print(index)
#
# else:
#
#     print(-1)
