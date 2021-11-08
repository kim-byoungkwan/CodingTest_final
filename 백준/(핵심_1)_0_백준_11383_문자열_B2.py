N,M = map(int,input().split())

matrix_1 = [[] for _ in range(N)]

matrix_2 = [[] for _ in range(N)]

for i in range(N):

    value = list(input())

    matrix_1[i] = value


result = [[] for _ in range(N)]

for j in range(N):

    value_2 = list(input())

    matrix_2[j] = value_2

for p in range(N):

    for q in range(M):

        for _ in range(2):

            result[p].append(matrix_1[p][q])


if matrix_2 == result:

    print("Eyfa")

else:

    print("Not Eyfa")
