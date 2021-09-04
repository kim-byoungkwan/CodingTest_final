T_num = 0

dict = {'}{':2,
        '{{':1,
        '}}':1
        }

box = []

while True:

    T_num = T_num + 1

    word = input()

    if '-' in word:

        break

    else:

        word = word.replace('{}','')

    if len(word) == 0:

        box.append(0)

    else:

        for key,value in dict.items():

            if key in word:

                word = word.replace(key,'')

                box.append(value)

    answer = sum(box)

    result = '{0}. {1} '.format(T_num,answer)

    print(result)

    box = []
