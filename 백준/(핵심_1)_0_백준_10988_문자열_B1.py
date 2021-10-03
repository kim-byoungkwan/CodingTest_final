from collections import deque

word = input()

stack = []

queue = deque()

result = 0

for i in word:

    stack.append(i)

    queue.append(i)

while len(stack) !=0:

    word_stack = stack.pop()

    word_queue = queue.popleft()

    if word_stack == word_queue:

        continue

    else:

        result = 1

        break


if result == 1:

    print(0)

else:

    print(1)


