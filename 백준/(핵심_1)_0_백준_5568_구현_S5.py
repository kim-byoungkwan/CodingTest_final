from itertools import permutations

n = int(input())

k = int(input())

result = []

for _ in range(n):

    num = int(input())

    result.append(num)

result = list(permutations(result,k))

answer = []

for value in result:

    value_new = int(''.join(list(map(str,list(value)))))

    answer.append(value_new)

print(len(set(answer)))

