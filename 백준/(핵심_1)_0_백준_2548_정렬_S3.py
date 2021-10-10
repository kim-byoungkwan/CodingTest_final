###.2

import sys

N = int(sys.stdin.readline())

arr = sorted(list(map(int,sys.stdin.readline().split())))

result_1 = []

result_2 = []

if len(arr) % 2 ==0:

    middle_1 = arr[len(arr)//2]

    middle_2 = arr[(len(arr)//2)-1]

    for i in arr:

        result_1.append(abs(middle_1 - i))

        result_2.append(abs(middle_2 - i))

    answer = min(sum(result_1),sum(result_2))

    if answer == middle_1:

        print(middle_1)

    else:

        print(middle_2)

else:

    middle_1 = arr[len(arr)//2]

    print(middle_1)















































###.1

# import sys
#
# N = int(sys.stdin.readline())
#
# arr = list(map(int,sys.stdin.readline().split()))
#
# dict = {}
#
# for i in range(len(arr)):
#
#     answer = 0
#
#     for j in range(len(arr)):
#
#         if i == j:
#
#             continue
#
#         else:
#
#             answer += abs(arr[i] - arr[j])
#
#     dict[arr[i]] = answer
#
# print(sorted(dict.items(),key=lambda x: (x[1],x[0]))[0][0])
