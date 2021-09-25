from collections import deque

import sys

N = int(sys.stdin.readline())

dict = {}

visited = [False]*(N+1)

adjacency_list =[[] for i in range(N+1)]

for _ in range(N-1):

    a,b = map(int,sys.stdin.readline().split())

    adjacency_list[a].append(b)

    adjacency_list[b].append(a)

def bfs(V):

    queue = deque([V])

    while queue:

        current = queue.popleft()

        visited[current] = True

        for i in adjacency_list[current]:

            if visited[i] == False:

                visited[i] = True

                dict[i] = dict.get(i, 0) + current

                queue.append(i)

    return dict

answer = sorted(bfs(1).items())

for result in answer:

    print(result[1])
