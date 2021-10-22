###.2

N = int(input())

word = list(input())

for i in range(len(word)):

    if word[i] == '?' and word[::-1][i] =='?':

        word[i] = 'a'

        word[::-1][i] = 'a'

    else:

        if word[i] !='?':

            word[::-1][i] = word[i]

        else:

            word[i] = word[::-1][i]

print(''.join(word))


























































###.1

# N= int(input())
#
# word = list(input())
#
# for i in range(1,len(word)):
#
#     if set(word) == {'?'}:
#
#         word = ['a']*len(word)
#
#     if word[i] == '?':
#
#         word[i-1] = word[-i]
#
#     elif word[-i] == '?':
#
#         word[-i] = word[i-1]
#
#     elif word[i-1] == word[-i] and word[i-1] != '?':
#
#         continue
#
# print(''.join(word))

