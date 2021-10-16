count = 0

result = []

A,B = map(int,input().split())

while True:

    count += 1

    for _ in range(count):

        result.append(count)

    if len(result) >= B:

        print(sum(list(map(int,result[A-1:B]))))

        break

    else:

        continue
