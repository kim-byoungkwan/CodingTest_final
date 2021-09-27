N = int(input())

arr = list(map(int,input().split()))

## 항상 진짜 약수가 작은 수부터 정렬되어 주어진 것이 아니므로, 0번째 인덱스 -1번째 인덱스를 이용하여 구하는 방법은
## 무수히 많은 반례가 존재할 수 있다.

print(min(arr) * max(arr))