N = int(input())

matrix = [[] for _ in range(N)]

for i in range(N):

    matrix[i] = list(input())

K = int(input())

if K == 1:

    for i in range(len(matrix)):

        print(''.join(matrix[i]))

elif K == 2:

    for i in range(len(matrix)):

        print(''.join(matrix[i][::-1]))

else:

    for i in range(len(matrix)):

        print(''.join(matrix[-i-1]))
