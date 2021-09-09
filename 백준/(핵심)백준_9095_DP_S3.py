T = int(input())

for _ in range(T):

    array = [1, 2, 4]

    n = int(input())

    if n >= 4:

        for i in range(3,n):

            array.append((array[i-3] + array[i-2] + array[i-1]))

        print(array[-1])

    else:

        array = [1,2,4]

        print(array[n-1])

