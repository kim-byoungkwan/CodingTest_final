def solution(scores,cutline):
    answer = 0
    for s in scores:
        if s >= cutline:
            answer += 1
    return answer


scores = [80,90,55,60,59]
cutline = 60
ret = solution(scores,cutline)
print(ret)
