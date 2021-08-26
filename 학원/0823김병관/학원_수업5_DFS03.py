visited = [False]*9

adjacency_list = [[],
                  [2,3,8],
                  [1,7],
                  [1,4,5],
                  [3,5],
                  [3,4],
                  [7],
                  [2,6,8],
                  [1,7]]

def dfs(adjacency_list,visited,v):

    print(v, end=' ')

    visited[v] = True

    for i in adjacency_list[v]:

        if not visited[i]:

           dfs(adjacency_list,visited,i)


dfs(adjacency_list,visited,1)

# 재귀의 동작을 묵혀두는 동작과 스택의 먼저 들어간 값이 묵혀 있다가 나중에 나오는 동작은 본질적으로 비슷하다. 따라서, DFS를 구현할 때 스택을 이용하는 것이 가능하다면, 이를 재귀함수로 표현하는 것도 가능하다.








