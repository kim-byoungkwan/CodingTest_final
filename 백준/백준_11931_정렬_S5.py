import sys

N = int(sys.stdin.readline())

arr = []

for _ in range(N):

    num = int(sys.stdin.readline())

    arr.append(num)

for i in sorted(arr,reverse=True):

    print(i)