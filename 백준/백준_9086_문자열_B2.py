T = int(input())

answer = ''

for _ in range(T):

    word = input()

    answer = answer + (word[0] + word[-1])

    print(answer)

    answer = ''