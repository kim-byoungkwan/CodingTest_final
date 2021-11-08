A,B = input().split()

result = []

A_list = list(A)

B_list = list(B)

while True:

    if A_list:

        first = A_list.pop()

    else:

        first = 0


    if B_list:

        second = B_list.pop()

    else:

        second = 0

    result.append(int(first) + int(second))

    if len(A_list) == 0 and len(B_list) == 0:

        break

print(''.join(list((map(str,result)))[::-1]))