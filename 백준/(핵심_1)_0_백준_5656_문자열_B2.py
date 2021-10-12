count = 0

while True:

    count += 1

    word = input().split()

    if word[1] == '>':

        if int(word[0]) > int(word[2]):

            answer = "true"

        else:

            answer = "false"

    elif word[1] == '>=':

        if int(word[0]) >= int(word[2]):

            answer = "true"

        else:

            answer = "false"

    elif word[1] == '<':

        if int(word[0]) < int(word[2]):

            answer = "true"

        else:

            answer = "false"

    elif word[1] == '<=':

        if int(word[0]) <= int(word[2]):

            answer = "true"

        else:

            answer = "false"

    elif word[1] == '==':

        if int(word[0]) == int(word[2]):

            answer = "true"

        else:

            answer = "false"


    elif word[1] == '!=':

        if int(word[0]) != int(word[2]):

            answer = "true"

        else:

            answer = "false"

    else:

        break

    print("Case {}: {}".format(count,answer))


