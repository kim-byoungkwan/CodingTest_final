###.1

# word = list(input())
#
# s = ''
#
# count = 0
#
# for i in word:
#
#     count += 1
#
#     s = s + i
#
#     if count == 10:
#
#         print(s)
#
#         s = ''
#
#         count = 0
#
#     else:
#
#         continue
#
# print(s)


###.2

word = input()

for i in range(0,len(word),10):

    print(i)

    print(word[i:i+10])
