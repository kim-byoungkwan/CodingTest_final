sum = 0

max_count = 0

for _ in range(4):

    out,come = map(int,input().split())

    sum = sum + (-out + come)

    if sum > max_count:

        max_count = sum

    else:

        continue

print(max_count)