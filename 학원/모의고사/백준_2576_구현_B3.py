result = []

for _ in range(7):

    num = int(input())

    if num % 2 != 0:

        result.append(num)

    else:

        continue

if result:

    print(sum(result))

    print(sorted(result)[0])

else:

    print(-1)