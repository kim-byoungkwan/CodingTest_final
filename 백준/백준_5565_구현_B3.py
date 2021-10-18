result = []

for _ in range(10):

    price = int(input())

    result.append(price)

result = sorted(result,reverse=True)

print(result[0] - sum(result[1:]))
