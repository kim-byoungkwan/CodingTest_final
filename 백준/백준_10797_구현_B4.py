N = int(input())

number = list(map(int,input().split()))


count = 0

for i in number:

    if i == N:

        count += 1

    else:

        continue

print(count)
