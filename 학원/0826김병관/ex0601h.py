length = int(input("삼각형의 길이 입력:"))

for i in range(0,length):
    s_str = ""
    for j in range(0,length):
        if j >= length - 1 - i:
            s_str = s_str + "*"
        else:
            s_str = s_str + " "
    print(s_str)
