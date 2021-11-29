###.2









































###.1

# import heapq
#
# import sys
#
# INF = int(1e9)
#
# input = sys.stdin.readline
#
# N,E = map(int,input().split())
#
# graph = [[] for _ in range(N+1)]
#
# for _ in range(E):
#
#     a,b,c = map(int,input().split())
#
#     graph[a].append((b,c))
#
#     graph[b].append((a,c))
#
# v1,v2 = map(int,input().split())
#
# def dijkstra(start):
#
#     distance = [INF] * (N + 1)
#
#     distance[start] = 0
#
#     h = []
#
#     heapq.heappush(h,(0,start))
#
#     while h:
#
#         dist,now = heapq.heappop(h)
#
#         if distance[now] < dist:
#
#             continue
#
#         for i in graph[now]:
#
#             cost = dist + i[1]
#
#             if cost < distance[i[0]]:
#
#                 distance[i[0]] = cost
#
#                 heapq.heappush(h,(cost,i[0]))
#
#     return distance
#
# result_1 = dijkstra(1)
#
# result_v1 = dijkstra(v1)
#
# result_v2 = dijkstra(v2)
#
#
# answer_1 = result_1[v1] + result_v1[v2] + result_v2[N]
#
# answer_2 = result_1[v2] + result_v2[v1] + result_v1[N]
#
# final = min(answer_1,answer_2)
#
# if final < INF:
#
#     print(final)
#
# else:
#
#     print(-1)
