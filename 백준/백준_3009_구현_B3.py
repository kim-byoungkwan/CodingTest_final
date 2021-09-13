dict = {}

box = []

answer = []

for _ in range(3):

    A,B = map(int,input().split())

    dict[A] = dict.get(A,[]) + [B]


for key in dict:

    box.append(set(dict[key]))

list_1 = []

list_2 = []


for j in box:

    if len(j) > 1:

        list_1 = j

    else:

        list_2 = j


point = list(list_1 - list_2)

for k in dict:

    if len(dict[k]) < 2:

        point_key = k

    else:

        continue

answer.append(point_key)

answer.append(point[0])

for m in answer:

    print(m,end=' ')


