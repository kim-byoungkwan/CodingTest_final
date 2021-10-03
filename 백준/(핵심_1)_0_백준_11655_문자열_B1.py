def ROT13(word):

    arr = []

    word = list(word)

    for i in word:

        if i.isdigit():

            arr.append(i)

        else:

            former = ord(i)

            latter = ord(i) + 13

            if i.isupper():

                if latter >90:

                    gap = latter -90

                    arr.append(chr(64+gap))

                else:

                    arr.append(chr(latter))


            elif i.islower():

                if latter > 122:

                    gap = latter -122

                    arr.append(chr(96+gap))

                else:

                    arr.append(chr(latter))

            else:

                arr.append(i)

    result = ''.join(arr)

    return result

word = input()

print(ROT13(word))