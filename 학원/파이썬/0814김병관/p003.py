arr = []
mx = 0

for a in range(9):
    num = int(input("숫자입력:"))
    arr.append(num)

for b in range(9):
    if mx < arr[b]:
        mx = arr[b]
        index = b

print(mx,index+1)
