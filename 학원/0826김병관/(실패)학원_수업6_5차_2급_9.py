def solution(score):

    adjacency_list = [[]*len(score)]

    adjacency_list[].append()

    dict = {}

    score_ranked = sorted(score,reverse=True)

    for index, value in enumerate(score_ranked):

        dict[index+1] = value

    return dict


score = [90,87,87,23,35,28,12,46]

print(solution(score))


