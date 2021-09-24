dict = {}

N = int(input())


for _ in range(N):

    age, name = input().split()

    dict[age] = dict.get(age,[]) + [name]

dict = sorted(dict.items())

for key,value in dict:

    for i in value:

        print(key,end=' ')

        print(i)
