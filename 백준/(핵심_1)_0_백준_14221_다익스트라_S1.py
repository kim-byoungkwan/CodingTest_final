import sys

import heapq

INF = int(1e9)

input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]


for _ in range(M):

    a,b,c = map(int,input().split())

    graph[a].append((b,c))

    graph[b].append((a,c))


def dijkstra(start):

    distance = [INF] * (N + 1)

    h = []

    distance[start] = 0

    heapq.heappush(h,(0,start))

    while h:

        dist,now = heapq.heappop(h)

        if distance[now] < dist:

            continue

        for i in graph[now]:

            cost = dist + i[1]

            if cost < distance[i[0]]:

                distance[i[0]] = cost

                heapq.heappush(h,(cost,i[0]))

    return distance

p,q = map(int,input().split())


home = list(map(int,input().split()))

gs = list(map(int,input().split()))


result = INF

for h in home:

    sample_list = dijkstra(h)

    for g in gs:

        low_value = sample_list[g]

        if result > low_value:

            result = low_value

            index = h

print(index)


