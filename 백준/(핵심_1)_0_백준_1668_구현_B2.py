import sys

input = sys.stdin.readline

N = int(input())

box = []

for _ in range(N):

    value = int(input())

    box.append(value)

start = box[0]

count = 1

for number in box[1:]:

    if start < number:

        start = number

        count += 1

print(count)

start = box[::-1][0]

count = 1

for number in box[::-1][1:]:

    if start < number:

        start = number

        count += 1

print(count)






