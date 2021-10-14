while True:

    S = input()

    if S == '*':

        break

    else:

        standard = [0] * 26

        count = 0

        for i in S:

            if i.isalpha():

                index = ord(i)-97

                count += 1

                standard[index] += count

            else:

                continue

        result = 'Y'

        for m in standard:

            if m >0:

                continue

            else:

                result = 'N'

                break

    print(result)