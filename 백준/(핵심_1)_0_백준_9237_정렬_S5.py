N = int(input())

arr = sorted(list(map(int,input().split())),reverse=True)

answer =[]

for index,value in enumerate(arr):

    result = (index+1) + (value)

    answer.append(result)

print(max(answer)+1)

