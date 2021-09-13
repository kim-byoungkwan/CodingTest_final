standard = ['a','e','i','o','u','A','E','I','O','U']

while True:

    count = 0

    word = input()

    if word == '#':

        break

    for string in word:

        if string in standard:

            count += 1

    print(count)
