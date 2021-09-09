str1 = input("문장 입력:")
str2 = []
str2.append(str1[0])

for i in range(1,len(str1)):
    count = 0
    for j in range(0,i):
        if str1[i] == str1[j]:
            count = count + 1
    if count < 1:
        str2.append(str1[i])

print(str2,"알파벳 만으로 구성")
