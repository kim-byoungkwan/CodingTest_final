s = 0

num  = int(input("숫자입력:"))

while(num > 0):
    s = s + (num % 10)
    num = num // 10

print("각 자리수의 합:",s)
