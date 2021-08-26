def binary_search(array,target,start,end):

    while start <= end:

        mid = (start + end)//2

        if array[mid] > target:

            end = mid - 1

        elif array[mid] < target:

            start = mid + 1

        else:

            return mid

    return None


n = int(input())

array = list(map(int,input().split()))

array.sort()

m = int(input())

x = list(map(int,input().split()))



for i in x:

    result = binary_search(array,i,0,n-1)

    if result != None:

        print('Yes',end=' ')

    else:

        print('No',end=' ')





