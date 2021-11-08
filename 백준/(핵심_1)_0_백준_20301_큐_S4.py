from collections import deque

N,K,M = map(int,input().split())

queue = deque()

for i in range(1,N+1):

    queue.append(i)

count = 0

result = []

for j in range(N):

    count +=1

    queue.rotate(-(K-1))

    result.append(queue.popleft())

    if count == M:

        queue.reverse()

        count = 0

for i in result:

    print(i)