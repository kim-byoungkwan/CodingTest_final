S =input()

for i in S:

    box = []

    num = ord(i)

    while num:

        residual = num % 10

        box.append(residual)

        num = num // 10

    count = sum(box)

    print(i*count)

