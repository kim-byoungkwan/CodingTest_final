N,K = map(int,input().split())

result = []

for i in range(1,N+1):

    if N % i == 0:

        result.append(i)

    else:

        continue

if len(result) < K:

    print(0)

else:

    answer = result[K-1]

    print(answer)