def solution(usage):

    answer = 0

    if usage <= 20:

        answer = usage * 430

    elif 20 < usage and 30 > usage:

        one_step = usage // 20

        two_step = usage % 20

        answer = (one_step * 20 * 430) + (two_step * 570)

    else:

        one_step = usage // 20

        two_step = (usage % 20) // 10

        three_step = (usage % 20) % 10

        answer = (one_step * 20 * 430) + (two_step * 10 * 570) + (three_step * 840)

    return answer


usage = 35


print(solution(usage))



