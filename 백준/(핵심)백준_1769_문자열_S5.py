N_list = list(input())

count = 0

sum = 0

if len(N_list) <= 1:

    sum = int(N_list[0])

while len(N_list) > 1:

    for i in N_list:

        i_int = int(i)

        sum += i_int

    count += 1

    if sum >= 10:

        N_list = []

        while sum != 0:

            N_list.append(sum % 10)

            sum = sum // 10

    else:

        break

print(count)

if sum %3 ==0:

    print('YES')

else:

    print('NO')