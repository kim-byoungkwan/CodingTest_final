def solution(member_age,transportation):
    answer = 0

    if transportation == 'Bus':
        adult_expense = 40000
        child_expense = 15000
    elif transportation == 'Ship':
        adult_expense = 30000
        child_expense = 13000
    elif transportation == 'Airplane':
        adult_expense = 70000
        child_expense = 45000

    if len(member_age) >= 10:
        adult_expense = adult_expense / 10 * 9
        child_expense = child_expense / 10 * 8

    for age in member_age:
        if age > 19:
            answer += adult_expense
        else:
            answer += child_expense

    return answer


member_age1 = [13,33,45,11,20]
transportation1 = "Bus"
ret1 = solution(member_age1,transportation1)
print(ret1)

member_age2 = [25,11,27,56,7,19,52,31,77,8]
transportation2 = "Ship"
ret2 = solution(member_age2,transportation2)
print(ret2)
