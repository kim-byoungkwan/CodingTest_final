###.3

import sys

input = sys.stdin.readline

T = int(input())

dict= {

    '1' : [1],

    '2' : [2,4,8,6],

    '3' : [3,9,7,1],

    '4' : [4,6],

    '5' : [5],

    '6' : [6],

    '7' : [7,9,3,1],

    '8' : [8,4,2,6],

    '9' : [9,1],

    '0' : [10]

      }


for _ in range(T):

    a,b = map(int,input().split())

    a = a % 10

    a = str(a)

    if a == '0':

        print(10)

        continue

    index = b % len(dict[a])

    print(dict[a][index-1])








































###.2

# import sys
#
# input = sys.stdin.readline
#
# T = int(input())
#
# for _ in range(T):
#
#     a,b = map(int,input().split())
#
#     print(a**b % 10)











































###.1

# import sys
#
# T = int(sys.stdin.readline())
#
# for _ in range(T):
#
#     a, b = map(int, sys.stdin.readline().split())
#
#     total = a ** b
#
#     index = total % 10
#
#     print(index)



