A,B = input().split()

min = 100

for k in range(abs(len(A)-len(B))+1):

    count = 0

    for i in range(len(A)):

        if A[i] == B[i+k]:

            continue

        else:

            count +=1

    if min >= count:

        min = count

    else:

        continue

print(min)