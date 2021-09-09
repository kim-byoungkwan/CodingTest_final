# 특정 거리의 도시 찾기

from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:

# 한번이라도 직접적인 경로에 의하여 방문이 된 경우 if문의 아래의 코드에 의해서 초깃값 -1에서 벗어나게 되므로, -1 이 아닌 경우의 인덱스의 노드는 이미 최단거리로 방문된 상태임을 표현한다.
# 따라서, -1이 아닌 경우는 제외하고 아래의 연산을 생각해주면 아직 최단거리로 방문된 적이 없는 상태이므로, 최단거리값을 구할 수 있다.

            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)
    
# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면 -1 출력
if check == False:
    print(-1)
