N = int(input())

arr = []

for _ in range(N):

    arr.append(list(map(int,input().split())))

for result in sorted(arr,key = lambda x : (x[1],x[0])):

    print(result[0],end=' ')

    print(result[1])