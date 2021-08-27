N = int(input())

star = ''

for i in range(1,N+1):

    star = star + " "*(N-i) + "*"*((2*i)-1)

    print(star)

    star = ''

for j in range(1,N):

    star = star + " "*j + "*"*(2*N-(2*j+1))

    print(star)

    star = ''