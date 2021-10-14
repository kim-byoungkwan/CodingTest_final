find = input()

n = int(input())

count = 0

for _ in range(n):

    sentance = input()

    real_sentance = sentance + sentance

    if real_sentance.count(find) != 0:

        count += 1

    else:

        continue

print(count)