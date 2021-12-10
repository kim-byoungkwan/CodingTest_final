import sys

input = sys.stdin.readline

A_score = list(map(int,input().split()))

B_score = list(map(int,input().split()))


A_result = 0

B_result = 0

state = 'D'

for i in range(10):

    if A_score[i] > B_score[i]:

        A_result += 3

        state = 'A'

    elif A_score[i] < B_score[i]:

        B_result += 3

        state = 'B'

    else:

        A_result += 1

        B_result += 1


print(A_result,B_result)


if A_result > B_result:

    print('A')

elif A_result < B_result:

    print('B')

else:

    print(state)



