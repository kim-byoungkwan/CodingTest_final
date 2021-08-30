def solution(people):
    answer = [0,0,0,0]
    for p in people:
        if p < 95:
            answer[0] += 1
        elif p >= 95 and p < 100:
            answer[1] += 1
        elif p >= 100 and p < 105:
            answer[2] += 1
        elif p >= 105:
            answer[3] += 1
    return answer


people = [97,102,93,100,107]
ret = solution(people)
print(ret)
