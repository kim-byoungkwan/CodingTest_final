T = int(input())

for _ in range(T):

    count = 0

    first = input()

    second = input()

    for i in range(len(first)):

        if first[i] == second[i]:

            continue

        else:

            count += 1

    print("Hamming distance is {}.".format(count))
