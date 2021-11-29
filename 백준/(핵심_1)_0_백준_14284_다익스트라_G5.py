import sys

import heapq

input = sys.stdin.readline

INF = int(1e9)

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

distance = [INF]*(N+1)

for _ in range(M):

    a,b,c = map(int,input().split())

    graph[a].append((b,c))

    graph[b].append((a,c))


def dijkstra(start,end):

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

    return distance[end]

start,end = map(int,input().split())

print(dijkstra(start,end))


