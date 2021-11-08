N = int(input())

arr = [0] * 100

list = map(int,input().split())

result = 0

for i in list:

    arr[i-1] += 1

for j in arr:

    if j >1:

        result += j-1

    else:

        continue

print(result)
