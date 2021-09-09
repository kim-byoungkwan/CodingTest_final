def solution(classes,m):
    count = 0
    for num in classes:
        while num > 0:
            num -= m
            count += 1
    return count


classes = [80,45,33,20]
m = 30
ret = solution(classes,m)
print(ret)
