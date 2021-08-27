def solution(score):
    answer = [0] * len(score)
    seq = 0
    for s in score:
        rank = 1
        for s2 in score:
            if s < s2:
                rank = rank +1
        answer[seq] = rank
        seq = seq + 1
    return answer


score1 = [90, 87, 87, 23, 35, 28, 12, 46]
ret1 = solution(score1)
print(ret1)

score2 = [10, 20, 20, 30]
ret2 = solution(score2)
print(ret2)
