from itertools import combinations

N,S = map(int,input().split())

array = list(map(int,input().split()))

count = 0

for i in range(1,len(array)+1):

    combi = list(combinations(array, i))

    for j in combi:

        if sum(j) == S:

            count = count + 1

        else:

            continue

print(count)
