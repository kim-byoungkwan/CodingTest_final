import sys

import heapq

input = sys.stdin.readline

INF = int(1e9)

start,end = map(int,input().split())

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

distance = [INF]*(N+1)

for _ in range(M):

    a,b = map(int,input().split())

    graph[a].append((b,1))

    graph[b].append((a,1))


def dijkstra(start,end):

    h = []

    distance[start] = 0

    heapq.heappush(h,(0,start))

    while h:

        dist,now = heapq.heappop(h)

        if distance[now] < dist:

# 아래의 for문이 한타임 반복될 때, 같은 노드에 대한 연결상태가 표현되는 경우가 있는 경우 힙 안에 같은 노드에 대한 최소거리 상태가 여러개 존재할 수 있으므로, 위의 조건을 통해 이러한 상황을 필터링해야한다.
# 즉, distance엔 항상 최소 거리가 할당되어 있지만, heap안에는 최소거리 이전의 아직 반영되지 않은 노드에 대한 거리 값이 존재할 수 있는것이므로 위의 조건이 반드시 필요하다.

            continue

        for i in graph[now]:

            cost = dist + i[1]

            if cost < distance[i[0]]:

                distance[i[0]] = cost

                heapq.heappush(h,(cost,i[0]))

    return distance[end]


answer = dijkstra(start,end)

if answer == INF:

    print(-1)

else:

    print(answer)
