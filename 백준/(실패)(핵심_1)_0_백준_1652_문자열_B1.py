N = int(input())

matrix = [[] for _ in range(N)]

for i in range(N):

    matrix[i] = list(input())

box_horizon = []

box_vertical = []


for m in range(N):

    count = 1

    for n in range(1,N):

        if matrix[m][n-1] == '.' and matrix[m][n-1] == matrix[m][n]:

            count +=1

        else:

            if count >= 2:

                box_horizon.append(count)

            else:

                count = 1

        if n == N-1:

            if count >=2:

                box_horizon.append(count)


for b in range(N):

    count = 1

    for a in range(1,N):

        if matrix[a][b] == '.' and matrix[a-1][b] == matrix[a][b]:

            count +=1

        else:

            if count >=2:

                box_vertical.append(count)

            else:

                count = 1

        if a == N-1:

            if count >=2:

                box_vertical.append(count)


print(len(box_horizon),len(box_vertical))