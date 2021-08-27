# 수열을 내림차순으로 정렬하기

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array,reverse=True)

for i in array:
    print(i,end=' ')
                
