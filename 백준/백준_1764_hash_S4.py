N, M = map(int, input().split())

dict = {}

for i in range(N + M):

    name = input()

    dict[name] = dict.get(name, 0) + 1

result = []

for key, value in dict.items():

    if value >= 2:
        
        result.append(key)

print(len(result))

for j in sorted(result):

    print(j)