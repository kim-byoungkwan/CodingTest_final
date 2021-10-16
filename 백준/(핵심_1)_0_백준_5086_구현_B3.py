while True:

    first, second = map(int,input().split())

    if first == 0 and second == 0:

        break

    else:

        target = max(first,second)

        attack = min(first,second)

        if target % attack == 0:

            if target == first:

                print('multiple')

            else:

                print('factor')

        else:

            print('neither')
