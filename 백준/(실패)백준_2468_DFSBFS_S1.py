from collections import deque

import copy

N = int(input())

matrix = []

for i in range(N):

    matrix.append(list(map(int,input().split())))

matrix_temp = copy.deepcopy(matrix)

max_num = 0

for m in range(N):

    for n in range(N):

        if max_num < matrix[m][n]:

            max_num = matrix[m][n]

        else:

            continue

matrix_box = []

for k in range(1,max_num+1):

    for g in range(N):

        for h in range(N):

            if matrix[g][h] <= k:

                matrix[g][h] = 0

            else:

                matrix[g][h] = 1

    matrix_box.append(matrix)

    matrix = matrix_temp

print(matrix_box)











