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

# 보다 효율적인 방법(N이 K의 배수가 되도록 효율적으로 한번에 빼는 방식)

n, k = map(int,input().split())

result = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때 까지 1씩 빼기
    target = (n // k ) * k
    result = result + (n - target)
    n = target

    if n < k:
        break
    result = result + 1
    n = n // k

result = result + (n - 1)
print(result)
