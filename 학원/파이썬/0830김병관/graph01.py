# 학교에서 학생들에게 0번부터 N번까지의 번호를 부여함
# 처음에는 모든 학생이 서로 다른 팀으로 구분되어 총 N+1개의 팀이 존재
# 이 때 팀 합치기 연산과 같은 팀 여부 확인 연산을 사용할 수 있음

# 1. 팀 합치기 연산은 두팀을 합치는 연산이다.
# 2. 같은 팀 여부 확인 연산은 특정한 두 학생이 같은 팀에 속하는지를 확인하는 연산이다.

# M개의 연산을 수행할 수 있을 때 같은 팀 여부 확인 연산에 대한 연산 결과를 출력하는
# 프로그램을 작성하시오


# 입력조건

# 첫째줄에 N,M이 주어진다. M은 입력으로 주어지는 연산의 개수이다.(1<=N,M<=100,000)

# 다음 M개의 줄에는 각각의 연산이 주어진다.

# 팀 합치기 연산은 0 a b 형태로 주어진다. 이는 a번 학생이 속한 팀과
# b번 학생이 속한 팀을 합친다는 의미이다.

# 같은 팀 여부 확인 연산은 1 a b 형태로 주어진다. 이는 a번 학생과 b번 학생이
# 같은 팀에 속해 있는지를 확인하는 연산이다.

# a와 b는 N이하의 양의 정수이다.

# 출력조건

# 같은 팀 여부 확인 연산에 대하여 한 줄에 하나씩 YES 혹은 NO로 결과를 출력한다.

# 입력예시
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1

# 출력예시
# NO
# NO
# YES

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원수가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
parent = [0] * (n+1) # 부모 테이블 초기화

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(0,n+1):
    parent[i] = i

# 각 연산을 하나씩 확인
for i in range(m):
    oper,a,b = map(int,input().split())
    # 합집합(union) 연산인 경우
    if oper == 0:
        union_parent(parent,a,b)
    # 찾기(find) 연산인 경우
    elif oper == 1:
        if find_parent(parent,a) == find_parent(parent,b):
            print('YES')
        else:
            print('NO')
