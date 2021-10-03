standard = ['a','e','i','o','u']

word = input()

count = 0

for i in word:

    if i in standard:

        count += 1

    else:

        continue

print(count)
