T = int(input())

for _ in range(T):

    arr_lower = [0]*26

    arr_upper = [0]*26

    word = input()

    result = ''

    for i in word:

        if i.isupper():

            index = ord(i)-65

            arr_upper[index] =1

        elif i.islower():

            index = ord(i)-97

            arr_lower[index] =1

        else:

            continue

    for k in range(26):

        if arr_lower[k] == 1 or arr_upper[k] == 1:

            continue

        else:

            if arr_lower[k] ==0:

                result += chr(k+97)

            elif arr_upper[k] ==0:

                result += chr(k+65)

    print("missing {}".format(''.join(sorted(result))) if result else "pangram")