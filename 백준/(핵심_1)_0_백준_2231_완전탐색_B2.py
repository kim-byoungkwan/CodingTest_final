n = int(input())

def fuction(n):

    result = n

    while n:

        residual = n % 10

        result = result + residual

        n = n // 10

    return result

arr = [0]*n

answer = []

for i in range(n):

    arr[i] = fuction(i)

print(arr)

for index, value in enumerate(arr):

    if value == n:

        answer.append(index)

if answer:

    print(answer[0])

else:

    print(0)
