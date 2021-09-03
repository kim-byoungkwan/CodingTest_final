criteria = ['U','C','P','C']

word = input()

cri_index = 0

for word_index in range(len(word)):

    if criteria[cri_index] == word[word_index]:

        cri_index = cri_index + 1

        if cri_index == len(criteria):

            break

if cri_index == len(criteria):

    print("I love UCPC")

else:

    print("I hate UCPC")



