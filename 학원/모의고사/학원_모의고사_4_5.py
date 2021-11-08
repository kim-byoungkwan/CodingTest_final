def solution(arr):

    answer = []

    result = []

    for i in range(1,len(arr)):

        if arr[i-1] < arr[i]:

            result.append(arr[i-1])

        else:

            result.append(arr[i-1])

            if len(result) > len(answer):

                answer = result

                result = []

            else:

                result = []

                continue

        if i == len(arr)-1:

            result.append(arr[i])

            if len(result) > len(answer):

                answer = result

    return len(answer)

arr = [3,1,2,4,5,1,2,2,3,4]

print(solution(arr))












