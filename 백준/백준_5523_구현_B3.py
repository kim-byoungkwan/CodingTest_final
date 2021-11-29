import sys

input = sys.stdin.readline

N = int(input())

result = [0,0]

for _ in range(N):

    A_score,B_score = map(int,input().split())

    if A_score > B_score:

        result[0] += 1

    elif A_score < B_score:

        result[1] += 1

print(' '.join(list(map(str,result))))

