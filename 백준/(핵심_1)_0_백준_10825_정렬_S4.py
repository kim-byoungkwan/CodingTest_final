import sys

N = int(sys.stdin.readline())

dict = {}

for _ in range(N):

    score = list(sys.stdin.readline().split())

    dict[score[0]] = list(map(int,score[1:]))

for K in sorted(dict.items(),key=lambda x: (-x[1][0],x[1][1],-x[1][2],x[0])):

    print(K[0])