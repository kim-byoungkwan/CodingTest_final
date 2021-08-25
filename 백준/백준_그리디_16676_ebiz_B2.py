N = input()

length = len(N)

if N == "0":

    print(length)

elif int(N) < int("1"*length):

    print(length-1)

else:

    print(length)



