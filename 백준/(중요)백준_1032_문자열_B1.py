###.1

# N = int(input())
#
# dict = {}
#
# for i in range(N):
#
#     word = input()
#
#     for j in word:
#
#         dict[j] = dict.get(j,0) + 1
#
# print(dict)
#
# answer = ''
#
# for key,value in dict.items():
#
#     if value >= N:
#
#         answer = answer + key
#
#     else:
#
#         answer = answer + '?'
#
# print(answer)


###.2

N = int(input())


for j in range(N):

    word = input()

    if j == 0:

        box = [0] * len(word)

        for i in range(len(word)):

            box[i] = word[i]

    else:

        for i in range(len(word)):

            if word[i] != box[i]:

                box[i] = '?'

            else:

                box[i] = word[i]

print(''.join(box))


