N = int(input())

A = list(map(int,input().split()))

B = list(map(int,input().split()))

result = []


for i in range(N):

    result.append(sorted(A)[i] * sorted(B,reverse=True)[i])

print(sum(result))