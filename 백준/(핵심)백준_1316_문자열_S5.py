N = int(input())

count = 0

for _ in range(N):

    word = input()

    for i in range(1,len(word)):

        if word[i-1] == word[i]:

            continue

        else:

            if word[i-1] in word[i:]:

                count +=1

                break

            else:

                continue

print(N-count)