###.1

N = int(input())

star = ''

for i in range(1,N+1):

    star = star + "*"*(N+1-i)

    print(star)

    star = ''
