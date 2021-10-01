N,x = map(int,input().split())

N_list = list(map(int,input().split()))

count = 0

for i in N_list:

    if i == x:

        count +=1


if count:

    print(count)

else:

    print(-1)
