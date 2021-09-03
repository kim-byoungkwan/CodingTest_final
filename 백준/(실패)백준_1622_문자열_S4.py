while True:

    try:

        a = list(input())

        b = list(input())

        length_a = len(a)

        length_b = len(b)

        box = []

        if length_a > length_b:

            for k in b:

                if k in a:

                    box.append(k)

        elif length_a == length_b:

            for i in b:

                if i in a:

                    box.append(i)

                    a.remove(i)

                else:

                    continue

        else:

            for j in a:

                if j in b:

                    box.append(j)

        box = ''.join(sorted(box))

        print(box)

    except:

        break

