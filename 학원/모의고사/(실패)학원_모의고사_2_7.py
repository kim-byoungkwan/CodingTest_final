S = list(input())

S = list(map(int,S))

count = 0

total = S[0]

if total == 0:

    for i in range(len(S)):

        if i == 0:

            total = S[i]

        elif i == 1:

            total = total + S[i]

        else:

            if S[i] == 0 or S[i] ==1:

                total = total + S[i]

            else:

                total = total * S[i]

else:

    for i in range(1,len(S)):

        if S[i] == 0 or S[i] == 1:

            total = total + S[i]

        else:

            total = total * S[i]

print(total)

