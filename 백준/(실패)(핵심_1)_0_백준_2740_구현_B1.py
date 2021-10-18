N,M = map(int,input().split())

matrix_A = [0 for _ in range(N)]

for i in range(N):

    matrix_A[i] = list(map(int,input().split()))



M,K = map(int,input().split())

matrix_B = [[] for _ in range(M)]

for j in range(M):

    matrix_B[j] = list(map(int,input().split()))


matrix_final = [[] for _ in range(N)]

value = 0


for p in range(N):

    for s in range(K):

        for q in range(M):

            value += matrix_A[p][q] * matrix_B[q][s]

        matrix_final[p].append(value)

        value = 0

for answer in matrix_final:

    print(' '.join(list(map(str,answer))))


