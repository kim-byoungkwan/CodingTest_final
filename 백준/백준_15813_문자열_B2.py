n = int(input())

name = input()

answer = 0

for i in name:

    answer += ord(i)-64

print(answer)
