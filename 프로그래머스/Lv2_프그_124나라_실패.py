store = {}

store_124 = [1,2,4,11,12,14,21,22,24,41]

for i in range(1,11):

    store[i] = store_124[i-1]

print(store)

num = list(input())


for i in range(len(num)):

    if num[i] == store.keys():

        print(store.values())












