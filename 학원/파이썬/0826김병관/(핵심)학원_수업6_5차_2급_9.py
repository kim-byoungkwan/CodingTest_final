###.1

def solution(score):

    count = 1

    box = []

    for j in range(len(score)):

        for i in range(len(score)):

            if score[j] < score[i]:

                count += 1

        box.append(count)

        count = 1

    return box


score = [90,87,87,23,35,28,12,46]

print(solution(score))


