###.2


import sys

stamp = 0

while stamp // k < k:

    n, k = map(int, input().split())

    coupon = n

    coupon = coupon + n // k

    stamp = n + n // k

    coupon += stamp // k

    print(coupon)

























































###.1

# import sys
#
# while True:
#
#     try:
#
#         n,k = map(int,sys.stdin.readline().split())
#
#         count = 0
#
#         stamp = 0
#
#         while n != 0:
#
#             n -= 1
#
#             stamp += 1
#
#             count += 1
#
#             if stamp == k:
#
#                 n += 1
#
#                 stamp = 0
#
#         print(count)
#
#     except:
#
#         break