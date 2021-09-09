# 큰 수의 법칙

# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을
# M번 더하여 가장 큰 수를 만드는 법칙이라 하고
# 단 배열의 특정한 인덱스에 해당하는 수가 연속해서
# K번을 초과하여 더해 질 수 없는 것이 이 법칙의 특징이라 가정한다.

# 예를 들어 순서대로 2,4,5,4,6 으로 이루어진 크기가 N인 배열이 있을 때
# M이 8이고 K가 3이라 가정하면 6+6+6+5+6+6+6+5 = 46 이 된다.

# 입력예시
# 5 8 3
# 2 4 5 4 6

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int,input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

data.sort()
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result = result + first
        m = m - 1
    if m == 0:
        break
    result = result + second
    m = m - 1

print(result)
