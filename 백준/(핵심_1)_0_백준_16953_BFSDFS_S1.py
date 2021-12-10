




























###.1

# from collections import deque
#
# import sys
#
# input = sys.stdin.readline
#
# A,B = map(int,input().split())
#
# max = 10**9
#
# queue = deque()
#
# def bfs(x,y):
#
#     count = 0
#
#     queue.append((x,count))
#
#     while queue:
#
#         num, cnt = queue.popleft()
#
#         for nx in (num*2,int(str(num)+str(1))):
#
#             if nx > max:
#
#                 continue
#
#             new_cnt = cnt +1S
#
#             queue.append((nx,new_cnt))
#
#             if nx == y:
#
#                 return new_cnt+1
#
#     return -1
#
# print(bfs(A,B))
