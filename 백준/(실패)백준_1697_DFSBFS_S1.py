###.1

# import sys
#
# import heapq
#
# input = sys.stdin.readline
#
# N,K = map(int,input().split())
#
# h = []
#
# def bfs(N,K):
#
#     count = 0
#
#     heapq.heappush(h,(count,N))
#
#     while h:
#
#         count,value = heapq.heappop(h)
#
#         count += 1
#
#         for i in [value-1,value+1,value*2]:
#
#             if i < 0 or i > 100000:
#
#                 continue
#
#             if i == K:
#
#                 return count
#
#             heapq.heappush(h,(count,i))
#
# print(bfs(N,K))

