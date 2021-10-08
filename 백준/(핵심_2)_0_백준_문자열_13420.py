###.2

T = int(input())

for _ in range(T):

    S = input().split()

    first = int(S[0])

    second = int(S[2])

    operator = S[1]

    last = int(S[4])

    if operator == '+':

        result = first + second

    elif operator == '-':

        result = first - second

    elif operator == '*':

        result = first * second

    elif operator == '/':

        result = first // second

    if result == last:

        print('correct')

    else:

        print('wrong answer')
























































# ###.1
#
# T = int(input())
#
# for _ in range(T):
#
#     S = input().split('=')
#
#     former = S[0]
#
#     latter = S[1]
#
#     former = former.replace(' ','')
#
#     latter = latter.replace(' ','')
#
#     former_result = 0
#
#     latter_result = int(latter[:])
#
#     if '+' in former:
#
#         former = former.split('+')
#
#         former_result = int(former[0]) + int(former[1])
#
#     elif '-' in former:
#
#         former = former.split('-')
#
#         former_result = int(former[0]) - int(former[1])
#
#     elif '*' in former:
#
#         former = former.split('*')
#
#         former_result = int(former[0]) * int(former[1])
#
#     elif '/' in former:
#
#         former = former.split('/')
#
#         former_result = int(former[0]) // int(former[1])
#
#
#     if former_result == latter_result:
#
#         print('correct')
#
#     else:
#
#         print('wrong answer')
