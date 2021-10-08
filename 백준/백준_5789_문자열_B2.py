T = int(input())

for _ in range(T):

    S = input()

    if S[len(S)//2-1] == S[len(S)//2]:

        print('Do-it')

    else:

        print('Do-it-Not')
