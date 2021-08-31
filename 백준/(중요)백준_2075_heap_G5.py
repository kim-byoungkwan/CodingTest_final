###.1

# import heapq
#
# import sys
#
# heap = []
#
# box = []
#
# N = int(sys.stdin.readline())
#
# for i in range(N):
#
#     for j in map(int,sys.stdin.readline().split()):
#
#         heapq.heappush(heap,-j)
#
# for k in range(N):
#
#     box.append(-heapq.heappop(heap))
#
# print(box[-1])

###.2

import heapq

import sys

heap = []

N = int(sys.stdin.readline())

for _ in range(N):

    for i in map(int,sys.stdin.readline().split()):

        heapq.heappush(heap,i)

        while len(heap) > N:

            heapq.heappop(heap)

print(heapq.heappop(heap))

