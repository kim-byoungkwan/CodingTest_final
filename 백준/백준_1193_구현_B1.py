import sys


number = int(sys.stdin.readline())

box = []

i = 1

sum = 0

count = 0

while True:

    count += 1

    sum = sum + i

    i = i+1

    if number > sum:

        continue

    else:

        box.append(count)

        box.append(sum)

        break

print(count)

짝수일때 2/1 ,4/1 ,6/1 ~~ 부터 시작

홀수일때 1/1, 1/3, 1/5 ~~ 부터 시작

number - count



