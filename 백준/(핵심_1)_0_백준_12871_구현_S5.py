s = input()

t = input()

result = 1

for i in range(len(s)*len(t)):

    if s[i % len(s)] == t[i % len(t)]:

        continue

    else:

        result = 0

print(result)



























































###.1

# s = input()
#
# t = input()
#
# if len(set(s)) == len(set(t)) and len(set(s)) == 1 and set(s) == set(t):
#
#     print(1)
#
# else:
#
#     if len(s) >= len(t):
#
#         target = s
#
#         shot = t
#
#     else:
#
#         target = t
#
#         shot = s
#
#     portion = len(target) // len(shot)
#
#     if shot*portion == target:
#
#         print(1)
#
#     else:
#
#         print(0)
#
