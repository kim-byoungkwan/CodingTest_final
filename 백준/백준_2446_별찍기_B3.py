N = int(input())

star = ''

for i in range(1,N+1):

    star = star +" " *(i-1) +"*" *((2*N)-((2*i)-1))

    print(star)

    star = ''


for j in range(1,N):

    star = star + " " *(N-(j+1)) + "*" * ((2*j)+1)

    print(star)

    star = ''


