N = int(input())

number = list(map(int,input().split()))

up = False

height = 0

result = []

for i in range(1,len(number)):

    if number[i] - number[i-1] > 0:

        if up == False:

            up = True

            height = number[i] - number[i-1]

        else:

            height += number[i] - number[i-1]

    else:

        height = 0

        up = False

    result.append(height)

print(max(result))

