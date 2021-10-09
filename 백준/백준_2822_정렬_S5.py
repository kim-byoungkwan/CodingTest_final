dict = {}

result = []

answer = 0

for i in range(8):

    score = int(input())

    dict[i+1] = score

count = 0

for k in sorted(dict.items(),key=lambda x : (-x[1],x[0])):

    count += 1

    if count <= 5:

        answer += k[1]

        result.append(k[0])

    else:

        break

print(answer)

print(*sorted(result))

