N = int(input())

start = 0

end = N

result = 0

if N == 0:

    print(0)

else:

    while start <= end:

        mid = (start+end)//2

        if mid**2 > N:

            end = mid -1

        elif mid**2 < N:

            start = mid +1

        else:

            result = mid

            break

    if result == 0:

        print(start)

    else:

        print(result)