def solution(prices):

    max = -99999

    for i in range(len(prices)-1):

        for j in range(i+1,len(prices)):

            gap = prices[j] - prices[i]

            if max <= gap:

                max = gap

            else:

                continue

    return max


prices = [1,2,3]

prices_2 = [3,1]

print(solution(prices))