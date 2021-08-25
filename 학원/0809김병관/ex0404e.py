def f_sum(n):
    hap = 0
    for a in range(1,n+1):
        hap = hap + a
    return hap

n = int(input("숫자입력:"))
s = f_sum(n)
print("총합:",s)
