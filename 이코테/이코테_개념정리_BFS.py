from collections import deque

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

def bfs(graph,start,visited):

    queue = deque([start])

# deque 자료형으로 리스트 [start]를 정의하여 queue 변수에 할당한다. 즉, queue 변수는 데크 자료형의 모든 기능을 갖는 리스트이다.

    visited[start] = True

# 시작 노드를 표현하는 인덱스의 visited 리스트의 원소값을 True로 치환하여 시작 노드가 방문된 상태임을 나타낸다.

    while queue:

        v = queue.popleft()

# queue 변수는 데크 자료형으로 할당된 리스트 이므로, 데크 자료형이 갖는 모든 기능을 적용할 수 있는 리스트이다. 그러므로, 이경우 popleft()를 queue에 적용하면 queue 데크에 가장 먼저 들어간 원소를 출력하게된다.

        print(start,end=' ')

# queue 데크에 가장 먼저 들어간 원소를 출력 하여 보여준다. 즉, 가장 먼저 방문한 노드를 표현하는 것이다.

        for i in graph[v]:

# 가장 먼저 queue 데크에 할당된 노드를 표현하는 v의 graph 리스트에서의 값은 v와 인접하여 간선으로 연결된 모든 노드를 표현하는데, v와 인접한 모든 노드를 i에 할당하는 것이다.

            if not visited[i]:

# 이경우 가장 먼저 방문한 노드 v와 인접한 노드i가 방문하지 않은 상태이면, if not 조건문에 의해 True가 되어

                queue.append(i)

# 위의 코드가 실행되는데, 이는 v와 인접한 노드 i를 방문하여 i를 queue 데크에 할당하고,

                visited[i] = True

# i 노드를 방문했음을 표현할 수 있는 코드이다.

# 즉 for문이 반복적으로 실행되게 되면, 시작 노드 v와 인접한 모든 노드가 i에 할당되게 되고, i 노드를 방문하게 됨을 visitied[i]리스트의 요소가 True 로 치환되게 되면서 표현되고, 방문한 노드를 queue 데크에 할당한다.

# 이러한 for문이 모두 동작하고 난 뒤, 다시 while문으로 돌아가면, 방문한 노드가 queue 데크에 존재하므로 while 조건문은 참이되어 다시 지금까지의 동작이 반복되는데,
# 이때, 또다시 queue 데크에 현재 가장먼저 할당된 순서를 가진 노드가 v에 queue데크에서 출력되어 할당되게되고, 또 다시 v와 연결된 인접노드를 방문하지 않은 노드에 대해서 방문하는 동작을 취하게 된다.
# 그 결과 내가 어떠한 노드를 방문하고, 그 방문한 노드에 인접한 노드를 방문하지 않은 순서로 모두 방문하는 동작을 취하게 되고, 이러한 동작의 순서로 출력된 노드가 print로 표현되게된다.





