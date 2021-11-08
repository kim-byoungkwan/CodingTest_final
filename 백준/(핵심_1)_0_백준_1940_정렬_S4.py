###.2

N = int(input())

M = int(input())

num = sorted(list(map(int,input().split())))

left = 0

right = N-1

count = 0

while left < right:

    result = num[left] + num[right]

    if result == M:

        count += 1

        left = left + 1

        right = right -1

    elif result < M:

        left = left + 1

    elif result > M:

        right = right -1

print(count)














































###.1

# import sys
#
# N = int(sys.stdin.readline())
#
# M = int(sys.stdin.readline())
#
# num = sorted(list(map(int,sys.stdin.readline().split())))
#
# count = 0
#
# for i in range(len(num)-1):
#
#     if num[i:][0] + num[i:][-1] < M:
#
#         continue
#
#     else:
#
#         for j in range(i+1,len(num)):
#
#             if num[i]+num[j] == M:
#
#                 count +=1
#
# print(count)