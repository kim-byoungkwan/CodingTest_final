n = int(input())

dict = {}

for _ in range(n):

    name,dd,mm,yyyy = input().split()

    dict[name] = list(map(int,[yyyy,mm,dd]))

print(sorted(dict.items(),key=lambda x: (x[1][0],x[1][1],x[1][2],x[0]))[-1][0])

print(sorted(dict.items(),key=lambda x: (x[1][0],x[1][1],x[1][2],x[0]))[0][0])
