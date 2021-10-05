import heapq

n = int(input())

heap = []

for _ in range(n):

    gift = list(map(int, input().split()))

    if gift[0] == 0:

        if heap:

            print(-heapq.heappop(heap))

        else:

            print(-1)

    else:

        for i in gift[1:]:

            heapq.heappush(heap,-i)
