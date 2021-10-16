arr = []

for _ in range(5):

    num = int(input())

    arr.append(num)

print(sum(arr) // len(arr))

print(sorted(arr)[2])

