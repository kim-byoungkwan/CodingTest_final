while True:

    word = input().lower()

    if word == '#':

        break

    else:

        arr = [0]*26

        for i in word:

            if i.isalpha():

                index = ord(i) - 97

                arr[index] += 1

            else:

                continue

    count = 0

    for j in arr:

        if j == 0:

            continue

        else:

            count += 1

    print(count)