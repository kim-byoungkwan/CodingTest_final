def solution(schedule):

    answer = []

    #리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능

    for idx, i in enumerate(schedule):

        if i == "X":

            answer.append(idx+1)

    return answer


schedule = ["O","X","X","O","O","O","X","O","X","X"]
ret = solution(schedule)
print(ret)
