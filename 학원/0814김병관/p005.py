def solve(num):
    arr = []
    for a in range(1,num+1):
        if a % 3 == 0:
            arr.append("X")
        else:
            arr.append(str(a))
    return arr

arr2 = []
str2 = ""
num = int(input("숫자입력:"))
arr2 = solve(num)

for a in arr2:
    str2 = str2 + " " + a
print(str2)
