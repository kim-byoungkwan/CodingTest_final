###.1

S = input()

stack = []

for i in range(len(S)):

    if stack:

        if stack[-1] == S[i]:

            stack.pop()

        else:

            stack.append(S[i])

    else:

        stack.append(S[i])

print(stack)

print((len(stack)//2)//2)



















###.1 (실패)

# S = input()
#
# count = 0
#
# for i in range(1,len(S),2):
#
#     print(i)
#
#     if S[i-1] != S[i]:
#
#         count += 1
#
#     else:
#
#         continue
#
# print(count//2)
