import sys

input = sys.stdin.readline

N = int(input())

INF = int(1e9)

matrix = [[INF]*(N+1) for _ in range(N+1)]


while True:

    a,b = map(int,input().split())

    if a == -1 and b == -1:

        break

    else:

        matrix[a][b] = 1

        matrix[b][a] = 1

for k in range(1,N+1):

    for p in range(1,N+1):

        for q in range(1,N+1):

            if p == q:

                matrix[p][q] = 0

            if matrix[p][q] > (matrix[p][k] + matrix[k][q]):

                matrix[p][q] = matrix[p][k] + matrix[k][q]

answer = [[] for _ in range(N+1)]

result = []

for m in range(1,N+1):

    for n in range(1,N+1):

        if matrix[m][n] == INF:

            continue

        else:

            answer[m].append(matrix[m][n])

    result.append((m,max(answer[m])))


captin_list = sorted(result,key=lambda x:(x[1],x[0]))

captin_value = sorted(result,key=lambda x:(x[1],x[0]))[0][1]

count = 0

final = []

for w in captin_list:

    if w[1] == captin_value:

        count += 1

        final.append(w[0])

print(captin_value,count)

print(' '.join(list(map(str,final))))













