###.2



n = int(input())

for _ in range(n):

    arr = [0] * 26

    word = input()

    for i in word:

        if i == ' ':

            continue

        else:

            index = ord(i)-97

            arr[index] +=1

    if arr.count(max(arr)) > 1:

        print('?')

    else:

        print(chr(arr.index(max(arr))+97))









































###.1

# n = int(input())
#
# for _ in range(n):
#
#     dict = {}
#
#     word = input()
#
#     for i in word:
#
#         if i == ' ':
#
#             continue
#
#         else:
#
#             dict[i] = dict.get(i,0) + 1
#
#     result = []
#
#     max = sorted(dict.items(), key=lambda x: -x[1])[0][1]
#
#     for j in sorted(dict.items(), key=lambda x: -x[1]):
#
#         if max == j[1]:
#
#             result.append((j[0],j[1]))
#
#             continue
#
#         else:
#
#             break
#
#     print('?' if len(result) >1 else result[0][0])
