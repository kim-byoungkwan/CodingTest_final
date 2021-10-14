S = input()

find = input()

result = ''

for i in S:

    if i.isalpha():

        result += i

    else:

        continue

print("0" if result.count(find) == 0 else "1")
