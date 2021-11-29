T = int(input())

for _ in range(T):

    list_num = list(map(int,input().split()))

    answer = []

    for i in list_num:

        if i % 2 ==0:

            answer.append(i)

        else:

            continue

    answer = sorted(answer)

    sum_num = sum(answer)

    min_num = answer[0]

    print('{} {}'.format(sum_num,min_num))
