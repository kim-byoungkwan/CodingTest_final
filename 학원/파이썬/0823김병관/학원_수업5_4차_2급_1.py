###.1

def solution(schedule):

    box = []

    for index,value in enumerate(schedule):

        if value == "X":

            box.append(index+1)

    return box

schedule = ['O','X','X','O','O','O','X','O','X','X']

print(solution(schedule))

