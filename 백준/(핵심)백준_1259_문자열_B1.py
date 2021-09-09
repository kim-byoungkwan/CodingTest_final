from collections import deque


while True:

    number_first = input()

    number_list = list(number_first)

    stack = []

    queue = deque()

    if number_first == '0':

        break

    else:

        for i in number_list:

            stack.append(i)

            queue.append(i)

        for _ in range(len(stack)):

            stack_out = stack.pop()

            queue_out = queue.popleft()

            if stack_out == queue_out:

                continue

            else:

                print("no")

                break

    if stack:

        continue

    else:

        print("yes")
