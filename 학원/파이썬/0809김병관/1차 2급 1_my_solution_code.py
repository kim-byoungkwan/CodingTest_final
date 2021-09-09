def solution(shirt_size):
    answer = [0,0,0,0,0,0]
    for s in shirt_size:
        if s == "XS":
            answer[0] = answer[0] + 1
        elif s == "S":
            answer[1] = answer[1] + 1
        elif s == "M":
            answer[2] = answer[2] + 1
        elif s == "L":
            answer[3] = answer[3] + 1
        elif s == "XL":
            answer[4] = answer[4] + 1
        else:
            answer[5] = answer[5] + 1

    
    return answer


shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size)

print(ret)
