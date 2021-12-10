###.2

import sys

from collections import deque

input = sys.stdin.readline

queue = deque()

N,K = map(int,input().split())

max = 10**5

distance = [0]*(max+1)

def bfs(start,end):

    if start == end:

        return 0

    queue.append(start)

    distance[start] = 0

    while queue:

        position = queue.popleft()

        for dx in (position-1, position+1, position*2):

            if dx < 0 or dx > max or distance[dx]:

                continue

            distance[dx] = distance[position] +1

            queue.append(dx)

            if dx == end:

                return distance[dx]

print(bfs(N,K))
































###.1

# import sys
#
# import heapq
#
# input = sys.stdin.readline
#
# N,K = map(int,input().split())
#
# h = []
#
# def bfs(N,K):
#
#     count = 0
#
#     heapq.heappush(h,(count,N))
#
#     while h:
#
#         count,value = heapq.heappop(h)
#
#         count += 1
#
#         for i in [value-1,value+1,value*2]:
#
#             if i < 0 or i > 100000:
#
#                 continue
#
#             if i == K:
#
#                 return count
#
#             heapq.heappush(h,(count,i))
#
# print(bfs(N,K))

