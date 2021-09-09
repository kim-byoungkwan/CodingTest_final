###.1

# import sys
#
# from itertools import permutations
#
# N = list(sys.stdin.readline())
#
# per_list = list(permutations(N))
#
# box = []
#
# for i in per_list:
#
#     value_int = int(''.join(i))
#
#     if value_int % 30 == 0:
#
#         box.append(value_int)
#
#     else:
#
#         continue
#
# if box:
#
#     print(max(box))
#
# else:
#
#     print(-1)

###.2

N = list(input())

list_int = list(map(int,N))

list_int.sort(reverse=True)

if sum(list_int) % 3 == 0 and list_int[-1] == 0:

    print(''.join(list(map(str,list_int))))

else:

    print(-1)






