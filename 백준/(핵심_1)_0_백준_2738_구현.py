N,M = map(int,input().split())

matrix_1 = [[] for _ in range(N)]

matrix_2 = [[] for _ in range(N)]


for i in range(N):

    matrix_1[i] = list(map(int,input().split()))

for i in range(N):

    matrix_2[i] = list(map(int,input().split()))


answer = [[] for _ in range(N)]


for p in range(N):

    for q in range(M):

        answer[p].append(matrix_1[p][q] + matrix_2[p][q])

for k in answer:

    print(' '.join(list(map(str,k))))




