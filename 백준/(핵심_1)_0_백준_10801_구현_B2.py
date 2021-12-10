import sys

input = sys.stdin.readline

A_list = list(map(int,input().split()))

B_list = list(map(int,input().split()))

result = []

for i in range(10):

    if A_list[i] > B_list[i]:

        result.append('a')

    elif A_list[i] < B_list[i]:

        result.append('b')

    else:

        continue

A_count = result.count('a')

B_count = result.count('b')


if A_count > B_count:

    print('A')

elif A_count < B_count:

    print('B')

else:

    print('D')


