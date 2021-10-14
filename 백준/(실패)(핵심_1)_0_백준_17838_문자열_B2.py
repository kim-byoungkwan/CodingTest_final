T = int(input())

for _ in range(T):

    word = input()

    while word:

        if len(word) > 3:

            first = word[0]

            second = word[2]

            result = first*2 + second*2 + first + second*2

            if word == result:

                print(1)

            else:

                print(0)

                break

            for i in range(7):

                if i < len(word):

                    word = word.replace(word[i],'')

                else:

                    break

        else:

            break

