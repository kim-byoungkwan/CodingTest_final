###.1

# from collections import deque
#
# N, K = map(int,input().split())
#
# answer = []
#
# queue = deque()
#
# for i in range(1, N + 1):
#
#     queue.append(i)
#
# while queue:
#
#     queue.rotate(-2)
#
#     check = queue.popleft()
#
#     answer.append(check)
#
# print("<", end='')
#
# count = 0
#
# for i in answer:
#
#     count += 1
#
#     if count == len(answer):
#
#         print(i,end='')
#
#     else:
#
#         print(i, end=", ")
#
# print(">",end='')


###.2

from collections import deque

N, K = map(int,input().split())

answer = []

queue = deque([i for i in range(1,N+1)])

while queue:

    queue.rotate(-2)

    check = queue.popleft()

    answer.append(check)

print('<' + ', '.join(map(str,answer)) + '>')