while True:

    num_list = sorted(list(map(int,input().split())),reverse=True)

    if len(set(num_list)) == 1 and set(num_list).pop() == 0:

        break

    else:

        if num_list[0]**2 == num_list[1]**2 + num_list[2]**2:

            print('right')

        else:

            print('wrong')

