import sys

from collections import deque

input = sys.stdin.readline

N = int(input())

visited = [0]*(N+1)

list_num = list(map(int,input().split()))


queue = deque()


def bfs(start):

    queue.append(start)

    visited[start] = 0

    while queue:

        x = queue.popleft()

        for i in range(1,list_num[x-1]+1):

            nx = x + i

            if nx > N:

                continue

            if not visited[nx]:

                queue.append(nx)

                visited[nx] = visited[x] + 1

            if nx == N:

                return visited[nx]

    if N == 1:

        return 0

    return -1

print(bfs(1))
