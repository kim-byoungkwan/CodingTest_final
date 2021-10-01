S = list(input())

arr = []

for i in range(1,len(S)):

    if i == len(S)-1:

        if S[i] == arr[-1]:

            continue

        else:

            arr.append(S[i])

    if S[i-1] == S[i]:

        continue

    else:

        arr.append(S[i-1])


if len(arr) % 2 == 0:

    print(len(arr)//2)

else:

    print(min(arr.count('0'),arr.count('1')))

