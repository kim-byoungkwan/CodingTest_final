N = int(input())

count = 0

for _ in range(N):

    stack = []

    word_list = list(input())

    for i in word_list:

        if stack:

            if stack[-1] != i:

                stack.append(i)

            else:

                stack.pop()

        else:

            stack.append(i)

    if stack:

        stack = []

        continue

    else:

        count += 1

print(count)
