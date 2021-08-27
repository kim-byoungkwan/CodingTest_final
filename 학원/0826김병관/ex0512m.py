length = int(input("삼각형 길이 입력:"))

for i in range(0,length):
    s_str = ""
    for j in range(0,i+1):
        s_str = s_str + "*"
    print(s_str)
