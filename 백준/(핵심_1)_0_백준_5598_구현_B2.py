S = input()

result = ''

for i in S:

    if ord(i) <=67:

        result += chr(ord(i) + 23)

    else:

        result += chr(ord(i)-3)

print(result)
