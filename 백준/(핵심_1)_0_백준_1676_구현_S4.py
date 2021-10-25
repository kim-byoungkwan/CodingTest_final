def factorial(n):

    if n <= 1:

        return 1

    else:

        return n*factorial(n-1)


N = int(input())

result = factorial(N)

answer = []

while result:

    residual = result % 10

    result = result // 10

    if residual == 0:

        answer.append(residual)

    else:

        break

print(len(answer))


