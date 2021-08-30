# 파이썬에서는 Heap 기능을 위해 heapq 라이브러리를 제공함

# heapq는 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 사용됨

import heapq

def heapsort(iterable):

    h = []

    result = []

    # 모든 원소를 차례대로 힙에 삽입

    for value in iterable:

        heapq.heappush(h, -value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기

    for _ in range(len(h)):

        result.append(-heapq.heappop(h))

    return result


result = heapsort([1,3,5,7,9,2,4,6,8,0])

print(result)
