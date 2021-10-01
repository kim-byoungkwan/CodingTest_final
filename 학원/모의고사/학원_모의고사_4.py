N = int(input())

arr = []

result = []

dp = []

for _ in range(N):

    arr.append(int(input()))

for i in sorted(arr):

    result.append(i)

    if len(result) == 2:

        temp = sum(result)

        dp.append(temp)

        result = []

        result.append(temp)

print(sum(dp))