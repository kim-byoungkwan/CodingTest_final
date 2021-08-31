import sys

N = int(sys.stdin.readline())

dict = {}

for i in range(1,N+1):

    car_in = sys.stdin.readline()

    dict[car_in] = [i]

for j in range(1,N+1):

    car_out = sys.stdin.readline()

    dict[car_out] = dict.get(car_out,[]) + [j]

count = 0

for value in dict.values():

    if value[0] > value[1]:

        count = count + 1

    else:

        continue

print(count)
