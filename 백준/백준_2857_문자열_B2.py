count = 0

result = []

for _ in range(5):

    count +=1

    S = input()

    if 'FBI' in S:

        result.append(count)

    else:

        continue

if result:

    print(' '.join(list(map(str,result))))

else:

    print("HE GOT AWAY!")