length = int(input("삼각형 길이 입력:"))
n = -1

for i in range(0,length):
    s_str = ""
    for j in range(0,length):
        if j > n:
            s_str = s_str + "*"
        else:
            s_str = s_str + " "
    n = n + 1
    print(s_str)
