S = input()

stack = []

count = 0

for i in S:

    if i == '(':

        stack.append(i)

    else:

        if stack:

            if stack[-1] == '(':

                count += 2

                stack.pop()

        else:

            continue

print(abs(len(S) - count))
