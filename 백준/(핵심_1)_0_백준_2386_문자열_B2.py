while True:

    word = input()

    if word == '#':

        break

    else:

        find = word[0]

        sentance = word[2:]

        sentance = sentance.lower()

        print(find,sentance.count(find))
