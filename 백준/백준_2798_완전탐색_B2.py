from itertools import combinations

N,M = map(int,input().split())

num_list = list(map(int,input().split()))


combi_all = list(combinations(num_list,3))

combi_under_M = []


for i in combi_all:

    if sum(i) <= M:

        combi_under_M.append(sum(i))

print(max(combi_under_M))



