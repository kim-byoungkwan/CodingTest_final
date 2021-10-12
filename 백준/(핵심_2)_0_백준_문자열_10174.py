###.sol

n = int(input())

for _ in range(n):

    word = input().lower()

    print("Yes" if word == word[::-1] else "No")














































###.1

# from collections import deque
#
# n = int(input())
#
# for _ in range(n):
#
#     queue = deque()
#
#     stack = []
#
#     result = True
#
#     word = input()
#
#     for i in word:
#
#         value = i.lower()
#
#         queue.append(value)
#
#         stack.append(value)
#
#     for _ in range(len(stack)):
#
#         if stack.pop() == queue.popleft():
#
#             continue
#
#         else:
#
#             result = False
#
#     if result == True:
#
#         print("Yes")
#
#     else:
#
#         print("No")

