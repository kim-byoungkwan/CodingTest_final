def solution(temperature,A,B):

    answer = 0

    for i in range(A+1, B):

        if temperature[i] > temperature[A] and temperature[i] > temperature[B]:

            answer += 1

    return answer


temperature = [3,2,1,5,4,3,3,2]
A = 1
B = 6
ret = solution(temperature,A,B)
print(ret)
