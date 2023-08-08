def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x
p_list = []
n, m = map(int, input().split())
for _ in range(m):
    x, y, z = map(int, input().split())
    p_list.append([z, x, y])

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i
p_list.sort()
total = answer = 0
for p in p_list:
    total += p[0]
    if find_parent(p[1]) != find_parent(p[2]):
        union(p[1], p[2])
        answer += p[0]

print(total-answer)