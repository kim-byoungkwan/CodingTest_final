import heapq

heap = []

array = []

N = int(input())

for i in range(N):

    num = int(input())

    heapq.heappush(heap,-num)


for _ in range(len(heap)):

    try:

        out = -heapq.heappop()

    if out == 0:

        if len(h) == 0:

            print(0)

    else:

        print(out)

