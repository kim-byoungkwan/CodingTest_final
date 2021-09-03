word = list(input())

alphabet = 'abcdefghijklmnopqrstuvwxyz'

dict = {}

for k in alphabet:

    dict[k] = dict.get(k,0)

for i in word:

    dict[i] = dict.get(i) + 1

value_list = list(dict.values())

answer = ' '.join(list(map(str,value_list)))

print(answer)
