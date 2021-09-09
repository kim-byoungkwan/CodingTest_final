matrix = [[] for _ in range(8)]

for i in range(8):

    word = list(input())

    matrix[i] = word

count = 0

for m in range(8):

    for n in range(8):

        if m % 2 == 0 and n % 2 == 0:

            if matrix[m][n] == 'F':

                count += 1

        elif m % 2 !=0 and n % 2 != 0:

            if matrix[m][n] == 'F':

                count += 1

print(count)
