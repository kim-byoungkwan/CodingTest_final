def solution(cards):
    answer = 0
    count = [0,0,0]
    for card in cards:
        if card[0] == 'black':
            count[0] += 1
        elif card[0] == 'blue':
            count[1] += 1
        elif card[0] == 'red':
            count[2] += 1
        answer += int(card[1])
    if count[0] == 3 or count[1] == 3 or count[2] == 3:
        answer *= 3
    elif count[0] == 2 or count[1] == 2 or count[2] == 2:
        answer *= 2
    return answer


cards1 = [["blue","2"],["red","5"],["black","3"]]
ret1 = solution(cards1)
print(ret1)

cards2 = [["blue","2"],["blue","5"],["black","3"]]
ret2 = solution(cards2)
print(ret2)
