N = int(input())

box = []

for _ in range(N):

    box.append(int(input()))

for i in sorted(box):

    print(i)
