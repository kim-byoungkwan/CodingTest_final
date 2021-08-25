list1 = [4,2,3,8,7,1]

for i in range(0,len(list1)):
    min_i = i
    for j in range(i+1,len(list1)):
        if list1[min_i] > list1[j]:
            min_i = j
    tmp = list1[min_i]
    list1[min_i] = list1[i]
    list1[i] = tmp

print(list1)
