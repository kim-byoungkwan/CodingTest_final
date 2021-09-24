N = int(input())

num_region = sorted(list(map(int,input().split())))

budget = int(input())


if sum(num_region) < budget:

    print(max(num_region))

else:

    start = 0

    end = max(num_region)

    while start <= end:

        total = 0

        mid = (start + end)//2

        for i in num_region:

            if i > mid:

                total = total + mid

            else:

                total = total + i

        if total < budget:

            start = mid +1

        elif total > budget:

            end = mid -1

        else:

            break

    print(end)
