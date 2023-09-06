# 특정 원소가 속한 집합을 찾기 : find 함수
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    # 부모 테이블이기 때문에, 루트 노드까지가서 확인해야 같은 팀인지 알 수 있음
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 : union 함수
# a와 b의 루트 번호를 찾아서, 루트 번호 크기가 더 큰 쪽이 작은 쪽을 부모로 설정할 수 있게 함
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int, input().split())
parent = [0] * (n+1) # 모든 노드의 정보를 담을 수 있도록 부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(0,n+1):
    parent[i] = i

# 각 연산을 하나씩 확인
for i in range(m):
    oper, a, b = map(int, input().split())
    # 합집합(union) 연산인 경우
    if oper == 0:
        union_parent(parent, a, b)
    # 찾기(find) 연산인 경우
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')

