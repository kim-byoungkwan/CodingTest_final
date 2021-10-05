for _ in range(3):

    max = 0

    count = 1

    result = []

    num_1 = input()

    for i in range(1,8):

        if num_1[i-1] == num_1[i]:

            count +=1

        else:

            result.append(count)

            count = 1

        if max <= count:

            max = count

    print(max)