from itertools import combinations

L,C = map(int,input().split())

word = list(input().split())

vowel = ['a','e','i','o','u']

word_consonant = []

word_vowel = []

result = []

for m in word:

    if m in vowel:

        word_vowel.append(m)

    else:

        word_consonant.append(m)

combi_vowel = []

combi_consonant = []

for i in range(1,len(word_vowel)+1):

    combi_vowel.append(list(combinations(word_vowel,i)))

for j in range(2,len(word_consonant)+1):

    combi_consonant.append(list(combinations(word_consonant,j)))


print(combi_vowel)

print()

print(combi_consonant)