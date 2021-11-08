result = []

T = int(input())

for _ in range(T):

    S = input()

    for i in range(len(S)):

        if S[i].isalpha():

            S = S.replace(S[i],' ')


    for j in S.split(' '):

        if j =='':

            continue

        else:

            result.append(int(j))

for k in sorted(result):

    print(k)

