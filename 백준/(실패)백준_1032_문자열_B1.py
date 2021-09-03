N = int(input())

dict = {}

for i in range(N):

    word = input()

    for j in word:

        dict[j] = dict.get(j,0) + 1

print(dict)

answer = ''

for key,value in dict.items():

    if value >= N:

        answer = answer + key

    else:

        answer = answer + '?'

print(answer)


