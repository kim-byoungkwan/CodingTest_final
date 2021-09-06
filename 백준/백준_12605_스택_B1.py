N = int(input())

stack = []



for j in range(1,N+1):

    answer = ''

    word_list = input().split()

    for i in word_list:

        stack.append(i)

    for _ in range(len(stack)):

        answer = answer + stack.pop() + ' '

    print('Case #{0}: {1}'.format(j,answer))
