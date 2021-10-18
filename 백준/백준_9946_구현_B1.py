###.2

count = 0

while True:

    count += 1

    first = input()

    second = input()

    if first == 'END' and second =='END':

        break

    else:

        if sorted(second) == sorted(first):

            result = 'same'

        else:

            result = 'different'

        print("Case {}: {}".format(count,result))















###.1

# count = 0
#
# while True:
#
#     count += 1
#
#     first = input()
#
#     second = input()
#
#     if first == 'END' and second =='END':
#
#         break
#
#     else:
#
#         arr_1 = [0] * 26
#
#         arr_2 = [0] * 26
#
#         for i in first:
#
#             arr_1[ord(i)-97] += 1
#
#         for j in second:
#
#             arr_2[ord(j)-97] += 1
#
#         if arr_1 == arr_2:
#
#             result = 'same'
#
#         else:
#
#             result = 'different'
#
#         print("Case {}: {}".format(count,result))

