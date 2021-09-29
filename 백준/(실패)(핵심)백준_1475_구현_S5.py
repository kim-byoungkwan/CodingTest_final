###.1

N_list = list(input())

num_set = [0,1,2,3,4,5,7,8,9,9]

count = 1

for i in N_list:

    i = int(i)

    if i == 6:

        i = 9

        if i in num_set:

            index = num_set.index(i)

            num_set[index] = False

        else:

            num_set = [0, 1, 2, 3, 4, 5, 7, 8, 9, 9]

            num_set[index] = False

            count += 1

    else:

        if i in num_set:

            index = num_set.index(i)

            num_set[index] = False

        else:

            num_set = [0, 1, 2, 3, 4, 5, 7, 8, 9, 9]

            num_set[index] = False

            count += 1

print(count)