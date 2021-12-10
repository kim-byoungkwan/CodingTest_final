###.2

import sys

input = sys.stdin.readline

N,C = map(int,input().split())

time_box = [False]*(C+1)

answer = 0

for _ in range(N):

    time = int(input())

    for i in range(time,C+1,time):

        if time_box[i] == False:

            time_box[i] = True

            answer +=1

print(answer)

































###.1

# import sys
#
# input = sys.stdin.readline
#
# N,C = map(int,input().split())
#
# box_time = [0]*(C+1)
#
# for _ in range(N):
#
#     time_original = int(input())
#
#     time = time_original
#
#     while time <= C:
#
#         if box_time[time]:
#
#             time = time + time_original
#
#             continue
#
#         else:
#
#             box_time[time] = 1
#
#             time = time + time_original
#
# print(box_time.count(1))

