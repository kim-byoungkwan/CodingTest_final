from collections import deque

queue = deque()

N = int(input())

for i in range(1,N+1):

    queue.append(i)

result = []

while queue:

    result.append(queue.popleft())

    queue.rotate(-1)

print(' '.join(list(map(str,result))))







