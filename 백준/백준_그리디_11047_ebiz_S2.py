N, K = map(int,input().split())

box = []

count = 0

for i in range(N):

    box.append(int(input()))

box.sort(reverse=True)


for i in range(N):

    if K % box[i] == 0:

        count = count + (K // box[i])

        break

    else:

        if K // box[i] > 0:

            count = count + (K // box[i])

            K = K % box[i]

        else:

            continue

print(count)
