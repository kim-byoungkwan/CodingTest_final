length = int(input("길이입력:"))

for i in range(length):

    star = ""

    for j in range(i+1):

        star = star + "*"

    print(star)


for m in range(length-1):

    star = ""

    for n in range(length-1-m):

        star = star + "*"

    print(star)

