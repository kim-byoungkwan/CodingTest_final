import sys

N = int(sys.stdin.readline())

arr = []

for _ in range(N):

    score = sys.stdin.readline()

    arr.append(score)

for i in sorted(arr)[:8]:

    i = float(i)

    print(format(i,".3f"))