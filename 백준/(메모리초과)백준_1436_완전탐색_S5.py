from itertools import permutations

from itertools import product

N = int(input())

box = []

array = ['666','1','2','3','4','5','6','7','8','9']

product_list_all = set(product(array,repeat=N))

for list_one in product_list_all:

    if '666' in list_one:

        num_one = ''.join(list_one)

        box.append(num_one)

box.append('666')

box = map(int,box)

box = list(box)

box.sort()

print(box[N-1])
