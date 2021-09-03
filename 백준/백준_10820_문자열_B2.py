import sys

dict = {'lower' : 0,
        'upper': 0,
        'number' :0,
        'space' : 0}

while True:

    word = list(sys.stdin.readline().rstrip('\n'))

    if len(word) != 0:

        for i in word:

            if i.islower() == True:

                dict['lower'] = dict.get('lower') + 1

            elif i.isupper() == True:

                dict['upper'] = dict.get('upper') + 1

            elif i.isdigit() == True:

                dict['number'] = dict.get('number') + 1

            else:

                dict['space'] = dict.get('space') + 1


        answer = ' '.join(map(str,list(dict.values())))

        print(answer)

        dict = {'lower': 0,
                'upper': 0,
                'number': 0,
                'space': 0}

    else:

        break
