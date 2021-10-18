n = int(input())

for _ in range(n):

    count_g =0

    count_b =0

    word = input()

    for i in word:

        if i == 'g' or i == 'G':

            count_g +=1

        elif i == 'b' or i == 'B':

            count_b +=1

        else:

            continue

    if count_g > count_b:

        result = "GOOD"

    elif count_g < count_b:

        result = "A BADDY"

    else:

        result = "NEUTRAL"

    print("{} is {}".format(word,result))

