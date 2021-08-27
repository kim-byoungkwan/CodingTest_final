N = int(input())

star = ''

for i in range(1,N+1):

    star = star + " " *(N-i) + "*" *(i)

    print(star)

    star = ''

for j in range(1,N):

    star = star + " "*(j) + "*" *(N-j)

    print(star)

    star = ''