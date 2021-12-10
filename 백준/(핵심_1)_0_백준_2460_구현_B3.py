import sys

input = sys.stdin.readline

total = 0

answer = []

for idx in range(1,11):

    out_num,in_num = map(int,input().split())

    total = total -out_num +in_num

    answer.append((idx,total))

print(sorted(answer,key=lambda x:-x[1])[0][1])

