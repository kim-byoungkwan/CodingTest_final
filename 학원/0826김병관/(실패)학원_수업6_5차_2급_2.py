from collections import deque


time_table = [1,1,0,0,1,0,1,0,0,0]

queue = deque(time_table)


print(queue)



def solution(time_table):

    box = []

    queue = deque(time_table)

    while True:

        out = queue.pop()

        if out == 0:

            continue

        else:

            box.append(out)





