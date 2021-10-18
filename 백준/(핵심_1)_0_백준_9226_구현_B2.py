standard = ['a', 'e', 'i', 'o', 'u']

while True:

    word = input()

    if word == '#':

        break

    else:

        if word[0] in standard:

            print(word + 'ay')

        else:

            count = 0

            for i in range(len(word)):

                if word[i] not in standard:

                    count +=1

                    if count == len(word):

                        print(word + 'ay')

                    else:

                        continue

                else:

                    print(word[i:] + word[:i] + 'ay')

                    break
