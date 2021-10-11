###.2

standard = ['a','e','i','o','u']

word = list(input())

answer = ''


for i in range(len(word)):

    if word[i] in standard:

        answer += word[i]

        word[i+1] = ''

        word[i+2] = ''

    else:

        answer += word[i]

print(answer)








































###.1

# standard = ['a','e','i','o','u']
#
# S = list(input())
#
# result = ''
#
# for i in range(2,len(S)):
#
#     if S[i-2] in standard and S[i-1] == 'p' and S[i]==S[i-2]:
#
#         S[i-1] = ''
#
#         S[i] = ''
#
#         result = result + S[i-2]
#
#     else:
#
#         result = result + S[i-2]
#
#     if i == len(S) -1:
#
#         if S[i] != '' and S[i-1] != '':
#
#             result = result + S[i-1] + S[i]
#
# print(result)




