###.1

N = int(input())

me,relative = map(int,input().split())

num_rel = int(input())


adjacency_list = [[] for _ in range(N+1)]


for _ in range(num_rel):

    A,B = map(int,input().split())

    adjacency_list[A].append(B)

    adjacency_list[B].append(A)

    adjacency_list[A].sort()

    adjacency_list[B].sort()

print(adjacency_list)

visited = [False] * (N + 1)

def dfs(V):

    stack = [V]

    visited[V] = True

    record = []

    while stack:

        current = stack.pop()

        record.append(current)

        for i in adjacency_list[current]:

            if visited[i] == False:

                visited[i] = True

                stack.append(i)

    return record


for i in range(1,N+1):

    if visited[i] == False:

        print(dfs(i))

    else:

        continue





