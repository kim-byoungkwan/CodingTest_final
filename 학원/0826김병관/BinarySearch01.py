# 이진 탐색

# 보유하고 있는 부품 개수와 부품 번호 중에서
# 손님이 요청한 부품 번호의 순서대로 부품을 확인해
# 있으면 yes 없으면 no 출력하기

# 입력 예시
# 5
# 8 3 7 9 2
# 3
# 5 7 9

# no yes yes

def binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int,input().split()))
array.sort()

m = int(input())
x = list(map(int,input().split()))

for i in x:
    result = binary_search(array,i,0,n-1)
    if result != None:
        print('yes',end =' ')
    else:
        print('no',end=' ')
