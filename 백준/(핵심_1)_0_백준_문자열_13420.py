T = int(input())

for _ in range(T):

    S = input().split('=')

    former = S[0]

    latter = S[1]

    former = former.replace(' ','')

    latter = latter.replace(' ','')

    former_result = 0

    latter_result = int(latter[:])

    if '+' in former:

        former = former.split('+')

        former_result = int(former[0]) + int(former[1])

    elif '-' in former:

        former = former.split('-')

        former_result = int(former[0]) - int(former[1])

    elif '*' in former:

        former = former.split('*')

        former_result = int(former[0]) * int(former[1])

    elif '/' in former:

        former = former.split('/')

        former_result = int(former[0]) // int(former[1])


    if former_result == latter_result:

        print('correct')

    else:

        print('wrong answer')
