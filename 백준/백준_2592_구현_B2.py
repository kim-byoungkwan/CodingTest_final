box = []

dict = {}

for _ in range(10):

    A = int(input())

    box.append(A)

    dict[A] = dict.get(A,0) + 1

print(sum(box) // 10)

print(sorted(dict.items(),key=lambda x:-x[1])[0][0])