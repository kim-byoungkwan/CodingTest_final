w = int(input("가로길이 입력:"))
h = int(input("세로길이 입력:"))

for i in range(0,h):
    s_str = ""
    for j in range(0,w):
        s_str = s_str + "*"
    print(s_str)
