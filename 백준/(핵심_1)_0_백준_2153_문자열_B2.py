S = input()

result = 0

for i in S:

    if i.isupper():

        result += (ord(i)-38)

    else:

        result += (ord(i)-96)

answer = []

for j in range(2,result):

    if result % j ==0:

        answer.append(-1)

    else:

        continue

if answer:

    print("It is not a prime word.")

else:

    print("It is a prime word.")
