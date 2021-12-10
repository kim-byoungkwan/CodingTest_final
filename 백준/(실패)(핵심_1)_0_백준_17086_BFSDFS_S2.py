import sys

from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

matrix = [[] for _ in range(N)]

for i in range(N):

    matrix[i] = list(map(int,input().split()))

visited = [[False]*(M) for _ in range(N)]

dx = [0,0,1,-1,1,1,-1,-1]

dy = [1,-1,0,0,1,-1,1,-1]







