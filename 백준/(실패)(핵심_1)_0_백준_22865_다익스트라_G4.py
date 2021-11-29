###.1

import sys

import heapq

input = sys.stdin.readline

N = int(input())

A,B,C = map(int,input().split())

M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):

    a,b,c = map(int,input().split())

    graph[a].append((b,c))

    graph[b].append((a,c))

def dijkstra(start):

    INF = int(1e9)

    distance = [INF] * (N + 1)

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

    return distance

answer = []

for start in range(1,N+1):

    answer.append((start,sorted(dijkstra(start))[1]))

print(sorted(answer,key=lambda x : (-x[1],x[0]))[0][0])


























