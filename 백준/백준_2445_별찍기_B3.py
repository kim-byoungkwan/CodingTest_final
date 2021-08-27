N = int(input())

star_1 = ''

star_2 = ''

for i in range(1,N+1):

    star_1 = star_1 + "*" *(i) + " " *(N-i)

    star_2 = star_2 + " " *(N-i) + "*" *(i)

    result = star_1 + star_2

    print(result)

    star_1 = ''

    star_2 = ''

for j in range(1,N):

    star_1 = star_1 + "*" *(N-j) + " " *(j)

    star_2 = star_2 + " " *(j) + "*" *(N-j)

    result = star_1 + star_2

    print(result)

    star_1 = ''

    star_2 = ''