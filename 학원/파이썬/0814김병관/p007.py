def solve(num):
    ans = 0
    for a in range(1,num+1):
        if num % a == 0:
            ans = ans + a
    return ans

num = int(input("숫자입력:"))
print(solve(num))    
