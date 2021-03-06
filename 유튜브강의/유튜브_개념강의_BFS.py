from collections import deque

vertexList = ['0','1','2','3','4','5','6']

edgeList = [(0,1),(0,2),(1,0),(1,3),(2,0),(2,4),(2,5),(3,1),(4,2),(4,6),(5,2),(6,4)]



def bfs(vertexList,edgeList,start):

    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:

        adjacencyList[edge[0]].append(edge[1])

    queue = deque([start])

    visitedList = []

    while queue:

        current = queue.pop()

        for neighbor in adjacencyList[current]:

            if not neighbor in visitedList:

                queue.insert(0,neighbor)

        visitedList.append(current)

    return visitedList

print(bfs(vertexList,edgeList,0))