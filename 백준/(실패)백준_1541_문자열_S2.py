number = input().split('-')

if len(number) == 1:

    print(number[0])

else:

    number[0] = int(number[0])

    for i in range(1,len(number)):

        number[i] = -eval(number[i])

        print(sum(number))
