h = int(input("세로길이 입력:"))

w = int(input("가로길이 입력:"))

for i in range(h):

    star = ""

    for j in range(w):

        star = star + "*"

    print(star)

    