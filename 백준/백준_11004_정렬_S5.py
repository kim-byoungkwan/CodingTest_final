N,K = map(int,input().split())

count = 0

for i in sorted(list(map(int,input().split()))):

    count += 1

    if count == K:

        print(i)
