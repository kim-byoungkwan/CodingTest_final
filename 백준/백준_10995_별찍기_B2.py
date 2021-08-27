N = int(input())

star = ''

for i in range(1,N+1):

    if i % 2 != 0:

        star = star + ("*" + " ") *(N)

        print(star)

        star = ''

    else:

        star = star + (" " + "*") *(N)

        print(star)

        star = ''


