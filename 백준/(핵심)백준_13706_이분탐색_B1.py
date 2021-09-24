###.1

# import sys
#
# N = int(sys.stdin.readline())
#
# for i in range(1,N+1):
#
#     if i**2 == N:
#
#         print(i)
#
#         break
#
#     else:
#
#         continue


###.2

N = int(input())

start = 1

end = N

while start <= end:

    mid = (start+end)//2

    if mid**2 > N:

        end = mid-1

    elif mid**2 < N:

        start = mid+1

    else:

        print(mid)

        break
