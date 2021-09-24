N = int(input())

for _ in range(N):

    front, back = input().split('-')

    front = list(front)

    back = int(back)

    answer = 0

    for i in range(len(front)):

        answer = answer + (ord(front[i])-65)*26**(2-i)

    if abs(answer-back) <= 100:

        print("nice")

    else:

        print("not nice")
