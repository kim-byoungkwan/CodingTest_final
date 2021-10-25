word = input()

standard = 'abcdefghijklmnopqrstuvwxyz'

for i in standard:

    if i in word:

        standard = standard.replace(i,'')

    else:

        standard = standard.replace(i, '')




