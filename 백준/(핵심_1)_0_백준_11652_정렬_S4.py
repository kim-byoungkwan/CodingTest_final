import sys

N = int(sys.stdin.readline())

dict = {}

for _ in range(N):

    num = int(sys.stdin.readline())

    dict[num] = dict.get(num,0) + 1

print(sorted(dict.items(),key= lambda x: (-x[1],x[0]))[0][0])

# key = lambda x : (x[1]), reverse =True 와 같이 reverse = True 조건이 정의 되지 않으면 무조건 정렬대상은 최초에 오름차순으로 정렬된다.
# 즉, 이경우 x[0]에 대한 값은 표현되지 않았으므로, 자동으로 오름차순 정렬로 표현되는 상태인 것이다.






