from collections import deque

N,M = map(int,input().split())

matrix = [[] for _ in range(N)]

for i in range(N):

    matrix[i] = list(map(int,input()))

queue = deque()

def bfs(V):

    queue.append(V)









