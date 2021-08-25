# 1이 될 때 까지

# 어떠한 수 N이 1이 될 때 까지 다음의 두 과정 중 하나를 반복적으로
# 수행하려 한다. 단 두번째 연산은 N 이 K로 나누어 질 때만
# 선택할 수 있다고 가정한다.
# 1) N에서 1일 뺀다.
# 2) N을 K로 나눈다.
# N을 1로 만드는 최소 횟수를 구하시오

# 입력 예시
# 25 5
# 출력 예시
# 2

n, k = map(int,input().split())

result = 0

while n >= k:
    while n % k != 0:
        n = n - 1
        result = result + 1
    n = n // k
    result = result + 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n = n - 1
    result = result + 1
print(result)

