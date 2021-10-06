standard = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

T= int(input())

for _ in range(T):

    result = ''

    S = input()

    for i in standard:

        if i in S:

            continue

        else:

            result += i

    answer = 0

    for i in result:

        answer += ord(i)

    print(answer)
