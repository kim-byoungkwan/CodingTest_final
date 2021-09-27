word = list(input())

print(word)

stack = []

answer = []

result = []

for i in word:

    if i == '(':

        stack.append(i)

    elif i == ')':

        stack.pop()

        answer.append(2)

        answer.append(0)

    elif i == '[':

        stack.append(i)

    else:

        stack.pop()

        answer.append(3)

        answer.append(0)

    if len(stack) ==0:

        answer.append(0)

print(stack)

print(answer)

