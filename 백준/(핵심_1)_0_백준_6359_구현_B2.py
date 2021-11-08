T = int(input())

for _ in range(T):

    n = int(input())

    arr = []

    for i in range(1,n+1):

        arr.append(i)

    for k in range(2,n+1):

        for j in range(k-1,n,k):

            arr[j] = -arr[j]

    count = 0

    for p in arr:

        if p >0:

            count += 1

        else:

            continue

    print(count)
