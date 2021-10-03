T = int(input())

for _ in range(T):

    arr = []

    former, latter = input().split()

    for i in range(len(former)):

        if ord(former[i]) - ord(latter[i]) <=0:

            arr.append(abs(ord(former[i]) - ord(latter[i])))

        else:

            arr.append((26 + ord(latter[i]))-ord(former[i]))


    arr = list(map(str,arr))

    arr = ' '.join(arr)

    print("Distances:"+' '+arr)
