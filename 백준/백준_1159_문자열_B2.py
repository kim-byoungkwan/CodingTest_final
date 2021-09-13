N = int(input())

dict = {}

for _ in range(N):

    word = list(input())

    dict[word[0]] = dict.get(word[0],0) + 1

answer=''

for key,value in dict.items():

    if value >= 5:

        answer = answer + key

    else:

        continue

if answer:

    print(''.join(sorted(answer)))

else:

    print("PREDAJA")
