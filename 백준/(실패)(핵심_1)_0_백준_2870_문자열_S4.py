N = int(input())

result = ''

S = input()

for i in S:

    if i.isdigit():

        if int(i) != 0:

            result += i

        else:

            result += ' '

            continue

    else:

        result += ' '

        continue

result_list = list(result)

print(result_list)







