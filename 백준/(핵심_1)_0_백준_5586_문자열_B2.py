S = input()

answer_joi = 0

answer_ioi = 0


for i in range(2,len(S)):

    if S[i-2] == 'J' and S[i-1] == 'O' and S[i] == 'I':

        answer_joi += 1

    elif S[i-2] == 'I' and S[i-1] =='O' and S[i] == 'I':

        answer_ioi += 1

    else:

        continue

print(answer_joi)

print(answer_ioi)
