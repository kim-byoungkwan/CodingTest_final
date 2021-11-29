N = int(input())

num_list = list(map(int,input().split()))

box = [0]*N

for i in num_list:

    box[i] += 1

print(box)

print(box.index(2))

