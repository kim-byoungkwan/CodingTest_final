number = input().split('-')

if len(number) <= 1:

    number[0] = number[0].split('+')

    number[0] = list(map(int,number[0]))

    print(sum(number[0]))

else:

    for i in range(len(number)):

        if i == 0:

            number[i] = number[i].split('+')

            number[i] = list((map(int, number[i])))

            number[i] = sum(number[i])

        else:

            number[i] = number[i].split('+')

            number[i] = list((map(int,number[i])))

            number[i] = -sum(number[i])

    print(sum(number))
