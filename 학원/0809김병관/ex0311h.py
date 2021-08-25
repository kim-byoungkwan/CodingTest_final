array = input("공백을 구분자로 하는 숫자배열 입력:").split()
print(array)

max = int(array[0])
min = int(array[0])

for i in array:
    if int(i) > max:
        max = int(i)
    if int(i) < min:
        min = int(i)
print("최대값:",max)
print("최소값:",min)
