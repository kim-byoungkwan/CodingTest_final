while True:

    n = int(input())

    if n ==0:

        break

    else:

        arr = []

        for _ in range(n):

            word = input()

            word_small = word.lower()

            arr.append((word,word_small))

        print(sorted(arr,key=lambda x: x[1])[0][0])
