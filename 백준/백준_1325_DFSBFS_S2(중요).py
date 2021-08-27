###.1

# import sys
#
# from collections import deque
#
# N,M = map(int,sys.stdin.readline().split())
#
# adjacency_list = [[] for i in range(N+1)]
#
# for i in range(M):
#
#     a,b = map(int,sys.stdin.readline().split())
#
#     adjacency_list[b].append(a)
#
#
# def dfs(start):
#
#     visited = [0]*(N+1)
#
#     count = 0
#
#     stack = deque([start])
#
#     while stack:
#
#         current = stack.pop()
#
#         visited[current] = 1
#
#         for i in adjacency_list[current]:
#
#             if visited[i] == 0:
#
#                 stack.append(i)
#
#                 count = count + 1
#
#     return count
#
# result = []
#
# for j in range(1,N+1):
#
#     output = dfs(j)
#
#     result.append(output)
#
# max_count = 0
#
# box = []
#
# for i in range(N):
#
#     if max_count <= result[i]:
#
#         max_count = result[i]
#
#         box.append(i+1)
#
#     else:
#
#         continue
#
# for m in sorted(box):
#
#     print(m, end=' ')

###.2

import sys

from collections import deque

N,M = map(int,sys.stdin.readline().split())

adjacency_list = [[] for i in range(N+1)]

for i in range(M):

    a,b = map(int,sys.stdin.readline().split())

    adjacency_list[b].append(a)


def bfs(start):

    queue = deque([start])

    visited = [0] * (N + 1)

    visited[start] = 1

    count = 0

    while queue:

        current = queue.popleft()

        count = count + 1

        for i in adjacency_list[current]:

            if visited[i] == 0:

                visited[i] = 1

                queue.append(i)

            else:

                continue

    return count

result = []

for m in range(1,N+1):

    output = bfs(m)

    result.append(output)


for index,value in enumerate(result):

    if value == max(result):

        print(index+1,end=' ')


# 방문처리를 하는 코드는 반드시 큐에 방문할 노드를 집어넣기 전해줘야 한다. 이렇게 하지 않을 경우 간선관계가 많은 노드, 즉 인기가 많은 노드가 중복적으로 큐에 담겨서 중복 방문하는 것처럼 표시되는 잘못된 경우가 발생할 수 있다.
# 반례: 1->2,1->3,1->4,2->5,3->5,4->5,5->6,5->7 과 같이 5노드가 다른 노드와의 간선 관계까 많이 형성되어 있을 때, 5노드가 큐에 담기기전에 방문처리를 하지 않게 되면, 5가 큐에 담기고 나서도 방문처리가 아직 안된상황이 발생하여 5가 중복하여 담겨질 수 있다.













