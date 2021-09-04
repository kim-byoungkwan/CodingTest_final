from collections import deque

import sys

K = int(sys.stdin.readline())

stack = deque()

for _ in range(K):

    x = int(sys.stdin.readline())

    if x != 0:

        stack.append(x)

    else:

        stack.pop()

if stack:

    print(sum(stack))

else:

    print(0)
