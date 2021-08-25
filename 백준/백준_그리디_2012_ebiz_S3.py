import sys

input = sys.stdin.readline

N = int(input())

box_expect = []

result = 0

for i in range(N):

    box_expect.append(int(input()))

box_expect = sorted(box_expect)

for i in range(1,N+1):

    result += abs(box_expect[i-1]-i)

print(result)

