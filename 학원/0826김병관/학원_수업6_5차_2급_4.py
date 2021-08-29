###.1

def solution(taekwondo,running,shooting):

    score = 0

    gap_t = taekwondo - 25

    if gap_t > 0:

        score = score + 250 + (taekwondo*8)

    else:

        score = score + (taekwondo*8)

    gap_r = 60 - running

    if gap_r >= 0:

        score = score + 250 + (gap_r*5)

    else:

        score = score - (gap_r*5)

    count = 0

    for i in shooting:

        if i == 10:

            count = count + 1

    if count >= 7:

        score = score + 100 + sum(shooting)

    else:

        score = score + sum(shooting)

    return score


taekwondo = 27

running = 63

shooting = [9,10,8,10,10,10,7,10,10,10]


print(solution(taekwondo,running,shooting))
