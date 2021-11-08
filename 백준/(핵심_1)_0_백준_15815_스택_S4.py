S = input()

stack = []

for i in S:

    if i.isdigit():

        stack.append(int(i))

    else:

        if i == '+':

            first = stack.pop()

            second = stack.pop()

            third = second + first

            stack.append(third)

        elif i == '-':

            first = stack.pop()

            second = stack.pop()

            third = second - first

            stack.append(third)

        elif i =='*':

            first = stack.pop()

            second = stack.pop()

            third = second * first

            stack.append(third)

        elif i =='/':

            first = stack.pop()

            second = stack.pop()

            third = second // first

            stack.append(third)

print(stack[0])

