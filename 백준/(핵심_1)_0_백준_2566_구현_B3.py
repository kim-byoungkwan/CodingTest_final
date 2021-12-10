matrix = [[] for _ in range(9)]

for i in range(9):

    matrix[i] = list(map(int,input().split()))

max_value = 0

answer = []

for j in range(9):

    if max_value < max(matrix[j]):

        max_value = max(matrix[j])

        index = matrix[j].index(max_value)

        answer = [j+1,index+1]

print(max_value)

print(' '.join(list(map(str,answer))))