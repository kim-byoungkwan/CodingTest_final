T = int(input())



for _ in range(T):

    stack = []

    box = []

    word = list(input())

    for i in word:

        if i == '(':

            stack.append(i)

        else:

            if stack:

                stack.pop()

            else:

                box.append("NO")

                break

    if len(box) == 0 and len(stack) == 0:

        print("YES")

    else:

        print("NO")

