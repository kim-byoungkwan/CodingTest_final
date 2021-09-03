list = ['pi','ka','chu']

word = input().rstrip()

for i in list:

    word = word.replace(i,'*')

box = []

for j in word:

    if j == '*':

        continue

    else:

        box.append('NO')

if 'NO' in box:

    print("NO")

else:

    print("YES")

