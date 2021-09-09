# 숫자 카드 게임

# 숫자가 쓰인 카드들이 N * M 형태로 놓여 있다
# 각 행마다 가장 작은 수를 뽑기
# 뽑은 수들 중 가장 큰 수 뽑기

# 입력예시
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 출력예시
# 2

n, m = map(int,input().split())

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)
