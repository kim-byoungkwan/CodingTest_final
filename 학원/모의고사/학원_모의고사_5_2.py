# def solution(clothes):

def solution(clothes):

    dict = {}

    for i in range(len(clothes)):

        dict[clothes[i][1]] = dict.get(clothes[i][1],[]) + [clothes[i][0]]

    if len(dict.keys()) >=2:

        answer_1 = 0

        for key,value in dict.items():

            answer_1 += len(value)

        answer_2 = 1

        for key,value in dict.items():

            answer_2 *= len(value)

        return answer_1 + answer_2

    else:

        answer_2 = 1

        for key, value in dict.items():

            answer_2 *= len(value)

        return answer_2


clothes =[["yellowhat","headgear"],["bluesunglasses","eyewear"],["green_turban","headgear"]]

print(solution(clothes))


