n = int(input())

S = input()

for i in range(len(S)):

    if S[i].isalpha():

        S = S.replace(S[i],' ')

result = 0

for i in S.split(' '):

    if i =='':

        continue

    else:

        i = int(i)

        result += i

print(result)


###.문자열 연습

word = 'a,'+'b,'+'1'+'c,'+'2'+','

print(word)

print(word.split(','))
