###.2

T = int(input())

box = []

for _ in range(T):

    num = int(input())

    box.append(num)

new_box = sorted(box,reverse=True)

answer = 0

for i in range(len(new_box)):

    if i % 3 == 2:

        continue

    else:

        answer += new_box[i]

print(answer)




































###.1

# N = int(input())
#
# box = []
#
# for _ in range(N):
#
#     num = int(input())
#
#     box.append(num)
#
# box = sorted(box,reverse=True)
#
# count = 0
#
# result = []
#
# for i in box:
#
#     count +=1
#
#     if count % 3 == 0:
#
#         continue
#
#     else:
#
#         result.append(i)
#
# print(sum(result))



