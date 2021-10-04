N,M = map(int,input().split())

ball_weight = list(map(int,input().split()))

count = 0

for i in range(len(ball_weight)):

    for j in range(i+1,len(ball_weight)):

        if ball_weight[i] != ball_weight[j]:

            count +=1

        else:

            continue

print(count)