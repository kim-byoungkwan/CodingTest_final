N = int(input())

array = [0,0,1,1]

count = 0

if N <= 3:

    print(array[N])

else:

    for i in range(4,N+1):

        count += 1

        N_1 = i-1

        N_2 = i-1

        N_3 = i-1

        if i % 2 == 0:

            N_1 = i // 2

        if i % 3 == 0:

            N_2 = i // 3

        array.append(min(array[N_1],array[N_2],array[N_3]) + 1)

    print(array[-1])
