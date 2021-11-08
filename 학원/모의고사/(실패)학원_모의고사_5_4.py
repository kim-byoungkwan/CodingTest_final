import heapq

h = []

def solution(operations):

    for m in range(operations):

        if "D-" in m:

            heapq.heappop(h,int(m[-1]))











