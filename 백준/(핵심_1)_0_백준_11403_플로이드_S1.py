N = int(input())

matrix = [[] for _ in range(N)]

for i in range(N):

    matrix[i] = list(map(int,input().split()))


for k in range(N):

    for p in range(N):

        for q in range(N):

            if matrix[p][k] and matrix[k][q]:

                matrix[p][q] = 1

for j in matrix:

    print(' '.join(list(map(str,j))))

