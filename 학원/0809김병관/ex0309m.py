str1 = input("영어단어 입력:")
str2 = ""

length = len(str1)

for i in range(0,length):
    str2 = str2 + str1[length - 1 - i]

print(str1,"철자의 순서를 바꾸면:",str2)
