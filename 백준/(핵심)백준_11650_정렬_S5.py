import sys


N = int(sys.stdin.readline())

arr = []

for _ in range(N):

    position = list(map(int,sys.stdin.readline().split()))

    arr.append(position)

for result in sorted(arr,key = lambda x : (x[0],x[1])):

# key = lambda 에서의 x는 정렬하고자하는 리스트 arr의 각각의 요소를 표현한다. 그런데 이 경우 요소는 list 이므로 x의 인덱스를 x[0] , x[1] 과 같이 결정할 수 있고, 항상 정렬의 디폴트 값은 오름차순이므로, arr의 list 형의 각 요소의 [0]번째를 기준으로 오름차순으로 먼저 정렬하고, 그 뒤 [1]번째를 기준으로 오름차순으로 정렬한다.

    print(result[0], end =' ')

    print(result[1])

