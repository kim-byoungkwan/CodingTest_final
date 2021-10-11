###.2

import math

total, win = map(int,input().split())

prob = math.floor(100*win/total)

left = 0

right = 1000000000

if prob >= 99:

    print(-1)

else:

    while left <= right:

        middle = (left + right)//2

        total_new = total + middle

        win_new = win + middle

        prob_new = math.floor(100*win_new/total_new)

        if prob < prob_new:

            right = middle-1

        else:

            left = middle + 1

    print(right+1)


# 최종적으로 결정되는 right+1 는 본질적으로 내가 작성한 코드에 따라서, 바로 이전의 middle-1 값과 정확히 동일한 값이다.
# 즉, 직전의 middle 값이 최종적으로 도출해야하는 값이므로, right에 +1을 더해주는 것이다.
# 이분탐색에서 최종적인 값은 항상 중간값이 middle로 결정되는데, 그 표현이 어떻게 표현될지는 상황에 따라 다른 것이다.












































###.1

# import sys
#
# total,win = map(int,sys.stdin.readline().split())
#
# prob_first = int((win/total)*100)
#
# prob_second = prob_first
#
# count = 0
#
# if total == win:
#
#     count = -1
#
# else:
#
#     while prob_first == prob_second:
#
#         count += 1
#
#         total += 1
#
#         win += 1
#
#         prob_second = int((win/total)*100)
#
# print(count)
