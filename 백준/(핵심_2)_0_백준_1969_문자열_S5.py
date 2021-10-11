###.2

N,M = map(int,input().split())

arr = ['']*M


matrix = [[] for _ in range(N)]

for i in range(N):

    word = list(input())

    matrix[i] = word

for n in range(M):

    for m in range(N):

        arr[n] = arr[n] + matrix[m][n]

result = ''

for k in arr:

    answer = max(sorted(k),key=k.count)

    result += answer

print(result)

count = 0

for p in range(N):

    for q in range(M):

        if result[q] != matrix[p][q]:

            count += 1

print(count)






















































###.1 (문제 잘못 이해)


# N,M = map(int,input().split())
#
# arr = [0]*N
#
# dict = {}
#
# for i in range(N):
#
#     word = input()
#
#     arr[i] = word
#
# print(arr)
#
# for m in range(N):
#
#     count = 0
#
#     for n in range(N):
#
#         if m==n:
#
#             continue
#
#         else:
#
#             for p in range(M):
#
#                 if arr[m][p] != arr[n][p]:
#
#                     count += 1
#
#                 else:
#
#                     continue
#
#     dict[arr[m]] = count
#
# print(dict)