standard = [0]*26

count = 0

n = int(input())

word_standard = input()

for i in word_standard:

    standard[ord(i)-65] = standard[ord(i)-65] + 1

for _ in range(n-1):

    result = []

    sample = [0]*26

    word_sample = input()

    for m in word_sample:

        sample[ord(m)-65] = sample[ord(m)-65] + 1

    for p in range(26):

        result.append(abs(standard[p] - sample[p]))

    if len(word_standard) == len(word_sample):

        if (26 - result.count(0)) <= 2:

            if sum(result) <= 2:

                count += 1

            else:

                continue

        else:

            continue

    else:

        if (26 - result.count(0)) <= 1:

            if sum(result) <= 1:

                count += 1

            else:

                continue

        else:

            continue

print(count)


