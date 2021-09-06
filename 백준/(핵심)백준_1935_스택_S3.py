N = int(input())

word = list(input())

dict = {}

for i in range(N):

     dict[chr(65+i)] = int(input())

stack = []

calculator = ''

for i in word:

    if i.isalpha():

        stack.append(i)

    else:

        x_1 = stack.pop()

        x_2 = stack.pop()

        operater = i

        if operater == '+':

            output = (dict.get(x_2,x_2) + dict.get(x_1,x_1))

        elif operater == '-':

            output = (dict.get(x_2,x_2) - dict.get(x_1,x_1))

        elif operater == '*':

            output = (dict.get(x_2,x_2) * dict.get(x_1,x_1))

        else:

            output = (dict.get(x_2,x_2) / dict.get(x_1,x_1))

        stack.append(output)

print('%.2f' % stack.pop())


