T = int(input())

for _ in range(T):

    score_list = list(map(int,input().split()))

    score_avg = sum(score_list[1:]) / score_list[0]

    count = 0

    for i in score_list[1:]:

        if i > score_avg:

            count+=1

        else:

            continue

    result = (count / score_list[0])*100

    print("{:.3f}%".format(result))



