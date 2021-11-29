###.2

import heapq

import sys

input = sys.stdin.readline

INF = int(1e9)

V,E = map(int,input().split())

start = int(input())


graph = [[] for _ in range(V+1)]

distance = [INF]*(V+1)


for _ in range(E):

    a,b,c = map(int,input().split())

    graph[a].append((b,c))


def dijkstra(start):

    h = []

    heapq.heappush(h,(0,start))

    distance[start] = 0

    while h:

        dist, now = heapq.heappop(h)

        if distance[now] < dist:

            continue

        for i in graph[now]:

            cost = dist + i[1]

            if cost < distance[i[0]]:

                distance[i[0]] = cost

                heapq.heappush(h,(cost,i[0]))

dijkstra(start)

for j in range(1,V+1):

    if distance[j] == INF:

        print('INF')

    else:

        print(distance[j])































































###.1

# import heapq
#
# import sys
#
# input = sys.stdin.readline
#
# INF = int(1e9)
#
# V,E = map(int,input().split())
#
# start = int(input())
#
# graph = [[] for _ in range(V+1)]
#
# distance = [INF]*(V+1)
#
# for _ in range(E):
#
#     a,b,c = map(int,input().split())
#
#     graph[a].append((b,c))
#
# def dijkstra(start):
#
#     h = []
#
#     heapq.heappush(h,(0,start))
#
#     distance[start] = 0
#
#     while h:
#
#         dist, now = heapq.heappop(h)
#
#         if distance[now] < dist:
#
#             continue
#
#         for i in graph[now]:
#
#             cost = dist + i[1]
#
#             if cost < distance[i[0]]:
#
#                 distance[i[0]] = cost
#
#                 heapq.heappush(h,(cost,i[0]))
#
# dijkstra(start)
#
# for i in range(1,V+1):
#
#     if distance[i] == INF:
#
#         print("INF")
#
#     else:
#
#         print(distance[i])
#
