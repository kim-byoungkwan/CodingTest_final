array = [1,5,2,9,7]
i = 0
max = 1

while i < 5:
    if array[i] > max:
        max = array[i]
    i = i + 1
print("최대값:",max)
