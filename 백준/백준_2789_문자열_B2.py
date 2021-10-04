standard = ['C','A','M','B','R','I','D','G','E']

word = input()

result = ''

for i in word:

    if i in standard:

        continue

    else:

        result = result + i

print(result)