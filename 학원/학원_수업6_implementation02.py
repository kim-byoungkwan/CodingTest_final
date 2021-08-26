data = input()

result = []

value = 0

for i in data:

    if i.isalpha():

        result.append(i)

    else:

        value = value + int(i)

result.sort()

if value != 0:

    result.append(str(value))

    print(''.join(result))

else:

    print(''.join(result))

