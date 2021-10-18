N = int(input())

code = list(map(int,input().split()))

answer = input()

final = ''

for i in code:

    if i == 0:

        final += ' '

    elif i <= 26:

        final += chr(i+64)

    elif i <= 52:

        final += chr(i+70)

if sorted(final) == sorted(answer):

    print('y')

else:

    print('n')

