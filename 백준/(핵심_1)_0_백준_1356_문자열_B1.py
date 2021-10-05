num_list = list(input())

answer = 'NO'

for i in range(1,len(num_list)):

    result_former = 1

    result_latter = 1

    former = num_list[:i]

    latter = num_list[i:]

    for m in former:

        result_former = result_former*int(m)

    for n in latter:

        result_latter = result_latter*int(n)

    if result_former == result_latter:

        answer = 'YES'

        break

    else:

        continue

print(answer)
