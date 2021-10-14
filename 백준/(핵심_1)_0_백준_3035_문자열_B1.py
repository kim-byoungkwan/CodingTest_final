R,C,ZR,ZC = map(int,input().split())

matrix = [[] for _ in range(R)]

for i in range(R):

    word = list(input())

    matrix[i] = word

for p in range(R):

    for _ in range(ZR):

        for q in range(C):

            print(matrix[p][q]*ZC,end='')

        print()
