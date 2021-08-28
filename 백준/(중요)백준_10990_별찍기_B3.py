N = int(input())

star = ''

for i in range(1,N+1):

    if i == 1:

        star = star + " " *(N-i) + "*"

        print(star)

        star = ''

    else:

        star = star + " " *(N-i) + "*" + " " *((2*(i-1))-1) + "*"

        print(star)

        star = ''

