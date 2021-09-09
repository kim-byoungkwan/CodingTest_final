import sys


def avr(arr):

    result = round(sum(arr) / len(arr))

    return result

def mid(arr):

    arr.sort()

    return arr[len(arr)//2]

def many(arr):

    box = []

    dict = {}

    for i in arr:

        dict[i] = dict.get(i,0) + 1

    for key,value in dict.items():

        if value == max(dict.values()):

            box.append(key)

        else:

            continue

    if len(box) > 1:

        return sorted(box)[1]

    else:

        return box[0]


def diff(arr):

    return max(arr) - min(arr)


N = int(sys.stdin.readline())

arr = []

for _ in range(N):

    arr.append(int(sys.stdin.readline()))

print(avr(arr))

print(mid(arr))

print(many(arr))

print(diff(arr))
