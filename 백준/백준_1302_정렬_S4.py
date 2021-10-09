N = int(input())

dict = {}

for _ in range(N):

    name = input()

    dict[name] = dict.get(name,0) + 1

print(sorted(dict.items(),key=lambda x: (-x[1],x[0]))[0][0])
