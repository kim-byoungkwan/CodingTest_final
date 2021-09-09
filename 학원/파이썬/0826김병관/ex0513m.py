length = int(input("삼각형의 길이 입력:"))
n = length

for i in range(0,length):
    s_str = ""
    for j in range(0,n):
        s_str = s_str + "*"
    n = n - 1
    print(s_str)
