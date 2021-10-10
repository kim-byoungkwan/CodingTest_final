N = int(input())

for _ in range(N):

    A,B = list(input().split())

    A= list(A)

    B= list(B)

    if sorted(A) == sorted(B):

        print("{} & {} are anagrams.".format(''.join(A),''.join(B)))

    else:

        print("{} & {} are NOT anagrams.".format(''.join(A),''.join(B)))
