# deque는 스택과 큐의 장점을 모두 채택한 것으로
# 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적임
# queue 라이브러리를 이용하는 것보다 더 간단함

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력

print(list(queue))
