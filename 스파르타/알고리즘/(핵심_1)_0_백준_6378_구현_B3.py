import sys

input = sys.stdin.readline

state = True

while state:

    N = int(input())

    if N ==0:

        state = False

    else:

        box = []

        while N:

            residual = N % 10

            N = N // 10

            box.append(residual)

            if N == 0:

                sum_value = sum(box)

                if len(str(sum_value)) <=1:

                    print(sum_value)

                else:

                    N = sum_value

                    box = []


