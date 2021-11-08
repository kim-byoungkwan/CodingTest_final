s = input()

num_happy = s.count(':-)')

num_sad = s.count(':-(')

if num_happy > num_sad:

    print('happy')

elif num_happy < num_sad:

    print('sad')

elif num_happy == num_sad and num_happy ==0:

    print('none')

else:

    print('unsure')


