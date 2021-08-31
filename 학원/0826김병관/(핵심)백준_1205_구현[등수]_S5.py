import sys

N,Score_new,P = map(int,sys.stdin.readline().split())

if N ==0:

    current_score = []
else:

    current_score = list(map(int,sys.stdin.readline().split()))

def solution(Score_new):

    current_score.append(Score_new)

    count = 1

    box = []

    for i in range(len(current_score)):

        for j in range(len(current_score)):

            if current_score[i] < current_score[j]:

                count += 1

        box.append(count)

        count = 1

    if box[-1] == P and box.count(box[-1]) > 1:

        return -1

    elif box[-1] <P and box.count(box[-1]) > (P-box[-1]+1):

        return -1

    elif box[-1] > P:

        return -1

    else:

        return box[-1]

print(solution(Score_new))


