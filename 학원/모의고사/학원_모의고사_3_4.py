import heapq

def solution(scoville,K):

    result = 0

    heap = []

    for i in scoville:

        heapq.heappush(heap,i)

    count = 0

    while heap[0] < K:

        first = heapq.heappop(heap)

        second = heapq.heappop(heap)

        third = first + second*2

        heapq.heappush(heap, third)

        count += 1

    return count

scoville = [1,2,3,9,10,12]

K = 7

print(solution(scoville,K))







