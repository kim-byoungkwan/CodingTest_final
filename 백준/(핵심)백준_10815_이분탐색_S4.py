N = int(input())

card_num = list(map(int,input().split()))

card_num.sort()

M = int(input())

find_num = list(map(int,input().split()))

answer = []

result = 0



for i in find_num:

    start = 0

    end = len(card_num) - 1

    while start <= end:

        mid = (start + end)//2

        if i < card_num[mid]:

            end = mid-1

        elif i > card_num[mid]:

            start = mid+1

        else:

            result = 1

            break

    answer.append(str(result))

    result = 0

print(' '.join(answer))