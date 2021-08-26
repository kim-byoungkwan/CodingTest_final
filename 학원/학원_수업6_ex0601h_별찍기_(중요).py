length = int(input("삼각형의 길이 입력:"))

for i in range(length):

    star = ""

    for j in range(length):

        if j >= length -1 -i:

            star = star + "*"

        else:

            star = star + " "

    print(star)