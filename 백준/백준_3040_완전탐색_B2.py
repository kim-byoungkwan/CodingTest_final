from itertools import combinations

N = 9

array = []

for i in range(N):

    num = int(input())

    array.append(num)

output = list(combinations(array,7))

for list in output:

    if sum(list) == 100:

        for j in sorted(list):

            print(j)

        break
