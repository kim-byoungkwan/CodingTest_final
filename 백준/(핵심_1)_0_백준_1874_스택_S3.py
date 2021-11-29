N = int(input())

count = 1

stack = []

answer = []

for _ in range(N):

    num = int(input())

    while count <= num:

        stack.append(count)

        answer.append('+')

        count +=1

    if stack[-1] == num:

        stack.pop()

        answer.append('-')

    else:

        answer.append('NO')

        break

if answer[-1] == 'NO':

    print('NO')

else:

    for i in answer:

        print(i)


