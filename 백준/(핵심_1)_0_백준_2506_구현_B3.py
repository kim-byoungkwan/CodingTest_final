N = int(input())

arr = list(map(int,input().split()))

answer = 0

state = False

count = 0

for i in arr:

    if i == 1:

        if state == True:

            count += 1

            answer += count

        else:

            state = True

            count += 1

            answer += count

    else:

        state = False

        count = 0

print(answer)
