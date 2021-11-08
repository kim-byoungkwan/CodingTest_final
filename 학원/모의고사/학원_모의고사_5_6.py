def solution(revenue,k):

    max = 0

    for i in range(0,len(revenue)-k+1):

        if max < sum(revenue[i:i+k]):

            max = sum(revenue[i:i+k])

        else:

            continue

    return max



revenue = [1,1,9,3,7,6,5,10]

k = 4

revenue_1 = [1,1,5,1,1]

k_1 = 1


print(solution(revenue_1,k_1))
