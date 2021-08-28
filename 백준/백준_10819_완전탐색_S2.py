from itertools import combinations

from itertools import permutations

N = int(input())

array = list(map(int,input().split()))

all_array = list(permutations(array))

box = []

max_value = 0

for list in all_array:

    for i in range(1,len(list)):

        output = abs(list[i-1] - list[i])

        box.append(output)

    if max_value <= sum(box):

        max_value = sum(box)

    box = []

print(max_value)

