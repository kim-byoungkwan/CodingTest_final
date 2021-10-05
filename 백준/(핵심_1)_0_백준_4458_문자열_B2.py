T = int(input())

for _ in range(T):

    word = list(input())

    temp = word[0]

    new = temp.upper()

    word[0] = new

    print(''.join(word))
    