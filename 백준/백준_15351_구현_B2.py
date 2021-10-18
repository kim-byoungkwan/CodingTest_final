N = int(input())

for _ in range(N):

    result = 0

    word = input()

    for i in word:

        if i ==' ':

            continue

        else:

            result += ord(i)-64

    if result ==100:

        print("PERFECT LIFE")

    else:

        print(result)

