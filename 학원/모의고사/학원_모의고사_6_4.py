from itertools import permutations

card = [1,2,1,3]

n = 1312

permu_list = list(set(permutations(card)))

result = []

for i in permu_list:

    num = int(''.join(list(map(str,i))))

    result.append(num)

print(sorted(result))

print(sorted(result).index(n)+1)

