def solution(enemies,armies):

    answer = []

    for enemy in enemies:

        state = False

        for my in armies:

            if enemy <= my:

                state = True

            else:

                continue

        answer.append(state)

    final = answer.count(True)

    return final

enemies_1 = [1,4,3]

armies_1 = [1,3]

enemies_2 = [1,1,1]

armies_2 = [1,2,3,4]


print(solution(enemies_2,armies_2))






