###.1

# from itertools import combinations
#
# while True:
#
#     try:
#
#         s,t = input().split()
#
#         s_len = len(s)
#
#         t_all_combi = list(combinations(t,s_len))
#
#         s = tuple(s)
#
#         if s in t_all_combi:
#
#             print("YES")
#
#         else:
#
#             print("NO")
#
#     except:
#
#         break

###.2

while True:

    try:

        s,t = input().split()

        s_i = 0

        for t_i in range(len(t)):

            if s[s_i] == t[t_i]:

                s_i = s_i + 1

                if s_i == len(s):

                    break

        if s_i < len(s):

            print("No")

        else:

            print("Yes")

    except:

        break




