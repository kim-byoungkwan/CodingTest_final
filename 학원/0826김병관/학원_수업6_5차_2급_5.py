###.1

def solution(a,b):

    box_a = []

    box_b = []

    num_a = 0

    num_b = 0

    if a <= b:

        while True:

            num_a = num_a + a

            box_a.append(num_a)

            num_b = num_b + b

            box_b.append(num_b)

            if box_a[-1] in box_b:

                return box_a[-1]

            else:

                continue

    else:

        while True:

            num_a = num_a + a

            box_a.append(num_a)

            num_b = num_b + b

            box_b.append(num_b)

            if box_b[-1] in box_a:

                return box_b[-1]

            else:

                continue

a = 7

b = 9

print(solution(a,b))


###.sol

def solution(a,b):

    answer = 0

    for i in range(1, b + 1):

        if (a * i) % b == 0:

            answer = a * i

            break

    return answer


a = 4

b = 6

ret = solution(a,b)

print(ret)




