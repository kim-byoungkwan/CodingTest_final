## 함수를 사용하면 시간 효율성이 증가한다.


def binary(list_1, list_2):

    for i in list_2:

        start = 0

        end = len(list_1) - 1

        result = 0

        while start <= end:

            mid = (start + end) // 2

            if i > list_1[mid]:

                start = mid + 1

            elif i < list_1[mid]:

                end = mid - 1

            else:

                result = 1

                break

        answer.append(result)

    return answer

import sys

for _ in range(int(sys.stdin.readline())):

    N = int(sys.stdin.readline())

    diary_1 = sorted(list(map(int, sys.stdin.readline().split())))

    M = int(sys.stdin.readline())

    diary_2 = list(map(int, sys.stdin.readline().split()))

    answer = []

    for j in binary(diary_1,diary_2):

        print(j)

