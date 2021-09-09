def solution(floors):
    dist = 0
    for i in range(0,len(floors)-1):
        if floors[i+1] > floors[i]:
            dist += floors[i+1] - floors[i]
        else:
            dist += floors[i] - floors[i+1]
    return dist


floors = [1,2,5,4,2]
ret = solution(floors)
print(ret)
