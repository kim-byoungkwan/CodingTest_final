import sys

N = int(sys.stdin.readline())

box = []

result = False

answer = 0

for _ in range(N):

    num = int(sys.stdin.readline())

    box.append(num)

box_sorted = sorted(box,reverse=True)

for i in range(len(box_sorted)):

    if box_sorted[i] < sum(box_sorted[i+1:i+3]):

        result = True

        answer = sum(box_sorted[i:i+3])

        break

    else:

        continue

if result == False:

    print(-1)

else:

    print(answer)

