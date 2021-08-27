N = int(input())

star = ''

for i in range(1,N+1):

    star = star + " " *(N-i) + ("*"+" ")*i

    print(star)

    star = ''
