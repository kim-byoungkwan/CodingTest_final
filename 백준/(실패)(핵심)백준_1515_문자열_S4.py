x_num = input()

number_str = ''

x_num_index = 0

while True:

    N = 0

    try:

        N = N +1

        for i in range(1,N+1):

            number_str = number_str + str(i)

        x = len(str(N))-1

        for j in range(len(number_str)-(x)):

            if x_num[x_num_index] == number_str[j]:

                x_num_index = x_num_index + 1

                if x_num_index == len(x_num):

                    print(N)


    except:

        break
















