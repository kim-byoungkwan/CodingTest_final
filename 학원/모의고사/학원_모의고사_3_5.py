def solution(N,votes):

    result = []

    dict = {}

    for i in votes:

        dict[i] = dict.get(i,0) + 1

    max_value = sorted(dict.items(), key=lambda x: (-x[1], x[0]))[0][1]

    for key, value in sorted(dict.items(), key=lambda x: (-x[1], x[0])):

        if value == max_value:

            result.append(key)

        else:

            continue

    return result


votes = [1,5,4,3,2,5,2,5,5,4]

N = 5

votes_2 = [1,3,2,3,2]

N_2 = 3

print(solution(N,votes))











