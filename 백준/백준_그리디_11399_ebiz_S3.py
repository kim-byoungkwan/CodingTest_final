num = int(input())

box = []

time = list(map(int,input().split()))

time.sort()

for i in range(len(time)):

    box.append(sum(time[:i+1]))

print(sum(box))




