###.1

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    number = list(input().rstrip())

    number_reverse = number[::-1]

    number = int(''.join(number))

    number_reverse = int(''.join(number_reverse))

    total = number + number_reverse

    total_list = []

    while total:

        value = total % 10

        total = total // 10

        total_list.append(value)

    total_list_reverse = total_list[::-1]

    answer = 'YES'

    for i in range(len(total_list)):

        if total_list[i] != total_list_reverse[i]:

            answer = 'NO'

    print(answer)








