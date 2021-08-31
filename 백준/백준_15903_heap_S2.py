import sys

import heapq

heap = []

n,m = map(int,sys.stdin.readline().split())

array = list(map(int,sys.stdin.readline().split()))


out = 0

if m == 0:

    print(sum(array))

else:

    for k in range(m):

        array.sort(reverse=True)

        for i in range(2):

            one_out = array.pop()

            out = out + one_out

        for j in range(2):

            array.append(out)

        out = 0

        heapq.heappush(heap,-sum(array))

    print(-heapq.heappop(heap))


