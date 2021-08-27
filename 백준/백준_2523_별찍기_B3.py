N = int(input())

star = ''

for i in range(1,N+1):

    star = star + "*" *i

    print(star)

    star = ''

for j in range(1,N):

    star = star + "*"*(N-j)

    print(star)

    star = ''