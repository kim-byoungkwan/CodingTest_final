T = int(input())

for _ in range(T):

    n = int(input())

    n_bin = bin(n)

    result = []

    for index,value in enumerate(n_bin[2:][::-1]):

        if value == '1':

            result.append(index)

        else:

            continue

    print(' '.join(list(map(str,result))))

