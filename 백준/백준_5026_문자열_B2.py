n = int(input())

for _ in range(n):

    word = input().split('+')

    if word[0].isdigit():

        print(int(word[0]) + int(word[1]))

    else:

        print('skipped')
