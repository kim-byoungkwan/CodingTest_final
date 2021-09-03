###.1

# S = list(map(int,input()))
#
# num_zero = S.count(0)
#
# num_one = S.count(1)
#
# for i in range(num_zero//2):
#
#     S.remove(0)
#
# for j in range(num_one//2):
#
#     S.remove(1)
#
# print(''.join(list(map(str,sorted(S)))))


###.2

# from collections import deque
#
# S = list(input())
#
# num_zero = S.count('0')
#
# num_one = S.count('1')
#
# S.sort()
#
# queue = deque(S)
#
#
# for i in range(num_zero//2):
#
#     queue.popleft()
#
# for j in range(num_one//2):
#
#     queue.pop()
#
# print(''.join(list(map(str,queue))))






