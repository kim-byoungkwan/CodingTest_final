###.2

dp = [0] *46

dp[0] = 0

dp[1] = 1

n = int(input())

for i in range(2,n+1):

    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])





































###.1

# def fibo(n):
#
#     if n <= 1:
#
#         return n
#
#     else:
#
#         return fibo(n-1) + fibo(n-2)
#
#
# n = int(input())
#
# print(fibo(n))
