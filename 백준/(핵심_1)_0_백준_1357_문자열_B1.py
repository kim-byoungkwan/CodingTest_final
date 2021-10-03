def Rev(N):

    arr = []

    while N != 0:

        rest = N % 10

        N = N // 10

        arr.append(rest)

    arr = map(str,arr)

    result = ''.join(arr)

    result = int(result)

    return result

X,Y = map(int,input().split())

print(Rev(Rev(X)+Rev(Y)))

