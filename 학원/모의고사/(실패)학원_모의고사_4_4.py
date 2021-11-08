from collections import deque

truck_weights = [7,4,5,6]

queue = deque([truck_weights[0]])

print(sum(queue))

count =1

bridge_length = 2

weight = 10


for i in truck_weights:

    count += 1

    if count % 2 ==0:

        queue.popleft()

    if sum(queue) + i <= weight:

        queue.append(i)











