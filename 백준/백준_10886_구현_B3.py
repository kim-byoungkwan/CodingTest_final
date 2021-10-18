N = int(input())

arr = [0]*2

for _ in range(N):

    word = int(input())

    arr[word] += 1

if arr.index(max(arr))==0:

    result = 'not cute!'

    print("Junhee is {}".format(result))

else:

    result = 'cute!'

    print("Junhee is {}".format(result))
