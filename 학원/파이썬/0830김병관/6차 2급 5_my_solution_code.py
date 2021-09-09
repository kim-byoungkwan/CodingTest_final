def solution(money,price,n):
    answer = 0
    answer = money // price
    empty_bottle = answer
    while n <= empty_bottle:
        empty_bottle = empty_bottle - n
        answer += 1
        empty_bottle += 1
    return answer


money1 = 8
price1 = 2
n1 = 4
ret1 = solution(money1,price1,n1)
print(ret1)

money2 = 6
price2 = 2
n2 = 2
ret2 = solution(money2,price2,n2)
print(ret2)
