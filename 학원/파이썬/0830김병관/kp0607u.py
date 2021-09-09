t_h = int(input("삼각형의 높이 입력:"))

t_w = -1
for m in range(0,t_h):
    t_w = t_w + 2

n = 0
for i in range(0,t_h):
    str_s = ""
    for j in range(0,t_w):
        if (j < (t_w // 2) - n) or (j > (t_w // 2) + n):
            str_s = str_s + " "
        else:
            str_s = str_s + "*"
    n = n + 1
    print(str_s)


n = 0
for i in range(0,t_h - 1):
    str_s = ""
    for j in range(0,t_w):
        if (j > n) and (j <= t_w - n - 2):
            str_s = str_s + "*"
        else:
            str_s = str_s + " "
    n = n + 1
    print(str_s)
