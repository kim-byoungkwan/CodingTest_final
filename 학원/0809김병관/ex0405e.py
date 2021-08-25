def f_factorial(n):
    f = 1
    for a in range(1,n+1):
        f = f * a
    return f

n = int(input("숫자입력:"))
fac = f_factorial(n)
print(n,"의 팩토리얼 값:",fac)
