def solution(num,count):

    if count == 1:

        return num*100

    elif count == 2:

        return 1000+num*100

    elif count == 3:

        return 10000+num*1000


T = int(input())

answer = []

for _ in range(T):

    dict = {}

    arr_number = list(map(int,input().split()))

    for i in arr_number:

        dict[i] = dict.get(i,0) +1

    result = sorted(dict.items(), key=lambda x: (-x[1],-x[0]))[0]

    answer.append(solution(result[0],result[1]))

print(max(answer))


