while True:

    word = input()

    if word == '#':

        break

    else:

        word = list(word)

        if word[-1] == 'e':

            if word.count('1') % 2 == 0:

                word[-1] = 0

            else:

                word[-1] = 1

        else:

            if word.count('1') % 2 == 0:

                word[-1] = 1

            else:

                word[-1] = 0

    print(''.join(map(str,word)))