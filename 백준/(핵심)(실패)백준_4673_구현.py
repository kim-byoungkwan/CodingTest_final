def d(n):

    answer = n

    num_int = n

    num_str = str(n)

    for i in num_str:

        answer = answer + int(i)

    return answer

not_self_number = []

all_number = list(range(1,10001))


for i in range(1,10001):

    if d(i) <= 10000:

        not_self_number.append(d(i))

    else:

        continue

all_number = set(all_number)

not_self_number = set(not_self_number)

result = all_number - not_self_number

for i in sorted(result):

    print(i)
