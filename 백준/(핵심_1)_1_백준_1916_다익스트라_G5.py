###.2

import sys

import heapq

input = sys.stdin.readline

N = int(input())

M = int(input())

INF = int(1e9)

distance = [INF]*(N+1)

graph = [[] for _ in range(N+1)]

for _ in range(M):

    a,b,c = map(int, input().split())

    graph[a].append((b,c))


def dijkstra(start):

    h = []

    distance[start] = 0

    heapq.heappush(h,(0,start))

    while h:

        dist, now = heapq.heappop(h)

        if distance[now] < dist:

            continue

        for i in graph[now]:

            cost = dist + i[1]

            if cost < distance[i[0]]:

                distance[i[0]] = cost

                heapq.heappush(h,(cost,i[0]))

start,end = map(int,input().split())

dijkstra(start)

print(distance[end])





































































###.1

# import heapq
#
# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
#
# M = int(input())
#
# INF = int(1e9)
#
# graph = [[] for _ in range(N+1)]
#
# distance = [INF]*(N+1)
#
# for _ in range(M):
#
#     a,b,c = map(int,input().split())
#
#     graph[a].append((b,c))
#
# start, end = map(int,input().split())
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
# print(distance[end])
#
