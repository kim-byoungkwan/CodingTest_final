n = int(input())

position = list(map(int,input().split()))


dict = {}

for i in position:

    total = 0

    for j in range(len(position)):

        total = total + abs(i - position[j])

    dict[i] = dict.get(i,0) + total


answer = sorted(dict.items(), key=lambda x: (x[1],x[0]))

print(answer[0][0])
