###.1

import sys

sys.setrecursionlimit(10000)

def dfs(x,y):

    if x < 0 or x > N-1 or y < 0 or y > M-1:

        return False

    if matrix[x][y] == 1:

        matrix[x][y] = 0

        dfs(x+1,y)

        dfs(x-1,y)

        dfs(x,y+1)

        dfs(x,y-1)

        return True

    return False



T = int(input())

for m in range(T):

    M,N,K = map(int,input().split())

    matrix = [[0]*M for i in range(N)]

    for i in range(K):

        a,b = map(int,input().split())

        matrix[b][a] = 1

    count = 0

    for i in range(M):

        for j in range(N):

            if dfs(j,i) == True:

                count += 1

            else:

                continue

    print(count)

###.2
