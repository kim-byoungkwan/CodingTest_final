###.1

stand = [1,0,0]

arr = list(input())

for i in arr:

    if i == "A":

        if stand[0] == 1:

            stand[0] = 0

            stand[1] = 1

        elif stand[1] == 1:

            stand[1] = 0

            stand[0] = 1

        else:

            continue

    elif i == "B":

        if stand[1] == 1:

            stand[1] = 0

            stand[2] = 1

        elif stand[2] ==1:

            stand[2] = 0

            stand[1] = 1

        else:

            continue

    else:

        if stand[2] == 1:

            stand[2] = 0

            stand[0] = 1

        elif stand[0] == 1:

            stand[0] = 0

            stand[2] = 1

        else:

            continue

for j in stand:

    if j != 0:

        print(stand.index(j)+1)


