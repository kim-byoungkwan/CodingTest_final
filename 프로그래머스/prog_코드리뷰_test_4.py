import sys

import heapq

def solution(N,road,K):

    INF = int(1e9)

    matrix = [[] for _ in range(N+1)]

    distance = [INF]*(N+1)

    for i in road:

        matrix[i[0]].append((i[1],i[2]))

        matrix[i[1]].append((i[0],i[2]))

    h = []

    start = 1

    distance[start] = 0

    heapq.heappush(h,(0,start))

    while h:

        dist,node = heapq.heappop(h)

        if dist > distance[node]:

            continue

        for i in matrix[node]:

            cost = dist + i[1]

            if cost < distance[i[0]]:

                distance[i[0]] = cost

                heapq.heappush(h,(cost,i[0]))

    count = 0

    for value in distance:

        if value <= K:

            count +=1

    return count

N = 6

road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]

K = 4

print(solution(N,road,K))