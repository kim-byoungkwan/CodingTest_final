list1 = [14,5,12,8,9,23,17]

max = list1[0]
min = list1[0]

for i in list1:
    if i > max:
        max = i

    if i < min:
        min = i

print("최대값은 %d" %max)
print("최소값은 %d" %min)
