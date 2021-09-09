length = int(input("길이 입력:"))

for i in range(0,length):
    s_str = ""
    for j in range(0,i+1):
        s_str = s_str + "*"
    print(s_str)


for m in range(0,length-1):
    s_str = ""
    for n in range(0,length-1-m):
        s_str = s_str + "*"
    print(s_str)
