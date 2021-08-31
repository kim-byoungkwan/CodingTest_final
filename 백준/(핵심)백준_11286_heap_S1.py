import sys

import heapq

heap = []

N = int(sys.stdin.readline())

for i in range(N):

    x = int(sys.stdin.readline())

    if x:

        heapq.heappush(heap,(abs(x),x))

    else:

        try:

            print(heapq.heappop(heap)[1])

        except:

            print(0)