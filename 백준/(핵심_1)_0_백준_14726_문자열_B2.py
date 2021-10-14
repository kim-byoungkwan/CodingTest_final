###.2

T = int(input())

for _ in range(T):

    number = list(map(int,list(input())))

    for i in range(len(number)):

        if i % 2 ==0:

            number[i] = number[i]*2

            if number[i] >= 10:

                first = number[i] % 10

                second = number[i] // 10

                number[i] = first + second

            else:

                continue

        else:

            continue

    print("T" if sum(number) % 10 == 0 else "F")














































###.1

# n = int(input())
#
# for _ in range(n):
#
#     number = list(map(int,list(input())))
#
#     number = number[::-1]
#
#     print(number)
#
#     for i in range(len(number)):
#
#         if i % 2 == 0:
#
#             if number[i]*2 >= 10:
#
#                 temp = number[i]*2
#
#                 value = 0
#
#                 while temp:
#
#                     value = value + (temp % 10)
#
#                     temp = temp // 10
#
#                 number[i] = value
#
#             else:
#
#                 continue
#
#         else:
#
#             continue
#
#     print(number)
#
#     print(sum(number))
#
#     print("T" if sum(number) % 10 == 0 else "F")


