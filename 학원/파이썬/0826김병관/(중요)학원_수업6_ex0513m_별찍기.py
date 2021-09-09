length = int(input("삼각형의 길이 입력:"))

n = length

for i in range(length):

    star = ""

    for j in range(n):

        star = star + "*"

    n = n-1

    print(star)
