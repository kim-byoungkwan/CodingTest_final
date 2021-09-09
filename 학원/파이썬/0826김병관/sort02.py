# 두 배열의 원소 교체

# 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는
# 첫번째 배열의 모든 원소의 합의 최대값을 출력하라

# 입력예시
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

# 출력예시
# 26

n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break

print(sum(a))

         
