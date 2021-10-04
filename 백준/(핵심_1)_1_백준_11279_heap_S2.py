import heapq

import sys

heap = []

N = int(sys.stdin.readline())

for i in range(N):

    x = int(sys.stdin.readline())

    if x:

        heapq.heappush(heap,-x)

    else:

        try:

            print(-heapq.heappop(heap))

        except:

            print(0)

