word = input()

answer = ''

for i in word:

    if i.isupper() == True:

        i = i.lower()

        answer = answer + i

    else:

        i = i.upper()

        answer = answer + i

print(answer)