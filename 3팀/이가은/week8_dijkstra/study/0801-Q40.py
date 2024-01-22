INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    # 양방향 허용
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

max_dist = -1       # 헛간까지의 거리
max_dist_idx = -1   # 숨어야 하는 헛간 번호 (같은 헛간이 여러 개면 가장 작은 헛간 번호)
for j in range(1, n + 1):
    if graph[1][j] != INF and max_dist < graph[1][j]:
        max_dist = graph[1][j]
        max_dist_idx = j

cnt = 0             # max_dist를 갖는 헛간과 같은 거리를 갖는 헛간의 개수
for dist in graph[1]:
    if dist == max_dist:
         cnt += 1

print(max_dist_idx, max_dist, cnt)
