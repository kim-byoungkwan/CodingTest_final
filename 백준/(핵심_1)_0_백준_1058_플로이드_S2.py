import sys

input = sys.stdin.readline

N = int(input())

matrix = [[] for _ in range(N)]

visited = [[0]*N for _ in range(N)]

for i in range(N):

    matrix[i] = list(input().rstrip())

for k in range(N):

    for p in range(N):

        for q in range(N):

            if p == q:

                continue

            if matrix[p][q] == 'Y' or (matrix[p][k] == 'Y' and matrix[k][q] == 'Y'):

                visited[p][q] = 1

result = 0

for m in range(N):

    result = max(result,sum(visited[m]))

print(result)













































###.1

# N = int(input())
#
# matrix = [[] for _ in range(N)]
#
# for i in range(N):
#
#     friend_list = list(input())
#
#     matrix[i] = friend_list
#
# for a in range(N):
#
#     for b in range(N):
#
#         if matrix[a][b] == 'N':
#
#             matrix[a][b] = 0
#
#         else:
#
#             matrix[a][b] = 1
#
# for k in range(N):
#
#     for p in range(N):
#
#         for q in range(N):
#
#             if p == q:
#
#                 continue
#
#             if matrix[p][q] or (matrix[p][k] and matrix[k][q]):
#
#                 matrix[p][q] = 1
#
# result = 0
#
# for m in range(N):
#
#     result = max(result,sum(matrix[m]))
#
# print(result)



# 반례 : a와b와 친구이고,b와c가 친구이고 c와d가 친구일때, a와 d는 친구로 인정되지 않지만 위와 같이 매트릭스에서 직접 플로이드 워셜을 적용하는 방법은 최단거리를 구하는 방법처럼 연쇄적인 모든 값이 표현되기때문에 a와d도 친구로 인정되는 상황이 발생하여 문제가 생긴다.










