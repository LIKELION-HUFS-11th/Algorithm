INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    graph[a][a] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = min(graph[a][b], 1)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

answer = 0
for a in range(1, n+1):
    check = []
    for b in range(1, n+1):
        if a == b: continue
        if graph[a][b] != INF or graph[b][a] != INF:
            check.append(b)
    if len(check) == n-1:
        answer += 1
print(answer)
