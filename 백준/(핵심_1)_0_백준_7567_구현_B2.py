S = input()

height = 10

for i in range(1,len(S)):

    if S[i-1] == '(':

        if S[i] == '(':

            height += 5

        else:

            height += 10

    else:

        if S[i] == '(':

            height += 10

        else:

            height += 5

print(height)
