###.1

# from itertools import combinations
#
# import sys
#
# N = int(sys.stdin.readline())
#
# arr = []
#
# arr_combi = []
#
# arr_all_combi = []
#
# result = []
#
# for _ in range(N):
#
#     arr.append(int(sys.stdin.readline()))
#
# for i in range(1,N+1):
#
#     arr_combi.append(list(combinations(arr,i)))
#
# for m in arr_combi:
#
#     for n in m:
#
#         arr_all_combi.append(n)
#
# for k in arr_all_combi:
#
#     answer = min(k)
#
#     final = answer*len(k)
#
#     result.append(final)
#
# print(max(result))


###.2

T = int(input())

arr = []

result = []

count = 0

answer = []

for _ in range(T):

    arr.append(int(input()))

for i in sorted(arr,reverse=True):

    count += 1

    answer.append(i*count)

print(max(answer))