word_first = input()

word_second = input()

standard_first = [0]*26

standard_second = [0]*26

answer = 0

for i in word_first:

    standard_first[ord(i)-97] += 1

for j in word_second:

    standard_second[ord(j)-97] += 1

for k in range(26):

    answer += (abs(standard_first[k] - standard_second[k]))

print(answer)
