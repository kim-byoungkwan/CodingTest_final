def solution(A,B,temperature):

    count = 0

    for i in temperature:

        if temperature[A] < i and temperature[B] < i:

            count += 1

        else:

            continue

    return count


temperature = [3,2,1,5,4,3,3,2]

print(solution(1,6,temperature))

