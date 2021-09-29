for _ in range(3):

    test = list(map(int,input().split()))

    if test.count(0) == 0:

        print('E')

    elif test.count(0) == 1:

        print('A')

    elif test.count(0) == 2:

        print('B')

    elif test.count(0) == 3:

        print('C')

    else:

        print('D')
