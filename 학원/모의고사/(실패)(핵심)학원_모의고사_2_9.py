L,C = map(int,input().split())

word = input().split()

standard = ['a','e','i','o','u']

result_A = ''

result_B = ''

for i in word:

    if i in standard:

        result_A = result_A + i

    else:

        result_B = result_B + i

