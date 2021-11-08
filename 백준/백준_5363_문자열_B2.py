n = int(input())

for _ in range(n):

    word = input().split()

    temp = word[:2]

    original = word[2:]

    result = original + temp

    print(' '.join(result))
