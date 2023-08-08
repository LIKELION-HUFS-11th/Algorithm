def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

travel = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if travel[i][j] == 1:
            union(i+1, j+1)

m_list = list(map(int, input().split()))
for i in range(m-1):
    if parent[m_list[i]] != parent[m_list[i+1]]:
        print("NO")
        exit(0)
print("YES")