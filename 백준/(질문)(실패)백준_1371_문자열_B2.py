###.실패코드

##.Q

# read()에 의해 읽어들인 문자열은 print 할 수 없는가?


# import sys
#
# words = sys.stdin.readlines()
#
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
# dict = {}
#
# for i in alphabet:
#
#     dict[i] = dict.setdefault(i,0) + words.count(i)
#
# dic_val = list(dict.values())


###.2

import sys

dict = {}

alphabet = 'abcdefghijklmnopqrstuvwxyz'

while True:

    word = list(sys.stdin.readline())

    if word:

        for i in word:

            dict[i] = dict.get(i,0) + 1

    else:

        break

print(dict)









print(word)






