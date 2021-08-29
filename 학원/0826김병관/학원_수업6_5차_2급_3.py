###.1

def solution(speed,cars):

    fee = 0

    for i in cars:

        gap = i-speed

        if gap > 0:

            if speed*0.1 <= gap and gap < speed*0.2:

                fee = fee + 3

            elif speed*0.2 <= gap and gap < speed*0.3:

                fee = fee + 5

            else:

                fee = fee + 7

        else:

            continue

    return fee


speed = 100

cars = [110,98,125,148,120,112,89]

print(solution(speed,cars))
