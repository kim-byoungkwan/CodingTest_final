from collections import deque

n = int(input())

standard_input = []

stack = []

for _ in range(n):

    standard_input.append(int(input()))

queue = deque(standard_input)


for i in range(1,n+1):

    if i != queue[0]:

        stack.append(i)

        print('+')

    else:

        queue.popleft()

        stack.append(i)

        print('+')

        stack.pop()

        print('-')

        if len(stack) != 0 and len(queue) !=0:

            while True:

                if stack[-1] == queue[0]:

                    queue.popleft()

                    stack.pop()

                    print('-')

                else:

                    if i == n:

                        print("NO")

                        break

                    else:

                        continue

        else:

            break
