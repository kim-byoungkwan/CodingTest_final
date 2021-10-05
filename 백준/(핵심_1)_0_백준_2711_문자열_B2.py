T = int(input())

for _ in range(T):

    location, word = input().split()

    word = list(word)

    del word[int(location)-1]

    print(''.join(word))
