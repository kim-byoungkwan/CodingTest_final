count = 0

score_A = []

score_B = []

for _ in range(20):

    count +=1

    if count <= 10:

        score = int(input())

        score_A.append(score)

    else:

        score = int(input())

        score_B.append(score)

result_A = sum(sorted(score_A,reverse=True)[0:3])

result_B = sum(sorted(score_B,reverse=True)[0:3])

print(result_A,result_B)