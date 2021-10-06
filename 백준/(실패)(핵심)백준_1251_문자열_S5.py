S = input()

for i in range(len(S)-2):

    for j in range(i,len(S)-1):

        for k in range(j,len(S)):

            list_first = S[:i]

            list_second = S[j:k]

            list_third = S[k:]

S = 'ABCDEFG'

print(S[1:2])