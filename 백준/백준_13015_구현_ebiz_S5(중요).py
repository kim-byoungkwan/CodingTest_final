N = int(input())

star_1 = ''

star_gap = ''

star_2 = ''

for i in range(1,N+1):

    if i == 1:

        star_1 = star_1 + "*" *N

        star_gap = star_gap + " " *((2*N)-(2*i+1))

        star_2 = star_2 + "*" *N

        print(star_1, end='')

        print(star_gap, end='')

        print(star_2)

        star_1 = ''

        star_gap = ''

        star_2 = ''

    elif i == N:

        star_1 = star_1 + " " *(N-1) + "*" + " " *(N-2) + "*" + " " *(N-2) + "*"

        print(star_1)

        star_1 = ''

    else:

        star_1 = star_1 + " " *(i-1) + "*" + " " *(N-2) + "*"

        star_gap = star_gap + " " * ((2 * N) - (2 * i + 1))

        star_2 = star_2 + "*" + " " *(N-2) + "*"

        print(star_1,end='')

        print(star_gap, end='')

        print(star_2)

        star_1 = ''

        star_gap = ''

        star_2 = ''


for j in range(2,N+1):

    if j != N:

        star_1 = star_1 + " " *(N-j) + "*" + " " *(N-2) + "*"

        star_gap = star_gap + " " * ((2*(j-1))-1)

        star_2 = star_2 + "*" + " " *(N-2) + "*"

        print(star_1, end='')

        print(star_gap, end='')

        print(star_2,)

        star_1=''

        star_gap = ''

        star_2=''

    else:

        star_1 = star_1 + "*" *N

        star_gap = star_gap + " " * ((2*(j-1))-1)

        star_2 = star_2 + "*" *(N)

        print(star_1, end='')

        print(star_gap, end='')

        print(star_2)

        star_1 =''

        star_gap =''

        star_2= ''








