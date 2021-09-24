###.1

# N = int(input())
#
# me,relative = map(int,input().split())
#
# num_rel = int(input())
#
#
# adjacency_list = [[] for _ in range(N+1)]
#
#
# for _ in range(num_rel):
#
#     A,B = map(int,input().split())
#
#     adjacency_list[A].append(B)
#
#     adjacency_list[B].append(A)
#
#     adjacency_list[A].sort()
#
#     adjacency_list[B].sort()
#
# print(adjacency_list)
#
# visited = [False] * (N + 1)
#
# def dfs(V):
#
#     stack = [V]
#
#     visited[V] = True
#
#     record = []
#
#     while stack:
#
#         current = stack.pop()
#
#         record.append(current)
#
#         for i in adjacency_list[current]:
#
#             if visited[i] == False:
#
#                 visited[i] = True
#
#                 stack.append(i)
#
#     return record
#
#
# for i in range(1,N+1):
#
#     if visited[i] == False:
#
#         print(dfs(i))
#
#     else:
#
#         continue


###.2

from collections import deque

n = int(input())

me,relatives = map(int,input().split())

m = int(input())

adjacency_list = [[] for _ in range(n+1)]

visited = [False]*(n+1)

record = [0]*(n+1)


for _ in range(m):

    A,B = map(int,input().split())

    adjacency_list[A].append(B)

    adjacency_list[B].append(A)


def bfs(V):

    count = 0

    queue = deque([V])

    visited[V] = True

    while queue:

        current = queue.popleft()

        count = record[current]

        count += 1

        for i in adjacency_list[current]:

            if visited[i] == False:

                visited[i] = True

                record[i] = count

                queue.append(i)

    return record


result = bfs(me)[relatives]

if result !=0:

    print(result)

else:

    print(-1)


