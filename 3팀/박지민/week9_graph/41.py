# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니면 루트 노드를 찾을 때까지 재귀호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력
n, m = map(int, input().split())
parent = [0] * (n+1) # 부모 테이블 초기화

# 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(n):
    data = list(map(int), input().split())
    for j in range(n):
        if data[j] == 1: # 연결된 경우 union 연산 수행
            union_parent(parent, i+1, j+1)

# 여행 계획 입력
plan = list(map(int), input().split())

result = True

for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

if result:
    print("YES")
else:
    print("NO")



