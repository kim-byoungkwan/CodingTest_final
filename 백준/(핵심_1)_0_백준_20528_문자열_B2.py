N = int(input())

S = input().split()

set_box = set()


for i in range(len(S)):

    set_box.add(S[i][0])

if len(set_box) == 1:

    print(1)

else:

    print(0)