from itertools import permutations

X = input()

X_num = int(X)

X_list = list(X)

X_permu_all = list(permutations(X_list))

box = []

for i in X_permu_all:

    i = ''.join(i)

    box.append(i)

box_set = set(sorted(map(int,box)))

box_list = list(box_set)

box_list = sorted(box_list)

X_index = box_list.index(X_num)

if X_index == len(box_list)-1:

    print(0)

else:

    print(box_list[X_index+1])

