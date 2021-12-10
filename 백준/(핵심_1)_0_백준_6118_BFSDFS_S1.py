import sys

from collections import deque

queue = deque()

input = sys.stdin.readline

N,M = map(int,input().split())

adjacency_list = [[] for _ in range(N+1)]

for _ in range(M):

    A_i,B_i = map(int,input().split())

    adjacency_list[A_i].append(B_i)

    adjacency_list[B_i].append(A_i)

distance = [0]*(N+1)

def bfs(start):

    queue.append(start)

    distance[start] = 0

    while queue:

        position = queue.popleft()

        for dx in adjacency_list[position]:

            if dx == start or distance[dx]:

                continue

            distance[dx] = distance[position] + 1

            queue.append(dx)

    return distance

result = bfs(1)

max_dist = max(result)

max_position = result.index(max_dist)

max_count = result.count(max_dist)

print(max_position,max_dist,max_count)
