T = int(input())

for j in range(T):

    word = input()

    result = ''

    for i in word:

        if ord(i) == 90:

            result += 'A'

        else:

            result += chr(ord(i)+1)

    print('String #{}'.format(j+1))

    print(result)

    print()
