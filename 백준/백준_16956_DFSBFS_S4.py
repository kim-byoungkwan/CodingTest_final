R,C = map(int,input().split())

result = True

matrix = [list(input()) for i in range(R)]

dx = [0,0,1,-1]

dy = [1,-1,0,0]


for i in range(R):

    for j in range(C):

        if matrix[i][j] == "W":

            for m in range(4):

                nx = j + dx[m]

                ny = i + dy[m]

                if nx < 0 or nx > C-1 or ny < 0 or ny > R-1:

                    continue

                else:

                    if matrix[ny][nx] == "S":

                        result = False

                        break

        elif matrix[i][j] == "S":

            continue

        else:

            matrix[i][j] = "D"

if result == True:

    print(1)

    for n in range(R):

        print(''.join(matrix[n]))

else:

    print(0)



