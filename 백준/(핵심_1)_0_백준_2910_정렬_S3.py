N, C = map(int,input().split())

arr_num = list(map(int,input().split()))

dict = {}

answer=''

for i in arr_num:

    dict[i] = arr_num.count(i)

for p in sorted(dict.items(),key=lambda x: (-x[1])):

    for _ in range(p[1]):

        answer = answer + (str(p[0]) + ' ')

# key 에서 지정되지 않은 요소는 먼저 나온 순서대로 정렬되는 규칙이 있다.

print(answer)

