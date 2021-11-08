M = int(input())

N = int(input())

arr = []

result = []

for i in range(1,101):

    arr.append(i**2)

    if arr[i-1] >= M and arr[i-1] <= N:

        result.append(arr[i-1])

    else:

        continue

if result:

    print(sum(result))

    print(min(result))

else:

    print(-1)