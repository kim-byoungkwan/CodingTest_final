def solution(k,student):

    answer = []

    final = []

    for i in student:

        if i - 4*k >=0:

            answer.append(i-4*k)

        else:

            answer.append(0)

    for j in answer:

        if j == 0:

            continue

        else:

            if j < k:

                final.append(1)

            elif j == k:

                final.append(1)

            else:

                final.append(j // k +1)

    return sum(final)



k = 1

student = [4,4,4,4]

k_1 = 3

student_1 = [15,17,19,10,23]


print(solution(k_1,student_1))