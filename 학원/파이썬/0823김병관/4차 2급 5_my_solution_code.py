def solution(calorie):
    answer = 0
    min = 1000
    
    for x in calorie:
        if min < x:
            answer += (x - min)
        else:
            min = x

    return answer


calorie = [713,665,873,500,751]
ret = solution(calorie)
print(ret)
