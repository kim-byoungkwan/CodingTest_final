n = int(input())

def fibo(x):

    if x <= 1:

        array = [i for i in range(x + 1)]

        return array[x]

    else:

        array = [0 for _ in range(x + 1)]

        array[0] = 0

        array[1] = 1

        for i in range(2,x+1):

            array[i] = array[i-1] + array[i-2]

        return array[-1]

print(fibo(n))