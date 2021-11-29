def solution(s):

    result = ''

    answer = ''

    for i in s:

        result += i.lower()

    result_list = list(result)

    for j in range(1,len(result_list)):

        if result_list[j-1] != result_list[j]:

            answer += result_list[j-1]

            answer += str(result_list.count(result_list[j-1]))

        else:

            continue

    answer += result_list[-1]

    answer += str(result_list.count(result_list[-1]))

    return answer

s = "YYYYYbbbBbbBBBMmmM"

print(solution(s))



