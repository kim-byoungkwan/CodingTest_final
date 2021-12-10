import sys

input = sys.stdin.readline

box = sorted(list(map(int,input().split())))

A = box[0]

B = box[1]

C = box[2]


seq = list(input().rstrip())


for i in seq:

    if i == 'A':

        print(A, end =' ')

    elif i == 'B':

        print(B, end = ' ')

    else:

        print(C, end = ' ')
