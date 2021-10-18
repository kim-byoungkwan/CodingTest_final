win = 0

count = 0

for _ in range(5):

    count += 1

    score = list(map(int,input().split()))

    if win < sum(score):

        win = sum(score)

        num = count

print(num, win)
