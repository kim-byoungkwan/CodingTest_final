def solution(number):
    count = 0
    for i in range(1,number+1):
        while i != 0:
            if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
                count += 1
            i = i // 10
    return count

number = 40
ret = solution(number)

print(ret)
