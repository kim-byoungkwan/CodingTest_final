###.1

# from collections import deque
#
# import sys
#
# array = deque()
#
# queue_all = deque()
#
# K,L = map(int,sys.stdin.readline().split())
#
# for i in range(L):
#
#     id_num = int(sys.stdin.readline())
#
#     queue_all.append(id_num)
#
# for j in range(len(queue_all)):
#
#     out = queue_all.popleft()
#
#     if out in array:
#
#         array.remove(out)
#
#         array.append(out)
#
#     else:
#
#         array.append(out)
#
# for m in range(K):
#
#     print(array.popleft())


###.2

import sys

K,L = map(int,sys.stdin.readline().split())

dict = {}

for i in range(L):

    id_num = sys.stdin.readline().rstrip()

    dict[id_num] = i

count = 0

for key,value in sorted(dict.items(), key = lambda x : x[1]):

    count = count +1

    print(key)

    if count == K:

        break




