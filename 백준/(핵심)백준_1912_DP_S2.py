## dp의 요소값을 누적해서 더한 값으로 결정하는 것보다, 그냥 새로 시작하는 것이 더 큰 경우,
## 새로운 값으로 dp의 요소를 결정하는 동작이 핵심이다.

N = int(input())

arr = list(map(int,input().split()))

dp = [0]*N

dp[0] = arr[0]


for i in range(1,N):

    dp[i] = max(arr[i], dp[i-1]+arr[i])

print(max(dp))

