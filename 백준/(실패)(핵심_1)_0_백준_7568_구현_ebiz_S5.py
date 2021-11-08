N = int(input())

count = 0

dict = {}

for _ in range(N):

    count += 1

    height,weight = map(int,input().split())

    dict[count] = (height,weight)

for key,value in sorted(dict.items(),key=lambda x:(-x[1][0],-x[1][1])):

    print(key,value)



















