import sys

N = int(sys.stdin.readline())

stack = []

for _ in range(N):

    height = int(sys.stdin.readline())

    if stack:

        if stack[0] <= height:

            while True:

                stack.pop()

                if stack:

                    continue

                else:

                    break

            stack.append(height)


        else:

            while stack[-1] <= height:

                stack.pop()

            stack.append(height)

    else:

        stack.append(height)

print(len(stack))
