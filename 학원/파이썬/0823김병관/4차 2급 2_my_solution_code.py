def solution(scores):
    people_count = 0
    pass_score = [80,88,70]

    for score in scores:
        pass_count = 0
        for i in range(3):
            if score[i] < pass_score[i]/2:
                pass_count = 0
                break
            elif score[i] >= pass_score[i]:
                pass_count += 1
        if pass_count >1:
            people_count += 1
    return people_count


scores1 = [[30, 40, 100], [97, 88, 95]]
ret1 = solution(scores1)
print(ret1)

scores2 = [[90,88,70],[85,90,90],[100,100,70],[30,90,80],[40,10,20],[83,88,80]]
ret2 = solution(scores2)
print(ret2)
