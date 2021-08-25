list1 = [4,2,3,8,7,1]

for i in range(0,len(list1)):
    for j in range(0,len(list1) - 1):
        if list1[j] > list1[j+1]:
            tmp = list1[j+1]
            list1[j+1] = list1[j]
            list1[j] = tmp

print(list1)
